from django.db import models

from user.models import User

# Create your models here.
class Leave(models.Model):
    total_days=models.PositiveIntegerField()
    STATUS_CHOICES=[
        ('Pending','PENDING'),
        ('Approved','APPROVED'),
        ('Rejected','REJECTED')
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    days=models.PositiveIntegerField()
    reason=models.CharField(max_length=500, null= True)
    status=models.CharField(choices=STATUS_CHOICES, max_length=10)
    def __str__(self):
        return f'{self.user.username}`s-{self.title}'