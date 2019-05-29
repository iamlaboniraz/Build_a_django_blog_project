from django.contrib import admin
from django.urls import path
from .views import(
	 post_list,
     post_create,
     post_detail,
     post_update,
     post_delete,
       )

urlpatterns = [
    path('',post_list, name='list'),
    path('create/',post_create, name='create'),
    path('<int:id>/',post_detail, name='detail'),
    path('<int:id>/update/',post_update, name='update'),
    path('<int:id>/delete/',post_delete, name='delete'),

    #     url(r'^$', post_list, name='list'),
    # url(r'^create/$', post_create),
    # url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),

    #     path('index/', views.index, name='main-view'),
    # path('bio/<username>/', views.bio, name='bio'),
    # path('articles/<slug:title>/', views.article, name='article-detail'),
    # path('articles/<slug:title>/<int:section>/', views.section, name='article-section'),
    # path('weblog/', include('blog.urls')),
    
]