from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    )

    LANGUAGE_ENGLISH = "eng"
    LANGUAGE_KOREAN = "kor"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "eng"), (LANGUAGE_KOREAN, "kor"))

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bip = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=20, blank=True)
    superhost = models.BooleanField(default=False)

