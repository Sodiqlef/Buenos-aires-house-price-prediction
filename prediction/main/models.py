from django.db import models

class PricePrediction(models.Model):
    NEIGHBORHOOD_CHOICES = [
        ('Chacarita', 'Chacarita'),
        ('Villa Luro', 'Villa Luro'),
        ('Caballito', 'Caballito'),
        ('Constitución', 'Constitución'),
        ('Once', 'Once'),
        ('Almagro', 'Almagro'),
        ('Palermo', 'Palermo'),
        ('Flores', 'Flores'),
        ('Belgrano', 'Belgrano'),
        ('Liniers', 'Liniers'),
        ('Villa Crespo', 'Villa Crespo'),
        ('San Cristobal', 'San Cristobal'),
        ('Congreso', 'Congreso'),
        ('Saavedra', 'Saavedra'),
        ('Balvanera', 'Balvanera'),
        ('Parque Avellaneda', 'Parque Avellaneda'),
        ('Recoleta', 'Recoleta'),
        ('San Telmo', 'San Telmo'),
        ('Nuñez', 'Nuñez'),
        ('Barrio Norte', 'Barrio Norte'),
        ('Parque Centenario', 'Parque Centenario'),
        ('Abasto', 'Abasto'),
        ('Centro / Microcentro', 'Centro / Microcentro'),
        ('Paternal', 'Paternal'),
        ('Mataderos', 'Mataderos'),
        ('Villa Lugano', 'Villa Lugano'),
        ('Coghlan', 'Coghlan'),
        ('Las Cañitas', 'Las Cañitas'),
        ('Villa Urquiza', 'Villa Urquiza'),
        ('Monserrat', 'Monserrat'),
        ('Villa Pueyrredón', 'Villa Pueyrredón'),
        ('Parque Patricios', 'Parque Patricios'),
        ('San Nicolás', 'San Nicolás'),
        ('Villa del Parque', 'Villa del Parque'),
        ('Boedo', 'Boedo'),
        ('Parque Chacabuco', 'Parque Chacabuco'),
        ('Barracas', 'Barracas'),
        ('Parque Chas', 'Parque Chas'),
        ('Colegiales', 'Colegiales'),
        ('Villa General Mitre', 'Villa General Mitre'),
        ('Villa Ortuzar', 'Villa Ortuzar'),
        ('Villa Devoto', 'Villa Devoto'),
        ('Floresta', 'Floresta'),
        ('Retiro', 'Retiro'),
        ('Versalles', 'Versalles'),
        ('Boca', 'Boca'),
        ('Puerto Madero', 'Puerto Madero'),
        ('Agronomía', 'Agronomía'),
        ('Monte Castro', 'Monte Castro'),
        ('Tribunales', 'Tribunales'),
        ('Villa Santa Rita', 'Villa Santa Rita'),
        ('Velez Sarsfield', 'Velez Sarsfield'),
        ('Villa Soldati', 'Villa Soldati'),
    ]

    surface_area = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    neighborhood = models.CharField(max_length=50, choices=NEIGHBORHOOD_CHOICES)
    predicted_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.neighborhood} | {self.surface_area} m² → ${self.predicted_price:,.0f}"
