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
%include %{_rpmconfigdir}/macros.python

Name:           variety
Version:        0.5.4
Release:        1%{?dist}
Summary:        Wallpaper changer
License:        GPL-3.0
Group:          Productivity/Multimedia/Other
Url:            https://launchpad.net/variety/
Source0:        variety_%{version}.tar.gz
Source1:        variety.desktop
# Todo: Variety should follow FDO icon standards
Source2:        VarietyIcons.tar.gz
# PATCH-FIX-OPENSUSE variety-fix-varietyconfig-path.patch malcolmlewis@opensuse.org -- Set correct path to /usr/share/variety.
Patch0:         variety-fix-varietyconfig-path.patch
# PATCH-FIX-OPENSUSE variety-webkit3.0.patch malcolmlewis@opensuse.org -- Specify in the code that we require WebKit 3.0, not 'any' WebKit
Patch1:         variety-webkit3.0.patch
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
%setup -q -n %{name} -a 2
%patch0 -p1
%patch1 -p1

%build
%py2_build

%install
%py2_install
# python setup.py install --skip-build --prefix=%{_prefix} --root=${RPM_BUILD_ROOT}
# Create our own desktop file and remove the pre-installed version
# rm ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
desktop-file-install                                    \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
    %{SOURCE1}
desktop-file-validate %{buildroot}/%{_datadir}/applications/variety.desktop
# Todo: Add support for FDO icon standard upstream
install -Dm0644 data/media/variety.svg %{buildroot}%{_datadir}/pixmaps/variety.svg
cp VarietyIcons/* ${RPM_BUILD_ROOT}%{_datadir}/variety/media/

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
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_bindir}/%{name}
%{python2_sitelib}/jumble
%{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}_lib
%{python2_sitelib}/%{name}-%{version}-py%{py_ver}.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/variety.svg
%{_datadir}/%{name}

%changelog
      
