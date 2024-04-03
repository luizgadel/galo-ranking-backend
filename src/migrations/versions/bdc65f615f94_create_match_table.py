"""create match table

Revision ID: bdc65f615f94
Revises: 8d6b52cb5553
Create Date: 2024-04-01 13:45:31.332849

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdc65f615f94'
down_revision = '8d6b52cb5553'
branch_labels = None
depends_on = None

table_name = 'match'

def upgrade() -> None:
    op.create_table(
        table_name,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('team_one_id', sa.Integer, sa.ForeignKey('team.id'), nullable=False),
        sa.Column('team_two_id', sa.Integer, sa.ForeignKey('team.id'), nullable=False),
        sa.Column('score_team_one', sa.Integer, nullable=False, default=0),
        sa.Column('score_team_two', sa.Integer, nullable=False, default=0),
        sa.Column('date_time_start', sa.DateTime, nullable=False, default=sa.func.current_timestamp()),
        sa.Column('date_time_end', sa.DateTime, nullable=True)
    )


def downgrade() -> None:
    op.drop_table(table_name)
