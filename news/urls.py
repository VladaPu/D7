from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, NewsCreate, ArticlesCreate, PostUpdate, PostDelete, subscriptions


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('article/create/', ArticlesCreate.as_view(), name='article_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path ('subscriptions/', subscriptions, name='subscriptions')
]