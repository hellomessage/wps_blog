from .home import HomeView
from .about import about
from .room import room
from .news import news
from .policy import terms, privacy, disclaimer
from .posts import PostListView, PostDetailView, new, create, edit, update, delete,\
        PostCommentCreateView, comments_edit, comments_update, comments_delete
from .naver_posts import naver_posts_list
from .auth import login, signup, logout, mypage
