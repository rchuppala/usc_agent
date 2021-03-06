Summary: NETCONF protocol library for NETCONF applications.
Name: libnetconf
Version: 0.9.0
Release: 48_trunk
URL: http://www.liberouter.org/
Source: https://www.liberouter.org/repo/SOURCES/%{name}-%{version}-%{release}.tar.gz
Group: Liberouter
License: BSD
Vendor: CESNET, z.s.p.o.
Packager:  <>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires: gcc make doxygen pkgconfig libxml2-devel libxslt-devel  libssh2-devel >= 1.2.0 openssl-devel >= 1.0.0 libcurl-devel
Provides:  libnetconf-notifications libnetconf-url

%description
Library provides NETCONF protocol functionality for both client as well as
server side applications. It also handles access to the NETCONF
configuration data repositories.

%package devel
Summary: libnetconf development package
Group: Liberouter
Requires: libnetconf = %{version}-%{release}  libssh2-devel >= 1.2.0 openssl-devel >= 1.0.0
Provides: libnetconf-devel

%description devel
This package contains header files for libnetconf library. Install this package
if you want to develop your own NETCONF application.

%prep
%setup

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --with-rpm --enable-debug --enable-tls ;
make
make doc

%install
make DESTDIR=$RPM_BUILD_ROOT install

%post
ldconfig

%files
%{_libdir}/libnetconf.so.*
%{_libdir}/libnetconf.la
/var/lib/libnetconf/

%files devel
%{_libdir}/pkgconfig/libnetconf.pc
%{_libdir}/libnetconf.so
%{_libdir}/libnetconf.a
%{_prefix}/include/libnetconf*.h
%{_prefix}/include/libnetconf/*
%{_prefix}/share/libnetconf/doxygen/*
%{_bindir}/lnctool
%{_datadir}/libnetconf/templates/*
%{_datadir}/libnetconf/rnglib/*
%{_datadir}/libnetconf/xslt/*
