FROM alanfranz/centos5-i386:latest
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN linux32 yum clean metadata && linux32 yum -y update && linux32 yum -y install wget
RUN cd /tmp ; linux32 wget --no-check-certificate https://getfedora.org/static/217521F6.txt ; linux32 rpm --import /tmp/*.txt
RUN cd /tmp ;  wget --no-check-certificate https://dl.fedoraproject.org/pub/epel/epel-release-latest-5.noarch.rpm && linux32 yum -y localinstall /tmp/*.rpm
RUN linux32 yum -y install ruby ruby-devel rubygems libffi libffi-devel gcc make rpm-build rpmdevtools readline-devel ncurses-devel gdbm-devel tcl-devel openssl-devel db4-devel byacc libyaml-devel
RUN linux32 rpmdev-setuptree
COPY ruby193.spec /root/rpmbuild/SPECS/
COPY ruby-1.9.3-p551.tar.gz /root/rpmbuild/SOURCES/
RUN cd /root/rpmbuild/SPECS ; linux32 rpmbuild -bb ruby193.spec
RUN linux32 yum -y --nogpgcheck localinstall /root/rpmbuild/RPMS/i386/*.rpm
