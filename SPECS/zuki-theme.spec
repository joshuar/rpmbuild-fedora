%global debug_package %{nil}
%global commit          dda1726ac7b556df2ef9696e530f8c2eaa0aed37
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           zuki-themes
Version:        3.20
Release:        1%{?dist}
Summary:        Zuki themes for GNOME, Xfce


License:	GPL-3
URL:		https://github.com/lassekongo83/zuki-themes
Source0:	https://github.com/lassekongo83/zuki-themes/archive/%{commit}.zip


Requires:	gtk-murrine-engine
Requires:	gtk2-engines

BuildRoot:      %{_tmppath}/%{name}-%{commit}


%description
Zuki themes for GNOME, Xfce


%prep
%setup -q -n %{name}-%{commit}


%build


%install
rm -rf $RPM_BUILD_ROOT
%__install -d -m 0755 %{buildroot}/%{_datadir}/themes/Zuki
%__cp -r Zuki-shell/* %{buildroot}/%{_datadir}/themes/Zuki
%__install -d -m 0755 %{buildroot}/%{_datadir}/themes/Zukitre
%__cp -r Zukitre/* %{buildroot}/%{_datadir}/themes/Zukitre
%__install -d -m 0755 %{buildroot}/%{_datadir}/themes/Zukitwo
%__cp -r Zukitwo/* %{buildroot}/%{_datadir}/themes/Zukitwo



%files
%{_datadir}/themes/Zuki
%{_datadir}/themes/Zukitre
%{_datadir}/themes/Zukitwo
%license LICENSE
%doc README.md



%changelog
* Sat Jul 23 2016 Joshua Rich <joshua.rich@gmail.com>
- Initial package commit.
