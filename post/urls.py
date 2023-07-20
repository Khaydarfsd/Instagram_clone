from django.urls import path
from .views import PostListAPIView, PostCreateView, PostRetrieveUpdateDestroyView, PostCommentListView, \
    PostCommentCreateView, CommentListCreateApiView


urlpatterns = [
    path('list/', PostListAPIView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<uuid:pk>/', PostRetrieveUpdateDestroyView.as_view()),
    path('<uuid:pk>/comments/', PostCommentListView.as_view()),
    path('<uuid:pk>/comments/create/', PostCommentCreateView.as_view()),
    path('comments/', CommentListCreateApiView.as_view()),
]