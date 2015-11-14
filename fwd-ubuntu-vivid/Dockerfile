FROM ubuntu:vivid
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN apt-get -y update 
RUN apt-get -y install rubygems-integration ruby-dev build-essential rsync
RUN apt-get -y dist-upgrade
RUN gem install fpm -v 1.3.3
