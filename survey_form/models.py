from django.db import models
# from requests import session

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=255)

    def __str__(self):
        return self.cat_name # TODO

class Area(models.Model):
    area_name = models.CharField(max_length=255)

    def __str__(self):
        return self.area_name # TODO

class Channel(models.Model):
    cat = models.ForeignKey(Category, on_delete = models.CASCADE)
    channel_name = models.CharField(max_length=255)

    def __str__(self):
        return self.channel_name # TODO

class Shows(models.Model):
    cat = models.ForeignKey(Category, on_delete = models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete = models.CASCADE)
    show_name = models.CharField(max_length=255)

    def __str__(self):
        return self.show_name # TODO

class ServayEntry(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    sessionId = models.CharField(max_length=255)
    show = models.ForeignKey(Shows, on_delete = models.CASCADE , related_name = "show_survey")
    area = models.ForeignKey(Area, on_delete = models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    name = models.CharField(max_length=50,null=True,blank=True)



    def __str__(self):
        return self.sessionId # TODO