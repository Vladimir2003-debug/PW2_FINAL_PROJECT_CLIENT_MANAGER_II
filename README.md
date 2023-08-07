<div align="center">
<table>
    <theader>
        <tr>
            <td style="width:25%;"><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>
            <td>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </td>            
        </tr>
    </theader>
    <tbody>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Proyecto web</span>: Desarrollo de una aplicación web para inscripción de laboratorios</td>
        </tr>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Fecha</span>:  2022/08/09</td>
        </tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">PROYECTO WEB</span><br />
</div>


<table>
<theader>
<tr><th>INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
    <tr>
        <td>ASIGNATURA:</td><td>Programación Web 2</td>
    </tr>
    <tr>
        <td>SEMESTRE:</td><td>III</td>
    </tr>
    <tr>
        <td>FECHA INICIO:</td><td>30-May-2022</td><td>FECHA FIN:</td>
        <td>03-Jun-2022</td><td>DURACIÓN:</td><td>04 horas</td>
    </tr>
    <tr>
        <td colspan="3">DOCENTES:
        <ul>
        <li>Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</li>
        </ul>
        INTEGRANTES(Grupo A Laboratorio)
        <ul>
            <li>Sulla Quispe Vladimir Arturo(Grupo C - Teoria)</li>
            <li>Martell Villanueva Gabriela Vanessa(Grupo C - Teoria)</li>
            <li>Chaisa Fernandez Anthony(Grupo B - Teoria)</li>
        </ul>
        </td>
    </<tr>
</tdbody>
</table>

#   WebApp con Django

[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]

##  Tipo de Sistema
    El sistema consiste en conectar Contador con sus respectivos clientes. El contador elabora catalogos de cuentas que sirven para analisis financieros. Los clientes pueden ver los catalogos y ver como estan sus estados financieros en todo momento.

##  Requisitos del sistema
    El sistema debe satisfacer los siguientes requisitos funcionales y no funcionales:

    - RQ01 : El sistema debe estar disponible en Internet a traves de una URL.
    - RQ02 : El sistema debe permitir el inicio/cierre de sesión.
    - RQ03 : El sistem debe permitir a los contadores hacer las labores de CRUD
    - RQ04 : El sistema debe evitar que los clientes puedan eliminar los catalogos y su edicion sin la autorizacion de un contador   
    - RQ05 : El sistema debe permitir el envio de mensajes mediante su correo electronico  
    - RQ06 : Los catalogos pueden verse y descargarse en formato pdf 
    -   ...

##  Modelo de datos
    El modelo de datos esta conformado por las siguientes entidades.

    -   Usuario : La entidad principal que se ramifica en dos entidades
        - Cliente : El cliente puede logearse y ver catalogos
        - Contador : El contador se encarga de la elaboracion de catalogos y su manipulacion ya que tiene la autorizacion legal para hacerlo

##  Diccionario de datos

    En la construcción de software y en el diccionario de datos sobre todo se recomienda y se utilizará el idioma inglés para especificar objetos, atributos, etc.

| User | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| id  | UUID| No | Si | uuid.UUID | Código |
| name  | Cadena| No | No | Ninguno | Nombre |
| first_name | Cadena | No | No | Ninguno | Primer Nombre |
| last_name  | Cadena | No | No | Ninguno | Apellido |
| is_admin  | Boolean | No | No | Ninguno | Confirmacion para ver si es administrador |
| is_cliente  | Boolean | No | No | Ninguno | Verificacion de entidad cliente |
| is_contador  | Boolean | No | No | Ninguno | verificacion de entidad coontador |



| Banco | | | | | |
| -- | -- | -- | -- | -- | -- |
| id_bank  | UUID| No | Si | uuid.UUID | Código |
| name_bank  | Cadena| No | Si | Ninguno | nombre |
| type_bank | Cadena| No | No | Ninguno | tipo |
| description | Cadena| No | No | Ninguno | que tiene que decir del banco |


| Country | | | | | |
| -- | -- | -- | -- | -- | -- |
| id_bank  | UUID| No | Si | uuid.UUID | Código |
| name_bank  | Cadena| No | Si | Ninguno | nombre |
| type_bank | Cadena| No | No | Ninguno | tipo |


| Cuenta | | | | | |
| -- | -- | -- | -- | -- | -- |
| id_bank  | UUID| No | Si | uuid.UUID | Código |
| name_bank  | Cadena| No | Si | Ninguno | nombre |
| type_bank | Cadena| No | No | Ninguno | tipo |


| Activo | | | | | |
| -- | -- | -- | -- | -- | -- |
| id_bank  | UUID| No | Si | uuid.UUID | Código |
| name_bank  | Cadena| No | Si | Ninguno | nombre |
| type_bank | Cadena| No | No | Ninguno | tipo |


| Pasivo| | | | | |
| -- | -- | -- | -- | -- | -- |
| id_bank  | UUID| No | Si | uuid.UUID | Código |
| name_bank  | Cadena| No | Si | Ninguno | nombre |
| type_bank | Cadena| No | No | Ninguno | tipo |


| Cuenta | | | | | |
| -- | -- | -- | -- | -- | -- |
| id_bank  | UUID| No | Si | uuid.UUID | Código |
| name_bank  | Cadena| No | Si | Ninguno | nombre |
| type_bank | Cadena| No | No | Ninguno | tipo |


| CatalogoCuentas | | | | | |
| -- | -- | -- | -- | -- | -- |
| id_bank  | UUID| No | Si | uuid.UUID | Código |
| name_bank  | Cadena| No | Si | Ninguno | nombre |
| type_bank | Cadena| No | No | Ninguno | tipo |



##  Diagrama Entidad-Relación
    ...

##  Administración con Django
    Se muestran los pasos realizados para crear el Proyecto, la aplicación, creacion de modelos, migraciones y habilitación del panel de administración en Django.
    ...

##  Plantillas Bootstrap
    Se seleccionó la siguiente plantilla para el usuario final (No administrador).

    Demo online:
    URL: 

    Se muestran las actividades realizadas para adecuación de plantillas, vistas, formularios en Django.
    ...

##  CRUD - Core Business - Clientes finales
    El núcleo de negocio del sistema de inscripciones tiene valor de aceptación para los cliente finales (alumnos) radica en realizar el proceso de inscripción propiamente, que empieza desde que:
    1. Tanto el Cliente como el Contador pueden iniciar sesion
    2. El contador puede crear y elaborar catalogos el cliente solo puede mirar.
    3. Los catalogos se pueden ver y descargar en formato pdf .
    4. Los ususarios pueden enviar mensajes
    6. El usuario puede cerrar sesion.

    Todas y cada una de estas pantallas debe funcionar en la plantilla bootstrap.
    A continuación se muestran las actividades realizadas para su construcción:

##  Servicios mediante una API RESTful
    Se ha creado una aplicación que pondra a disposición cierta información para ser consumida por otros clientes HTTP.
    1. GET : Con el método get se devolverá la lista de cursos, grupos y horarios establecidos para que el alumno sobre todo vea esta información en cualquier otro medio. En formato JSON. 
    2. POST : Con este método se enviara el código del alumno y se devolvera sus inscripciones. En formato JSON.
    
    Ejemplo: Prueba en Página web, aplicación móvil, PDF, etc.
    Se especifican los pasos para crear el servicio RestFul
    ...

##  Operaciones asíncronas AJAX
    Se propone el uso de AJAX para realizar la asignación de carga académica a los docentes que estan registrados. Esta operación la realizará el usuario operador encargado por el DAISI.
    Se muestran los pasos necesarios a realizar.
    ....

##  Investigación: Email, Upload.
    - Email: Se utilizará la funcionalidad del uso de envío de correos electrónicos cuando el proceso de inscripciones culmine y al profesor le llegue la lista de alumnos inscritos en sus grupos a cargo.
    - Render PDF: Se utilizará esta funcionalidad para renderizar y elaborar pdfs 

Github del proyecto:


URL Playlist YouTube.
Producción de un PlayList en Youtube explicando cada una de los requerimientos.
Video 01 - Sistema - Requisitos.
Video 02 - Modelo de datos - DD - DER.
etc…


## REFERENCIAS


#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
