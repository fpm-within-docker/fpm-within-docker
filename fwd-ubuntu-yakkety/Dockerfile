FROM ubuntu:yakkety
MAINTAINER Alan Franzoni <username@franzoni.eu>
COPY 80-acquire-retries /etc/apt/apt.conf.d/
# workaround as long as yakkety is in beta state
RUN apt -y update && apt -y full-upgrade && apt -y install dirmngr ruby rubygems-integration ruby-dev build-essential rsync
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv A1D267C030C00DCB877900ED939C61C5D1270819
RUN echo "deb http://www.a9f.eu/apt/apt-current-v1/ubuntu yakkety main" > /etc/apt/sources.list.d/apt-current-v1.list
RUN apt-get -y update 
RUN apt-get -y install apt-current
RUN /bin/echo -e "MAXDELTA=3600\nCLEANUP_DOWNLOADED_PACKAGES=\"true\"\nCLEANUP_DOWNLOADED_LISTS=\"true\"\n" > /etc/apt-current.conf
RUN gem install fpm -v 1.7.0
