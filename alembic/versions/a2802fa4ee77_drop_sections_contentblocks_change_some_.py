"""Drop Sections, ContentBlocks, change some fields

Revision ID: a2802fa4ee77
Revises: f2554d34c8c4
Create Date: 2023-01-27 17:32:55.878926

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a2802fa4ee77'
down_revision = 'f2554d34c8c4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_completed_content_blocks_id_', table_name='completed_content_blocks')
    op.drop_table('completed_content_blocks')
    op.drop_index('ix_student_courses_id_', table_name='student_courses')
    op.drop_table('student_courses')
    op.drop_index('ix_content_blocks_id_', table_name='content_blocks')
    op.drop_table('content_blocks')
    op.drop_index('ix_profiles_id_', table_name='profiles')
    op.drop_table('profiles')
    op.drop_index('ix_sections_id_', table_name='sections')
    op.drop_table('sections')
    op.drop_index('ix_courses_id_', table_name='courses')
    op.drop_table('courses')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_id_', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id_', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('fist_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('bio', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id_'], name='profiles_user_id_fkey'),
    sa.PrimaryKeyConstraint('id_', name='profiles_pkey')
    )
    op.create_index('ix_profiles_id_', 'profiles', ['id_'], unique=False)
    op.create_table('content_blocks',
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id_', sa.INTEGER(), server_default=sa.text("nextval('content_blocks_id__seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('url', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('section_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('type_', postgresql.ENUM('lesson', 'quiz', 'assignment', name='contenttype'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['section_id'], ['sections.id_'], name='content_blocks_section_id_fkey'),
    sa.PrimaryKeyConstraint('id_', name='content_blocks_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_content_blocks_id_', 'content_blocks', ['id_'], unique=False)
    op.create_table('courses',
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id_', sa.INTEGER(), server_default=sa.text("nextval('courses_id__seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id_'], name='courses_user_id_fkey'),
    sa.PrimaryKeyConstraint('id_', name='courses_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_courses_id_', 'courses', ['id_'], unique=False)
    op.create_table('student_courses',
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id_', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id_'], name='student_courses_course_id_fkey'),
    sa.ForeignKeyConstraint(['student_id'], ['users.id_'], name='student_courses_student_id_fkey'),
    sa.PrimaryKeyConstraint('id_', name='student_courses_pkey')
    )
    op.create_index('ix_student_courses_id_', 'student_courses', ['id_'], unique=False)
    op.create_table('completed_content_blocks',
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id_', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('content_block_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('url', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('feedback', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('grade', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['content_block_id'], ['content_blocks.id_'], name='completed_content_blocks_content_block_id_fkey'),
    sa.ForeignKeyConstraint(['student_id'], ['users.id_'], name='completed_content_blocks_student_id_fkey'),
    sa.PrimaryKeyConstraint('id_', name='completed_content_blocks_pkey')
    )
    op.create_index('ix_completed_content_blocks_id_', 'completed_content_blocks', ['id_'], unique=False)
    op.create_table('sections',
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id_', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id_'], name='sections_course_id_fkey'),
    sa.PrimaryKeyConstraint('id_', name='sections_pkey')
    )
    op.create_index('ix_sections_id_', 'sections', ['id_'], unique=False)
    op.create_table('users',
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id_', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('role', postgresql.ENUM('teacher', 'student', name='role'), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_', name='users_pkey')
    )
    op.create_index('ix_users_id_', 'users', ['id_'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
    # ### end Alembic commands ###