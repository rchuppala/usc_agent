Summary: Netopeer - NETCONF implementation. Server part.
Name: netopeer-server
Version: %(cut -f1 ./VERSION | tr -d '\n')
Release: 1
URL: http://www.liberouter.org/
Source: https://www.liberouter.org/repo/SOURCES/%{name}-%{version}-%{release}.tar.gz
Group: Liberouter
License: BSD
Vendor: CESNET, z.s.p.o.
Packager:  <>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires: gcc make doxygen pkgconfig
BuildRequires:  python libxml2-devel libnetconf-devel
Requires:  python libxml2 libnetconf

%description
Netopeer project implements NETCONF protocol for remote configuration of
network devices. This package contains its server part.

%prep
%setup

%build
./configure --with-distro=ubuntu --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --with-rpm  --disable-dbus;
make
make doc

%install
make DESTDIR=$RPM_BUILD_ROOT install

%post
#SSHD config
if test -f /etc/ssh/sshd_config; then \
        grep -Ev "^Subsystem|^Port" /etc/ssh/sshd_config > %{_sysconfdir}/netopeer/sshd_config; \
else \
        touch %{_sysconfdir}/netopeer/sshd_config; \
fi; \
echo "" >> %{_sysconfdir}/netopeer/sshd_config; \
echo "# NETCONF SSH Subsystem settings" >> %{_sysconfdir}/netopeer/sshd_config; \
echo "Subsystem netconf %{_bindir}/netopeer-agent" >> %{_sysconfdir}/netopeer/sshd_config; \

%postun

%files
%{_bindir}/netopeer-server
%{_bindir}/netopeer-agent
%{_bindir}/netopeer-manager
%{_bindir}/netopeer-configurator
%{_prefix}/lib/python*/site-packages/netopeer*
%{_sysconfdir}/netopeer/*
%{_sysconfdir}/init.d/netopeer.rc
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_datadir}/netopeer/*.html



