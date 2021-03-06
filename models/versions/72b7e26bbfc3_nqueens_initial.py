"""nqueens initial

Revision ID: 72b7e26bbfc3
Revises: 
Create Date: 2018-11-25 17:53:35.919312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72b7e26bbfc3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nqueen_solution',
    sa.Column('number_of_queens', sa.Integer(), nullable=False),
    sa.Column('solutions', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('number_of_queens')
    )
    op.create_index('idx_number_of_queens', 'nqueen_solution', ['number_of_queens'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_number_of_queens', table_name='nqueen_solution')
    op.drop_table('nqueen_solution')
    # ### end Alembic commands ###
