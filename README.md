# Reportes de Consejería

El reporte de consejería funciona a partir de un archivo de hoja de cálculo donde los consejeros hacen las anotaciones, llamado **Quién es quién**, sobre los estudiantes en los siguientes rubros:
- **Fortalezas** (Las fortalezas como aprendiz que hemos detectado son:)
- **Trabajo** (Desde el área de consejería del Bachillerato, se trabajó lo siguiente:)
- **Mejoras** (Algo que es importante mejorar es:)
- **Otras recomendaciones**

> Se tienen campos adicionales en el archivo de hoja de cáculo que no se contemplan para fines de este reporte, se adjunta archivo [plantila](./resources/template.xlsx) con todos los campos.

Una vez que este reporte es completado por los consejeros se exporta a un archivo en formato _csv_ que debe ser colocado en el directorio [csv](./csv/) del proyecto.

> Se coloca archivo de ejemplo para poder validar las diferentes condiciones de los estudiantes y la estructura final del documento en el archivo [report.csv](./csv/report.csv).

Este reporte no contiene las calificaciones finales de los estudiantes, por lo que para evitar el error humano se ha contemplado utilizar el archivo que se obtiene de la plataforma al que se le eliminan los datos innecesarios. La relación que existe entre el archivo `report.csv` y el de calificaciones es el campo `email`.

> Se coloca archivo [grades.csv](./csv/grades.csv) de ejemplo para validar su estructura.

## Operación

Para correr el programa basta con ejecutar el archivo `report.py` mediante el comando:

`python report.py`

Mostrará resumen de los procesos que se encuentra realizando:
1. Cuando la tabla de estudiantes se ha creado.
2. El número de estudiantes que se encontró en el archivo `report.csv`.
3. La limpieza de los datos de la tabla estudiantes.
4. Inserción de los datos en la tabla estudiantes.
5. Número de calificaciones que se encontraron en el archivo `grades.csv`.
6. Inserción de las calificaciones.
7. Procesamiento de los archivos pdf.
8. Número de archivos pdf creados.

Después del mensaje **6** se presenta el mensaje de selección del tipo de reporte, se tienen 3 opciones diferentes:
1. Estudiante sin actividad o que no tiene actividad evaluable en plataforma.
2. Estudiante con calificación no aprobatoria.
3. Estudiante con calificación aprobatoria.

Se tendrá que colocar únicamente el número de la opción para que el procesamiento de los archivos comience. En este momento se crearan los archivos html en la ruta colocada previamente en la variable `html_dir` (vaya a la sección [Configuración inicial](#configuración-inicial) para detalles).

Para que los archivos pdf se puedan crear es necesario que el servidor web se encuentré funcionando ya que las rutas a las que se hace referencia fueron configuradas en la variable `url_location` por lo que si la url regresa un mensaje 404 no se procesará el archivo pdf. Los archivos pdf los encontrará posterior al procesamiento del programa en la ruta declarada en la variable `pdf_dir`.

## Instalación y configuración

### Requerimientos previos y entorno de desarrollo

Para ver los requerimientos previos y la configuración de entorno de desarrollo vea el siguiente [documento](./requirements.md)

### Configuración inicial

La configuración inicial del proyecto se lleva en el archivo [config.py](./setup/config.py) y considera los siguientes parámetros:

- Configuración de la base de datos.
- Ubicación del directorio en el servidor de Apache en donde se crearán los documentos HTML de los reportes.
- Directorio en el que se depositarán los archivos PDF que se generan, por _default_ `pdf/`.
- Ubicación y nombre del archivo de registros del Quién es quién.
- Ubicación y nombre del archivo con calificaciones finales de los estudiantes.

### Configuración del documento

Antes de ejecutar el programa es necesario colocar el directorio [assets](./resources/assets/) y su contenido en la ruta declarada en la variable `html_dir` ya que las referencias de la vista html apuntan a la ruta de la variable `url_location`.

El documento pdf que se procesa se encuentra separado en el archivo [html_operations.py](./utilities/html_operations.py) donde se encuentran las funciones que conforman el documento.

#### load_head()

Declara la cabecera del documento html, se encuentran los archivos de hoja de estilos necesarios para darle formato.

#### student_header(name,lastname,counselor)

Contruye la información del expediente para el documento, contiene los datos:

|variable que recibe|dato al que corresponde|
|---|---|
|name, lastname|nombre y apellido del estudiante|
|counselor|nombre del consejero|
|today|fecha de procesamiento|

Se encuentra maquetado a modo de tabla con la finalidad que conserve la proporción al momento de la creación del pdf.

#### resume_score(status,strengths,work,improvement,findings,score):

En esta sección se encuentra el cuerpo del reporte y se encuentra dividido de la siguiente manera:

|variable|información|
|---|---|
|general_findings|contiene una lista en formato html que presenta las **recomendaciones generales** del documento|
|status|aplica como un campo vacío para los estudiantes que presentan actividad en plataforma y contiene un valor cuando no existe actividad o actividad ponderable|
|resume_score|presenta cuando el valor de la variable `status` es _nulo_ y muestra un mensaje inicial seguido de la calificación obtenida en el curso|
|counselor|corresponde a la información proporcionada por el consejero en los campos: **Fortalezas** **Trabajo** **Mejoras** del documento [plantila](./resources/template.xlsx)|
|other_findings|corresponde a las recomendaciones más particulares hechas por el consejero en el campo **Otras recomendaciones**|
