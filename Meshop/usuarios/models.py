from django.db import models

# Create your models here. ffff    
class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_carrera

class Terminos_y_Condiciones(models.Model):
    texto = models.CharField(max_length=25000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto
    
class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_proveedor

class Publicidad(models.Model):
    nombre_anuncio = models.CharField(max_length=255)
    #imagen = models.ImageField(upload_to='publicidad/')  # Campo para almacenar imágenes
    imagen = models.CharField(max_length=1000)
    descripcion = models.TextField()
    link = models.TextField()
    idProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)  # Llave foránea a la tabla Proveedor
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()

    def __str__(self):
        return self.nombre_anuncio
    
class UsuarioEstudiante(models.Model):
    nickname = models.CharField(max_length=255)
    correo = models.CharField(max_length=100)    
    idCarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    #imagen = models.ImageField(upload_to='usuarios/')  # Campo para almacenar imágenes
    imagen = models.CharField(max_length=1000)
    genero = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField()
    #imagen = models.ImageField(upload_to='productos/')
    imagen = models.CharField(max_length=1000)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    idUsuario = models.ForeignKey(UsuarioEstudiante, on_delete=models.CASCADE)
    idCarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto
    
class UsuarioAdmin(models.Model):
    nombre_usuario = models.CharField(max_length=255)
    password = models.TextField()

    def __str__(self):
        return self.nombre_usuario
  