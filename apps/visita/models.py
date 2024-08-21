from django.db import models

class TipoPersona(models.Model):
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=25)
    
    def __str__(self):
        return self.descripcion

class TipoDocIdentidad(models.Model):
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=25)
    
    def __str__(self):
        return self.descripcion

class Visita(models.Model):
    visitante = models.CharField('Visitante', max_length=250)    
    visitante_doc = models.CharField('Nro. documento', max_length=30)
    entidad = models.CharField('Entidad', max_length=150)
    motivo = models.TextField('Motivo de visita')
    funcionario = models.CharField('Funcionario', max_length=350)
    funcionario_doc = models.CharField('Nro. documento', max_length=30)
    area = models.CharField('Área', max_length=300)
    sucursal = models.CharField('Sucursal', max_length=200)
    fecha = models.CharField('Fecha', max_length=12)
    hora_ing = models.CharField('Hora ing.', max_length=10)
    hora_salida = models.CharField('Hora sal.', max_length=10)
    
    def save(self, *args, **kwargs):
        self.visitante = self.visitante.strip().upper()
        self.entidad = self.entidad.strip().upper()
        self.motivo = self.motivo.strip().upper()
        self.funcionario = self.funcionario.strip().upper()
        self.area = self.area.strip().upper()
        self.sucursal = self.sucursal.strip().upper()
        super(Visita, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.visitante} {self.hora_ing}"
    
    class Meta:
        ordering = ['visitante', 'fecha','hora_ing']
    