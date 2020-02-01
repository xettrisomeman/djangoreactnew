from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _ 



class CustomUserManager(BaseUserManager):

    def create_user(self,first_name , last_name , email,password , **extra):

        if not first_name and last_name:
            raise ValueError(_('Name is required'))
        if not email:
            raise ValueError(_('Email is required'))

        #make email all small letter
        email = self.normalize_email(email)
        user = self.model(first_name = first_name , last_name=last_name , email=email , **extra)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,first_name,last_name, email,password,**extra):

        extra.setdefault('is_superuser' , True)
        extra.setdefault('is_active' , True)
        extra.setdefault('is_staff' , True)

        if not extra.get('is_active') is True:
            raise ValueError(_('Is staff should be True'))
        if not extra.get('is_superuser') is True:
            raise ValueError(_('Is superuser is set to be True'))

        return self.create_user(first_name , last_name , email,password , **extra)

