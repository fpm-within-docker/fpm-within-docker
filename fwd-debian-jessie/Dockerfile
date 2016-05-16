FROM debian:jessie
MAINTAINER Alan Franzoni <username@franzoni.eu>
COPY 80-acquire-retries /etc/apt/apt.conf.d/
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv A1D267C030C00DCB877900ED939C61C5D1270819
RUN echo "deb http://www.a9f.eu/apt/apt-current-v1/debian jessie main" > /etc/apt/sources.list.d/apt-current-v1.list
RUN apt-get -y update 
RUN apt-get -y install apt-current
RUN /bin/echo -e "MAXDELTA=3600\nCLEANUP_DOWNLOADED_PACKAGES=\"true\"\nCLEANUP_DOWNLOADED_LISTS=\"true\"\n" > /etc/apt-current.conf
RUN apt-get-current -y install rubygems-integration ruby-dev ruby build-essential rsync
RUN apt-get-current -y dist-upgrade
RUN gem install fpm -v 1.5.0
