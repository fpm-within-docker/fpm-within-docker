FROM fedora:22
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN dnf clean metadata && dnf -y update && dnf -y install ruby ruby-devel rubygems libffi libffi-devel @"Development Tools" rpm-build gnupg rsync
RUN gem install fpm -v 1.5.0
ADD files/etc/rpm/macros.fwd /etc/rpm/macros.fwd
