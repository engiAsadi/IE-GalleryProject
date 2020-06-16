from django.db import models
from account.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200) #, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True) #, verbose_name='آدرس پست')
    description = models.TextField() # verbose_name="محتوا")
    photo = models.ImageField(upload_to="images") #, verbose_name='تصویر')
    user = models.ForeignKey(User, on_delete=models.CASCADE) #, verbose_name='کاربر')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.title, self.user)
