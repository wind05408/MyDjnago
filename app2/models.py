from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    comment = models.CharField(max_length=32)
    age = models.IntegerField()
    password = models.CharField(max_length=32,default="123456")

    # def __str__(self):
    #     s = {"id": self.id, "name": self.name, "email": self.email}
    #     return s
    def __str__(self):
        return self.name



