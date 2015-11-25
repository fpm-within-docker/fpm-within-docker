# fpm-within-docker

Pre-baked images for package building. [fpm](https://github.com/jordansissel/fpm) is included!

## what does this do?

If you don't want to spend your nights in learning packaging an RPM or a DEB - which is a good idea - FPM can help.
But, out of the box, fpm doesn't provide a "sandbox" or any other "isolated environment" for building. Here comes this set of images.

You should still know something about package building.

For RPM see [Maximum RPM](http://www.rpm.org/max-rpm/), [Fedora RPM Howto](https://fedoraproject.org/wiki/How_to_create_an_RPM_package), or [Fedora RPM Guide](https://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/).

For DEB, see [Debian How To Package](https://wiki.debian.org/HowToPackageForDebian) or [Ubuntu Packaging New Software](http://packaging.ubuntu.com/html/packaging-new-software.html).

You'd better know what [docker](https://www.docker.com/) is, as well.

## Usage

Take a look at the example in the [example project](example-project) directory - it's an example build of a [lua interpreter](http://www.lua.org)
for Centos7 and Ubuntu Trusty. The files are commented to let you understand what happens when building and testing the package.

The main build scripts are commented and will tell you what you should know: see [build for centos 7](example-project/packaging/centos-7/build) and [build for ubuntu trusty](example-project/packaging/ubuntu-trusty/build)

## Limitations

Currently the images are x86_64 only. There's an exception for
centos5 i386, since I had an actual use case, but its creation
was very tedious, and docker doesn't officially endorse 32 bit guests.

I'll add 32 bit images only if help is provided.

## Using the fpm-within-docker images

They're available on Docker hub. All of them are just tagged **latest**.
I'll usually add images for Centos, Fedora, Ubuntu and Debian as soon
as they get out, and I'll try supporting them as long as they're supported upstream.

Take a look at the repository; all the directories starting with *fwd* are the sources
for their respective images, which can be found on [my page on Docker Hub](https://hub.docker.com/u/alanfranz/)

All images are tagged "latest"; so, for Centos 7 you'd use the **alanfranz/fwd-centos-7:latest**
docker image.
