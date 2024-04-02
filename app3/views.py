from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from app3.models import Course, FormData,Department

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phno = request.POST.get('phno')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department_id=request.POST.get('department')
        course_id = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials = request.POST.getlist('material')
        department_instance = get_object_or_404(Department, pk=department_id)
        course_instance = get_object_or_404(Course, pk=course_id)

        form_data = FormData(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phno=phno,
            email=email,
            address=address,
            department = department_instance,
            course=course_instance,
            purpose=purpose,
        )
        form_data.save()

        messages.success(request, 'Form submitted successfully!')
        return redirect('app3:form')
    else:
        return render(request, 'form.html')