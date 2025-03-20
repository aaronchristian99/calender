"""create collaborated events table

Revision ID: a16f72f5453f
Revises: 0e8b40d71a47
Create Date: 2025-03-20 01:30:28.771705

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a16f72f5453f'
down_revision: Union[str, None] = '0e8b40d71a47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('collaborated_events',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('event_id', sa.Integer(), sa.ForeignKey('calender.events.id', ondelete='CASCADE'), nullable=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('calender.users.id', ondelete='CASCADE'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='calender'
    )


def downgrade() -> None:
    op.drop_table('collaborated_events', schema='calender')
