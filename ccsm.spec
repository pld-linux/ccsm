Summary:	CompizConfig Settings Manager
Summary(pl.UTF-8):	CompizConfig Settings Manager - zarządca ustawień konfiguracji compiza
Name:		ccsm
Version:	0.7.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://releases.compiz-fusion.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	3f3f20fcb37aae475d103d231acaea23
URL:		http://forum.compiz-fusion.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires:	python-compizconfig >= %{version}
Requires:	python-pygtk-gtk >= 2:2.10.0
Suggests:	python-sexy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fully featured Python/GTK+ based settings manager for the
CompizConfig system.

%description -l pl.UTF-8
W pełni funkcjonalny, oparty o Pythona/GTK+ zarządca ustawień dla
systemu CompizConfig.

%prep
%setup -q

%build
%{__python} setup.py build \
	--prefix %{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT \
	--prefix %{_prefix}

%py_postclean %{py_sitescriptdir}/ccm

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ccsm
%{_datadir}/ccsm
%{py_sitescriptdir}/ccm
%{py_sitescriptdir}/%{name}*.egg-info
%{_desktopdir}/ccsm.desktop
%{_iconsdir}/hicolor/scalable/apps/ccsm.svg
%{_iconsdir}/hicolor/16x16/apps/ccsm.png
%{_iconsdir}/hicolor/22x22/apps/ccsm.png
%{_iconsdir}/hicolor/22x22/apps/ccsm.svg
%{_iconsdir}/hicolor/24x24/apps/ccsm.png
%{_iconsdir}/hicolor/32x32/apps/ccsm.png
%{_iconsdir}/hicolor/32x32/apps/ccsm.svg
%{_iconsdir}/hicolor/48x48/apps/ccsm.png
