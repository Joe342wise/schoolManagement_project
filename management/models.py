from django.db import models

# Create your models here.
class StudentTable(models.Model):
    student_id = models.AutoField(primary_key=True, db_column='stdIdpk')
    student_first_name = models.CharField(max_length=50, null=False ,db_column='stdFirstName')
    student_last_name = models.CharField(max_length=50, null=False, db_column='stdLastName')
    student_date_of_birth = models.DateField(blank=True, null=True, db_column='stdDateOfBirth')
    student_grade_level = models.IntegerField(blank=True, null=True, db_column='stdGradeLevel')
    student_emergency_contact_information = models.CharField(max_length=50, blank=True, db_column='stdEmergencyContactInfomation')

    def __str__(self):
        return f"{self.student_first_name} {self.student_last_name}"
    
    class Meta:
        app_label = "management"
        db_table = "tblStudents"

class TeacherTable(models.Model):
    teacher_id = models.AutoField(primary_key=True, db_column='techIdpk')
    teacher_first_name = models.CharField(max_length=50, null=False, db_column='techFirstName')
    teacher_last_name = models.CharField(max_length=50, null=False, db_column='techLastName')
    teacher_subject_tought = models.CharField(max_length=100, blank=True, db_column='techSubjectTought')
    teacher_email = models.EmailField(unique=True, db_column='techEmail')
    teacher_phone_number = models.CharField(max_length=20, blank=True, db_column='techPhoneNumber')

    def __str__(self):
        return f"{self.teacher_first_name} {self.teacher_last_name}"
    
    class Meta:
        app_label = "management"
        db_table = "tblTeachers"

class CourseTable(models.Model):
    course_id = models.AutoField(primary_key=True, db_column='cosIdpk')
    course_name = models.CharField(max_length=100, null=False, db_column='cosName')
    teacher_id = models.ForeignKey(TeacherTable, on_delete=models.CASCADE, db_column='techIdpk')

    def __str__(self):
        return self.course_name
    
    class Meta:
        app_label = "management"
        db_table = "tblCourses"

class EnrollmentTable(models.Model):
    enrollment_id = models.AutoField(primary_key=True, db_column='ermIpk')
    student_id = models.ForeignKey(StudentTable, on_delete=models.CASCADE, db_column='stdIdpk')
    course_id = models.ForeignKey(CourseTable, on_delete=models.CASCADE, db_column='cosIdpk')

    def __str__(self):
        return f"{self.student_id} {self.course_id}"
    
    class Meta:
        app_label = "management"
        db_table = "tblEnrollments"

class GradeTable(models.Model):
    grade_id = models.AutoField(primary_key=True, db_column='grdIdpk')
    student_id = models.ForeignKey(StudentTable, on_delete=models.CASCADE, db_column='stdIdpk')
    course_id = models.ForeignKey(CourseTable, on_delete=models.CASCADE, db_column='cosIdpk')
    grade = models.DecimalField(max_digits=5, decimal_places=2, db_column='grade')
    grade_date = models.DateField(blank=True, null=True, db_column='grdDate')

    def __str__(self):
        return f"{self.student_id} {self.course_id}"
    
    class Meta:
        app_label = "management"
        db_table = "tblGrades"

class UserTable(models.Model):
    user_id = models.AutoField(primary_key=True, db_column='userIdpk')
    user_name = models.CharField(max_length=100, unique=True, db_column='userName')
    user_email = models.EmailField(unique=True, db_column='Email')
    user_password = models.CharField(max_length=100, db_column='userPassword')
    user_role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('teacher', 'Teacher'), ('student', 'Student')], null=False, db_column='userRole')
    is_active = models.BooleanField(default=True, db_column='IsActive')

    def __str__(self):
        return self.user_name
    
    class Meta:
        app_label = "management"
        db_table = "tblUsers"

    