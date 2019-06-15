from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, Date, Index, types
from sqlalchemy.orm import relationship

from app.utils import constants
from . import Base


def _get_date():
    return datetime.now()


class FavoriteThings(Base):
    __tablename__ = constants.FAVORITE_THINGS_TABLE
    sr = Column(Integer, autoincrement=True)
    id = Column(String(32), primary_key=True)
    title = Column(String(32), nullable=False)
    description = Column(String(128), nullable=True)
    ranking = Column(Integer, nullable=False)
    category = Column(String(32), nullable=False)
    created = Column(Date, default=_get_date())
    updated = Column(Date, default=_get_date(), onupdate=_get_date())
    meta_data = Column(types.PickleType)
    user_id = Column(String(32), ForeignKey(f"{constants.USERS_TABLE}.id"))
    user = relationship("User", back_populates="favorite_things")

    def __init__(self, user_id: str, title, ranking: int, category: str, description: str = None):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.ranking = ranking
        self.category = category

    __table_args__ = (Index("category_ranking_idx", category, ranking),)
