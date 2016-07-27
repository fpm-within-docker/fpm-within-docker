FROM ubuntu:precise
MAINTAINER Alan Franzoni <username@franzoni.eu>
COPY 80-acquire-retries /etc/apt/apt.conf.d/
RUN apt-get -y update 
COPY *.deb /tmp/
RUN dpkg -i /tmp/*.deb || /bin/true
RUN apt-get -y -f install
RUN apt-get -y install build-essential rsync ca-certificates
RUN apt-get -y dist-upgrade
RUN gem install fpm -v 1.5.0
RUN apt-get clean
