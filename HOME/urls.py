from django.contrib import admin
from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path("", views.index, name="index"),
   path("contact/", views.contact, name="contact"),
   path("categories-page", views.categories_page, name="categories-page"),
   path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
   path('category/<slug:slug>/', views.category, name='category'),
   path('<slug:slug>/add_comment/',views.add_comment,name='add-comment'),
   path('search/', views.search_view, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
