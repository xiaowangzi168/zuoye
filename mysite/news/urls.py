from django.urls import path

from . import views

urlpatterns = [
    path('hw/create/', views.Homework(CreateView)),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]

