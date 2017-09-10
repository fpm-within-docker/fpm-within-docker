FROM centos:6
MAINTAINER Alan Franzoni <username@franzoni.eu>

ENV PATH /opt/rh/ruby193/root/usr/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV PKG_CONFIG_PATH /opt/rh/ruby193/root/usr/lib64/pkgconfig
ENV LD_LIBRARY_PATH /opt/rh/ruby193/root/usr/lib64

RUN yum clean metadata \
 && yum -y update \
 && yum install -y centos-release-scl \
 && yum -y install \
    @Base \
    @"Development Tools" \
    gnupg2 \
    libffi \
    libffi-devel \
    rsync \
    ruby193 \
    ruby193-ruby-devel \
 && yum clean all
RUN gem install --no-ri --no-rdoc fpm -v 1.8.1
COPY files/etc/rpm/macros.fwd /etc/rpm/macros.fwd
