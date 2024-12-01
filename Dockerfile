FROM python:3.11.4-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# # Copia el archivo entrypoint.sh
# COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# # Otorga permisos de ejecución
# RUN chmod +x /usr/src/app/entrypoint.sh

# Copia el resto de los archivos del proyecto
COPY . /usr/src/app/


# Define el script de entrada
# ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
