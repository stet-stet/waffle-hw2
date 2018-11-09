from django.urls import path

from . import views
app_name = 'board'
urlpatterns = [
    # ##########################Views##########################
    path('nope/', views.four_oh_four, name='fourOhFour'),
    path('', views.Index, name='index'),
    path('read/<int:post_id>', views.Read, name='read'),
    path('write/', views.Write, name='write'),
    path('verify/<int:post_id>/', views.Verify, name='verify'),
    path('update/<int:post_id>/<str:password>/', views.Update, name='update'),
    path('delete/<int:post_id>', views.Delete, name='delete'),
    # ##########################Queries########################
    path('write/render/', views.PostBlogpostQuery, name='postblogpostquery'),
    path('update/get/<int:post_id>',
         views.HandleVerifyQuery, name="handleverifyquery"),
    path('delete/action/<int:post_id>',
         views.HandleDeleteQuery, name="handledeletequery"),
    path('update/action/<int:post_id>',
         views.HandleUpdateQuery, name="handleupdatequery")
]
