%global commit          3e7a66cf03234e3c79cd04f6743dcfe7fe992d68
%global shortcommit     %(c=%{commit}; echo ${c:0:7})


Summary:	Flatbed cursors theme
Name:		flatbed-cursor-theme
Version:	0.4
Release:	0%{?dist}
License:	GPL
Group:		User Interface/Desktops
URL:		http://www.limitland.de/flatbedcursors.html
Source0:        flatbed-cursor-theme-0.4.tar.gz
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
%setup -q -n flatbedcursors-v%{version}-%{commit}

%build

%install
%__install -d %{buildroot}%{_datadir}/icons/
ICONSDIR=%{buildroot}%{_datadir}/icons/ ./install-all

%files
%doc README.md AUTHORS INSTALL NEWS
%{_datadir}/icons/*


%changelog
* Sat Jul 9 2016  Joshua Rich  <joshua.rich@gmail.com>
- Update to 0.4.
* Thu Nov 6 2014  Joshua Rich  <joshua.rich@gmail.com>
- Avoid using Fedora specific rpm macros OBS doesn't understand.
