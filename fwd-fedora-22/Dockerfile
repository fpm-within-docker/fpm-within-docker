FROM fedora:22
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN dnf clean metadata && dnf -y update && dnf -y install ruby ruby-devel rubygems libffi libffi-devel @"Development Tools"
RUN gem install fpm -v 1.3.3
