from .declarative_base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import *

class Work(Base):
    __tablename__ = 'tblWork'
    idWk = Column(Integer, primary_key = True)
    daysWk = Column(Integer)
    extraHours = Column(Integer)
    daysNoWk = Column(Integer)
    minutesNoWk = Column(Integer)
    netIncome = Column(Float)
    idRemun = Column(Integer, ForeignKey('tblRemuneration.idRemun'))
    idDisc = Column(Integer, ForeignKey('tblDiscount.idDisc'))

    employee = relationship('Employee', back_populates= 'work')
    remuneration = relationship('Remuneration',back_populates='work')
    discounts = relationship('Discount', back_populates='work')
