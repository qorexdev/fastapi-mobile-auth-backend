from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.auth import get_current_user
from app.database import get_db
from app.models import User, Transaction, TransactionType
from app.schemas import (
    BalanceResponse,
    BalanceTopUp,
    BalanceTransfer,
    TransactionResponse,
)

router = APIRouter(prefix="/balance", tags=["Balance"])


@router.get("", response_model=BalanceResponse)
def get_balance(current_user: User = Depends(get_current_user)):
    return BalanceResponse(balance=current_user.balance)


@router.post("/topup", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def topup_balance(
    data: BalanceTopUp,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    current_user.balance += data.amount

    transaction = Transaction(
        sender_id=None,
        receiver_id=current_user.id,
        amount=data.amount,
        type=TransactionType.topup,
        description="Balance top-up",
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


@router.post("/transfer", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def transfer_balance(
    data: BalanceTransfer,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if data.receiver_id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot transfer to yourself",
        )

    if current_user.balance < data.amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient balance",
        )

    receiver = db.query(User).filter(User.id == data.receiver_id).first()
    if not receiver:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Receiver not found",
        )

    current_user.balance -= data.amount
    receiver.balance += data.amount

    transaction = Transaction(
        sender_id=current_user.id,
        receiver_id=receiver.id,
        amount=data.amount,
        type=TransactionType.transfer,
        description=data.description or f"Transfer to {receiver.username}",
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


@router.get("/transactions", response_model=List[TransactionResponse])
def get_transactions(
    skip: int = 0,
    limit: int = 50,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    transactions = (
        db.query(Transaction)
        .filter(
            or_(
                Transaction.sender_id == current_user.id,
                Transaction.receiver_id == current_user.id,
            )
        )
        .order_by(Transaction.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return transactions
