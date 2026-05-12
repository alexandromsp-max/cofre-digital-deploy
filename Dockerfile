# 1. Começamos com uma imagem leve (Slim)
FROM python:3.11-slim

# 2. Criamos um usuário sem privilégios para não rodar como root
RUN useradd -m appuser

# 3. Definimos a pasta de trabalho
WORKDIR /app

# 4. Copiamos o nosso script para dentro da imagem
COPY app.py .

# 5. Mudamos o dono dos arquivos para o nosso usuário comum
RUN chown -R appuser:appuser /app

# 6. Trocamos para o usuário comum
USER appuser

# 7. Comando para rodar a aplicação
CMD ["python", "app.py"]
