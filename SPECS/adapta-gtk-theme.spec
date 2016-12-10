%global debug_package %{nil}

Name:           adapta-gtk-theme
Version:	3.89.1.98
Release:        0%{?dist}
Summary:        An adaptive Gtk+ theme based on Material Design Guidelines
License:	GPL-2
URL:		https://github.com/tista500/Adapta
Source0:	https://github.com/tista500/Adapta/archive/3.89.1.98.zip
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
BuildRequires:  gdk-pixbuf2-devel

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
- Bump version.
* Tue Aug 2 2016  Joshua Rich <joshua.rich@gmail.com>
- Add rubypick dependancy.
* Sat Jul 23 2016 Joshua Rich <joshua.rich@gmail.com>
- Initial package commit.
