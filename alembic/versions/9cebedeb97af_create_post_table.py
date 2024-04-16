"""create post table

Revision ID: 9cebedeb97af
Revises: 
Create Date: 2024-04-15 19:47:42.868815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9cebedeb97af'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('test',sa.column('id',sa.Integer()))
    pass


def downgrade() -> None:
    pass
