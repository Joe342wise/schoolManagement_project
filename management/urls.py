from django.urls import path, include
from rest_framework.routers import DefaultRouter
from management.views import StudentView, TeacherView, CourseView, EnrollmentView, GradeView, UserView

router = DefaultRouter()
router.register(r'students', StudentView)
router.register(r'teachers', TeacherView)
router.register(r'courses', CourseView)
router.register(r'enrollments', EnrollmentView)
router.register(r'grades', GradeView)
router.register(r'users', UserView)

urlpatterns = [
    path('', include(router.urls)),
]

