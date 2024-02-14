"""Initial migration

Revision ID: 3fbee182ae89
Revises: 
Create Date: 2024-02-14 10:45:32.849711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fbee182ae89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create new tables
    op.create_table(
        'client',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('first_name', sa.String(length=50), nullable=False),
        sa.Column('last_name', sa.String(length=50), nullable=False),
        sa.Column('phone', sa.String(length=20), nullable=False)
    )
    op.create_table(
        'operator',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('first_name', sa.String(length=50), nullable=False),
        sa.Column('last_name', sa.String(length=50), nullable=False)
    )
    op.create_table(
        'request',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('body', sa.Text(), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=False),
        sa.Column('created_by', sa.Integer(), sa.ForeignKey('client.id')),
        sa.Column('processed_by', sa.Integer(), sa.ForeignKey('operator.id'), nullable=True)
    )


def downgrade():
    # Drop new tables
    op.drop_table('client')
    op.drop_table('request')
    op.drop_table('operator')
