from django.views import View
from django.shortcuts import render, redirect
from api.repositories import ClassRepository
from api.serializers import ClassSerializer, ClassEntity
from datetime import datetime


class ClassGenerate(View):
    def get(self, request):
        repository = ClassRepository(collectionName='classes')
        classes = ClassEntity(
            classname="Sala ADS-1",
            details="Sala dos programadores tlg",
            time=datetime.now(),
            status=True
        )
        serializer = ClassSerializer(data=classes.__dict__)
        if (serializer.is_valid()):
            repository.insert(serializer.data)
        else:
            print(serializer.errors)
        return redirect('booklist')