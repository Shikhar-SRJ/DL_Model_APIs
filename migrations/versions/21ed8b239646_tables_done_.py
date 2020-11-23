"""tables done_!

Revision ID: 21ed8b239646
Revises: 
Create Date: 2020-11-23 12:36:11.929241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21ed8b239646'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('predictions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('belong_to_class', sa.String(length=40), nullable=False),
    sa.Column('confidence', sa.Float(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('coordinates', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('belong_to_class')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=60), nullable=False),
    sa.Column('phone_no', sa.String(length=22), nullable=False),
    sa.Column('unique_id', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('unique_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.Column('prediction_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['prediction_id'], ['predictions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data')
    op.drop_table('user')
    op.drop_table('predictions')
    # ### end Alembic commands ###