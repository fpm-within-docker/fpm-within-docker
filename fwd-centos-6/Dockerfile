FROM centos:6
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN yum clean metadata && yum -y update && yum -y install ruby ruby-devel rubygems libffi libffi-devel @"Development Tools"
RUN gem install fpm -v 1.3.3
