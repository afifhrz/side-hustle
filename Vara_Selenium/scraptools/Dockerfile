FROM python:3.8.10-slim as builder

COPY . /scraptools
WORKDIR /scraptools

# We need wget to set up the PPA and xvfb to have a virtual screen and unzip to install the Chromedriver
RUN apt-get update -y && apt-get install -y gnupg2 && apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get install -y wget xvfb unzip

RUN pip install --upgrade -r /scraptools/requirements.txt

ENV TZ=Asia/Jakarta
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["uvicorn", "scraptools.asgi:application", "--host", "0.0.0.0", "--port", "2023", "--reload"]

EXPOSE 2023

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update

# Update the package list and install chrome
RUN apt-get install -y google-chrome-stable
RUN apt-get install -y libgconf-2-4

# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 111.0.5563.64
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir $CHROMEDRIVER_DIR

# Download and install Chromedriver
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR

# Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH