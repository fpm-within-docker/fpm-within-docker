FROM ubuntu:noble
MAINTAINER Alan Franzoni <username@franzoni.eu>
COPY 80-acquire-retries /etc/apt/apt.conf.d/
RUN apt-get update && apt-get -y install apt-transport-https curl gnupg ruby rubygems-integration ruby-dev build-essential rsync && apt -y dist-upgrade
RUN gem install fpm -v 1.15.1
