from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(verbose_name="Номер телефона", default='+375(__)-___-__-__', max_length=30)
    #добавить группу
    country = models.CharField(verbose_name="Страна", default='Belarus', max_length=50, blank=True, null=True)
    city = models.CharField(verbose_name="Город", max_length=50, blank=True, null=True)
    index = models.CharField(verbose_name="Индекс", max_length=12, blank=True, null=True)
    adress1 = models.CharField(verbose_name="Адрес 1", max_length=50, blank=True, null=True)
    adress2 = models.CharField(verbose_name="Адрес 2", max_length=50, blank=True, null=True)
    discription = models.TextField(verbose_name='Дополнительная информация', max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse('home')
    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"      

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(verbose_name="Номер телефона", default='+375(__)-___-__-__', max_length=30)
    #добавить группу
    country = models.CharField(verbose_name="Страна", default='Belarus', max_length=50, blank=True, null=True)
    city = models.CharField(verbose_name="Город", max_length=50, blank=True, null=True)
    index = models.CharField(verbose_name="Индекс", max_length=12, blank=True, null=True)
    adress1 = models.CharField(verbose_name="Адрес 1", max_length=50, blank=True, null=True)
    adress2 = models.CharField(verbose_name="Адрес 2", max_length=50, blank=True, null=True)
    discription = models.TextField(verbose_name='Дополнительная информация', max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"     

  
# class MyUser(User):
#     phone_number = models.CharField(verbose_name="Номер телефона", default='+375(__)-___-__-__', max_length=30)
#     discription = models.TextField(verbose_name='Дополнительная информация', max_length=200, blank=True, null=True)
    
#     def __str__(self) -> str:
#         return f"{self.username}"

#     def get_absolute_url(self):
#         return reverse('home')

# class Staff(models.Model):
#     login = models.CharField(verbose_name="Логин", max_length=30)
#     password = models.CharField(verbose_name="Пароль", max_length=30)
#     email = models.CharField(verbose_name="Адрес электронной почты", max_length=50)
#     first_name = models.CharField(verbose_name="Имя", max_length=30, blank=True, null=True)
#     surname = models.CharField(verbose_name="Фамилия", max_length=30, blank=True, null=True)
#     phone_number = models.CharField(verbose_name="Номер телефона", default='+375(__)-___-__-__', max_length=30)
#     customer_check = models.BooleanField(verbose_name="Покупатель", default=True) #нужна блокировка по-умолчанию

#     country = models.CharField(verbose_name="Страна", default='Belarus', max_length=50, blank=True, null=True)
#     city = models.CharField(verbose_name="Город", max_length=50, blank=True, null=True)
#     index = models.CharField(verbose_name="Индекс", max_length=12, blank=True, null=True)
#     adress1 = models.CharField(verbose_name="Адрес 1", max_length=50, blank=True, null=True)
#     adress2 = models.CharField(verbose_name="Адрес 2", max_length=50, blank=True, null=True)
#     discription = models.TextField(verbose_name='Дополнительная информация', max_length=200, blank=True, null=True)


#     def __str__(self) -> str:
#         return f"{self.login}"

#     def get_absolute_url(self):
#         return reverse('home')
#     class Meta:
#         verbose_name = "Сотрудник"
#         verbose_name_plural = "Сотрудники"        
