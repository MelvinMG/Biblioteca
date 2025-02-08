from django.contrib import admin
from django.urls import include, path
from biblioteca_app.views import index, login, register, logout, admin_material, agregar_material, editar_material, eliminar_material
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),       # Ruta para el panel de administración
    path('', index, name='inicio'),  # Ruta para la vista 'index'
    path('login/', login, name='login'),    # Ruta para la vista 'login'
    path('register/', register, name='register'), # Ruta para la vista 'register'
    path('logout/', logout, name='logout'), # Ruta para la vista 'logout'
  # 🔹 Rutas de administración de materiales
    path('admin_material/', include([
        path('', admin_material, name='admin_material'),
        path('agregar/', agregar_material, name='agregar_material'),
        path('editar/', editar_material, name='editar_material'),
        path('eliminar/', eliminar_material, name='eliminar_material'),
    ])),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
