Name:			awoken-icon-theme
Summary:		Awsome Token Icon Theme
Version:		2.5
Release:		2%{?dist}
License:		Creative Commons Attribution-ShareAlike 2.5 License Agreement
Group:			User Interface/Desktops
URL:			http://www.deviantart.com/download/163570862/
Source:			AwOken-%{version}.zip
BuildRequires:	        fdupes
Requires:               zenity
Requires:               ImageMagick
BuildArch:		noarch

%description
This is one combination of the customizable AwOken Icon Theme.  This
icon theme is suitable for GNOME/XFCE/LXDE desktops.

%prep
%setup -q -n AwOken-%{version}
gzip -dc AwOken.tar.gz | tar -xf -
gzip -dc AwOkenDark.tar.gz | tar -xf -
gzip -dc AwOkenWhite.tar.gz | tar -xf -

%build

%install
#using the install utility to install and create directories and files
#with the correct permissions 
%__install -d -m 0755 %{buildroot}/%{_bindir}
%__install -m 0755 AwOken/awoken-icon-theme-customization %{buildroot}/%{_bindir}/awoken-icon-theme-customization
%__install -d -m 0755 %{buildroot}/%{_datadir}/icons/AwOken
%__install -m 0755 AwOken/awoken-icon-theme-customization-clear %{buildroot}/%{_datadir}/icons/AwOken/awoken-icon-theme-customization-clear
%__install -d -m 0755 %{buildroot}/%{_datadir}/icons/AwOkenDark
%__install -m 0755 AwOkenDark/awoken-icon-theme-customization-dark %{buildroot}/%{_datadir}/icons/AwOkenDark/awoken-icon-theme-customization-dark
%__install -d -m 0755 %{buildroot}/%{_datadir}/icons/AwOkenWhite
%__install -m 0755 AwOkenWhite/awoken-icon-theme-customization-white %{buildroot}/%{_datadir}/icons/AwOkenWhite/awoken-icon-theme-customization-white
%__rm AwOken*/awoken-icon-theme-customization*
%__cp -r AwOken/* %{buildroot}/%{_datadir}/icons/AwOken
%__cp -r AwOkenDark/* %{buildroot}/%{_datadir}/icons/AwOkenDark
%__cp -r AwOkenWhite/* %{buildroot}/%{_datadir}/icons/AwOkenWhite
find %{buildroot}/usr/share/icons/AwOken* -type f -exec %__chmod 0644 "{}" +

#using fdupes to eliminate duplicated files
%fdupes %{buildroot}/usr/share/icons

%posttrans
gtk-update-icon-cache %{_datadir}/icons/AwOken &>/dev/null || :
gtk-update-icon-cache %{_datadir}/icons/AwOkenDark &>/dev/null || :
gtk-update-icon-cache %{_datadir}/icons/AwOkenWhite &>/dev/null || :

%files
%defattr(-,root,root)
%{_bindir}/awoken-icon-theme-customization
%{_datadir}/icons/AwOken*

%changelog
* Tue Jul 1 2014 Joshua Rich - joshua.rich@gmail.com
- small tweaks in spec file

* Tue Jul 30 2013 Joshua Rich - joshua.rich@gmail.com
- updated to version 2.5.0
- create package from original zip
- install customisation scripts
- run gtk-update-icon-cache in postrans phase

* Sat May 26 2012 Matthias Propst - propstmatthias@googlemail.com
- updated to version 2.4.1 
  + suse internal release
  + removed dirty scripts and configured the iconset

* Sat May 26 2012 Matthias Propst - propstmatthias@googlemail.com
- updated to version 2.4

* Tue Sep 06 2011 Matthias Propst - propstmatthias@googlemail.com
- cleaned up spec file
- fixed bug in package
	+ folders where not in package

* Tue Sep 06 2011 Matthias Propst - propstmatthias@googlemail.com
- fixed: source was tar.gz. should be tar.bz2

* Tue Sep 06 2011 Matthias Propst - propstmatthias@googlemail.com
- fixed: source was tar.gz instead of tar.bz2

* Tue Sep 06 2011 Matthias Propst - propstmatthias@googlemail.com
- updated to version 2.2
	+ gnome3 support

* Sun Aug 28 2011 Matthias Propst - propstmatthias@googlemail.com
- updated to version 2.1 with new icon styleset

* Fri Nov 26 2010 Matthias Propst - propstmatthias@googlemail.com
- initial local build
