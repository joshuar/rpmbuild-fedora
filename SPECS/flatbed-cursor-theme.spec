Summary:	Flatbed cursors theme
Name:		flatbed-cursor-theme
Version:	0.4
Release:	1%{?dist}
License:	GPL
Group:		User Interface/Desktops
URL:		http://www.limitland.de/flatbedcursors.html
Source:        	http://limitland.de/downloads/flatbedcursors/FlatbedCursors-sources-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	bc
BuildRequires:  librsvg2-tools
BuildRequires:	xorg-x11-apps

%description
X11 mouse theme, clean and simple, with a smooth shape and appealing
transparency. Package comes with 20 mouse themes: 5 colors (black,
blue, green, orange and white) 4 sizes (small, regular, large and
huge)


%prep
%setup -q -n FlatbedCursors-sources-%{version}


%build


%install
%__install -d %{buildroot}%{_datadir}/icons/
ICONSDIR=%{buildroot}%{_datadir}/icons/ ./install-all
find %{buildroot}%{_datadir}/icons -type f -name index.theme -delete
rmdir %{buildroot}%{_datadir}/icons/default


%files
%doc README.md AUTHORS INSTALL NEWS
%{_datadir}/icons/*


%changelog
* Thu Aug 2 2016  Joshua Rich  <joshua.rich@gmail.com>
- Remove index.theme files.  Remove default directory.
* Sat Jul 9 2016  Joshua Rich  <joshua.rich@gmail.com>
- Update to 0.4.
* Thu Nov 6 2014  Joshua Rich  <joshua.rich@gmail.com>
- Avoid using Fedora specific rpm macros OBS doesn't understand.
