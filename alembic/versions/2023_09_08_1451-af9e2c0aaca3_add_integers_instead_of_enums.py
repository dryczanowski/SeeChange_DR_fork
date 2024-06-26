"""add integers instead of enums

Revision ID: af9e2c0aaca3
Revises: e78c1e8bec33
Create Date: 2023-08-31 14:51:58.162907

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'af9e2c0aaca3'
down_revision = 'b33a5b72da8b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cutouts', sa.Column('_format', sa.SMALLINT(), nullable=False))
    op.drop_column('cutouts', 'format')
    op.add_column('exposures', sa.Column('_type', sa.SMALLINT(), nullable=False))
    op.add_column('exposures', sa.Column('_format', sa.SMALLINT(), nullable=False))
    op.drop_index('ix_exposures_type', table_name='exposures')
    op.create_index(op.f('ix_exposures__type'), 'exposures', ['_type'], unique=False)
    op.drop_column('exposures', 'type')
    op.drop_column('exposures', 'format')
    op.add_column('images', sa.Column('_format', sa.SMALLINT(), nullable=False))
    op.add_column('images', sa.Column('_type', sa.SMALLINT(), nullable=False))
    op.drop_index('ix_images_type', table_name='images')
    op.create_index(op.f('ix_images__type'), 'images', ['_type'], unique=False)
    op.drop_column('images', 'type')
    op.drop_column('images', 'format')
    op.add_column('source_lists', sa.Column('_format', sa.SMALLINT(), nullable=False))
    op.drop_column('source_lists', 'format')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('source_lists', sa.Column('format', postgresql.ENUM('fits', 'hdf5', 'csv', 'npy', name='file_format'), autoincrement=False, nullable=False))
    op.drop_column('source_lists', '_format')
    op.add_column('images', sa.Column('format', postgresql.ENUM('fits', 'hdf5', 'csv', 'npy', name='file_format'), autoincrement=False, nullable=False))
    op.add_column('images', sa.Column('type', postgresql.ENUM('Sci', 'ComSci', 'Diff', 'ComDiff', 'Bias', 'ComBias', 'Dark', 'ComDark', 'DomeFlat', 'ComDomeFlat', 'SkyFlat', 'ComSkyFlat', 'TwiFlat', 'ComTwiFlat', name='image_type'), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_images__type'), table_name='images')
    op.create_index('ix_images_type', 'images', ['type'], unique=False)
    op.drop_column('images', '_type')
    op.drop_column('images', '_format')
    op.add_column('exposures', sa.Column('format', postgresql.ENUM('fits', 'hdf5', 'csv', 'npy', name='file_format'), autoincrement=False, nullable=False))
    op.add_column('exposures', sa.Column('type', postgresql.ENUM('Sci', 'ComSci', 'Diff', 'ComDiff', 'Bias', 'ComBias', 'Dark', 'ComDark', 'DomeFlat', 'ComDomeFlat', 'SkyFlat', 'ComSkyFlat', 'TwiFlat', 'ComTwiFlat', name='image_type'), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_exposures__type'), table_name='exposures')
    op.create_index('ix_exposures_type', 'exposures', ['type'], unique=False)
    op.drop_column('exposures', '_format')
    op.drop_column('exposures', '_type')
    op.add_column('cutouts', sa.Column('format', postgresql.ENUM('fits', 'hdf5', 'csv', 'npy', name='file_format'), autoincrement=False, nullable=False))
    op.drop_column('cutouts', '_format')
    # ### end Alembic commands ###
