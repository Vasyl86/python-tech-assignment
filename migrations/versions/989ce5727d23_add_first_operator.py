"""Add first operator

Revision ID: 989ce5727d23
Revises: 3fbee182ae89
Create Date: 2024-02-14 11:13:53.281920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '989ce5727d23'
down_revision = '3fbee182ae89'
branch_labels = None
depends_on = None


def upgrade():
    metadata = sa.MetaData()
    operator_table = sa.Table('operator', metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50)),
        sa.Column('last_name', sa.String(50))
    )
    op.bulk_insert(
        operator_table,
        [
            {'id': 1, 'first_name': 'First', 'last_name': 'Operator'}
        ]
    )


def downgrade():
    pass
