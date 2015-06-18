# fpm-within-docker

Pre-baked images for package building. [fpm](https://github.com/jordansissel/fpm) is included!

## what does this do?

If you don't want to spend your nights in learning packaging an RPM or a DEB - which is a good idea - FPM can help.

But, out of the box, fpm doesn't provide a "sandbox" or any other "isolated environment" for building. Here comes this set of images.

## Usage

In a directory, let's call it *build-directory*, create a new Dockerfile that inherits from the one for the distro you need and installs your build dependencies, e.g.:

```
FROM alanfranz/fwd-centos-7:latest
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN yum clean metadata && yum -y update
RUN yum -y install python-devel libffi-devel
```

And in the same dir create a script to be run inside the container, something like

```
#!/bin/bash
set -ex
[ -n "$1" ]
mkdir -p /opt
cd /application
rsync -av --filter=':- .gitignore' --exclude='.git' . /tmp/myapplication
cd /tmp/myapplication
make clean all install PREFIX=/opt/myapplication
cd /build
fpm -t rpm -s dir -n dorkbox --version "$1" --depends something --depends somethingelse -C / opt
chmod 666 *
```

In this example, */application* is where the sources of your app get bindmounted, while */build* is where the output deb/rpm is saved.
The application gets installed in /opt. You should specify all the runtime dependencies in the fpm invocation.

Then create the build image and use it to build your package (assuming your sources are in the current dir):

```
docker build --pull -t myapplication-build build-directory
docker run --rm -v $(pwd):/application:ro -v $(pwd)/out:/build -w /application myapplication-build /application/build-directory/make-package.sh 1.2.3
```
## Using the images

They're available on Docker hub. All of them are just tagged **latest**.

```
alanfranz/fwd-fedora-rawhide
alanfranz/fwd-fedora-22
alanfranz/fwd-centos-6
alanfranz/fwd-centos-7
alanfranz/fwd-centos-7
alanfranz/fwd-ubuntu-precise
alanfranz/fwd-ubuntu-trusty
alanfranz/fwd-ubuntu-utopic
alanfranz/fwd-ubuntu-vivid
alanfranz/fwd-debian-wheezy
alanfranz/fwd-debian-jessie


```

