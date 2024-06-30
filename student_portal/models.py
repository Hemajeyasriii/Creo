# from django.db import models

# # Create your models here.
# from django.db import models
# class Student(models.Model):
#   Name=models.CharField(max_length=50)
#   Age=models.IntegerField()
#   Email=models.EmailField()
#   city=models.TextField(blank=True)


#   class Subject_Marks(models.Model):
#     student = models.ForeignKey(student, on_delete=models.CASCADE)
#     Language_1=models.IntegerField()
#     Language_2=models.IntegerField()
#     Acting=models.IntegerField()
#     Dance=models.IntegerField()


from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Email = models.EmailField()
    city = models.TextField()

  

class Subject_Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Language_1 = models.IntegerField()
    Language_2 = models.IntegerField()
    Acting = models.IntegerField()
    Dance = models.IntegerField()


