FROM centos:7
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN yum clean metadata \
 && yum -y update \
 && yum -y install \
    @"Development Tools" \
    gnupg2 \
    libffi \
    libffi-devel \
    rsync \
    centos-release-scl && yum clean packages
RUN yum -y install rh-ruby23-ruby rh-ruby23-ruby-devel rh-ruby23-rubygems && yum clean all
# RUN yum clean all
RUN source /opt/rh/rh-ruby23/enable && gem install --no-ri --no-rdoc fpm -v 1.13.1
COPY files/etc/rpm/macros.fwd /etc/rpm/macros.fwd
COPY files/usr/local/bin/fpm /usr/local/bin/fpm 
RUN chmod +x /usr/local/bin/fpm
