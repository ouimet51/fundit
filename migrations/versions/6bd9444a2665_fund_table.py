"""fund table

Revision ID: 6bd9444a2665
Revises: 036a63503deb
Create Date: 2018-07-09 22:26:53.253533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bd9444a2665'
down_revision = '036a63503deb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fund',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=140), nullable=True),
    sa.Column('goal', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fund_name'), 'fund', ['name'], unique=False)
    op.create_index(op.f('ix_fund_timestamp'), 'fund', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fund_timestamp'), table_name='fund')
    op.drop_index(op.f('ix_fund_name'), table_name='fund')
    op.drop_table('fund')
    # ### end Alembic commands ###
