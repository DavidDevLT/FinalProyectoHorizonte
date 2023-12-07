from .declarative_base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Discount(Base):
    __tablename__ = 'tblDiscount'
    idDisc = Column(Integer, primary_key=True)
    lackDisc = Column(Float)
    lateDisc = Column(Float)
    totalDisc = Column(Float)

    work = relationship('Work', back_populates='discounts')