"""migrate produto

Revision ID: cbc2042357a5
Revises: b495250c4ad5
Create Date: 2024-01-02 13:59:51.087297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbc2042357a5'
down_revision = 'b495250c4ad5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('marca', sa.String(length=20), nullable=False),
    sa.Column('modelo', sa.String(length=20), nullable=False),
    sa.Column('descricao', sa.String(length=120), nullable=False),
    sa.Column('lance_inicial', sa.Float(), nullable=False),
    sa.Column('lance_adicional', sa.Float(), nullable=False),
    sa.Column('vendido', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produto')
    # ### end Alembic commands ###
