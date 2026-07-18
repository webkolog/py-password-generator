# Resmi Python imajını kullan
FROM python:3.14-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Script dosyasını kopyala
COPY generator.py .

# Uygulamayı çalıştır
CMD ["python", "generator.py"]