# fpm-within-docker

**VERY IMPORTANT NOTICE:** because of time constraints, I'll keep this updated for Debian and Ubuntu LTS. Fedora and Ubuntu intermediate releases will be dropped. If I'm lagging behind, please open a ticket.

Pre-baked images for RPM and DEB package building. [fpm](https://github.com/jordansissel/fpm) is included!

All images are  updated to the latest FPM version, currently: **1.15.1**.

## Donate!

Do you like this project? Is it useful to you? If you'd like to reward me, donate something from [my wish list](http://amzn.eu/98Ey0a8)

## what does this do?

If you don't want to spend your nights in learning packaging an RPM or a DEB - which is a good idea - FPM can help.
But, out of the box, fpm doesn't provide a "sandbox" or any other "isolated environment" for building. Here comes this set of images.

You should still know something about package building.

For RPM see [Maximum RPM](http://www.rpm.org/max-rpm/), [Fedora RPM Howto](https://fedoraproject.org/wiki/How_to_create_an_RPM_package), or [Fedora RPM Guide](https://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/).

For DEB, see [Debian How To Package](https://wiki.debian.org/HowToPackageForDebian) or [Ubuntu Packaging New Software](http://packaging.ubuntu.com/html/packaging-new-software.html).

You'd better know what [docker](https://www.docker.com/) is, as well.

## Usage

I recommend you **take a look at the example in the [example project](example-project) directory** - it's an example build of a [lua interpreter](http://www.lua.org)
for Centos7 and Ubuntu Trusty. The directory contains the extracted source of lua 5.3.1, while the [packaging](example-project/packaging) dir contains our build scripts. The main build scripts are commented and will tell you what you should know: see [build for centos 7](example-project/packaging/centos-7/build) and [build for ubuntu trusty](example-project/packaging/ubuntu-trusty/build)

The build chain goes something like this:

* First, a build-image is constructed via docker. That usually inherits from an fpm-within-docker image. This image should include whatever is needed to **build** the software - most probably a bunch of *-dev* or *-devel* packages. I suggest you **don't install requirements which are specific to your project rather than your OS** - i.e. don't do ```pip install``` or ```gem install``` for your project dependencies. Although that could provide faster build speed, it will mingle OS dependencies with project level dependencies, and later it could happen that your project builds even though you forgot a dependency in your project file.
* Then, a build script is run into a container from that build image. Such build script can access the software source, which is usually employed to build and install the software, and performs the actual dep fetching, build, **and install**, so you'll get the software installed as it should be in such docker container - i.e. */usr/bin/mybinary* and */usr/share/mybinary/something*. Then, at the end of the build script, *fpm* is invoked with such paths and will create a deb/rpm package containing the binaries.
* After that (optionally), a test-image is constructed via docker. That **doesn't inherit from an fpm-within-docker image**; it's an image as bare as possible should be used, since the dependency checking part is performed in the next step.
* As a last step, a test script is invoked **within a container launched from the test image**. Such script should install the package that was just built, should let the package manager install any required dependency, and should run the test suite for the software, which will be tested in an environment **very close to actual production scenario**. This is especially useful to detect issues with missing or broken dependencies.

I suggest you just **copy** the whole packaging directory from the examples to your own project, then you add/remove the various distro-related subdirectories and modify them in place.

## Goodies

**I don't necessarily include apt-current anymore.**

## Limitations

Currently the images are x86_64 only. There's an exception for
centos5 i386, since I had an actual use case, but its creation
was very tedious, and docker doesn't officially endorse 32 bit guests.

I'll add 32 bit images only if help is provided.

## Signing RPMs

Fpm supports signing rpms, but there's a minimum of setup involved; check the [build for centos 7](example-project/packaging/centos-7/build) to see 
how it's done. You can both sign and verify the signature is OK.

**WARNING:** I retained some RPM macros that used to be necessary in Centos 6 and 7 in rocky linux 8 and 9, but I haven't actually tested proper signing with
such distro. If signing fails, please open an issue.

DEB packages are signed in the repository only, so no issue while building.

## Using the fpm-within-docker images

They're available on Docker hub, so they can be used straight from your docker command line, without the need of rebuilding them locally.

[fpm-within-docker images on Docker Hub](https://hub.docker.com/r/alanfranz/fpm-within-docker/tags)

All images are are x86_64 only. Please note: some older images may exist on docker hub, but if they're not listed down there, consider them unsupported.


Available images:

```
docker.io/alanfranz/fpm-within-docker:fedora-40
docker.io/alanfranz/fpm-within-docker:rockylinux-8
docker.io/alanfranz/fpm-within-docker:rockylinux-9
docker.io/alanfranz/fpm-within-docker:debian-bookworm
docker.io/alanfranz/fpm-within-docker:debian-bullseye
docker.io/alanfranz/fpm-within-docker:ubuntu-noble
docker.io/alanfranz/fpm-within-docker:ubuntu-jammy
docker.io/alanfranz/fpm-within-docker:ubuntu-focal
```

Please note that older images can exist on Docker Hub; I don't remove unsupported images when they're no longer built, that's up to you to choose when old is too old. 

## Thanks, in no special order

- Kevin Pankonen


