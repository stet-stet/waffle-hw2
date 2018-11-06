from django.urls import path

from . import views
app_name = 'board'
urlpatterns = [
    path('', views.Index, name='index'),
    path('write/', views.Write, name='write'),
    path('read/<int:post_id>', views.Read, name='read'),
    path('update/<int:post_id>', views.Update, name='update'),
    path('delete/<int:post_id>', views.Delete, name='delete'),
    path('delete/action/<int:post_id>', views.Delete_action, name="deleteAction"),
    path('nope/', views.four_oh_four, name='fourOhFour'),
    # delete is to be implemented separately.
]
