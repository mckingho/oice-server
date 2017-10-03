import sqlalchemy as sa
from modmod.models.base import Base


user_like_story = sa.Table(
    'user_like_story',
    Base.metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False),
    sa.Column('story_id', sa.Integer, sa.ForeignKey('story.id'), nullable=False),
    sa.UniqueConstraint('user_id', 'story_id', name='user_like_story_unique')
)
