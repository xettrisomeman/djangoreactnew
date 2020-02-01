from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(_("first_name"), max_length=50)
    last_name = models.CharField(_("last_name"), max_length=50)
    email= models.EmailField(_("Email Address"), max_length=254, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name' , 'last_name']

    object = CustomUserManager()

    def username(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email
    

class Posts(models.Model):
    title = models.CharField(_("Title"), max_length=150)
    content = models.TextField(_("Add Your Content"))
    created_at = models.DateTimeField(_("Created Time") , editable=False)
    modified_at = models.DateTimeField(_('Modified Time') ,auto_now=True)

    class Meta:
        db_table = 'Posts'
        verbose_name_plural = "Posts"

    def save(self):
        if not self.id:
            self.created_at =now()
        return super().save()

