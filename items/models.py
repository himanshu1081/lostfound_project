from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('Electronics','Electronics'),
    ('Books','Books'),
    ('Clothing','Clothing'),
    ('ID Card','ID Card'),
    ('Other','Other'),
]

class LostItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=120)
    date_lost = models.DateField()
    image = models.ImageField(upload_to='lost_images/', blank=True, null=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class FoundItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=120)
    date_found = models.DateField()
    image = models.ImageField(upload_to='found_images/', blank=True, null=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return self.title
