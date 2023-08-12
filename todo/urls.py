from django.urls import path
from todo.views import TodoListView, update_completed, TodoCompleteView, TodoCreateView,TodoDeleteView,TodoDetailView,TodoUpdateView

urlpatterns = [
    path("todos/", TodoListView.as_view(), name="show_todo"),
    path("complete/<int:id>/", update_completed, name="update_completed"),
    path("todos/complete", TodoCompleteView.as_view(), name="show_todo_complete"),
    path("todo/create/", TodoCreateView.as_view(), name="create_todo"),
    path("todo/update/<int:pk>/", TodoUpdateView.as_view(), name="update_todo"),
    path("todo/detail/<int:pk>/", TodoDetailView.as_view(), name="detail_todo"),
    path("todos/delete/<int:pk>/", TodoDeleteView.as_view(), name="delete_todo"),
]
