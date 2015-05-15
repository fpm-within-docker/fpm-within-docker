FROM fedora:rawhide
MAINTAINER Alan Franzoni <username@franzoni.eu>
# fedora rawhide docker image has not dnf yet, while fc22 has... sigh.
RUN yum clean metadata && yum -y update
RUN dnf clean metadata && dnf -y update && dnf -y install ruby ruby-devel rubygems libffi libffi-devel @"Development Tools" redhat-rpm-config
RUN gem install fpm -v 1.3.3
