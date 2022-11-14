from django.views.generic import View, ListView
from django.shortcuts import render, redirect

from myapp.forms import ContactForm
from myapp.models import Student

class StudentDetails(View):
    
    def get(self, request):
        form = ContactForm() 
        return render(request, "myapp/student.html", {"form": form})
    
    def post(self, request):
        form = ContactForm(request.POST) 
        if form.is_valid():
            instance = form.save()
            return render(request, "myapp/preview.html", {"data": instance})
        else:
            return render(request, "myapp/student.html", {"form": form})

class StudentListDetails(ListView):
    template_name = "myapp/student-list.html"
    context_object_name = "records"
    queryset = Student.objects.all()

class StudentUpdateDetails(View):

    def get(self, request, id):
        form = ContactForm(instance=Student.objects.get(id=id))
        return render(request, "myapp/student.html", {"form": form})
    
    def post(self, request, id):
        form = ContactForm(request.POST, instance=Student.objects.get(id=id))
        if form.is_valid():
            instance = form.save()
            return redirect("list-student")
        else:
            return render(request, "myapp/student.html", {"form": form})