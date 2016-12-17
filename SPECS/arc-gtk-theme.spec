%global debug_package %{nil}

Name:           arc-gtk-theme
Version:		20161119
Release:        0%{?dist}
Summary:        A flat theme with transparent elements
License:		GPL-3
URL:			https://github.com/horst3180/arc-theme
Source0:		https://github.com/horst3180/arc-theme/archive/20161119.zip
Requires:		gtk-murrine-engine
Requires:		gnome-themes-standard
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk3-devel

BuildArch:    	noarch

%description
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and
Gnome-Shell. It supports GTK 3 and GTK 2 based desktop environments
like Gnome, Unity, Budgie, Pantheon, etc.


%prep
%autosetup -n arc-theme-%{version}


%build
./autogen.sh --prefix=/usr


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find ${RPM_BUILD_ROOT} -name "*.sh" -exec chmod -x {} \;


%files
%doc
%{_datadir}/themes/Arc
%{_datadir}/themes/Arc-Darker
%{_datadir}/themes/Arc-Dark


%changelog
* Sat Dec 17 2016  Joshua Rich <joshua.rich@gmail.com>
- Initial package commit.
