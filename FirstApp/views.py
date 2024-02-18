from django.shortcuts import render, redirect

from .forms import StudentModelForm
from .models import Student


# Create your views here.
def show_students_view(request):
    template_name = "FirstApp/show_students.html"
    all_students = Student.objects.all()
    context = {"all_students":all_students}
    return render(request, template_name, context)

def add_student_view(request):
    form = StudentModelForm()
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    template_name = "FirstApp/add_student.html"
    context = {"form":form}
    return render(request, template_name, context)

def update_student_view(request,i):
    student = Student.objects.get(id=i)
    form = StudentModelForm(instance=student)
    if request.method == "POST":
        form = StudentModelForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect("")
    template_name = "FirstApp/add_student.html"
    context = {"form":form}
    return render(request, template_name, context)

def delete_student_view(request,i):
    student = Student.objects.get(id=i)
    student.delete()
    return redirect("")



