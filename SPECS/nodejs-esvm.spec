Name:           nodejs-esvm
Version:        3.2.1
Release:        0%{?dist}
Summary:        Command line application used for development to manage different versions of Elasticsearch
License:        Apache-2.0
Group:          Productivity/Other
Source0:        http://registry.npmjs.org/esvm/-/esvm-%{version}.tgz
Url:            https://github.com/simianhacker/esvm
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
Elasticsearch Version Manager is a command line application used for
development to manage different versions of Elasticsearch. It should
not be used in production since it's probably a bad idea to wrap a
process with Node.js. But nevertheless it's extremely useful if you
need to develop against multiple versions of Elasticsearch.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/esvm
cp -pr package.json lib/ \
   %{buildroot}%{nodejs_sitelib}/esvm
mkdir -p %{buildroot}%{nodejs_sitelib}/esvm/bin
    install -p -D -m0755 bin/esvm.js %{buildroot}%{nodejs_sitelib}/esvm/bin/esvm.js
    mkdir -p %{buildroot}%{_bindir}
    ln -s %{nodejs_sitelib}/esvm/bin/esvm.js %{buildroot}%{_bindir}/esvm

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha -R spec
%endif

%files
%doc LICENSE README.md
%{nodejs_sitelib}/esvm/
%{_bindir}/esvm

%changelog
