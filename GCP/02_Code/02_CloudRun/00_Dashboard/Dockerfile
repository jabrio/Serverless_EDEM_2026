# Usamos Python oficial
FROM python:3.11-slim

# Crear carpeta de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código
COPY main.py .

# Puerto que usa Streamlit
ENV PORT 8080
ENV STREAMLIT_SERVER_PORT 8080
ENV STREAMLIT_SERVER_HEADLESS true
ENV STREAMLIT_SERVER_ENABLECORS false

# Comando para ejecutar Streamlit
CMD ["streamlit", "run", "main.py"]
