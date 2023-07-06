from django.urls import path
from .views import  HomePage, NothingPage, PostCreate, PostDetail, PostDelete, PostUpdate, GameDetail

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('game/<str:game>/', GameDetail.as_view(), name='game_detail'),
    path('nothing/', NothingPage.as_view(), name='nothing'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('post/<int:pk>/update', PostUpdate.as_view(), name='post_update'),
]