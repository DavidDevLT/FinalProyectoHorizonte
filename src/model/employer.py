from .declarative_base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Employer(Base):
    __tablename__ = 'tblEmployer'
    idEmpl = Column(Integer, primary_key = True)
    dniEmpl = Column(String(20))
    nameEmpl = Column(String(20))
    surnameDadEmpl = Column(String(20))
    surnameMomEmpl = Column(String(20))
    emailEmpl = Column(String(30))
    phoneEmpl = Column(Numeric(9))

    voucher = relationship('Voucher', back_populates='employer')

