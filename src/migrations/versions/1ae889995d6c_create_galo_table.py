"""create galo table

Revision ID: 1ae889995d6c
Revises: bdc65f615f94
Create Date: 2024-04-01 13:48:34.182055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ae889995d6c'
down_revision = 'bdc65f615f94'
branch_labels = None
depends_on = None

table_name = 'galo'

def upgrade() -> None:
    op.create_table(
        table_name,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('match_id', sa.Integer, sa.ForeignKey('match.id'), nullable=False),
        sa.Column('team_wr', sa.Integer, sa.ForeignKey('team.id'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table(table_name)

