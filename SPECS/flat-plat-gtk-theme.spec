%global debug_package %{nil}

Name:       flat-plat-gtk-theme
Version:	3.20.20161109
Release:    0%{?dist}
Summary:    A Material Design-like theme for GNOME/GTK+ based desktop environments
License:	GPL-2
URL:		https://github.com/nana-4/Flat-Plat
Source0:	https://github.com/nana-4/Flat-Plat/archive/v3.20.20161109.zip
Requires:	gtk-murrine-engine
Requires:	gtk2-engines
BuildRequires:	rubygem-bundler
BuildRequires:	rubygem-sass
BuildRequires:	inkscape
BuildRequires:	glib2-devel > 2.48.0
Requires:       rubypick
BuildRequires:  rubypick
BuildRequires:  sassc
BuildRequires:  parallel


%description
An adaptive Gtk+ theme based on Material Design Guidelines. Lots of
elements were forked from Flat-Plat at the start.


%prep
%autosetup


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
* Sat Dec 10 2016  Joshua Rich <joshua.rich@gmail.com>
- Initial package commit.
