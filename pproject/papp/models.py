from django.db import models

# Create your models here.
class place(models.Model):

    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics1')
    desc=models.TextField()
    #def __str__(self):
       # return self.name


from django.db import models
