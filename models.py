from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    mail = Column(String)
    login = Column(String)
    password = Column(String)
    roles = Column(String)
    activity = Column(Boolean)
    services = Column(String)

    projects = relationship("Projects", secondary="user_project", back_populates='users')


class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    shortname = Column(String)
    production_type = Column(String)
    task_type = Column(String)
    task_status = Column(String)
    resolution = Column(String)
    fps = Column(String)
    colorspace = Column(String)
    root_path = Column(String)
    env_var = Column(String)
    tempplate = Column(String)
    toolkit = Column(String)
    software = Column(String)

    users = relationship("User", secondary="user_project", back_populates='projects')


user_project = Table('user_project',
                     Base.metadata,
                     Column('users_id', ForeignKey('users.id'), primary_key=True),
                     Column('project_id', ForeignKey('projets.id'), primary_key=True)
                     )
