FROM ubuntu:focal
MAINTAINER Alan Franzoni <username@franzoni.eu>
COPY 80-acquire-retries /etc/apt/apt.conf.d/
RUN apt-get update && apt-get -y install apt-transport-https curl gnupg
RUN curl https://www.franzoni.eu/keys/D401AB61.txt | apt-key add -
RUN apt -y install ruby rubygems-integration ruby-dev build-essential rsync
RUN apt -y dist-upgrade
RUN gem install fpm -v 1.13.1
