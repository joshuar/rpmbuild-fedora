Summary:	Comix cursors theme
Name:		comix-cursor-theme
Version:	0.8.2
Release:	2%{?dist}
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

%files
%doc README AUTHORS INSTALL NEWS
%{_datadir}/icons/*
