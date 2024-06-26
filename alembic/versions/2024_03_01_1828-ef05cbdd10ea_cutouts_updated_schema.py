"""cutouts updated schema

Revision ID: ef05cbdd10ea
Revises: d24b0fc0eada
Create Date: 2024-03-01 18:28:57.733955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef05cbdd10ea'
down_revision = 'd24b0fc0eada'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cutouts', sa.Column('x', sa.Integer(), nullable=False))
    op.add_column('cutouts', sa.Column('y', sa.Integer(), nullable=False))
    op.add_column('cutouts', sa.Column('_upstream_bitflag', sa.BIGINT(), nullable=False))
    op.drop_index('ix_cutouts_new_image_id', table_name='cutouts')
    op.drop_index('ix_cutouts_ref_image_id', table_name='cutouts')
    op.drop_index('ix_cutouts_filepath', table_name='cutouts')
    op.create_index(op.f('ix_cutouts_filepath'), 'cutouts', ['filepath'], unique=False)
    op.create_index(op.f('ix_cutouts__upstream_bitflag'), 'cutouts', ['_upstream_bitflag'], unique=False)
    op.drop_constraint('cutouts_new_image_id_fkey', 'cutouts', type_='foreignkey')
    op.drop_constraint('cutouts_source_list_id_fkey', 'cutouts', type_='foreignkey')
    op.drop_constraint('cutouts_ref_image_id_fkey', 'cutouts', type_='foreignkey')
    op.create_foreign_key('cutouts_source_list_id_fkey', 'cutouts', 'source_lists', ['sources_id'], ['id'], ondelete='CASCADE')
    op.drop_column('cutouts', 'pixel_x')
    op.drop_column('cutouts', 'ref_image_id')
    op.drop_column('cutouts', 'pixel_y')
    op.drop_column('cutouts', 'new_image_id')
    op.drop_index('measurements_q3c_ang2ipix_idx', table_name='measurements')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cutouts', sa.Column('new_image_id', sa.BIGINT(), autoincrement=False, nullable=False))
    op.add_column('cutouts', sa.Column('pixel_y', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('cutouts', sa.Column('ref_image_id', sa.BIGINT(), autoincrement=False, nullable=False))
    op.add_column('cutouts', sa.Column('pixel_x', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint('cutouts_source_list_id_fkey', 'cutouts', type_='foreignkey')
    op.create_foreign_key('cutouts_ref_image_id_fkey', 'cutouts', 'images', ['ref_image_id'], ['id'])
    op.create_foreign_key('cutouts_source_list_id_fkey', 'cutouts', 'source_lists', ['sources_id'], ['id'])
    op.create_foreign_key('cutouts_new_image_id_fkey', 'cutouts', 'images', ['new_image_id'], ['id'])
    op.drop_index(op.f('ix_cutouts__upstream_bitflag'), table_name='cutouts')
    op.drop_index(op.f('ix_cutouts_filepath'), table_name='cutouts')
    op.create_index('ix_cutouts_filepath', 'cutouts', ['filepath'], unique=False)
    op.create_index('ix_cutouts_ref_image_id', 'cutouts', ['ref_image_id'], unique=False)
    op.create_index('ix_cutouts_new_image_id', 'cutouts', ['new_image_id'], unique=False)
    op.drop_column('cutouts', '_upstream_bitflag')
    op.drop_column('cutouts', 'y')
    op.drop_column('cutouts', 'x')
    # ### end Alembic commands ###
