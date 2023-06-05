"""models fix

Revision ID: 86cef191051f
Revises: e1de071dea54
Create Date: 2023-06-05 11:35:19.357929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86cef191051f'
down_revision = 'e1de071dea54'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('buyback_data', sa.Column('key_word', sa.String(), nullable=False))
    op.add_column('buyback_data', sa.Column('product_link', sa.String(), nullable=False))
    op.add_column('buyback_data', sa.Column('item_size', sa.String(), nullable=True))
    op.add_column('buyback_data', sa.Column('bb_amount', sa.Integer(), nullable=False))
    op.drop_constraint('buyback_data_user_id_fkey', 'buyback_data', type_='foreignkey')
    op.drop_column('buyback_data', 'wb_keyword')
    op.drop_column('buyback_data', 'approved_amount')
    op.drop_column('buyback_data', 'user_id')
    op.drop_column('buyback_data', 'ordered_amount')
    op.drop_column('buyback_data', 'pc_url')
    op.add_column('user_account', sa.Column('order', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'user_account', ['user_id'])
    op.create_foreign_key(None, 'user_account', 'buyback_data', ['order'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_account', type_='foreignkey')
    op.drop_constraint(None, 'user_account', type_='unique')
    op.drop_column('user_account', 'order')
    op.add_column('buyback_data', sa.Column('pc_url', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('buyback_data', sa.Column('ordered_amount', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('buyback_data', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('buyback_data', sa.Column('approved_amount', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('buyback_data', sa.Column('wb_keyword', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_foreign_key('buyback_data_user_id_fkey', 'buyback_data', 'user_account', ['user_id'], ['user_id'])
    op.drop_column('buyback_data', 'bb_amount')
    op.drop_column('buyback_data', 'item_size')
    op.drop_column('buyback_data', 'product_link')
    op.drop_column('buyback_data', 'key_word')
    # ### end Alembic commands ###