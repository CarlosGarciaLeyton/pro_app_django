from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('login/', views.signin, name='login'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/pending/', views.tasks_pending, name='tasks_pending'),
    path('tasks/completed/', views.tasks_completed, name='tasks_completed'),
    path('tasks/new/', views.tasks_new, name='tasks_new'),
    path('tasks/<int:pk>/', views.tasks_detail, name='tasks_detail'),
    path('tasks/<int:pk>/edit/', views.tasks_edit, name='tasks_edit'),
    path('tasks/<int:pk>/complete/', views.tasks_complete, name='tasks_complete'),
    path('tasks/<int:pk>/delete/', views.tasks_delete, name='tasks_delete'),

]
