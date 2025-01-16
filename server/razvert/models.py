from django.db import models


#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField("date published")


#class WeatherRequest(models.Model):
#    city = models.CharField(max_length=100)
#    forecast = models.TextField()
#    created_at = models.DateTimeField(auto_now_add=True)
#
#   def __str__(self):
#        return f"{self.city} - {self.created_at}"


class RandomUser(models.Model):
    gender = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
