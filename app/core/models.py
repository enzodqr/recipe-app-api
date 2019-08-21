from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):
    """ This class provides the helper functions for
        creating a user or a super user"""

    def create_user(self, email, password=None, **extra_fields):
        """Creates and save a new user"""
        """ The **extra_fields takes any of the extra functions the are
            pass in"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # crates and save all the data in the user model
        user.set_password(password)
        # encrypted the password
        user.save(using=self._db)
        # saves the model
        # for supporting multiple data bases

        return user

    def create_superuser(self, email, password):
        """Creates and save a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
