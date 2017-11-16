FROM fedora:27
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN dnf clean metadata \
 && dnf -y update \
 && dnf -y install \
    @"Development Tools" \
    gnupg \
    libffi \
    libffi-devel \
    rpm-build \
    rpm-sign \
    rsync \
    ruby \
    ruby-devel \
    rubygems \
 && dnf clean all
RUN gem install --no-ri --no-rdoc fpm -v 1.9.3
