from django.db import models
RED = "RD"
BLACK = "BK"
BLUE = "BL"
BROWN = "BR"
CLEAR = "CL"
GREEN = "GN"
GREY = "GY"
ORANGE = "OR"
PURPLE = "PR"
WHITE = "WH"
YELLOW = "YL"
PINK = "PK"
COLOR = [
        (RED, "Rojo"),
        (BLACK, "Negro"),
        (BLUE, "Azul"),
        (BROWN, "Café"),
        (CLEAR, "Transparente"),
        (GREEN, "Verde"),
        (GREY, "Gris"),
        (ORANGE, "Naranja"),
        (PURPLE, "Púrpura"),
        (WHITE, "Blanco"),
        (YELLOW, "Amarillo"),
        (PINK, "Rosa"),
    ]

class Material(models.Model):
    MATERIAL_TAGS = [
        ("Paper", "Papel"),
        ("Rock", "Piedra"),
        ("Scissors", "Tijeras"),
    ]

    name = models.CharField(max_length=200, default="Material")
    material_type = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=1000, blank=True)
    measure_type = models.CharField(max_length=30, default="units")
    amount_per_measure = models.FloatField(default=0)
    price_per_measure = models.FloatField(default=0)
    # image = models.ImageField()
    color = models.CharField(max_length=100, choices=COLOR, blank=True)
    tags = models.CharField(max_length=100, choices=MATERIAL_TAGS, blank=True)

    def __str__(self):
        return str(self.name)


class Flower(models.Model):
    name = models.CharField(max_length=200, default="Material")
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    # image = models.ImageField()
    color = models.CharField(max_length=100, choices=COLOR, blank=True)
    tags = models.CharField(max_length=100, blank=True)
    materials_quantity = []
    materials_price = []
    
    def __str__(self):
        return str(self.name)

    def addMaterial(material: Material, quantity: float):
        Flower.materials_quantity.append(
            {str(material.name): quantity}
        )
        Flower.materials_price.append(
            {str(material.name): (quantity * material.price_per_measure)}
        )
        print("Material {{material.name}} successfully added!")
        # No sé si este método funciona. Debería revisarse para mayor seguridad


class Foliage(models.Model):
    name = models.CharField(max_length=200, default="Material")
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    # image = models.ImageField()
    color = models.CharField(max_length=100, choices=COLOR, blank=True)
    tags = models.CharField(max_length=100, blank=True)
    materials_quantity = []
    materials_price = []
    
    def __str__(self):
        return str(self.name)


class Arrangement(models.Model):
    WEDDING = "WD"
    BIRTHDAY = "BD"
    ANNIVERSARY = "AS"
    RELIGIOUS = "RG"
    CATEGORY = {
        (WEDDING, "Boda"),
        (BIRTHDAY, "Cumpleaños"),
        (ANNIVERSARY, "Aniversario"),
        (RELIGIOUS, "Religioso"),
    }

    name = models.CharField(max_length=200, default="Material")
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=100, blank=True, choices=CATEGORY)
    price = models.FloatField(default=0)
    # image = models.ImageField()
    tags = models.CharField(max_length=100, blank=True)
    flowers = []
    foliages = []
    
    def __str__(self):
        return str(self.name)