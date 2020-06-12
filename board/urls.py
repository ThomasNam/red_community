from django.urls import path

from board import views

urlpatterns = [
    path('list/', views.board_list),
    path('detail/<int:pk>', views.board_detail),
    path('write/', views.board_write)
]