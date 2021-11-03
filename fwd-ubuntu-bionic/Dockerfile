FROM ubuntu:bionic
MAINTAINER Alan Franzoni <username@franzoni.eu>
COPY 80-acquire-retries /etc/apt/apt.conf.d/
RUN apt-get update && apt-get -y install apt-transport-https curl gnupg
RUN apt -y install ruby rubygems-integration ruby-dev build-essential rsync
RUN apt -y dist-upgrade
RUN gem install fpm -v 1.13.1
