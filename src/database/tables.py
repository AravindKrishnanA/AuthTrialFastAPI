from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint, ForeignKey, DECIMAL, Date
from sqlalchemy.orm import declarative_base, relationship


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="postgres",
    host="localhost",
    database="ORMTest1",
    port=5432
)

engine = create_engine(url)

#creating models
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
    role = Column(String, default = "guest") #add possible check constraint

class Tenant(Base):
    __tablename__ = "tenants"

    tenant_id = Column(Integer, primary_key=True)
    name = Column(Integer)

    #other possible fields here


class TenancyAgreement(Base):
    __tablename__ = "tenancy_agreements"

    agreement_no = Column(Integer, primary_key=True)
    agreement_type = Column(String)
    rent_amt = Column(DECIMAL(precision=10, scale=2))
    rent_cycle = Column(Integer) #number of days
    start_date = Column(Date)
    end_date = Column(Date)
    document_id = Column(Integer)
    tenant_id = Column(Integer, ForeignKey('tenants.tenant_id'))
    #units = relationship("Unit", cascade="all", back_populates="tenancy_agreements")#check

class Property(Base):
    __tablename__ = "properties"
    pid = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))#new
    name = Column(String)
    type = Column(String)
    nunits = Column(Integer)
    floors = Column(Integer)

    #units = relationship("Unit", cascade="all, delete", back_populates="properties")#check


class Unit(Base):
    __tablename__ = "units"

    uid = Column(Integer, primary_key=True)
    pid = Column(Integer, ForeignKey('properties.pid', ondelete='CASCADE'))
    name = Column(String)
    type = Column(String)
    floor = Column(Integer)
    tenancy_agreement_no = Column(Integer, ForeignKey('tenancy_agreements.agreement_no', ondelete='SET NULL'), nullable=True)
    
    #tenancy_agreeement = relationship("TenancyAgreement", back_populates="units")#check
    #property = relationship("Property", back_populates="units")






#add other tables here



Base.metadata.create_all(engine)