from django.shortcuts import render, redirect
from django.views import View
from api.forms import ClassForm
from api.serializers import ClassSerializer
from api.repositories import ClassRepository

class CreateClass(View):
    def get(self, request):
        class_form = ClassForm()
        return render(request, "form.html", {"form": class_form})
    
    def post(self, request):
        class_form = ClassForm(request.POST)
        if class_form.is_valid():
            serializer = ClassSerializer(data=class_form.cleaned_data)
            if serializer.is_valid():
                repository = ClassRepository(collectionName='classes')
                repository.insert(serializer.validated_data)
                return redirect('booklist') 
            else:
                print(serializer.errors)
        else:
            print(class_form.errors)

        return render(request, "main.html", {"form": class_form})
