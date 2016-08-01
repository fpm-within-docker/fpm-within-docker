FROM ubuntu:wily
MAINTAINER Alan Franzoni <username@franzoni.eu>
COPY 80-acquire-retries /etc/apt/apt.conf.d/
RUN apt-get -y update 
RUN apt-get -y install ruby rubygems-integration ruby-dev build-essential rsync
RUN apt-get -y dist-upgrade
RUN gem install fpm -v 1.6.2
RUN apt-get clean
