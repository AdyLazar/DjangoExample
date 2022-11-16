from django.db import models
from django.utils import timezone
from django.utils import timezone
from django.contrib.auth.models import User

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date}"
        

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=10)
    content = models.TextField(max_length=10)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # this is how we define a one-to-many relationship btw User and Post
    # the on_delete assures us that if a user is deleted ALL of its posts are deleted as well 
