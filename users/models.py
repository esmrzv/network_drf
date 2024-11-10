from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Почта", unique=True)
    phone = models.CharField(
        max_length=50, verbose_name="Телефон", null=True, blank=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email}, {self.phone}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
