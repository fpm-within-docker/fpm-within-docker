FROM fedora:rawhide
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN touch /var/lib/rpm/*
RUN dnf clean metadata && dnf -y update && dnf -y install ruby ruby-devel rubygems libffi libffi-devel @"Development Tools" rpm-build rsync
RUN gem install fpm -v 1.9.3
RUN dnf clean all
