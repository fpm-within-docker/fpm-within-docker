# credits should go to lnxchk - https://github.com/lnxchk/ruby-1.9.3-rpm
%define rubyver         1.9.3
%define rubyminorver    p551

Name:           ruby193
Version:        %{rubyver}%{rubyminorver}
Release:        2%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libyaml-devel
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}-%{rubyminorver}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}-%{rubyminorver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --bindir=/opt/ruby193/bin \
  --mandir=/opt/ruby193/usr/share/man \
  --includedir=/opt/ruby193/include/ruby \
  --libdir=/opt/ruby193/lib \
  --prefix=/opt/ruby193

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/opt/ruby193

%changelog
* Wed Jan 18 2012 Mandi Walls <mandi.walls@gmail.com> - 1.9.3-p0
- Update ruby version to 1.9.3-p0
* Mon Aug 29 2011 Gregory Graf <graf.gregory@gmail.com> - 1.9.2-p290
- Update ruby version to 1.9.2-p290
* Sat Jun 25 2011 Ian Meyer <ianmmeyer@gmail.com> - 1.9.2-p180-2
- Remove non-existant --sitearchdir and --vedorarchdir from %configure
- Replace --sitedir --vendordir with simpler --libdir
- Change %{_prefix}/share to %{_datadir}

* Tue Mar 7 2011 Robert Duncan <robert@robduncan.co.uk> - 1.9.2-p180-1
- Update prerequisites to include make
- Update ruby version to 1.9.2-p180
- Install /usr/share documentation
- (Hopefully!?) platform agnostic

* Sun Jan 2 2011 Ian Meyer <ianmmeyer@gmail.com> - 1.9.2-p136-1
- Initial spec to replace system ruby with 1.9.2-p136
