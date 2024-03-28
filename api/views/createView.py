from django.shortcuts import render, redirect
from django.views import View
from forms import ClassForm
from serializers import ClassSerializer
from repositories import ClassRepository

class ClassCriar(View):
    def get(self, request):
        class_form = ClassForm()
        return render(request, "class_form.html", {"form": class_form})
    
    def post(self, request):
        class_form = ClassForm(request.POST)
        if class_form.is_valid():
            serializer = ClassSerializer(data=class_form.cleaned_data)
            if serializer.is_valid():
                repository = ClassRepository(collectionName='class')
                repository.insert(serializer.validated_data)
                return redirect('createView') 
            else:
                print(serializer.errors)
        else:
            print(class_form.errors)

        return render(request, "class_form.html", {"form": class_form})
