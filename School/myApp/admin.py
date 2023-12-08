from django.contrib import admin
from .models import SchoolClasses,Student,Book,BookManage
# Register your models here.
# admin.site.register(SchoolClasses)
# admin.site.register(Student)
# admin.site.register(Book)
# admin.site.register(BookManage)

    
@admin.register(SchoolClasses)
class SchoolClassesAdmin(admin.ModelAdmin):
    list_display=('class_name','location')
    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('student_name','student_class','roll_no',"age")
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('book_name','author_name','book_no')
    
    
@admin.register(BookManage)
class BookManageAdmin(admin.ModelAdmin):
    list_display=('id','book_name','issue_date',"submit_date")
