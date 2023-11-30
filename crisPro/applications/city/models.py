from django.db import models
from applications.country.models import Country


# Create your models here.
class City(models.Model):
    nameCity = models.CharField(
        'name', 
        null=False,
        max_length=30, 
        default=''
    )

    countryCode = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE
    )

    district = models.CharField(
        'District', 
        max_length=20, 
        null=False, 
        default=''
    )

    population = models.IntegerField(
        'Population', 
        max_length=11, 
        null=False, 
        default='0'
    )

    securityRate = models.DecimalField(
        'SecurityRate', 
        max_digits=3, 
        decimal_places=2, 
        null=False, 
        default='0.00'
    )

    pollutionRate = models.DecimalField(
        'PollutionRate', 
        max_digits=3, 
        decimal_places=2, 
        null=False, 
        default='0.00'
    )

    search_fields = ('name', 'countryCode',)
    list_filter = ('name',)
    class Meta:
            verbose_name = 'Nombre City'
            verbose_name_plural = 'Nombres Citys'
            ordering = ['name']
            unique_together = ('name', 'countryCode')
    def __str__(self):
        return self.name + ' - ' + self.countryCode + str(self.id)


