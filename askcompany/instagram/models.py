from django.core.validators import MinLengthValidator
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    objects = models.Manager()
    message = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False,verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag',blank=True)
    

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('instagram:post_detail',args=[self.pk])
    6

    class Meta:
        ordering = ['-id']


    def message_length(self):
        return len(self.message)
    def strpath(self):
        return 'instagram/post/%Y/%m/%d'
    message_length.short_description = "메세지 글자수" 


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,
                                        limit_choices_to={'is_public':True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pass

class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)
    #post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name