Name:           nodejs-libesvm
Version:        3.2.1
Release:        0%{?dist}
Summary:        Library for managing Elasticsearch instances for testing and development environments
License:        Apache-2.0
Group:          Productivity/Other
Source0:        http://registry.npmjs.org/libesvm/-/libesvm-%{version}.tgz
Url:            https://github.com/simianhacker/libesvm
BuildRequires:	nodejs-packaging
BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
%endif

%description
This is a library for managing Elasticsearch instances for testing and
development environments. It's not intended to be used in production
(just don't). We uses it to download specific versions of
Elasticsearch and start them up in our setup and tear down steps of
our testing framework. It's also used for our esvm tool for managing
our development enviroments.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/libesvm
cp -pr package.json lib/ \
   %{buildroot}%{nodejs_sitelib}/libesvm

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha -R spec
%endif

%files
%doc README.md
%{nodejs_sitelib}/libesvm/

%changelog
