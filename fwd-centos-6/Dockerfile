FROM centos:6
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN yum clean metadata && yum -y update && yum -y install ruby ruby-devel rubygems libffi libffi-devel gnupg2 @"Development Tools" @Base rsync
RUN gem install fpm -v 1.4.0
ADD files/etc/rpm/macros.fwd /etc/rpm/macros.fwd
