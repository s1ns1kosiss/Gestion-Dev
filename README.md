1. Crear y Activar el Entorno Virtual
bash
Copiar
Editar
python -m venv venv
En Windows:

bash
Copiar
Editar
venv\Scripts\activate
En macOS/Linux:

bash
Copiar
Editar
source venv/bin/activate
2. Instalar las Dependencias del Proyecto
bash
Copiar
Editar
pip install -r requirements.txt
3. Aplicar Migraciones
bash
Copiar
Editar
python manage.py migrate
4. Iniciar el Servidor de Desarrollo
bash
Copiar
Editar
python manage.py runserver
