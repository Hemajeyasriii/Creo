
from django.shortcuts import render, get_object_or_404
from .models import Student, Subject_Marks

def student_detail(request, student_id):

    student = get_object_or_404(Student, pk=student_id)
    subject_marks = Subject_Marks.objects.filter(student=student)

    list = {
        'student': student,
        'subject_marks': subject_marks,
    }
    return render(request, 'student_detail.html', list)

