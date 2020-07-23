from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    Gender_choice = (
        ('M', 'Male',),
        ('F', 'Female',),
        ('O', 'LGBTQ',),
        ('N', 'Prefer Not To Say',),

    )
    username = models.CharField('username', max_length=50, unique=True,
        help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
             'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField(unique=True, blank=False, error_messages={
                                                            'unique': "A user with that email already exists.",
                                                        })
    gender = models.CharField(max_length=1, choices=Gender_choice)
    status = models.BooleanField(default=False)
    about = models.TextField(blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "gender"]

    def __unicode__(self):
        return self.email
