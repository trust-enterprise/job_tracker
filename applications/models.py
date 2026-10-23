from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JobApplication(models.Model):

    STATUS_CHOICES = [
    ('Applied', 'Applied'),
    ('Interview', 'Interview'),
    ('Rejected', 'Rejected'),
    ('Selected', 'Selected'),
    ]
    
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    status = models.CharField(max_length=15, choices = STATUS_CHOICES, default="Applied")
    applied_date = models.DateField(auto_now=False, auto_now_add=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return {{self.title}}