from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'post_author')
    image = models.ImageField(upload_to = 'post_images')
    caption = models.CharField(max_length = 255, blank = True)
    upload_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-upload_date',]

    def __str__(self):
        return self.caption


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'post_like')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_like')
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '{} likes {} | {}'.format(self.user, self.post, self.date_created.strftime('%d %b %Y %H:%M:%S'))
