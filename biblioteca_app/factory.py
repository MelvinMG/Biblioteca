from biblioteca_app.models import Libro, Revista, Tesis

class MaterialFactory:
    """Clase abstracta para la creación de materiales"""
    @staticmethod
    def crear_material(tipo, titulo, autor, fecha, foto, **kwargs):
        if tipo == "L":
            return LibroFactory().crear_material(
                titulo, autor, fecha, foto, 
                genero=kwargs.get("genero"), 
                editorial=kwargs.get("editorial")
            )
        elif tipo == "R":
            return RevistaFactory().crear_material(
                titulo, autor, fecha, foto, 
                volumen=kwargs.get("volumen")
            )
        elif tipo == "T":
            return TesisFactory().crear_material(titulo, autor, fecha, foto)
        else:
            raise ValueError("Tipo de material no válido")

class LibroFactory(MaterialFactory):
    def crear_material(self, titulo, autor, fecha, foto, genero=None, editorial=None):
        return Libro.objects.create(
            titulo=titulo, autor=autor, fecha=fecha, foto=foto,
            genero=genero, editorial=editorial
        )

class RevistaFactory(MaterialFactory):
    def crear_material(self, titulo, autor, fecha, foto, volumen=None):
        return Revista.objects.create(
            titulo=titulo, autor=autor, fecha=fecha, foto=foto, volumen=volumen
        )

class TesisFactory(MaterialFactory):
    def crear_material(self, titulo, autor, fecha, foto):
        return Tesis.objects.create(
            titulo=titulo, autor=autor, fecha=fecha, foto=foto
        )
