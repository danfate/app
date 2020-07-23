"""empty message

Revision ID: 7128f87af701
Revises: a3c9a43e41f4
Create Date: 2020-06-28 11:18:22.765690

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7128f87af701'
down_revision = 'a3c9a43e41f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mailbox', sa.Column('nb_failed_checks', sa.Integer(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mailbox', 'nb_failed_checks')
    # ### end Alembic commands ###