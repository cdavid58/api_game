from django.db import models

class Rol(models.Model):
	name = models.CharField(max_length= 35)

	def __str__(self):
		return self.name

class Skill(models.Model):
	name = models.CharField(max_length = 150)
	additional_damage = models.IntegerField()

	def __str__(self):
		return self.name


class Hero(models.Model):
	hp = models.IntegerField()
	physical_damage = models.IntegerField()
	magic_damage = models.IntegerField()
	attack_speed = models.IntegerField()
	armor = models.IntegerField()
	magic_resist = models.IntegerField()
	movement_speed = models.IntegerField()
	skill = models.ManyToManyField(Skill)
	rol = models.ForeignKey(Rol,on_delete=models.CASCADE)

