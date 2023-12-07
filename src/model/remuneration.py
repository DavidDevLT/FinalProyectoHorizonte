from .declarative_base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Remuneration(Base):
    __tablename__ = 'tblRemuneration'
    idRemun = Column(Integer, primary_key=True)
    bonusOvertime = Column(Float)
    bonusMobility = Column(Float)
    bonusSupplemt = Column(Float)
    computableRemun = Column(Float)
    cts = Column(Float)
    totalRemun = Column(Float)

    work = relationship('Work', back_populates='remuneration')