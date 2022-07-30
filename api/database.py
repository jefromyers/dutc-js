from contextlib import contextmanager

from sqlalchemy import (Column, ForeignKey, Integer, String, Table,
                        create_engine)
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_URL = "sqlite:///./dutc.db"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



class Campaign(Base):

    __tablename__ = "campaign"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    projects = relationship('Project')

    def __str__(self):
        return f'{self.title}'

class Project(Base):

    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    campaign_id = Column(Integer, ForeignKey('campaign.id'))

    campaign = relationship('Campaign', back_populates='projects')

    def __str__(self):
        return f'{self.title}'

