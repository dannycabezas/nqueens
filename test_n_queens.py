"""Test module."""

from n_queens import NQueens


class TestNQueens(object):
    """NQueens test solutions."""

    def test_n_queens_known_solutions(self, get_resource):
        """Test the solutions for N queens.

        Args:
            get_resource (method): Method to get global resources
        """
        known_solutions = get_resource("known_solutions.json")
        solutions = known_solutions.get("solutions")
        for number_queens, number_solutions in solutions.items():
            print(
                "Triying to find solutions for {} Queens".format(
                    number_queens
                )
            )
            nqueens_model = NQueens(int(number_queens))
            assert nqueens_model.number_solutions == number_solutions
