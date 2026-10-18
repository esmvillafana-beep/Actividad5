# Actividad 5 — Preparación, entrenamiento y trazabilidad de IA

**Autora:** Esmeralda Villafaña · **Asignatura:** Gestión de Proyectos de Inteligencia Artificial.

## Descripción y alcance
Proyecto académico de PLN aplicado a comentarios **sintéticos** sobre el Copiloto Operativo para Empleados de **Banco Horizonte Digital**, organización ficticia. Se reutilizan los 36 comentarios de la Actividad 4 (12 POS, 12 NEG, 12 NEU), como muestra de partida; esta cantidad no basta para validar generalización ni comparar modelos con alta confianza.

## Estado actual
**Punto 1 — preparación del entorno y estructura del repositorio.** No se ha entrenado ningún modelo de Actividad 5 ni registrado ejecuciones de MLflow en esta entrega inicial. Se prevé comparar al menos dos modelos, usar `GridSearchCV` con validación cruzada, y registrar parámetros, métricas y artefactos en MLflow.

## Estructura
```text
Actividad5/
├── datos/
│   ├── datos_ini/comentarios_originales_v1.csv
│   └── datos_limp/README.md
├── fuentes/
│   ├── entrena.ipynb
│   ├── datos_prep.py
│   └── train.py
├── resultados/
├── README.md
├── CHANGELOG.md
├── requirements.txt
└── .gitignore
```

## Entorno de ejecución
Python 3.10+; Google Colab o entorno local. Bibliotecas en `requirements.txt`. La preparación del dataset no requiere GPU; los clasificadores tradicionales propuestos tampoco.

## Reproducción de la preparación
```bash
pip install -r requirements.txt
python fuentes/datos_prep.py
```
Se generará `datos/datos_limp/comentarios_limpios_v1.csv`. Las reglas conservan tildes y semántica; normalizan espacios y etiquetas; eliminan nulos y duplicados exactos. Toda modificación se deberá documentar en `CHANGELOG.md`.

## Git y GitHub
Crear en GitHub un repositorio **vacío** llamado `Actividad5-PLN-Banco-Horizonte-Digital` (sin README automático). Desde la carpeta `Actividad5`:
```bash
git init
git add .
git commit -m "Actividad 5: estructura inicial y dataset versionado"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/Actividad5-PLN-Banco-Horizonte-Digital.git
git push -u origin main
```
Sustituir `TU_USUARIO` por el usuario de GitHub. La conexión a la cuenta y el `push` deben hacerse por la propietaria de la cuenta; este archivo no significa que ya se publicaron.

## Resultados y conclusiones parciales
En esta etapa queda organizada una versión inicial del conjunto de datos y preparada la estructura de ejecución. Todavía no existen resultados nuevos de entrenamiento ni trazas MLflow. La conclusión principal es que el repositorio facilita el seguimiento del ciclo de vida, pero será necesario ampliar y validar datos para evaluar modelos de manera rigurosa.

## Seguridad
No incluir tokens de Hugging Face, GitHub, credenciales o datos personales. Usar secretos de Colab para las credenciales.
