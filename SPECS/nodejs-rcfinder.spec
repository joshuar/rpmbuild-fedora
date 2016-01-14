Name:           nodejs-rcfinder
Version:        0.1.8
Release:        1%{?dist}
Summary:        Find a config file (like .jshintrc) by walking up from a specific directory
License:        MIT
Source0:        http://registry.npmjs.org/rcfinder/-/rcfinder-%{version}.tgz
Url:         	https://github.com/spenceralger/rcfinder   
BuildRequires:	nodejs-packaging
BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

%if 0%{?enable_tests}
BuildRequires:  npm(mocha) = 1.17.1
BuildRequires:  npm(expect.js) = 0.2.0
%endif

%description
This module provides the file lookup logic for the generally more
useful rcloader package.

Find a config file (like .jshintrc) by walking up from a specific
directory.

Custom logic can be implemented for loading your config files, and
calls to the file system are cached so that you can find files
relative to every file in a project without making a ton of
unnecessary calls.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/rcfinder
cp -pr package.json index.js \
   %{buildroot}%{nodejs_sitelib}/rcfinder

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha -R spec
%endif

%files
%doc README.md
%{nodejs_sitelib}/rcfinder/

%changelog
