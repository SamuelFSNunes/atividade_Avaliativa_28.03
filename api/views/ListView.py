from django.views import View
from django.shortcuts import render, redirect
from api.repositories import ClassRepository
from api.serializers import ClassSerializer, ClassEntity
from datetime import datetime


class ClassList(View):
    def get(self, request):
        repository = ClassRepository(collectionName='classes')
        classes = list(repository.getAll())
        serializer = ClassSerializer(data=classes, many=True)
        if (serializer.is_valid()):
            books = serializer.save()
            print(serializer.data)
        else:
            print(serializer.errors)
        return render(request, "home.html", {"books":books})
    
class WeatherReset(View):
    def get(self, request): 
        repository = ClassRepository(collectionName='classes')
        repository.deleteAll()

        return redirect('booklist')