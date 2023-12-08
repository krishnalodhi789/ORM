from django.db import models

# Create your models here.
class SchoolClasses(models.Model):
    class_name = models.CharField(max_length=30,primary_key=True)
    location = models.CharField(max_length=30)
    
    def __str__(self):
        return self.class_name

class Student(models.Model):
    student_class = models.ForeignKey(SchoolClasses, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    roll_no = models.IntegerField(unique=True)
    age = models.IntegerField()
    
    def __str__(self):
        return self.student_name
    
class Book(models.Model):
    book_name = models.CharField(max_length=30, primary_key=True)
    book_no = models.IntegerField()
    author_name = models.CharField(max_length=30)
    
    def _str__(self):
        return self.book_name

class BookManage(models.Model):
    student = models.ManyToManyField(Student)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField()
    submit_date = models.DateTimeField(null=True,blank=True)
    
    
    
    
    
    