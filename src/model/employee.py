from .declarative_base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__ = 'tblEmployee'
    idEmp = Column(Integer, primary_key = True)
    dniEmp = Column(String(20))
    nameEmp = Column(String(20))
    surnameDadEmp = Column(String(20))
    surnameMomEmp = Column(String(20))
    emailEmp = Column(String(30))
    phoneEmp = Column(Numeric(9))
    savAcctEmp = Column(Numeric(14))
    minWageEmp = Column(Float)
    idWk = Column(Integer, ForeignKey('tblWork.idWk'))

    voucher = relationship('Voucher', back_populates='employee')
    work = relationship('Work', back_populates='employee')
