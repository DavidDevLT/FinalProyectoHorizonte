from .declarative_base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class CompanyData(Base):
    __tablename__ = 'tblCompanyData'
    idCo = Column(Integer, primary_key = True)
    rucCo = Column(Numeric(11))
    businnesnameCo = Column(String(20))
    categoryCo = Column(String(20))
    addresCo = Column(String(50))

    voucher = relationship('Voucher', back_populates='companyData')

