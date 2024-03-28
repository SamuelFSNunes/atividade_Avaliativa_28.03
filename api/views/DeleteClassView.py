from django.views import View
from django.shortcuts import render, redirect
from api.repositories import ClassRepository
from api.serializers import ClassSerializer, ClassEntity

class DeleteClassView(View):
    def get(self, request): 
        repository = ClassRepository(collectionName='weathers')
        repository.deleteOne(1)
        return redirect('ClassView')