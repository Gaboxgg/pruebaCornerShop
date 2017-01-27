from django.db import models

# Create your models here.
#Actividad permite registrar diferentes actividades bajo su descripcion
#El codigo lo coloque como un extra ya que es una buena practica.
class Actividad(models.Model):
    descripcion = models.CharField(max_length=200)
    codigo = models.CharField(max_length=100,unique=True)

    def __unicode__(self):
        return u"Actividad: %s" % (self.descripcion)

#Se puede registrar los Shoppers con que se trabaja.
#Se pueden ir tambien agregando los shoppers nuevos.
class Shopper(models.Model):
    nombre = models.CharField(max_length=100)
    nro_telefono = models.CharField(max_length=50)
    
    def __unicode__(self):
        return u"Mi nombre es %s" % (self.nombre)

#Feedbacks posee dos foraneas que van indicar que shopper dio el feedback
#Y bajo que actividad.
class Feedbacks (models.Model):
    feedback = models.CharField(max_length=200)
    fk_shopper = models.ForeignKey(Shopper, on_delete=models.CASCADE)
    fk_actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"Feedback: %s" % (self.feedback)
