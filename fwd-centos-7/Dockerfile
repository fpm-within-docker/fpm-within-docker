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
    ruby \
    ruby-devel \
    rubygems \
 && yum clean all
RUN gem install --no-ri --no-rdoc fpm -v 1.8.1
COPY files/etc/rpm/macros.fwd /etc/rpm/macros.fwd
