from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=(255),
        verbose_name="Название сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to="logo/"
    )
    tel = models.CharField(
        max_length=30,
        verbose_name="Мои контакты"
    )
    students = models.IntegerField(
        verbose_name="Количество студентов",
        blank=True,null=True
    )
    email = models.EmailField(
    max_length=254, 
    unique=True,  
    blank=False,  
    null=False, 
    verbose_name="Email Address" 
    )
    about = models.TextField(
        verbose_name="О нас"
    )
    resource = models.TextField(
        verbose_name="Наши ресурсы"
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
