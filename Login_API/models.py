from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'user_profile')
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)
    description = models.TextField(blank = True)
    full_name = models.CharField(max_length = 255, blank = True)
    date_of_birth = models.DateField(blank = True, null = True)
    website = models.URLField(blank = True)
    facebook = models.URLField(blank = True)

    def __str__(self):
        return self.user.email


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'follower')
    following = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'following')

    def __str__(self):
        return '{} --follows--> {}'.format(self.following, self.follower)
