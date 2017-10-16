FROM fedora:26
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN dnf clean metadata && dnf -y update && dnf -y install ruby ruby-devel rubygems libffi libffi-devel @"Development Tools" rpm-build gnupg rpm-sign rsync
RUN gem install fpm -v 1.8.1
RUN dnf clean all
