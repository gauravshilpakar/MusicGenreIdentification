# 1 
FROM ubuntu:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh 

# 2
RUN apt-get install -y python3.6
RUN apt install -y python3-pip
RUN pip3 install flask gunicorn tensorflow numpy pandas firebase-admin pytube3 librosa matplotlib joblib SoundFile
RUN apt-get install - libsndfile1-dev
# 3
# COPY src/ app/
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# 4
ENV PORT 8080

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app