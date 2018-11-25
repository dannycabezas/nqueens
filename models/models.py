"""Models module."""


from sqlalchemy import Column
from sqlalchemy import Index
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class NQueenSolution(Base):
    """Represent a solution for the N-queen problem.

    Attributes:
        number_of_queens (int): Number of queen in the problem.
        solutions (list): list of solutions.
    """

    __tablename__ = 'nqueen_solution'

    __table_args__ = (
        Index('idx_number_of_queens', 'number_of_queens'),
    )

    number_of_queens = Column(Integer, primary_key=True)
    solutions = Column(JSON, nullable=False)
