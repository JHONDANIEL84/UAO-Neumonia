# UAO-Neumonía  
**Software para el apoyo al diagnóstico médico de neumonía**

---

## 📌 Información general

**Asignatura:** Desarrollo de Proyectos de Inteligencia Artificial  
**Institución:** Universidad Autónoma de Occidente (UAO)  
**Periodo:** 2026-01  
**Tipo de entrega:** Proyecto neumonía

---

## 👨‍🎓 Integrantes del grupo

- **JHON DANIEL CALVACHE**  
  Código: **22503009**

- **DIEGO FERNANDO BOLAÑOS BUSTOS**
  Código: **2237182**

---

## 🧠 Descripción del proyecto

UAO-Neumonía es una aplicación de escritorio desarrollada en **Python** que sirve como **herramienta de apoyo al diagnóstico médico** de neumonía a partir de **imágenes radiográficas de tórax**.

El sistema utiliza un **modelo de Deep Learning (CNN)** entrenado previamente para clasificar imágenes en las siguientes categorías:

- Neumonía bacteriana  
- Neumonía viral  
- Normal (sin neumonía)

Además, la aplicación incorpora **técnicas de explicabilidad (Grad-CAM)** para generar mapas de calor que permiten visualizar las regiones de la imagen que influyen en la decisión del modelo.

---

## ⚙️ Funcionalidades principales

- Carga de imágenes médicas en formatos **DICOM, JPG, JPEG y PNG**
- Preprocesamiento automático de imágenes
- Predicción de clase y probabilidad
- Visualización de **heatmap (Grad-CAM)**
- Interfaz gráfica desarrollada con **Tkinter**
- Exportación de resultados a:
  - Archivo CSV (historial)
  - Reporte en PDF
- Ejecución sin warnings críticos

---

## 🧪 Tecnologías utilizadas

- **Python 3.10+**
- **TensorFlow / Keras**
- **OpenCV**
- **NumPy**
- **Pillow (PIL)**
- **Tkinter**
- **UV** (gestión moderna de dependencias)
- **Docker**

---

## 🧬 Modelo de Deep Learning

- **Archivo:** `conv_MLP_84.h5`
- **Tipo:** Red neuronal convolucional (CNN)
- **Uso:** Clasificación de imágenes radiográficas
- **Explicabilidad:** Grad-CAM sobre la última capa convolucional

⚠️ El archivo del modelo es binario y no se visualiza en el editor de texto, lo cual es el comportamiento esperado.

---

## 📁 Estructura del proyecto

```text
UAO-NEUMONIA/
├── .github/
│   └── copilot-instructions.md
├── detector_neumonia.py
├── main.py
├── conv_MLP_84.h5
├── pyproject.toml
├── uv.lock
├── Dockerfile
├── README.md
├── historial.csv
└── .gitignore


## 📦 Gestión de dependencias (UV)

Este proyecto utiliza UV en lugar de requirements.txt, cumpliendo con las recomendaciones del curso.

Crear entorno virtual
uv venv

Instalar dependencias
uv pip install -e .

## ▶️ Ejecución del proyecto
python main.py


Al ejecutar el proyecto se abrirá la interfaz gráfica para cargar imágenes y realizar predicciones.

## 🐳 Docker

El proyecto incluye un Dockerfile funcional para facilitar la ejecución en entornos controlados.

docker build -t uao-neumonia .
docker run uao-neumonia

🧾 Evidencia de ejecución

La aplicación ejecuta correctamente sin errores críticos.
Se incluyen evidencias visuales de ejecución.

⚠️ Advertencias conocidas

Algunos mensajes informativos de TensorFlow (oneDNN, deprecations) son propios de la librería y no afectan el funcionamiento del sistema.

Se utilizan funciones tf.compat.v1 por compatibilidad con Grad-CAM.

📄 Licencia

Proyecto académico desarrollado con fines educativos.

✅ Estado del proyecto

✔ Repositorio limpio
✔ Uso de UV
✔ README profesional
✔ Docker funcional
✔ Evidencia de ejecución
✔ Modelo incluido



