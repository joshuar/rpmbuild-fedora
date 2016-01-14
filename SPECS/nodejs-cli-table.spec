Name:           nodejs-cli-table
Version:        0.3.1
Release:        0%{?dist}
Summary:        Render unicode-aided tables on the command line from your node.js scripts
License:        as-is
Source0:        http://registry.npmjs.org/cli-table/-/cli-table-%{version}.tgz
Url:            https://github.com/Automattic/cli-table
BuildRequires:	nodejs-packaging
BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

%if 0%{?enable_tests}
BuildRequires:  npm(expresso)
BuildRequires:  npm(should)
%endif

%description
Features:

* Customizable characters that constitute the table.
* Color/background styling in the header through colors.js
* Column width customization
* Text truncation based on predefined widths
* Text alignment (left, right, center)
* Padding (left, right)
* Easy-to-use API

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/cli-table
cp -pr package.json lib/ \
   %{buildroot}%{nodejs_sitelib}/cli-table

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha -R spec
%endif

%files
%doc README.md
%{nodejs_sitelib}/cli-table/

%changelog
