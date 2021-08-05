from django.db import models
from django.contrib.auth.models import User


class Inventory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gold = models.BigIntegerField()
    def __str__(self):
        return self.user.username + "_Inventory"

class Item(models.Model):
    name = models.CharField(max_length=30)
    cost = models.BigIntegerField()
    description = models.CharField(max_length=30)
    image = models.ImageField()
    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    def __str__(self):
        return self.inventory.user.username + " - " + self.item.name

class Char(models.Model):
    name = models.CharField(max_length=30)
    base_force = models.BigIntegerField()
    base_resistence = models.BigIntegerField()
    base_agility = models.BigIntegerField()
    base_level = models.BigIntegerField()
    type_class = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = models.ImageField()
    def __str__(self):
        return self.name

class InventoryChar(models.Model):
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    char = models.ForeignKey('Char', on_delete=models.CASCADE)
    force = models.BigIntegerField()
    resistence = models.BigIntegerField()
    agility = models.BigIntegerField()
    level = models.BigIntegerField()
    skill_1 = models.ManyToManyField('Item')
    def __str__(self):
        return self.inventory.user.username + " - " + self.char.name





