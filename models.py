from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String




Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, unique=True)
    email = Column(String)
    
def __repr__(self):
    return f"\nUser " \
        +f"id={self.id} " \
        +f"first_name={self.first_name}, "\
        +f"last_name={self.last_name}, " \
        +f"email={self.email}" \
        +" >"
        