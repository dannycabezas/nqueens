*N Queens problem. (Python Solution)*

This is a solution to the problem of n-queens using Python, SQLAlchemy and Docker.

How to execute the code?

*< prerequisites >*

*Installing requirements:*

* cd nqueens/
* pip install -r requirements.txt

*Running the docker postgres image:*

* sudo docker run --name nqueens --network="host" -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=nqeens -d postgress

*Execute the main.py file*

* python main.py

*Options*

1. Running the file n_queens.py:
   * cd nqueens
   
   * python n_queens.py 8 yes

In this case 8 (case base) represents the number of queens that are desired to be placed on the chessboard, you can indicate any positive number (N > 0). "yes" indicates that you want to print per console each chessboard with its solution (you can omit this parameter).

2. Running pytest:
   * cd nqueens
   * pytest -sv test_n_queens.py

3. Docker: 

* cd nqueens
* docker build -t nqueens_docker .
* docker run -it nqueens_docker:latest