FROM ubuntu:utopic
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN apt-get -y update 
RUN apt-get -y install rubygems-integration ruby-dev build-essential ca-certificates
RUN apt-get -y dist-upgrade
RUN update-ca-certificates
RUN gem install fpm -v 1.3.3
