from django.shortcuts import render
from rest_framework import status, viewsets
from management.models import StudentTable as Student, TeacherTable as Teacher, CourseTable as Course, EnrollmentTable as Enrollment, GradeTable as Grade, UserTable as User
from management.serializers import StudentSerializer, TeacherSerializer, CourseSerializer, EnrollmentSerializer, GradeSerializer, UserSerializer

# Create your views here.
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentView(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class GradeView(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer