"""migration

Revision ID: 7968122ba8de
Revises: 8e6b04e4d878
Create Date: 2018-11-21 10:00:11.914767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7968122ba8de'
down_revision = '8e6b04e4d878'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pitch_pitch'), 'pitch', ['pitch'], unique=False)
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_comment'), 'comment', ['comment'], unique=False)
    op.drop_index('ix_roles_email', table_name='roles')
    op.drop_index('ix_roles_username', table_name='roles')
    op.drop_table('roles')
    op.drop_constraint('users_role_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_role_id_fkey', 'users', 'roles', ['role_id'], ['id'])
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('bio', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('profile_pic_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name='roles_role_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    op.create_index('ix_roles_username', 'roles', ['username'], unique=False)
    op.create_index('ix_roles_email', 'roles', ['email'], unique=True)
    op.drop_index(op.f('ix_comment_comment'), table_name='comment')
    op.drop_table('comment')
    op.drop_index(op.f('ix_pitch_pitch'), table_name='pitch')
    op.drop_table('pitch')
    # ### end Alembic commands ###
