FROM python:3.8
ENV DEBIAN_FRONTEND noninteractive
ENV TZ=Asia/Taipei\
    DEBIAN_FRONTEND=noninteractive
RUN apt update \
    && apt install -y tzdata \
    && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update
RUN apt-get clean -y
COPY / /api/
WORKDIR /api
RUN pip install -r requirment.txt
CMD ["gunicorn", "-c", "./gunicorn.conf.py","app:app"]