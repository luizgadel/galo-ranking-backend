"""create player table

Revision ID: 7765b4c6a2c6
Revises: 
Create Date: 2024-04-01 10:52:24.318649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7765b4c6a2c6'
down_revision = None
branch_labels = None
depends_on = None

table_name = 'player'

def upgrade() -> None:
    op.create_table(
        table_name,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table(table_name)
