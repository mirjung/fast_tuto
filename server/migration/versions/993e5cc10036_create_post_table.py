"""create post table

Revision ID: 993e5cc10036
Revises: 6688e8684072
Create Date: 2021-10-27 10:09:41.191760

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '993e5cc10036'
down_revision = '6688e8684072'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String),
        sa.Column('content', sa.Text),
        sa.Column('author_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('updated_at', sa.DateTime, default=datetime.now),
        sa.Column('created_at', sa.DateTime, default=datetime.now)
    )


def downgrade():
    op.drop_table('posts')
