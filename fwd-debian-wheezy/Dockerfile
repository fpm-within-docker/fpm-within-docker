FROM debian:wheezy
MAINTAINER Alan Franzoni <username@franzoni.eu>
COPY 80-acquire-retries /etc/apt/apt.conf.d/
RUN apt-get -y update 
RUN apt-get -y install rubygems-integration ruby-dev ruby build-essential rsync
RUN apt-get -y dist-upgrade
RUN gem install json -v 1.8.3
RUN gem install fpm -v 1.8.1
RUN apt-get clean
