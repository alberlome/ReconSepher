
# Aplicación Flask para Buscar CVEs

Este es un proyecto simple utilizando Flask para buscar información sobre vulnerabilidades CVE (Common Vulnerabilities and Exposures) a través de una API externa ( https://cve.circl.lu/api/) y mostrar los resultados en una página web.

## Características

- Interfaz web donde el usuario puede buscar detalles de una vulnerabilidad CVE introduciendo su código.
- Muestra información detallada sobre la vulnerabilidad, incluyendo descripción, productos afectados, plataformas, versiones y más.
- Diseño responsivo utilizando CSS.

![image](https://github.com/user-attachments/assets/59ff4183-6df4-4a11-89e7-fb34bd04197c)

![image](https://github.com/user-attachments/assets/632e9f22-bc19-4f98-b2d6-e41e5bc34340)


## Requisitos

- Python 3.x
- Flask
- requests (para hacer peticiones HTTP a la API)

## Instalación

1. Clona este repositorio o descarga los archivos.
   ```bash
   git clone https://github.com/tu_usuario/repo.git
   ````
   
Crea un entorno virtual (opcional pero recomendado):
````bash
python -m venv venv
````

Activa el entorno virtual:
En Windows:
````bash
venv\Scripts\activate
````

En Mac/Linux:
````bash
source venv/bin/activate
````
Instala las dependencias necesarias:
````bash
pip install -r requirements.txt
````
Si no tienes un archivo requirements.txt, puedes instalar Flask y requests manualmente:

bash
Copiar
pip install flask requests
Estructura del Proyecto
El proyecto tiene la siguiente estructura:

````bash
/Proyecto
│
├── app.py                  # Archivo principal de la aplicación Flask
├── /templates              # Carpeta que contiene las plantillas HTML
│   ├── index.html          # Página de inicio con el formulario de búsqueda
│   └── cve_results.html    # Página para mostrar los resultados de la búsqueda
└── /static                 # Carpeta que contiene los archivos estáticos (CSS)
    └── styles.css          # Estilos CSS para la interfaz
````
Ejecutar la Aplicación
Para ejecutar la aplicación, usa el siguiente comando:

````bash
python app.py
````
Esto iniciará el servidor Flask localmente. En tu navegador, abre la URL:

cpp
Copiar
http://127.0.0.1:5000/
Ahí podrás ingresar el código CVE y ver los detalles de la vulnerabilidad.

Uso
Página de búsqueda: En la página principal (index.html), puedes ingresar un código CVE en el formulario y hacer clic en "Buscar".

Resultados: Si el código CVE es válido, se mostrarán los detalles relacionados con la vulnerabilidad. Si no se encuentran detalles, se mostrará un mensaje indicando que no se encontró información.

Contribución
Si deseas mejorar este proyecto, ¡no dudes en hacer un fork y enviar tus contribuciones!

Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

markdown
Copiar

### Explicación:

- **Instalación**: El archivo explica cómo clonar el proyecto, crear un entorno virtual y cómo instalar las dependencias necesarias.
- **Estructura del Proyecto**: Describe la estructura de los archivos, donde `app.py` es el archivo principal, las plantillas HTML se encuentran en la carpeta `templates`, y el archivo CSS está en la carpeta `static`.
- **Ejecutar la Aplicación**: Instrucciones para ejecutar la aplicación de Flask localmente.
- **Uso**: Explica cómo interactuar con la aplicación.
- **Contribución y Licencia**: Espacio para que otros desarrolladores puedan contribuir y el tipo de licencia.

Este archivo `README.md` proporcionará a cualquier usuario o desarrollador la información necesaria para entender y ejecutar tu aplicación correctamente.

Tú dijiste:
Me lo puedes poner todo en un unico fichero explicado, por favor, no a saltos. Gracias

ChatGPT Plus
¡Por supuesto! Aquí tienes el archivo README.md completo y detallado para tu aplicación Flask en un único bloque:

markdown
Copiar
# Aplicación Flask para Buscar CVEs

Este proyecto es una sencilla aplicación web construida con Flask que permite a los usuarios buscar información sobre vulnerabilidades **CVE** (Common Vulnerabilities and Exposures) utilizando una API externa. Los resultados se muestran de forma organizada en una página web.

## Características

- **Interfaz web intuitiva**: El usuario puede buscar información sobre vulnerabilidades CVE introduciendo su código en un formulario.
- **Detalles completos**: La aplicación muestra información detallada sobre la vulnerabilidad, como la descripción, productos afectados, plataformas, versiones, entre otros.
- **Diseño responsivo**: La interfaz se adapta a diferentes tamaños de pantalla, mejorando la experiencia de usuario tanto en dispositivos de escritorio como móviles.

## Requisitos

Para ejecutar esta aplicación, necesitas tener instalados los siguientes componentes:

- **Python 3.x**: Lenguaje de programación utilizado para el desarrollo.
- **Flask**: Framework web para Python, utilizado para construir la aplicación.
- **requests**: Librería para hacer peticiones HTTP a la API externa que proporciona información sobre las vulnerabilidades CVE.

## Instalación

1. **Clonar el repositorio**: Primero, clona el repositorio o descarga los archivos de la aplicación.

   ```bash
   git clone https://github.com/tu_usuario/repo.git
   ````
Crear un entorno virtual (opcional pero recomendado): Esto es útil para manejar las dependencias de manera aislada.

````bash
python -m venv venv
````
Activar el entorno virtual:

En Windows:

````bash
venv\Scripts\activate
````
En Mac/Linux:
````bash
source venv/bin/activate
````
Instalar las dependencias necesarias: Una vez activado el entorno virtual, instala las dependencias requeridas.

Si tienes un archivo requirements.txt (como se indica en el proyecto):

````bash
pip install -r requirements.txt
````
Si no tienes el archivo requirements.txt, puedes instalar Flask y requests manualmente:

````bash
pip install flask requests
````
Estructura del Proyecto
El proyecto tiene la siguiente estructura de archivos:

````bash
/Proyecto
│
├── app.py                  # Archivo principal de la aplicación Flask
├── /templates              # Carpeta que contiene las plantillas HTML
│   ├── index.html          # Página de inicio con el formulario de búsqueda
│   └── cve_results.html    # Página para mostrar los resultados de la búsqueda
└── /static                 # Carpeta que contiene los archivos estáticos (CSS)
    └── styles.css          # Estilos CSS para la interfaz
````

Ejecutar la Aplicación
Para ejecutar la aplicación, sigue estos pasos:

Asegúrate de que tienes un entorno virtual activado y las dependencias instaladas.

Ejecuta el siguiente comando en el directorio raíz del proyecto:

````bash
python app.py
````
Esto iniciará el servidor Flask localmente. Abre tu navegador y ve a la siguiente URL para ver la aplicación:

http://127.0.0.1:5000/

Uso de la Aplicación
Página de búsqueda: Al acceder a la URL principal, verás un formulario donde podrás ingresar un código CVE (por ejemplo, CVE-2021-1234).

Buscar CVE: Después de ingresar el código CVE y hacer clic en "Buscar", la aplicación hará una solicitud a la API externa para obtener detalles sobre la vulnerabilidad correspondiente.

Resultados: Si la vulnerabilidad es encontrada, se mostrará información detallada, como la descripción de la vulnerabilidad, los productos afectados, las plataformas vulnerables, las versiones, etc. Si no se encuentra la vulnerabilidad, se mostrará un mensaje de error.

Contribución
Si deseas mejorar esta aplicación o agregar nuevas características, puedes hacerlo de las siguientes maneras:

Haz un fork de este repositorio.

Crea una nueva rama (feature-branch).

Realiza tus cambios y abre una pull request con tus contribuciones.

Licencia
Este proyecto está bajo la Licencia MIT. Puedes revisar los detalles en el archivo LICENSE.

### Explicación del contenido:

1. **Instalación**: Proporciona los pasos para clonar el repositorio, crear un entorno virtual, y luego instalar las dependencias necesarias para la aplicación.
2. **Estructura del Proyecto**: Detalla cómo están organizados los archivos dentro del proyecto.
3. **Ejecutar la Aplicación**: Instrucciones claras para ejecutar el servidor Flask localmente y cómo acceder a la aplicación.
4. **Uso**: Describe cómo interactuar con la aplicación web, cómo buscar un CVE y cómo ver los resultados.
5. **Contribución**: Anima a otros desarrolladores a contribuir al proyecto mediante forks y pull requests.
6. **Licencia**: Incluye información sobre la licencia del proyecto.

Este `README.md` proporciona toda la información necesaria para que otros usuarios o desarrolladores puedan instalar, ejecutar y contribuir a tu proyecto.

