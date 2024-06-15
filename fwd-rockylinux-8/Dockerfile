FROM rockylinux:8
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN dnf clean metadata \
 && dnf -y update \
 && dnf -y install @"Development Tools"  gnupg2  libffi libffi-devel   rsync  ruby rubygems ruby-devel && dnf -y clean all
# we need to do this because of gem dep resolution and pleaserun dotenv dependency which requires ruby 3.0+
RUN gem install dotenv -v 2.8.1 -N
RUN gem install clamp -v 1.0.1 -N
RUN gem install mustache -v 0.99.8 -N
RUN gem install cabin insist stud arr-pm backports rexml -N
RUN gem install pleaserun --ignore-dependencies -N
RUN gem install fpm --ignore-dependencies -N --no-document -v 1.15.1
COPY files/etc/rpm/macros.fwd /etc/rpm/macros.fwd
