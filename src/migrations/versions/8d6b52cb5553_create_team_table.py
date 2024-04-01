"""create team table

Revision ID: 8d6b52cb5553
Revises: 7765b4c6a2c6
Create Date: 2024-04-01 13:38:55.163994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d6b52cb5553'
down_revision = '7765b4c6a2c6'
branch_labels = None
depends_on = None

table_name = 'team'

def upgrade() -> None:
    op.create_table(
        table_name,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('player_one', sa.Integer, sa.ForeignKey('player.id'), nullable=False),
        sa.Column('player_two', sa.Integer, sa.ForeignKey('player.id'), nullable=False),
        sa.Column('team_name', sa.String(50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table(table_name)
