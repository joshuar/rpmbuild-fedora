Summary:	Comix cursors theme
Name:		comix-cursor-theme
Version:	0.8.2
Release:	2%{?dist}
License:	GPL
Group:		User Interface/Desktops
URL:		http://www.limitland.de/comixcursors.html
Source0:        http://www.limitland.de/comixcursors/ComixCursors-0.8.2.tar.bz2
Source1:        http://www.limitland.de/comixcursors/ComixCursors-Opaque-0.8.2.tar.bz2
Source2:        http://www.limitland.de/comixcursors/ComixCursors-LH-0.8.2.tar.bz2
Source3:        http://www.limitland.de/comixcursors/ComixCursors-LH-Opaque-0.8.2.tar.bz2
BuildArch:	noarch

%description
X11 mouse theme with a comics feeling.  The package comes with 12
different mouse themes for X11.  6 colors (black, blue, green, orange,
red and white) 2 different weights (slim and normal)

%prep
%setup -q -c %{name}
find -type f -name link-cursors.sh -delete
find -type f -name index.theme -delete

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_datadir}/icons/
%__cp -pr * %{buildroot}%{_datadir}/icons/

%files
%defattr(-,root,root,-)
%{_datadir}/icons/*
