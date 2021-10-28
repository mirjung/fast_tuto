"""create user table

Revision ID: 6688e8684072
Revises: 
Create Date: 2021-10-27 10:08:56.087846

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6688e8684072'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.String, primary_key=True, index=True),
        sa.Column('name', sa.String),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('password', sa.String),
        sa.Column('is_active', sa.Boolean),
        sa.Column('updated_at', sa.DateTime, default=datetime.now),
        sa.Column('created_at', sa.DateTime, default=datetime.now)
    )


def downgrade():
    op.drop_table('users')