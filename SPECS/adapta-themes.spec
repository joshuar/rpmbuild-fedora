%global debug_package %{nil}

Name:           adapta-themes
Version:	3.21.4
Release:        43
Summary:        An adaptive Gtk+ theme based on Material Design Guidelines

License:	GPL-2
URL:		https://github.com/tista500/Adapta
Source0:	https://github.com/tista500/Adapta/archive/3.21.4.43.zip

Requires:	gtk-murrine-engine
Requires:	gtk2-engines
BuildRequires:	rubygem-bundler
BuildRequires:	rubygem-sass
BuildRequires:	inkscape
BuildRequires:	glib2-devel > 2.48.0


%description
An adaptive Gtk+ theme based on Material Design Guidelines. Lots of
elements were forked from Flat-Plat at the start.

%prep
%setup -q -n Adapta-%{version}.%{release}


%build
./autogen.sh
%configure --enable-gtk_next
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_datadir}/themes/Adapta*



%changelog
* Sat Jul 23 2016 vagrant
- Initial package commit.
