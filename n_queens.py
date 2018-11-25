"""NQueens solution."""

import argparse

from connection import get_connection
from copy import copy
from models import NQueenSolution
from sqlalchemy.orm import sessionmaker


connection = get_connection()
Session = sessionmaker(bind=connection)


class NQueens(object):
    """Modeling N-queens solution."""

    def __init__(self, number_queens, print_solutions=False):
        """Constructor.

        Args:
            number_queens (int): Represents the number of queens

            print_solutions (bool): Indicates whether the chessboard
                                    should be printed with each of
                                    the solutions
            that you want to place on the chessboard.
        """
        super(NQueens, self).__init__()
        self.session = Session()
        self.number_queens = number_queens
        self.number_solutions = 0
        self.solutions = []
        self.print_solutions = print_solutions
        self.start()

    def start(self):
        """Start to solve the problem."""
        previous_solutions = self.find_previous_solutions()
        if previous_solutions:
            self.solutions = previous_solutions
            self.number_solutions = len(previous_solutions)
        else:
            self.find_solutions()
        self.show_result()

    def find_previous_solutions(self):
        """Find previous solutions calculated into the storage."""
        nqueens_solution = self.session.query(NQueenSolution).filter_by(
            number_of_queens=self.number_queens
        ).first()
        if nqueens_solution:
            print("There is a previous solution!")
            solutions = nqueens_solution.solutions
            return solutions

    def find_solutions(self):
        """Try to find all the solutions to N-queens problem."""
        positions = self.generate_initial_positions()
        initial_row = 0
        self.place_queen(positions, initial_row)
        self.persist_solutions()

    def generate_initial_positions(self):
        """Generate the initial queen positions on the chessboard.

        Returns:
            list: List of initial positions.
        """
        positions = [-1] * self.number_queens
        return positions

    def place_queen(self, positions, target_row):
        if target_row == self.number_queens:
            solution = copy(positions)
            self.add_solution(solution)
            self.number_solutions += 1
        else:
            columns = range(self.number_queens)
            for column in columns:
                if not self.is_place_under_attack(positions,
                                                  target_row,
                                                  column):
                    positions[target_row] = column
                    next_row = target_row + 1
                    self.place_queen(positions, next_row)

    def add_solution(self, solution):
        """Add a found solution to the list of solutions.

        Args:
            solution (list): List of queen positions that represent a solution
        """
        self.solutions.append(solution)

    def is_in_same_column(self, positions, row, column):
        """Check if there a queen in the same column.

        Args:
            positions (list): List of queen positions
            row (int): current row
            column (int): current queen position

        Returns:
            bool: True if there queen in same column,False otherwise
        """
        return positions[row] == column

    def is_in_same_diagonal(self, positions, row, column, full_rows):
        """Check if there a queen in the same diagonal.

        Args:
            positions (list): List of queen positions
            row (int): current row
            column (int): current queen position
            full_rows (int): number of ocuppied rows

        Returns:
            bool: True if there queen in same diagonal,False otherwise
        """
        left_diagonal = positions[row] - row == column - full_rows
        right_diagonal = positions[row] + row == column + full_rows
        return left_diagonal or right_diagonal

    def is_place_under_attack(self, positions, full_rows, column):
        """Check if a place (colum) is under attack from other queens.

        Args:
            positions (list): list of queen positions
            full_rows (int): number of full rows
            column (int): target column

        Returns:
            bool: True if the place is under attack, False otherwise
        """
        for i in range(full_rows):
            if self.is_in_same_column(positions, i, column) or \
                    self.is_in_same_diagonal(positions, i, column, full_rows):
                return True
        return False

    def persist_solutions(self):
        """Persist all the solutions into the storage."""
        print("Persisting the solutions...")
        try:
            solution = NQueenSolution(number_of_queens=self.number_queens,
                                      solutions=self.solutions)
            self.session.add(solution)
            self.session.commit()
            print("Solutions persisted!")
        except Exception as e:
            print("Something is wrong ", e)

    def show_result(self):
        """Show the results."""
        if self.print_solutions:
            self.show_chessboard()
            print("\n")
        print("Found", self.number_solutions,
              "solutions for", self.number_queens, " Queens")

    def show_chessboard(self):
        """Show the chessboard with all the found solutions.

        Args:
            solutions (list): list of list with solutions.
        """
        for solution in self.get_solution():
            for row in range(self.number_queens):
                line = ""
                for column in range(self.number_queens):
                    if solution[row] == column:
                        line += "Q "
                    else:
                        line += ". "
                print(line)
            print("\n")

    def get_solution(self):
        """Get a solution from solutions list as a generator.

        Yields:
            list: list of queen positions.
        """
        for solution in self.solutions:
            yield solution


def str2bool(value):
    """Convert a str to bool.

    Args:
        value (str): The str to be evaluated

    Returns:
        bool: True/False according input

    Raises:
        argparse.ArgumentTypeError: raise exception if a
                                    unexpected argument is passed
    """
    value = value.lower()
    affirmatives = ('yes', 'true', 't', 'y', '1')
    negatives = ('no', 'false', 'f', 'n', '0')
    boolean_value = None
    if value in affirmatives:
        boolean_value = True
    elif value in negatives:
        boolean_value = False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
    return boolean_value


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Find solutions to the problem of the N-queens.'
    )
    parser.add_argument(
        'queens',
        metavar='N',
        type=int,
        help='Number of queens that you want to place on the chessboard')

    parser.add_argument(
        'show_chessboard',
        type=str2bool,
        nargs='?',
        const=False,
        help='Show the chessboard?')

    args = parser.parse_args()

    n_queens = NQueens(args.queens, args.show_chessboard)
