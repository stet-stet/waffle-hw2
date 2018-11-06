from django.urls import path

from . import views
app_name = 'board'
urlpatterns = [
    path('', views.Index, name='index'),
    path('write/', views.Write, name='write'),
    path('read/<int:post_id>', views.Read, name='read'),
    path('update/<int:post_id>', views.Update, name='update'),
    path('delete/<int:post_id>', views.Delete, name='delete'),
    path('delete/action/<int:post_id>',
         views.HandleDeleteQuery, name="handledeletequery"),
    path('update/action/<int:post_id>',
         views.HandleUpdateQuery, name="handleupdatequery"),
    path('nope/', views.four_oh_four, name='fourOhFour'),
    path('write/render/', views.PostBlogpostQuery, name='postblogpostquery')
    # delete is to be implemented separately.
]
