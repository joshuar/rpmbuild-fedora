Summary:	Flatbed cursors theme
Name:		flatbed-cursor-theme
Version:	0.3
Release:	3%{?dist}
License:	GPL
Group:		User Interface/Desktops
URL:		http://www.limitland.de/flatbedcursors.html
Source0:        http://www.limitland.de/flatbedcursors/FlatbedCursors-0.3.tar.bz2
Source1:        http://www.limitland.de/flatbedcursors/FlatbedCursors-LH-0.3.tar.bz2
BuildArch:	noarch

%description
X11 mouse theme, clean and simple, with a smooth shape and appealing
transparency. Package comes with 20 mouse themes: 5 colors (black,
blue, green, orange and white) 4 sizes (small, regular, large and
huge)

%prep
%setup -q -c %{name}
find -type f -name link-cursors.sh -delete
find -type f -name index.theme -delete

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_datadir}/icons/
cp -pr * %{buildroot}%{_datadir}/icons/


%files
%defattr(-,root,root,-)
%{_datadir}/icons/*


%changelog
* Thu Nov 6 2014  Joshua Rich  <joshua.rich@gmail.com>
- Avoid using Fedora specific rpm macros OBS doesn't understand.
