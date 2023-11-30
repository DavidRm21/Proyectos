from django.db import models
from applications.country.models import Country

# Create your models here.
class LanguageInfo(models.Model):
    language = models.CharField(
        'Language', 
        null=False,
        max_length=30
    )

    isOfficial = models.BooleanField(
        'active', 
        null=False,
        default=False
    )

    Percentege = models.DecimalField(
        'Percentage', 
        max_digits=4, 
        decimal_places=1,
        default='0.0' 
    )

    ISOCode = models.CharField(
        'ISOCode', 
        null=False,
        max_length=3,
        default=''
    )

    languageLevel = models.CharField(
        'LanguageLevel', 
        max_length=3,
        null=False,
        default=''
    )
    
    pais = models.ManyToManyField(Country)

    class Meta:
        verbose_name = 'LanguageInfo'
        verbose_name_plural = 'LanguagesInfo'
    def __str__(self):
        return self.LanguageInfo+' ' + self.LanguagesInfo + ' - ' + str(self.id)