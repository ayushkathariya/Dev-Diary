from django.urls import path
from .views import (
    HomePageView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)


urlpatterns = [
    # path("", HomePageView.as_view(), name="home"),
    path("", TaskListView.as_view(), name="task_list"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("new/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
]
