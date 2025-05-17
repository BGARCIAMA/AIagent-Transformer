
# Guión + Estructura de Presentación en Video Demo

## Slide 1: Portada
**Proyecto Final - Agente Transformador de Datos**
> "Buenas tardes grupo, soy Blanca. En este video presento mi proyecto final para la materia de Temas selectos de análisis de datos.El tema que decidí desarrollar es Agentes de IA: un asistente que transforma datos entre formatos como CSV, JSON y XML sin perder su estructura semántica."

---

## Slide 2: Objetivo
**¿Qué resuelve esta herramienta?**
> "Este agente resuelve el problema de compatibilidad entre diferentes estructuras de datos. Muchas veces nos pasa que necesitamos cambiar el formato de los archivos con los que trabajamos para que puedan encajar en nuestra estructura o nuestros modelos, pero al cambiar su formato, perdemos o cambiamos información del formato original, por ello es que este agente es tan relevante, ya que a través de análisis semántico, puede transformar archivos sin que se pierda el significado de las columnas."

---

## Slide 3:
**Flujo:**
“Ahora, ¿cómo funciona este agente?
Básicamente sigue cinco pasos principales:
-Carga del archivo: el usuario puede subir un archivo en formato CSV, JSON o XML.
-Análisis de estructura: el agente detecta automáticamente el formato y extrae la estructura del archivo, es decir, identifica las columnas presentes y cómo están organizadas.
-Mapeo semántico: aquí es donde entra la parte más interesante.
La estructura semántica se refiere al significado que tienen las columnas dentro de un conjunto de datos, más allá de su nombre.
Por ejemplo, dos archivos pueden tener columnas llamadas cliente_nombre, nombre_completo o titular, pero todas representan lo mismo: el nombre del cliente.
Para resolver estas diferencias, el agente utiliza embeddings, es decir, vectores que representan el significado de los nombres de columna.
Con ellos, puede calcular similitud semántica entre columnas de diferentes archivos y proponer un mapeo inteligente.
-Transformación: una vez establecido el mapeo, el sistema transforma el archivo al formato deseado (CSV, JSON o XML), pero manteniendo la semántica del contenido, es decir, respetando lo que representa cada columna.
Validación de consistencia: al final, el agente compara la estructura original con la transformada y verifica que los elementos clave —como cliente, monto o fecha— se hayan preservado correctamente.
Si el porcentaje de coincidencia estructural es suficientemente alto, se aprueba la transformación.
Si no, el sistema avisa que hubo una pérdida de consistencia.
-Descarga: por último se peude realizar la descarga en el fortmato final.

En resumen, al subir un archivo, el agente detecta su estructura, propone un mapeo semántico con columnas estándar, transforma al nuevo formato y valida que la información siga teniendo el mismo significado que al inicio."

---

## Slide 4: Demo
Una rápida demostración de este agente Transformador de datos, conlleva el:

### 1. Subir archivo
> "Voy a subir un archivo CSV con columnas típicas de transacciones."

### 2. Ver mapeo semántico
> "Aquí se muestran las sugerencias de columnas equivalentes gracias al modelo de embeddings."


### 3. Transformar formato
> "Selecciono JSON como formato de salida. La app muestra el contenido transformado y permite descargarlo."

### 4. Validación
> "El sistema verifica que las columnas clave estén presentes después de la transformación y muestra un porcentaje de coincidencia"

---

## Slide 5: Métricas
> “Durante las pruebas, el agente logró un porcentaje de coincidencia semántica superior al 80% cuando las columnas del archivo original tenían nombres con relación clara al esquema estándar.

En todos los casos correctamente mapeados, la validación de consistencia estructural también fue exitosa, es decir, el archivo transformado conservó las entidades clave como cliente, monto, fecha o estatus.

Además, se realizaron pruebas con archivos intencionalmente modificados —por ejemplo, con columnas mal nombradas o faltantes—, y el sistema fue capaz de identificar estas inconsistencias y reportarlas como transformaciones inválidas.”

---

## Slide 6: Conclusión
“En resumen, este proyecto demuestra cómo es posible aplicar inteligencia artificial a un problema muy concreto pero muy común: la transformación de datos entre sistemas con estructuras distintas.

-Desarrollé una aplicación funcional en Streamlit que incluye:
-Validación inteligente de estructura basada en significado,
-Mapeo semántico automático mediante embeddings,
-Pruebas automatizadas para garantizar la robustez,
-Y una documentación clara y completa del proceso.

Este agente puede adaptarse fácilmente a distintos sectores: financieros, médicos, académicos o administrativos, facilitando la interoperabilidad entre sistemas heterogéneos.
---

## Cierre
> "Gracias por su tiempo e interés por ver este demo. Toda la documentación, código y pruebas están disponibles en el repositorio de GitHub."

---

