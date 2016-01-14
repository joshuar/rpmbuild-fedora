Name:           nodejs-rcloader
Version:        0.2.0
Release:        1%{?dist}
Summary:        For build system plugins that need to fetch relative config files (like .jshintrc)
License:        MIT
Source0:        http://registry.npmjs.org/rcloader/-/rcloader-%{version}.tgz
Url:            https://github.com/spenceralger/rcloader
BuildRequires:	nodejs-packaging
BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

%if 0%{?enable_tests}
BuildRequires:  npm(mocha) = 2.1.0
BuildRequires:  npm(should) = 4.6.2
%endif

%description
Find the closest config file (like .jshintrc) relative to the file you are linting
* Lookups are cached to limit IO operations
* Accepts input directly from plugin consumers to
  * specifiy a file that should always be used
  * specify a default file
  * specify overrides
  * disable file lookup

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/rcloader
cp -pr package.json index.js \
   %{buildroot}%{nodejs_sitelib}/rcloader

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha -R spec
%endif

%files
%doc README.md
%{nodejs_sitelib}/rcloader/

%changelog
