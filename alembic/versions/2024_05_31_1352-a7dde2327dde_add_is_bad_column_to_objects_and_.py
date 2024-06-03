"""Add is_bad column to Objects and Measurements

Revision ID: a7dde2327dde
Revises: f36d17393be7
Create Date: 2024-05-31 13:52:26.008896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7dde2327dde'
down_revision = 'f36d17393be7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('measurements', sa.Column('is_bad', sa.Boolean(), nullable=False))
    op.create_index(op.f('ix_measurements_is_bad'), 'measurements', ['is_bad'], unique=False)
    op.add_column('objects', sa.Column('is_bad', sa.Boolean(), nullable=False))
    op.create_index(op.f('ix_objects_is_bad'), 'objects', ['is_bad'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_objects_is_bad'), table_name='objects')
    op.drop_column('objects', 'is_bad')
    op.drop_index(op.f('ix_measurements_is_bad'), table_name='measurements')
    op.drop_column('measurements', 'is_bad')
    # ### end Alembic commands ###
