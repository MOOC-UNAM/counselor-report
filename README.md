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
