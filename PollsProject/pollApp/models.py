from django.db import models

# Create your models here.
class poll(models.Model):
    question = models.TextField()
    opt1 = models.CharField(max_length = 30)
    opt2 = models.CharField(max_length = 30)
    opt3 = models.CharField(max_length = 30) 
    opt1_count = models.IntegerField(default=0)
    opt2_count = models.IntegerField(default=0)
    opt3_count = models.IntegerField(default=0)

    def __str__(self):
        return self.question
    
    def sum(self):
        return self.opt1_count + self.opt2_count + self.opt3_count
