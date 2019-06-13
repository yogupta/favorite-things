from sqlalchemy import Column, Integer, String, Index
from sqlalchemy.orm import relationship

from app.utils import constants
from . import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(32), unique=True)
    password = Column(String(32))
    favorite_things = relationship("FavoriteThings", back_populates="user")

    def __init__(self, email, password):
        self.email = email
        self.password = password

    __tablename__ = constants.USERS_TABLE
    __table_args__ = (Index("user_email_idx", email),)
