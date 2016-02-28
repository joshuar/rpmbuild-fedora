#
# spec file for package variety
#
# Copyright (c) 2014 Malcolm J Lewis <malcolmlewis@opensuse.org>
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

Name:           variety
Version:        0.6.0
Release:        1%{?dist}
Summary:        Wallpaper changer
License:        GPL-3.0
Group:          Productivity/Multimedia/Other
Url:            http://peterlevi.com/variety/
Source0:        variety_%{version}.tar.gz
# PATCH-FIX-OPENSUSE variety-fix-varietyconfig-path.patch malcolmlewis@opensuse.org -- Set correct path to /usr/share/variety.
Patch0:         variety-fix-varietyconfig-path.patch
BuildRequires:  gobject-introspection
BuildRequires:  intltool
BuildRequires:  python2-devel
BuildRequires:  python-distutils-extra
BuildRequires:  python-setuptools
BuildRequires:  desktop-file-utils
Requires:       ImageMagick
Requires:       dbus-python
Requires:       libnotify
Requires:       python-beautifulsoup4
Requires:       python-configobj
Requires:       python-httplib2
Requires:       python-lxml
Requires:       python-pillow
Requires:       python-pycurl
Requires:       pyexiv2
Requires:       pywebkitgtk
Requires:       yelp
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Variety changes the desktop wallpaper on a regular basis, using user-specified
or automatically downloaded images.

Variety sits conveniently as an indicator in the panel and can be easily paused
and resumed. The mouse wheel can be used to scroll wallpapers back and forth
until you find the perfect one for your current mood.

Apart from displaying images from local folders, several different online sources
can be used to fetch wallpapers according to user-specified criteria.


%prep
%setup -q -n %{name}
%patch0 -p0
 

%build
%py2_build


%install
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT
install -Dm0644 data/media/variety.svg %{buildroot}%{_datadir}/pixmaps/variety.svg
desktop-file-install                                    \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
    build/share/applications/variety.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/variety.desktop


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
if [ $1 -eq 0 ] ; then
    /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :


%files
%doc AUTHORS COPYING
%{_bindir}/%{name}
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/variety.svg
%{_datadir}/%{name}

%changelog
      
