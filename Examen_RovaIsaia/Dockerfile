# Image de Base python
FROM python:3.10-slim

# Informations
LABEL maintainer="isaiapix@gmail.com"

# Dossier de travail
WORKDIR /app

# copier et installer les dependeces
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copier le code source
COPY app.py .
EXPOSE 5000
# command de lancement
CMD ["python","app.py"]