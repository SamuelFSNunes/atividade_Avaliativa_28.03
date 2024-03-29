from django.urls import path
from api.views.ListView import ClassList
from api.views.DeleteClassView import DeleteClassView
from api.views.GenerateView import ClassGenerate

urlpatterns = [
    path("api/salas/", ClassList.as_view(), name="booklist"),
    path("api/salas/<id>/excluir/", DeleteClassView.as_view(), name="delete classes"),
    path("api/salas/generate/", ClassGenerate.as_view(), name="generatebooks")
]
