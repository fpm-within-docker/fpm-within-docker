FROM ubuntu:precise
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN apt-get -y update 
RUN apt-get -y install ruby1.9.1-full ruby1.9.1-dev build-essential rsync
RUN apt-get -y dist-upgrade
RUN gem install fpm -v 1.3.3
