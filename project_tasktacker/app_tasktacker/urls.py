from xml.dom.minidom import Document
from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('task/create/', views.task_create, name= 'task.create'),
    path('task/update/', views.task_update, name= 'task.update'),
    path('tasks/', views.task_index, name="task.index"),
    path('tasks/edit/<int:id>', views.task_edit, name="task.edit"),
    path('tasks/show/<int:id>', views.task_show, name="task.show"),
    path('tasks/delete/<int:id>', views.task_delete, name="task.delete"),
    path('user/login/', views.user_login, name='user.login'),
    path('user/register/', views.user_register, name='user.register'),
    path('user/logout/', views.user_logout, name='user.logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)