# Apache-Nifi


<p align="center">
<img src= "https://nifi.apache.org/assets/images/apache-nifi-logo.svg" width="500">
</p>

# Descripcion

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
 

# Componentes principales

**Flow**

Definición del flujo de datos que se implementa en NiFi(Workflow o topología).Indica la forma en la que se deben gestionar los datos.

**Flowfile** 

Es un contenedor de datos que viaja por el flujo entre los procesadores.Es su cabecera, se encuentrán los atributos(clave-valor) que ayudan a enriquecer el dato.No contiene el propio dato , solo es un puntero que apunta hacía el repositorio de contenido donde se encuentra el dato.

**Processor**

Son los componentes principales en Nifi , se encargan de ejecutar las acciones de los datos o el flujo.
