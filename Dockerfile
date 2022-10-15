# creating ubuntu container from ubuntu image downloading it from docker hub
FROM ubuntu

#it downloads the package information from the Internet
RUN apt-get update

# it downloads the package and install it
RUN apt-get upgrade

# install git
RUN apt-get install git -y

# install python
RUN apt-get install python-is-python3 -y

# install virtualenv
RUN apt-get install virtualenv -y

# cloning repo project
RUN git clone https://github.com/yogesh2k21/fly-backend.git

# setting working directory
WORKDIR /fly-backend

# creating virtual env
RUN virtualenv venv

# show permission error so i give all premission 777 read,write,delete
RUN chmod 777 venv
 
# activating and installing dependencies
RUN . venv/bin/activate && pip install -r requirements.txt

# exposing port of ubuntu container
EXPOSE 8000

# running the bash.sh file to start venv and django server
CMD [ "bash","run.sh" ]