#
# spec file for package hamster-time-tracker
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%global commit0 81737fd06fe8033dd8949b460052730a732bc120
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           hamster-time-tracker
Version:        20151031git%{shortcommit0}
Release:        0%{?dist}
Summary:        A time tracker for GNOME
License:        GPL-3.0+ and CC-BY-SA-3.0
Group:          Productivity/Other
Source0:        https://github.com/projecthamster/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Url:            http://projecthamster.wordpress.com/
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  GConf2
BuildRequires:  python2-devel
BuildRequires:  glib2-devel
BuildRequires:  dbus-glib
Requires(pre):  GConf2
Requires(post): GConf2
Requires(preun): GConf2
Obsoletes:      hamster-applet <= 2.91.2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Project Hamster is time tracking for masses. It helps you to keep track
on how much time you have spent during the day on activities you have
set up.

%prep
%setup -qn hamster-%{commit0}

%build
./waf --prefix=%{_prefix} --libdir=%{_libdir} --libexecdir=%{_libexecdir} configure build

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
./waf install --destdir=%{buildroot}
%find_lang %{name} %{?no_lang_C}
%find_lang %{name} --with-gnome
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
%fdupes %{buildroot}

%pre
%gconf_schema_prepare hamster-time-tracker

%post
%gconf_schema_upgrade hamster-time-tracker
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%preun
%gconf_schema_remove hamster-time-tracker

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS NEWS
%{_libdir}/hamster-time-tracker
%{_bindir}/hamster
%{_datadir}/applications/hamster-time-tracker.desktop
%{_datadir}/applications/hamster-time-tracker-overview.desktop
%{_datadir}/applications/hamster-windows-service.desktop
%{_datadir}/dbus-1/services/org.gnome.hamster.service
%{_datadir}/dbus-1/services/org.gnome.hamster.Windows.service
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/%{name}/
%{_sysconfdir}/gconf/schemas/hamster-time-tracker.schemas
%{python2_sitelib}/hamster/
%{_sysconfdir}/bash_completion.d/hamster.bash

%changelog
