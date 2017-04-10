FROM centos:7
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN yum clean metadata && yum -y update && yum -y install ruby ruby-devel rubygems libffi libffi-devel gnupg2 @"Development Tools" rsync
RUN gem install fpm -v 1.8.1
ADD files/etc/rpm/macros.fwd /etc/rpm/macros.fwd
RUN yum clean all
