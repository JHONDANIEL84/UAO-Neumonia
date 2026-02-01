FROM python:3.10-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    python3-opencv \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instalar UV
RUN pip install uv

# Directorio de trabajo
WORKDIR /app

# Copiar proyecto
COPY . .

# Crear entorno e instalar dependencias con UV
RUN uv pip install -e .

# Ejecutar la aplicación
CMD ["python", "main.py"]
