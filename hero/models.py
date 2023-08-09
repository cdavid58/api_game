from django.db import models

class Rol(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()  
    additional_damage = models.IntegerField()

    def __str__(self):
        return self.name

class Hero(models.Model):
    hp = models.PositiveIntegerField()
    physical_damage = models.PositiveIntegerField()
    magic_damage = models.PositiveIntegerField()
    attack_speed = models.FloatField()  
    armor = models.PositiveIntegerField()
    magic_resist = models.PositiveIntegerField()
    movement_speed = models.PositiveIntegerField()
    skills = models.ManyToManyField(Skill, blank=True)  
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rol} - HP: {self.hp}"

    class Meta:
        ordering = ['rol']  
