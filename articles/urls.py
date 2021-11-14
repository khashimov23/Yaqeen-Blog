from django.urls import path


from . import views


app_name = 'blog'

urlpatterns = [
    path('new/', views.ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name="article_edit"),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    
    
    path('',views.post_list,name="post_list"),
    path('<slug:post>/',views.post_detail,name="post_detail"),
    path('comment/reply/', views.reply_page, name="reply"),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'),    
]

