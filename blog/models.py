from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=["-timestamp", "title"]
