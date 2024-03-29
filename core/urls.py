from django.urls import path
from api.views.ListView import ClassList
from api.views.DeleteClassView import DeleteClassView
from api.views.createView import CreateClass

urlpatterns = [
    path("api/salas/", ClassList.as_view(), name="list classes"),
    path("api/salas/<id>/excluir/", DeleteClassView.as_view(), name="delete classes"),
    path("api/salas/criar/", CreateClass.as_view(), name="create classes")
]
