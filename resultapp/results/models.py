from codecs import getreader
from django.db import models
import random
# Create your models here.

ExamSubject = [
    ('Agriculture', 'Agriculture'),
    ('Economics', 'Economics'),
    ('Biology', 'Biology'),
    ('English Language', 'English Language'),
    ('Mathamtics', 'Mathamtics'),
    ('Physical', 'Physical'),

]




ExamYear = [
    ('2000', '2000'),
    ('20002', '20002'),
    ('20003', '20003'),
    ('20004', '20004'),
    ('20005', '20005'),
    ('20006', '20006'),

]



ExamGrade = [
    ('A1', 'A1'),
    ('B1', 'B1'),
    ('C1', 'C1'),
    ('D1', 'D1'),
    ('E1', 'E1'),
    ('F9', 'F9'),

]

class Pinverification(models.Model):
    Pin = models.CharField(max_length=200)
    # Status = models.BigAutoField(default=True)


    def __str__(self):
        return self.Pin

def generateid():
    numbers = random.randint(908934, 90781234)
    return numbers





class Schoolstudent(models.Model):
    schoolexam =  models.CharField(max_length=200)


    def __str__(self):
        return self.schoolexam

# class ExamNo(models.Model):
   
class Allstudent(models.Model):
    sitnumber  =models.BigAutoField(primary_key=True, default=generateid)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

  
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)




class Resultstudent(models.Model):
    mystudentname = models.ForeignKey(Allstudent, on_delete=models.CASCADE)
    school =  models.ForeignKey(Schoolstudent, on_delete=models.CASCADE)
    examyear = models.DateField()
    Grade   = models.CharField(max_length=50, choices=ExamGrade, default='A')
    Subject  =models.CharField(max_length=50, choices=ExamSubject, default='English')


    class Meta:
        ordering = ('-Subject',)
  


    def __str__(self):
        return self.Grade


    



# student
# examNo
# School
# examyear
# PIN
# Grade 
# Subject 
