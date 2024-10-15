"""empty message

Revision ID: 336da525bb0a
Revises: 
Create Date: 2024-10-14 10:32:20.932720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '336da525bb0a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department', sa.String(length=255), nullable=False),
    sa.Column('login', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('executor_id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.Date(), nullable=False),
    sa.Column('deadline', sa.Date(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('is_valid', sa.Boolean(), nullable=True),
    sa.Column('completion_note', sa.Text(), nullable=True),
    sa.Column('completion_confirmed', sa.Boolean(), nullable=True),
    sa.Column('completion_confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('admin_note', sa.Text(), nullable=True),
    sa.Column('attached_file', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['executor_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    op.drop_table('user')
    # ### end Alembic commands ###
