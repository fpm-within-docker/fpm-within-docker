FROM centos:6
MAINTAINER Alan Franzoni <username@franzoni.eu>

RUN yum clean metadata \
 && yum -y update \
 && yum install -y centos-release-scl \
 && yum -y install \
    @"Development Tools" \
    gnupg2 \
    libffi \
    libffi-devel \
    rsync \
    ruby193 \
    ruby193-ruby-devel \
 && yum clean all

RUN scl enable ruby193 "gem install --no-ri --no-rdoc fpm -v 1.9.3"
COPY files/etc/rpm/macros.fwd /etc/rpm/macros.fwd
COPY files/usr/bin/fpm /usr/bin/fpm
