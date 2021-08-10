FROM python:3.8-slim
# FROM tiangolo/uvicorn-gunicorn:python3.8
# FROM centos/python-36-centos7

# copia tudo dentro do contexto para o diretorio /app dentro do container
COPY . /app

# seta o /app como diretorio base
WORKDIR /app

# instala as dependencias do python
RUN pip install uvicorn
RUN pip install fastapi
RUN pip install sklearn
RUN pip install pandas

# requerimento para rodar o flask run
ENV FASTAPI_APP=main.py

# comando rodado ao iniciar o container
CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000", "--reload"]
