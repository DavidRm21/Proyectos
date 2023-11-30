from django.db import models

# Create your models here.
class Country(models.Model):

    codigoPais = models.CharField(
        'code', 
        null=False,
        max_length=7
        )
    
    nombrePais = models.CharField(
        'Name', 
        null=False,
        max_length=50, 
        unique=True
        )
    
    continente = models.CharField(
        'Continent', 
        null=False,
        default='Asia'
        )
    
    region = models.CharField(
        'Region', 
        null=False,
        max_length=26, 
        default=''
        )
    
    superficie = models.DecimalField(
        'SurfaceArea', 
        null=False,
        max_digits=10, 
        decimal_places=2,
        default='0.0' 
        )
    independencia = models.SmallIntegerField(
        'IndepYear', 
        null=False,
        max_length=6, 
        )
    
    poblacion = models.BigIntegerField(
        'Population', 
        null=False,
        max_length=8,
        default='0' 
        )
    
    esperanzaVida = models.DecimalField(
        'LifeExpectancy', 
        null=False,
        max_digits=3, 
        decimal_places=1,
        default='0.0'
        )
    
    productoNacionalBruto = models.DecimalField(
        'GNP', 
        null=True,
        max_digits=10, 
        decimal_places=2,
        default='0.00' 
        )
    
    productoNacionalBrutoAnterior = models.DecimalField(
        'GNPOld', 
        null=True,
        max_digits=10, 
        decimal_places=2,
        default='0.00' 
        )
    
    nombreLocal = models.CharField(
        'LocalName', 
        null=False,
        default='', 
        max_length=50
        )
    
    formaGobierno = models.CharField(
        'GovernmentForm', 
        max_length=50,
        default=''
        )
    
    jefeEstado = models.CharField(
        'HeadOfState', 
        max_length=60,
        default='' 
        )
    
    capital = models.IntegerField(
        'Capital', 
        max_length=11,
        default='' 
        )
    
    areaCultivable = models.DecimalField(
        'ArableLandArea', 
        null=False,
        max_digits=10, 
        decimal_places=2,
        default='0.00' 
        )
    
    desarrolloHumano = models.DecimalField(
        'HDI', 
        max_digits=5, 
        decimal_places=3,
        default=''
        )
    
    monedaNacional = models.CharField(
        'NationalCurrency', 
        null=False,
        max_length=4,
        default='' 
        )
    
    search_fields = ('Name', 'code',)
    list_filter = ('Name',)
    class Meta:
            verbose_name = 'Pais'
            verbose_name_plural = 'Paises'
            ordering = ['Name']
            unique_together = ('Name', 'code')
    def __str__(self):
        return self.Name + ' - ' + self.code + str(self.id)

