# 📚 Bienvenidos a mi Repositorio de Tópicos Avanzados de Programación Web y Móviles

Este repositorio contiene el código del proyecto desarrollado en la materia de **Tópicos Avanzados de Programación Web y Móviles**. Aquí aplicaremos tecnologías avanzadas para el desarrollo de aplicaciones web con **Django**, **PostgreSQL** y más.

## 📂 Enlace a los Recursos en Google Drive
Puedes encontrar documentación, diagramas UML y otros recursos adicionales en el siguiente enlace:

🔗 [Google Drive - Material del Proyecto](https://drive.google.com/drive/folders/1KDNGrDUTTMQU29YijULnv4IH5hyy6k9H?usp=sharing)

---

## 🛠️ Instalación y Configuración

### Requisitos

Asegúrate de tener instalado lo siguiente antes de comenzar:

- Python 3.x
- pip (administrador de paquetes de Python)
- PostgreSQL (o el sistema de bases de datos que estés utilizando)


###  **1. Clonar el Repositorio**
Para obtener el código fuente en tu computadora, abre una terminal y ejecuta:

```bash
git clone https://github.com/MelvinMG/Biblioteca.git
cd Biblioteca
```

### **2. Crear el entorno virtual**
```bash
python -m venv venv
venv/scripts/activate
```
### **3. Instalar las dependencias**
```bash
pip install -r requirements.txt
```
☝🏿Si falla instalarlos manualmente

### **4. Configurar la base de datos para postgres** 
Configuracion para Postgres
``` bash
DATABASES = {

    'default': {
    
        'ENGINE': 'django.db.backends.postgresql',
        
        'NAME': 'nombre_base_datos',
        
        'USER': 'tu_usuario',
        
        'PASSWORD': 'tu_contraseña',
        
        'HOST': 'localhost',
        
        'PORT': '5432',
        
    }
    
}
```
### **5. Aplicar las migraciones**
Aplica las migraciones para crear las tablas en la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```

Nota: Borrar el contenido de la carpeta migratas antes de usar este comando, y debes aplicar el siguiente comando

Tambien si quieres cargar un modelo en particular solo pon el nombre adelante de makemigrations

###  **6. Crear un superusuario**
Crea un superusuario para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```
Sigue las instrucciones en pantalla para crear el superusuario.

*Usuario: SU*

*Corre: Tu correo electronico (Puede ser opcional)*

*Contrasenia:SU1234*


### **7. Ejecutar el servidor de desarrollo**
Finalmente, ejecuta el servidor de desarrollo de Django:
```bash
python manage.py runserver
```

