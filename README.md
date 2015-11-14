# fpm-within-docker

Pre-baked images for package building. [fpm](https://github.com/jordansissel/fpm) is included!

## what does this do?

If you don't want to spend your nights in learning packaging an RPM or a DEB - which is a good idea - FPM can help.

But, out of the box, fpm doesn't provide a "sandbox" or any other "isolated environment" for building. Here comes this set of images.

## Usage

Take a look at the example in the [example usage](tree/master/example-usage) directory - it's an example build of [GNU Wget](https://savannah.gnu.org/git/?group=wget)
for Centos7 and Ubuntu Trusty.

In a directory, let's call it *build-directory*, create a new Dockerfile that inherits from the one for the distro you need and installs your build dependencies, e.g.:

```
FROM alanfranz/fwd-centos-7:latest
MAINTAINER Alan Franzoni <username@franzoni.eu>
RUN yum clean metadata && yum -y update
RUN yum -y install python-devel libffi-devel
```

The *yum install* line (but it would be the same for apt-get) is the same as your *BuildRequires* in an RPM specfile (or *Build-Depends* for DEB): it should install the *prerequisites* for doing the build (e.g. compilers, headers, etc). While you *could* do such install in the script below, you don't want to, since the build requirements can usually be cached, something that docker does wonderfully.

And in the same dir create a script to be run inside the container, something like:

```make-package.sh
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
chown -R --reference /application/make-package.sh .
```

In this example, */application* is where the sources of your app get bindmounted, while */build* is where the output deb/rpm is saved.
The application gets installed in /opt. You should specify all the runtime dependencies in the fpm invocation - those are the same as *Requires* in a RPM specfile, or *Depends* for a DEB package.

Then create the build image and use it to build your package (assuming your sources are in the current dir):

```
docker build --pull -t myapplication-build build-directory
docker run --rm -v $(pwd):/application:ro -v $(pwd)/out:/build -w /application myapplication-build /application/build-directory/make-package.sh 1.2.3
```

## Limitations

Currently the images are x86_64 only. There's an exception for
centos5 i386, since I had an actual use case, but its creation
was very tedious, and docker doesn't officially endorse 32 bit guests.

I'll add 32 bit images only if help is provided.

## Using the images

They're available on Docker hub. All of them are just tagged **latest**.
I'll usually add images for Centos, Fedora, Ubuntu and Debian as soon
as they get out, and I'll try supporting them as long as they're supported upstream.

Take a look at the repository; all the directories starting with *fwd* are the sources
for their respective images, which can be found on [my page on Docker Hub](https://hub.docker.com/u/alanfranz/)

All images are tagged "latest"; so, for Centos 7 you'd use the **alanfranz/fwd-centos-7:latest**
docker image.

