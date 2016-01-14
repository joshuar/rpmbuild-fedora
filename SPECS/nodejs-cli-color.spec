Name:           nodejs-cli-color
Version:        0.3.3
Release:        0%{?dist}
Summary:        Colors, formatting and other tools for the console
License:        MIT
Source0:        http://registry.npmjs.org/cli-color/-/cli-color-%{version}.tgz
Url:            https://github.com/medikoo/cli-color
BuildRequires:	nodejs-packaging
BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

%if 0%{?enable_tests}
BuildRequires:  npm(tad) = 0.2.3
BuildRequires:  npm(xlint) = 0.2.2
BuildRequires:  npm(xlint-jslint-medikoo) = 0.1.4
%endif

%description
Colors, formatting and other goodies for the console. This package
won't mess with built-ins and provides neat way to predefine
formatting patterns, see below.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/cli-color
cp -pr package.json *.js lib/ \
   %{buildroot}%{nodejs_sitelib}/cli-color

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha -R spec
%endif

%files
%doc CHANGES LICENSE README.md
%{nodejs_sitelib}/cli-color/

%changelog
