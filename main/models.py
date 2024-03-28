from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

class Articles(models.Model):
    object = None
    title = models.CharField("Name news", max_length=50)
    anons = models.CharField('News', max_length=250)
    full_text = models.TextField('Announce')
    date = models.DateTimeField('Дата публикации')
    def __str__(self):
        return self.title
    slug = models.SlugField(unique=True, max_length=100, blank=True, null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Генерация слага на основе заголовка статьи
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    from django.utils.text import slugify

class SampleModel(models.Model):
    login = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class MyModel(models.Model):
    my_file = models.FileField(upload_to='files/')
    my_image = models.ImageField(upload_to='images/')

class VisitedPage(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    page_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
def __str__(self):
    return f"{self.user.username} visited {self.page_name} at {self.timestamp}"

