## Versión 0.2 — Integración de MLflow

**Cambios incorporados:**

- Se configuró MLflow con seguimiento local mediante SQLite.
- Se ejecutó un modelo piloto de regresión logística con TF-IDF.
- Se registraron parámetros y métricas de clasificación.
- Se generaron evidencias de predicciones, reporte de clasificación y matriz de confusión.
- Se incorporó el cuaderno `entrena_mlflow.ipynb` en la carpeta `fuentes/`.
- Se añadieron las evidencias experimentales en `resultados/piloto_mlflow/`.
- Se actualizó la documentación para reflejar el estado actual del proyecto.

**Pendiente:** entrenamiento comparativo de regresión logística y SVM lineal, optimización con GridSearchCV y validación cruzada.
