from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from biblioteca_app.factory import MaterialFactory
from .models import Libro, Perfil, Revista, Tesis, material_Biblioteca
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

def index(request):
    """
    Vista principal que muestra todos los materiales disponibles en la biblioteca.

    Permite filtrar por título, autor y tipo de material. Además, se implementa
    la paginación para mostrar hasta 50 materiales por página.

    Parámetros:
        request: Petición HTTP.

    Retorna:
        render: Renderiza la plantilla 'index.html' con los materiales disponibles.
    """
    query = request.GET.get('q', '')
    tipo = request.GET.get('tipo', '')

    # Obtener materiales de cada tabla
    libros = list(Libro.objects.all())
    revistas = list(Revista.objects.all())
    tesis = list(Tesis.objects.all())

    # Agregar el tipo manualmente antes de enviarlo al template
    for material in libros:
        material.tipo = "Libro"
    for material in revistas:
        material.tipo = "Revista"
    for material in tesis:
        material.tipo = "Tesis"

    # Unir todas las listas
    materiales = libros + revistas + tesis

    # Filtrar por búsqueda en título o autor
    if query:
        materiales = [m for m in materiales if query.lower() in m.titulo.lower() or query.lower() in m.autor.lower()]

    # Filtrar por tipo de material
    if tipo:
        materiales = [m for m in materiales if m.tipo == tipo]

    # Ordenar por fecha de creación
    materiales.sort(key=lambda x: x.created_at, reverse=True)

    # Paginación
    paginator = Paginator(materiales, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'materiales': page_obj})


def login(request):
    """
    Vista para iniciar sesión de usuarios.

    Si la autenticación es exitosa, redirige al usuario a la página de inicio.

    Parámetros:
        request: Petición HTTP.

    Retorna:
        render: Renderiza la plantilla 'login.html'.
    """

    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si la autenticación es exitosa, loguear al usuario
            auth_login(request, user)
            messages.success(request, 'Bienvenido de nuevo!')
            return redirect('inicio')  # Redirige a la página de inicio o dashboard
        else:
            # Si las credenciales son incorrectas
            messages.error(request, 'Credenciales incorrectas. Inténtalo nuevamente.')
            return redirect('login')  # Redirige al formulario de login

    # Si no se envía el formulario, simplemente renderiza la página de login
    return render(request, 'login.html')
def register(request):
    
    """
    Vista para registrar un nuevo usuario.

    Verifica si el usuario o correo ya existen y valida las contraseñas antes de crear la cuenta.

    Parámetros:
        request: Petición HTTP.

    Retorna:
        render: Renderiza la plantilla 'register.html'.
    """
    
    # Verificar si el método es POST (cuando el usuario envía el formulario)
    if request.method == 'POST':
        # Obtener los datos enviados por el formulario
        username = request.POST.get('username')
        email = request.POST.get('email')
        nombre = request.POST.get('nombre')
        ap_paterno = request.POST.get('ap_paterno')
        tipo_usuario = request.POST.get('tipo_usuario')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validar que las contraseñas coincidan
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('register')

        # Verificar si el nombre de usuario o el correo ya existen
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está registrado')
            return redirect('register')

        try:
            # Crear el usuario
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            
            # Crear el perfil asociado al usuario
            perfil = Perfil.objects.create(
                user=user,
                nombre=nombre,
                ap_Paterno=ap_paterno,
                rol=tipo_usuario  # Asumiendo que 'tipo_usuario' está relacionado con el rol
            )

            # Mostrar mensaje de éxito
            messages.success(request, f'Cuenta creada exitosamente para {username}')
            
            # Redirigir al login o página de inicio
            if user is not None:
            # Si la autenticación es exitosa, loguear al usuario
                auth_login(request, user)
             
                return redirect('inicio')  # Redirige a la página de inicio o dashboard
            else:
                # Si las credenciales son incorrectas
              
                return redirect('register')  # Redirige al formulario de login

        except Exception as e:
            messages.error(request, f'Error al crear la cuenta: {e}')
            return redirect('register')
    
    # Si el método no es POST, simplemente renderizamos la página de registro
    return render(request, 'register.html')

 



# Vista para el logout
def logout(request):
    """
    Cierra la sesión del usuario y lo redirige a la página de inicio.

    Parámetros:
        request: Petición HTTP.

    Retorna:
        redirect: Redirige a la vista 'inicio'.
    """   
    auth_logout(request)  # Cerrar sesión
    return redirect('inicio')  # Redirige al login


# Vista para mostrar materiales
def admin_material(request):
    """
    Vista para administrar materiales en la biblioteca.

    Muestra una lista de todos los materiales registrados.

    Parámetros:
        request: Petición HTTP.

    Retorna:
        render: Renderiza la plantilla 'material.html' con los materiales disponibles.
    """    
    libros = list(Libro.objects.all())
    revistas = list(Revista.objects.all())
    tesis = list(Tesis.objects.all())

    # Agregar el tipo manualmente antes de enviarlo al template
    for material in libros:
        material.tipo = "Libro"
    for material in revistas:
        material.tipo = "Revista"
    for material in tesis:
        material.tipo = "Tesis"

    materiales = libros + revistas + tesis
    materiales.sort(key=lambda x: x.created_at, reverse=True)

    return render(request, 'material.html', {'materiales': materiales})


# Vista para añadir material
###
"""
@csrf_exempt

def agregar_material(request):
    
    Vista para agregar un nuevo material a la biblioteca.

    Permite registrar libros, revistas y tesis. Cada tipo de material tiene atributos 
    específicos que se manejan de manera condicional.

    Parámetros:
         request: Petición HTTP con los datos del formulario.

    Retorna:
        HttpResponseRedirect: Redirige a la vista 'admin_material' si el registro es exitoso.
        HttpResponse: Renderiza 'material.html' en caso de error.

    
    if request.method == 'POST':
            # Obtener los datos comunes del formulario
            titulo = request.POST.get('titulo')
            autor = request.POST.get('autor')
            tipo = request.POST.get('tipo')
            fecha = request.POST.get('fecha')
            foto = request.FILES.get('foto')
            genero = request.POST.get('genero')
            volumen = request.POST.get('volumen')
            # Crear el objeto según el tipo de material
            if tipo == "L":
                
                material = Libro.objects.create(titulo=titulo, autor=autor, fecha=fecha, foto=foto, genero=genero)
            elif tipo == "R":
            
                material = Revista.objects.create(titulo=titulo, autor=autor, fecha=fecha, foto=foto, volumen=volumen)
            elif tipo == "T":
                material = Tesis.objects.create(titulo=titulo, autor=autor, fecha=fecha, foto=foto)
            else:
                return render(request, 'material.html', {'error': 'Tipo de material no válido'})

            return redirect('admin_material')

    return render(request, 'material.html')
"""


@csrf_exempt
def agregar_material(request):

    """
    Vista para agregar un nuevo material a la biblioteca.

    Utiliza el Factory Method para crear objetos según el tipo de material.

    Parámetros:
        request: Petición HTTP.

    Retorna:
        redirect: Redirige a 'admin_material' en caso de éxito.
        JsonResponse: Devuelve un error si el tipo de material no es válido.
 

"""

    if request.method == 'POST' :
        tipo = request.POST.get('tipo')
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        fecha = request.POST.get('fecha')
        foto = request.FILES.get('foto')

        # Obtener atributos opcionales según el tipo
        genero = request.POST.get('genero') if tipo == "L" else None
        editorial = request.POST.get('editorial') if tipo == "L" else None
        volumen = request.POST.get('volumen') if tipo == "R" else None

        # Usamos la fábrica para crear el material
        try:
            material = MaterialFactory.crear_material(tipo, titulo, autor, fecha, foto, 
                                                      genero=genero, editorial=editorial, volumen=volumen)
            return redirect('admin_material')
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    return render(request, 'material.html')


@csrf_exempt
def editar_material(request):
    """
    Vista para editar un material existente.

    Parámetros:
        request: Petición HTTP.

    Retorna:
        JsonResponse: Indica si la edición fue exitosa o si hubo un error.
    """
    if request.method == 'POST':
        material_id = request.POST.get('id')
        tipo = request.POST.get('tipo')  # Detectar el tipo de material
        
        # Buscar en la tabla correcta
        if tipo == "L":
            material = get_object_or_404(Libro, id=material_id)
            material.genero = request.POST.get('genero')
            material.editorial = request.POST.get('editorial')
        elif tipo == "R":
            material = get_object_or_404(Revista, id=material_id)
            material.volumen = request.POST.get('volumen')
        elif tipo == "T":
            material = get_object_or_404(Tesis, id=material_id)
        else:
            return JsonResponse({"error": "Tipo de material no válido"}, status=400)

        # Actualizar los valores comunes
        material.titulo = request.POST.get('titulo')
        material.autor = request.POST.get('autor')
        material.fecha = request.POST.get('fecha')

        # Si hay nueva foto, actualizarla
        if 'foto' in request.FILES:
            material.foto = request.FILES['foto']

        material.save()
        return JsonResponse({"success": True})

@csrf_exempt
def eliminar_material(request):
    """
    Vista para eliminar un material de la biblioteca.

    Parámetros:
        request: Petición HTTP.

    Retorna:
        JsonResponse: Indica si la eliminación fue exitosa o si hubo un error.
    """
    if request.method == 'POST':
        material_id = request.POST.get('id')
        tipo = request.POST.get('tipo')  # Detectar tipo de material
        
        if tipo == "L":
            material = get_object_or_404(Libro, id=material_id)
        elif tipo == "R":
            material = get_object_or_404(Revista, id=material_id)
        elif tipo == "T":
            material = get_object_or_404(Tesis, id=material_id)
        else:
            return JsonResponse({"error": "Tipo de material no válido"}, status=400)

        material.delete()
        return JsonResponse({"success": True})

