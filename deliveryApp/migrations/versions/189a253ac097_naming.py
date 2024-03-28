"""naming

Revision ID: 189a253ac097
Revises: 44e5bc9b4a3f
Create Date: 2024-03-22 15:26:32.766791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '189a253ac097'
down_revision: Union[str, None] = '44e5bc9b4a3f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('user', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('user', 'id')
    # ### end Alembic commands ###