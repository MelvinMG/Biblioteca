from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Perfil(models.Model):
    Genero_Choices = [('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro'),('P','Prefiero no decirlo')]
    Rol_Choices = [('E', 'Estudiante'), ('M', 'Maestro'), ('A', 'Administrativo')]  # Opciones de roles
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    ap_Paterno = models.CharField(max_length=100)
    ap_Materno = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    genero = models.CharField(max_length=1, choices=Genero_Choices, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_perfil', blank=True, null=True)
    rol = models.CharField(max_length=1, choices=Rol_Choices)  # Campo para definir el rol
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.nombre + ' ' + self.ap_Paterno

    
from django.db import models

# Clase base abstracta para Materiales de la Biblioteca
class material_Biblioteca(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha = models.DateField()
    foto = models.ImageField(upload_to='fotos_material', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # No se creará una tabla en la base de datos

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

# Modelo para Libros
class Libro(material_Biblioteca):
    genero = models.CharField(max_length=100, blank=True, null=True)
    editorial = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'libros'
        verbose_name_plural = 'Libros'

    def get_tipo(self):
        return "Libro"

# Modelo para Revistas
class Revista(material_Biblioteca):
    volumen = models.CharField(max_length=50,blank=True, null=True)

    class Meta:
        db_table = 'revistas'
        verbose_name_plural = 'Revistas'

    def get_tipo(self):
        return "Revista"

# Modelo para Tesis
class Tesis(material_Biblioteca):

    class Meta:
        db_table = 'tesis'
        verbose_name_plural = 'Tesis'

    def get_tipo(self):
        return "Tesis"


class Prestamo(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=True, blank=True)
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE, null=True, blank=True)
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE, null=True, blank=True)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.perfil.nombre + ' ' + self.material.titulo
    
    class Meta:
        db_table = 'Prestamo'
        verbose_name_plural = 'Prestamos'

class historial_Multas(models.Model):
    Estado_Choices = [('P', 'Pagado'), ('N', 'No Pagado')]
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    fecha_multa = models.DateField()
    estado=models.CharField(max_length=1,choices=Estado_Choices)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prestamo.perfil.nombre + ' ' + self.prestamo.material.titulo    
    class Meta:
        db_table = 'Historial'
        verbose_name_plural = 'Historiales'