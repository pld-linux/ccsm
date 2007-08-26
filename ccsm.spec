# TODO: next time don't use patches to rename files
Summary:	CompizConfig Settings Manager
Summary(pl.UTF-8):	CompizConfig Settings Manager - zarządca ustawień konfiguracji compiza
Name:		ccsm
Version:	0.5.2
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://releases.compiz-fusion.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	e267eaa2400d833bcc3da6383bf054ff
Patch0:		%{name}-PL.patch
Patch1:		%{name}-PT.patch
URL:		http://forum.compiz-fusion.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
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
%patch0 -p1
%patch1 -p1

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ccsm
%{_datadir}/ccsm
%{py_sitescriptdir}/ccm
%{py_sitescriptdir}/%{name}*.egg-info
%{_desktopdir}/ccsm.desktop
%{_iconsdir}/hicolor/scalable/apps/ccsm.svg
%{_pixmapsdir}/ccsm.png
