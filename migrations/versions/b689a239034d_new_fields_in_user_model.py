"""new fields in user model

Revision ID: b689a239034d
Revises: 8f65702b564b
Create Date: 2025-03-09 15:41:33.003266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b689a239034d'
down_revision = '8f65702b564b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
