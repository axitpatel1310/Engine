from django.db import models
from django.contrib.auth.models import User

class user(User):
    earnings = models.FloatField(default=0.0) 
    description = models.TextField(default="Apex Engine User")
    image = models.URLField(max_length=2000)
    payment_method = models.CharField(max_length=500)
    payment_info = models.TextField(default=' ')
    
    def __str__(self):
        return self.username

class Search(models.Model):
    query = models.TextField(max_length=200)
    result_link = models.URLField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)  
    date = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.query
    
class Ads(models.Model):
    title= models.CharField(max_length=50)
    description = models.TextField()
    tags = models.TextField()
    start = models.DateTimeField()
    End = models.DateTimeField()
    
class Ads_3rd_Party(models.Model):
    code = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
class UserActivity(models.Model):
    user = models.ForeignKey("app.user",on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
class gen_notification(models.Model):
    message = models.TextField()
    brodcast_date = models.DateTimeField()
    stop_date = models.DateTimeField()
    
class per_notification(models.Model):
    user = models.ForeignKey("app.user", on_delete=models.CASCADE)
    message = models.TextField()
    brodcast_date = models.DateTimeField()
    stop_date = models.DateTimeField()
    
class contact_us(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    