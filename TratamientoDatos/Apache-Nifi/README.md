# Apache-Nifi


<p align="center">
<img src= "https://nifi.apache.org/assets/images/apache-nifi-logo.svg" width="500">
</p>

# Descripción

Apache NiFi es una plataforma de flujo de datos de código abierto diseñada para automatizar el flujo de trabajo de datos entre sistemas informáticos, es decir , se encarga de realizar todo el proceso de extracción transformación y carga de datos (ETL).

Esta herramienta se ha utilizado para ayudar a los usuarios a analizar datos masivos, gestionar flujos de trabajo de datos, mejorar la seguridad de los datos, integrar sistemas, procesar datos en tiempo real y mucho más.

 NiFi proporciona una interfaz gráfica de usuario (GUI) para administrar los flujos de datos en tiempo real, permitiendo que los usuarios visualicen, monitoreen y controle los datos que pasan a través de sus sistemas.

Entre las características de Apache-Nifi destacan:

- Flexibilidad, con soporte a formatos variados (Json, csv, etc).
- Escalabilidad y toleancia a fallos.
- Con conectores a múltiples fuentes y destinos de datos.
- Integración y conexión con gran cantidad de tecnologías
- Facilita la implementación de ETLs visualmente con una
sencilla interfaz gráfica

**Ejemplo de implementación con Kafka y Elasticsearch**

<p align="center">
<img src= "https://raw.githubusercontent.com/nacho-pascual/EDEM2022/main/TratamientoDatos/Captura%20de%20Pantalla%202022-12-05%20a%20las%208.22.23.png" width="500">
</p>
 

# Componentes principales

**Flow**

Definición del flujo de datos que se implementa en NiFi(Workflow o topología).Indica la forma en la que se deben gestionar los datos.

**Flowfile** 

Es un contenedor de datos que viaja por el flujo entre los procesadores.Es su cabecera, se encuentrán los atributos(clave-valor) que ayudan a enriquecer el dato.No contiene el propio dato , solo es un puntero que apunta hacía el repositorio de contenido donde se encuentra el dato.


<p align="center">
<img src= "https://aprenderbigdata.com/wp-content/uploads/estructura-flowfile-nifi-300x250.png.webp" width="200">
</p>

**Processor**

Son los componentes principales en Nifi , se encargan de ejecutar las acciones de los datos o el flujo. Proporciona la interfaz para acceder a los flowfiles.Se pueden implementar procesadores personalizados mediante una api de java y además se puede programar su ejecucuón mediante crome, tiempo predefinido o eventos de entrada. Llevan incorporado un validador de comunicación y gráficas con las estadísticas y trazas.

**Conexiones**

Son las tuberías de conexión entre dos Processors que les permiten interactuar. Es la encargada de transmitir los flowfiles entre los componentes y de gestionar las colas y su capacidad. Las colas , definen las reglas con las prioridades de los flowfiles. Pueden ser de tipo FIFO(first in first out) o de tipo LIFO(Last in first out)

Las conexiones actúan como un buffer para los flowfiles, y tienen un sistema de backpressure en función del número de eventos o del tamaño en disco(esto nos permite evitar que las colas crezcan de forma infinita). También es posible establecer la caducidad para los flowfiles o su prioridad. Mediante los funnels, NiFi permite agrupar varias conexiones en una.

**Grupos de Proceso**

Agrupación de procesadores y conexiones que sirve para tratarlos como una unidad lógica independiente dentro del flujo de procesamiento. Para interactuar con el resto de componentes tienen puertos de entrada y de salida que gestionan el envío de flowfiles.

**Controller Service y Plantillas**

Los controller service o controladores se utilizan para compartir un recurso entre distintos processors. Por ejemplo puede ser una conexión a una base de datos, a AWS S3 o a un contenedor de Azure.

Apache NiFi también nos permite crear plantillas (templates) con un flow almacenado. Las plantillas resultan muy útiles para añadir de forma rápida un nuevo conjunto de componentes estándar o mover sub-flujos entre distintos entornos de trabajo.

