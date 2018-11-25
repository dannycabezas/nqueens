"""Main module."""

import os

app = "n_queens.py"
test = "test_n_queens.py"

path_app = os.path.join(os.getcwd(), app)
path_test = os.path.join(os.getcwd(), test)

number_queens = 8
show_chessboard = "y"

app_command = "python {} {} {}".format(path_app,
                                       number_queens,
                                       show_chessboard)
test_command = "pytest -sv {}".format(path_test)

os.system('echo running base 8 queens...')
os.system(app_command)

os.system('echo running test...')
os.system(test_command)
