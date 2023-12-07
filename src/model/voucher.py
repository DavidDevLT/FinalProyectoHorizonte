from .declarative_base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship


class Voucher(Base):
    __tablename__ = 'tblVoucher'
    idVch = Column(Integer, primary_key = True)
    dateVch = Column(Date)
    idEmpl = Column(Integer, ForeignKey('tblEmployer.idEmpl'))
    idCo = Column(Integer, ForeignKey('tblCompanyData.idCo'))
    idEmp = Column(Integer, ForeignKey('tblEmployee.idEmp'))

    employer = relationship('Employer', back_populates='voucher')
    companyData = relationship('CompanyData', back_populates='voucher')
    employee = relationship('Employee', back_populates='voucher')
