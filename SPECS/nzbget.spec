%global _hardened_build 1

Name:          nzbget
Summary:       A binary newsgrabber
Version:       17.1
Release:       1%{?dist}
License:       GPL-2.0
Url:           http://nzbget.net/
Source0:       https://github.com/nzbget/nzbget/releases/download/v%{version}/%{name}-%{version}-src.tar.gz
BuildRequires: libxml2-devel
BuildRequires: ncurses-devel
BuildRequires: gnutls-devel
BuildRequires: openssl-devel


%description
NZBGet is a binary newsgrabber, which downloads files from usenet
based on information given in nzb-files. NZBGet can be used in
standalone and in server/client modes.

%prep
%autosetup

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_pkgdocdir}

%changelog
* Sat Dec 10 2016 Joshua Rich  <joshua.rich@gmail.com>
- 17.1
* Fri Dec 5 2014 Joshua Rich  <joshua.rich@gmail.com>
- 14.1
* Thu Oct 2 2014 Joshua Rich <joshua.rich@gmail.com>
- Version bump.
- Switch to hardened build.
* Tue Jul 1 2014 Joshua Rich <joshua.rich@gmail.com>
- small tweaks in spec file
