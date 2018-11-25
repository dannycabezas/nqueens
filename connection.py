from sqlalchemy import create_engine


def get_connection():
    connection = create_engine(
        'postgresql://postgres:postgres@localhost/nqueens'
    )
    return connection
