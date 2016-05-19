FROM fedora:rawhide
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN dnf clean metadata && dnf -y update && dnf -y install ruby ruby-devel rubygems libffi libffi-devel @"Development Tools" rpm-build rsync
RUN gem install fpm -v 1.5.0
RUN dnf clean all
