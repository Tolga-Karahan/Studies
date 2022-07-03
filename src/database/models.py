from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

Base = declarative_base()

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer(), primary_key=True, nullable=False)
    title = Column(String(), nullable=False) 
    content = Column(String(), nullable=False)
    published = Column(Boolean(), server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

