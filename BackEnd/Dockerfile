FROM python:3-alpine

#set work directory
WORKDIR /usr/src/BackEnd

#set enviroment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONBUFFERED 1

#Pillow dependencies
RUN apk update \
                && apk --no-cache add postgresql-dev\
                gcc \
                python3-dev \
                musl-dev \
                zlib-dev \
                freetype-dev \
                lcms2-dev \
                openjpeg-dev \
                tiff-dev \
                tk-dev \
                tcl-dev \
                harfbuzz-dev \
                fribidi-dev

#install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/BackEnd/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/BackEnd/entrypoint.sh

# copy project
COPY . /usr/src/BackEnd/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/BackEnd/entrypoint.sh"]