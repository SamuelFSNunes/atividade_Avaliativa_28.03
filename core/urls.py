from django.urls import path
from api.views.ListView import ClassList , WeatherReset
from api.views.DeleteClassView import DeleteClassView
from api.views.GenerateView import ClassGenerate
from api.views.createView import CreateClass

urlpatterns = [
    path("api/salas/", ClassList.as_view(), name="booklist"),
    path("api/salas/<id>/excluir/", DeleteClassView.as_view(), name="deletebooks"),
    path("api/salas/generate/", ClassGenerate.as_view(), name="generatebooks"),
    path("api/salas/criar/", CreateClass.as_view(), name="create classes"),
    path("api/deleteall", WeatherReset.as_view(), name="deleteall")
]
