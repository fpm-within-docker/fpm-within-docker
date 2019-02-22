FROM centos:6
MAINTAINER Alan Franzoni <username@franzoni.eu>

RUN yum clean metadata \
 && yum -y update \
 && yum install -y centos-release-scl \
 && yum install -y rh-ruby24 rh-ruby24-ruby-devel \
 && yum -y install \
    @"Development Tools" \
    scl-utils \
    gnupg2 \
    libffi \
    libffi-devel \
    rsync \
 && yum clean all

RUN scl enable rh-ruby24 "gem install --no-ri --no-rdoc fpm -v 1.11.0"
COPY files/etc/rpm/macros.fwd /etc/rpm/macros.fwd
COPY files/usr/bin/fpm /usr/bin/fpm
