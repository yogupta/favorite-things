from sqlalchemy import Column, ForeignKey, Integer, String, Index, UniqueConstraint
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


class FavoriteCategory(Base):
    id = Column(Integer, primary_key=True)
    category = Column(String(32), nullable=False)
    user_id = Column(Integer, ForeignKey(f"{constants.USERS_TABLE}.id"))
    user = relationship("User")

    UniqueConstraint(category, user_id)

    def __init__(self, category, user):
        self.user = user
        self.category = category

    __tablename__ = constants.USER_CATEGORY_MAPPER
    __table_args__ = (Index("user_category_idx", category, user_id, unique=True),)
