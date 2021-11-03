FROM centos:8
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN dnf clean metadata \
 && dnf -y update \
 && dnf -y install @"Development Tools"  gnupg2  libffi libffi-devel   rsync  ruby rubygems ruby-devel && dnf -y clean all
RUN gem install --no-ri --no-rdoc fpm -v 1.13.1
COPY files/etc/rpm/macros.fwd /etc/rpm/macros.fwd
