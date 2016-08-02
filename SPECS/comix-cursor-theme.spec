Summary:	Comix cursors theme
Name:		comix-cursor-theme
Version:	0.9.0
Release:	0%{?dist}
License:	GPL
Group:		User Interface/Desktops
URL:		http://www.limitland.de/comixcursors.html
Source:		http://limitland.de/downloads/comixcursors/ComixCursors-sources-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	bc
BuildRequires:  librsvg2-tools
BuildRequires:	xorg-x11-apps

%description
X11 mouse theme with a comics feeling.  The package comes with 12
different mouse themes for X11.  6 colors (black, blue, green, orange,
red and white) 2 different weights (slim and normal)


%prep
%setup -q -n ComixCursors-sources-%{version}


%build


%install
%__install -d %{buildroot}%{_datadir}/icons/
ICONSDIR=%{buildroot}%{_datadir}/icons/ ./install-all
find %{buildroot}%{_datadir}/icons -type f -name index.theme -delete
rmdir %{buildroot}%{_datadir}/icons/default


%files
%doc README.md AUTHORS INSTALL NEWS CURSORNAMES.md COPYING LICENSE.GPL
%{_datadir}/icons/*


%changelog
* Tue Aug 2 2016  Joshua Rich  <joshua.rich@gmail.com>
- Update to 0.9. Remove index.theme files.  Remove default directory.
