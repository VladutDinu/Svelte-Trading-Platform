import sqlalchemy as db
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('mysql+mysqlconnector://root:vladutcalut123@@localhost:3306/tradingplatform')
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email    = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    children = relationship("Share")

    def __repr__(self):
        return "<User(id='%s', username='%s', email='%s')>" % (
                                self.id, self.username, self.email)

    
    
class Stock(Base):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    tag = db.Column(db.String(64), unique=True, index=True)
    sale_price = db.Column(db.Float(precision=2))
    buy_price = db.Column(db.Float(precision=2))



class Share(Base):
    __tablename__ = 'shares'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    stock_tag = db.Column(db.String(64))
    no_of_stocks = db.Column(db.Float(3))
    stock_price = db.Column(db.Float(2))


class Resident(Base):
    __tablename__='Residents'
    residentID  = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64))
    lastName     = db.Column(db.String(64))
    coinsBalance = db.Column(db.Integer)
    cashBalance = db.Column(db.Integer)
    energyValue = db.Column(db.Float(3))
    energyUnits = db.Column(db.String(1))
    cashCurrency = db.Column(db.String(1))

class Bank(Base):
    __tablename__='Banks'
    bankID  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    coinsBalance = db.Column(db.Integer)
    cashBalance = db.Column(db.Integer)
    cashCurrency = db.Column(db.String(1))

class UtilityCompany(Base):
    __tablename__='UtilityCompanies'
    utilityID   = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(64))
    coinsBalance = db.Column(db.Integer)
    energyValue = db.Column(db.Float(3))
    energyUnits = db.Column(db.String(1))

Base.metadata.create_all(engine)