FROM ubuntu:trusty
MAINTAINER Alan Franzoni <username@franzoni.eu>
COPY 80-acquire-retries /etc/apt/apt.conf.d/
RUN apt-get update && apt-get -y install apt-transport-https curl
RUN curl https://www.franzoni.eu/keys/D401AB61.txt | apt-key add -
RUN echo "deb https://dl.bintray.com/alanfranz/apt-current-v1-ubuntu-trusty trusty main" > /etc/apt/sources.list.d/apt-current-v1.list
RUN apt-get -y update 
RUN apt-get -y install apt-current
RUN /bin/echo -e "MAXDELTA=3600\nCLEANUP_DOWNLOADED_PACKAGES=\"true\"\nCLEANUP_DOWNLOADED_LISTS=\"true\"\n" > /etc/apt-current.conf
RUN apt-get-current -y dist-upgrade
RUN apt-get-current -y install rubygems-integration ruby-dev build-essential rsync
RUN gem install json -v 1.8.3
RUN gem install fpm -v 1.8.1
