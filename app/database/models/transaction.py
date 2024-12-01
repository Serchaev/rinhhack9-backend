from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from app.database.models.base import Base


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    record_id = Column(Integer, nullable=False)
    transaction_id = Column(Integer, nullable=False)
    ip = Column(String(45), nullable=False)
    device_id = Column(Float, nullable=False)
    device_type = Column(String(50), nullable=False)
    tran_code = Column(Integer, nullable=False)
    mcc = Column(Integer, nullable=False)
    client_id = Column(Integer, nullable=False)
    card_type = Column(String(50), nullable=False)
    pin_inc_count = Column(Integer, nullable=False, default=0)
    card_status = Column(String(100), nullable=False)
    datetime = Column(DateTime, nullable=False)
    sum = Column(Float, nullable=False)
    oper_type = Column(String(50), nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    balance = Column(Integer, nullable=False)
    pred = Column(Float, nullable=False)

    def __repr__(self):
        return (
            f"<Transaction(id={self.id}, record_id={self.record_id}, transaction_id={self.transaction_id}, "
            f"client_id={self.client_id}, oper_type={self.oper_type}, sum={self.sum}, pred={self.pred})>"
        )

    def __str__(self):
        return self.__repr__()
