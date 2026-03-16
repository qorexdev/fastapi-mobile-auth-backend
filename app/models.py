from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    ForeignKey,
    Enum,
)
from sqlalchemy.orm import relationship
import enum

from app.database import Base


class TransactionType(str, enum.Enum):
    topup = "topup"
    transfer = "transfer"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, default="")
    avatar_url = Column(String, default="")
    balance = Column(Float, default=0.0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    sent_transactions = relationship(
        "Transaction", foreign_keys="Transaction.sender_id", back_populates="sender"
    )
    received_transactions = relationship(
        "Transaction",
        foreign_keys="Transaction.receiver_id",
        back_populates="receiver",
    )


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    description = Column(String, default="")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    sender = relationship("User", foreign_keys=[sender_id], back_populates="sent_transactions")
    receiver = relationship("User", foreign_keys=[receiver_id], back_populates="received_transactions")
