# Reportes de Consejería

El reporte de consejería funciona a partir de un archivo de hoja de cálculo donde los consejeros hacen las anotaciones, llamado **Quién es quién**, sobre los estudiantes en los siguientes rubros:
- **Fortalezas** (Las fortalezas como aprendiz que hemos detectado son:)
- **Trabajo** (Desde el área de consejería del Bachillerato, se trabajó lo siguiente:)
- **Mejoras** (Algo que es importante mejorar es:)
- **Otras recomendaciones**

> Se tienen campos adicionales en el archivo de hoja de cáculo que no se contemplan para fines de este reporte, se adjunta archivo [plantila](./resources/template.xlsx) con todos los campos.

Una vez que este reporte es completado por los consejeros se exporta a un archivo en formato _csv_ que debe ser colocado en el directorio [csv](./csv/) del proyecto.

> Se coloca archivo de ejemplo para poder validar las diferentes condiciones de los estudiantes y la estructura final del documento en el archivo [report.csv](./csv/report.csv).

## Instalación y configuración

### Requerimientos previos

Es importante contar con las siguientes aplicaciones para que el proyecto pueda operar.

- Python en una versión 3 o superior.
- Servidor Apache para previsualizar los archivos de salida.
- Motor de base de datos MySQL.

#### Base de datos

Se debe contar con una base de datos con un usuario con permisos de creación, lectura, escritura y eliminación de tablas.

### Configuración de entorno de desarrollo

Dependiendo del entorno en el que se vaya a ejecutar el proyecto deberá tener instalado el manejador de paquetes **pip** para la versión de Python requerida.

#### Instalar virtualenv

Desde la terminal se debe instalar _virtualenv_ para la versión de Python a emplear.

`pip3 install virtualenv`

#### Configuración del ambiente virtual de desarrollo

1. Identificar en qué ruta se encuentra instalado Python:

    `which python3`

    > Para este caso se dirá que la ruta que regreso la ejecución del comando fue: `/home/username/opt/python-3.6.2/bin/python3`

2. Ir al directorio donde se creará el ambiente virtual.

3. Crear un ambiente virtual mientras se específica la versión de Python que se desea usar. El siguiente comando crea un virtualenv llamado 'venv' y usa una bandera -p para especificar el camino a la versión de Python 3.

    `virtualenv -p /home/username/opt/python-3.6.2/bin/python3 venv`

4. Para activar el nuevo ambiente virtual:

    `source venv/bin/activate`

    > Se encontrará que previo a mostrar el usuario del sistema en la línea de comandos se encontrará `(venv)` indicando que se encuentra trabajando dentro del ambiente virtual.

5. Para verificar la versión correcta de Python:

    `python -V`

6. Cuando se termina de usar el ambiente virtual se debe desactivar con el comando:

    `deactivate`

### Instalación de paquetes del proyecto

Este proyecto emplea los siguientes paquetes:

- [wkhtmltopdf](https://wkhtmltopdf.org/)
- [pdfkit](https://pdfkit.org/)
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)

Para lo que puede emplear el archivo [requirements.txt](./requirements.txt) mediante el comando:

`pip install -r requirements.txt`

Para el uso de **pdfkit** se debe instalar el paquete `wkhtmltopdf`.

> La instucción puede cambiar dependiendo el sistema operativo, pare el caso de Debian/Ubuntu:
>
> `sudo apt-get install wkhtmltopdf`