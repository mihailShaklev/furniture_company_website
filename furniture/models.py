from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kitechen_posts')
    updated_on = models.DateTimeField(auto_now=True)
    description = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    project_type = models.CharField(max_length=20, choices=[('kitchen', 'kitchen'), ('furniture', 'furniture')], default='kitchen')
    main_image = models.ImageField(upload_to='uploads', default='null')
    image_1 = models.ImageField(upload_to='uploads', default='null')
    image_2 = models.ImageField(upload_to='uploads', default='null')
    image_3 = models.ImageField(upload_to='uploads', default='null')
    image_4 = models.ImageField(upload_to='uploads', default='null')
    image_5 = models.ImageField(upload_to='uploads', default='null')
    image_6 = models.ImageField(upload_to='uploads', default='null')


    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title


