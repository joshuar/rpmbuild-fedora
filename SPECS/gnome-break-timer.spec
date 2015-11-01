#
# spec file for package
#
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global commit0 c126b1463330ff4c6736b1a81676f997b811cfa4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           gnome-break-timer
Version:        20151031git%{shortcommit0}
Release:        0%{?dist}
License:        GPL-3.0+
Summary:        GNOME Break Timer
Url:            https://wiki.gnome.org/GnomeBreakTimer
Group:          System/GUI/GNOME
Source0:        https://github.com/GNOME/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  intltool >= 0.40.0
BuildRequires:  gettext
BuildRequires:  vala
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gee-1.0) >= 0.6.2
BuildRequires:  pkgconfig(gio-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.16.0
BuildRequires:  pkgconfig(libcanberra) >= 0.28
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.28
BuildRequires:  pkgconfig(libnotify) >= 0.4.5
BuildRequires:  pkgconfig(cairo) >= 1.12.14
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.10.0
BuildRequires:  pkgconfig(x11) >= 1.4.99.1
BuildRequires:  pkgconfig(xi) >= 1.5.99.3
BuildRequires:  pkgconfig(xtst) >= 1.2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Take a Break - GNOME Break Timer helps you remember about it.

%prep
%setup -qn %{name}-%{commit0}

%build
./autogen.sh && %{configure}

%install
%make_install
%find_lang %{name}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING README
%{_bindir}/%{name}
%{_bindir}/%{name}-service
%dir %{_datadir}/appdata
%{_datadir}/appdata/gnome-break-timer.appdata.xml
%{_datadir}/applications/gnome-break-timer-service.desktop
%{_datadir}/applications/gnome-break-timer.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.break-timer.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%config %{_sysconfdir}/xdg/autostart/gnome-break-timer-autostart.desktop

%changelog
