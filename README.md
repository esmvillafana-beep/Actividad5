# Actividad 5 — Preparación, entrenamiento y trazabilidad de IA

**Autora:** Esmeralda Villafaña  
**Asignatura:** Gestión de Proyectos de Inteligencia Artificial  
**Proyecto:** Análisis de sentimientos aplicado al Copiloto Operativo para Empleados de Banco Horizonte Digital.

## Descripción del proyecto

Este repositorio contiene los archivos técnicos de un proyecto académico de procesamiento de lenguaje natural aplicado a la clasificación de sentimientos de comentarios ficticios en español.

El caso de uso se relaciona con el Copiloto Operativo para Empleados de Banco Horizonte Digital, una organización ficticia.

Se utiliza un conjunto inicial de 36 comentarios sintéticos, distribuidos en tres categorías: positivo (POS), negativo (NEG) y neutral (NEU).

## Estado actual

Se completaron las siguientes actividades:

- Preparación y versionado inicial del dataset.
- Creación del repositorio y organización del código.
- Configuración de MLflow con almacenamiento local mediante SQLite.
- Ejecución piloto de regresión logística con representación TF-IDF.
- Registro de parámetros, métricas y artefactos experimentales.
- Incorporación del cuaderno y las evidencias al repositorio.

La comparación definitiva entre regresión logística y SVM lineal, utilizando validación cruzada y GridSearchCV, corresponde a la siguiente etapa del proyecto.

## Estructura del repositorio

```text
Actividad5/
├── datos/
│   ├── datos_ini/
│   │   └── comentarios_originales_v1.csv
│   └── datos_limp/
│       └── comentarios_limpios_v1.csv
├── fuentes/
│   ├── datos_prep.py
│   ├── entrena.ipynb
│   ├── entrena_mlflow.ipynb
│   └── train.py
├── resultados/
│   └── piloto_mlflow/
│       ├── parametros_mlflow.csv
│       ├── metricas_mlflow.csv
│       ├── predicciones.csv
│       ├── reporte_clasificacion.json
│       ├── matriz_confusion.png
│       ├── resumen_ejecucion.json
│       └── identificador_ejecucion.txt
├── README.md
├── CHANGELOG.md
└── requirements.txt
```

## Entorno de ejecución

El proyecto utiliza Python, Google Colab, Pandas, Scikit-learn, Matplotlib y MLflow.

El experimento piloto se ejecutó mediante CPU y utilizó SQLite como base de datos de seguimiento local.

## Pasos de reproducción

1. Obtener una copia del repositorio.
2. Instalar las dependencias indicadas en `requirements.txt`.
3. Ejecutar `fuentes/datos_prep.py` para preparar el dataset.
4. Abrir `fuentes/entrena_mlflow.ipynb` en Google Colab.
5. Ejecutar las celdas del cuaderno en orden.
6. Verificar el registro de parámetros, métricas y artefactos.
7. Consultar las evidencias almacenadas en `resultados/piloto_mlflow/`.

## Resultados y evidencias

La ejecución piloto permitió registrar información experimental mediante MLflow.

Las métricas observadas se encuentran en `resultados/piloto_mlflow/metricas_mlflow.csv`.

Los parámetros utilizados se encuentran en `resultados/piloto_mlflow/parametros_mlflow.csv`.

También se conservan las predicciones, el reporte de clasificación, la matriz de confusión, el resumen de ejecución y el identificador del experimento.

## Conclusiones parciales

La configuración de MLflow permitió comprobar la utilidad del seguimiento experimental para documentar pruebas de aprendizaje automático.

El registro de parámetros y métricas facilita la trazabilidad, mientras que los artefactos aportan evidencia adicional para revisar las predicciones.

Sin embargo, la muestra utilizada contiene únicamente 36 comentarios sintéticos. Por esta razón, los resultados corresponden a una prueba académica y no permiten garantizar el desempeño del modelo en un entorno productivo.

La siguiente etapa consistirá en comparar regresión logística y SVM lineal mediante validación cruzada, GridSearchCV y registros adicionales de MLflow.

## Repositorio

https://github.com/esmvillafana-beep/Actividad5

## Seguridad

Los datos utilizados son sintéticos. No se incluyen datos personales reales ni credenciales de acceso.

Las bases de datos locales y los artefactos completos de MLflow pueden conservarse como respaldo independiente cuando no sea necesario publicarlos.
