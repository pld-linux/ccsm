Summary:	compizconfig-settings-manager
Summary(pl.UTF-8):	compizconfig-settings-manager
Name:		ccsm
Version:	0.5.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://releases.compiz-fusion.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	e267eaa2400d833bcc3da6383bf054ff
URL:		http://forum.compiz-fusion.org/
BuildRequires:	libcompizconfig-devel >= %{version}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-Pyrex
BuildRequires:	rpm-pythonprov
Requires:	compizconfig-python
Requires:	python-pygtk-gtk
Suggests:	python-sexy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fully featured Python/GTK based settings manager for the
CompizConfig system.

%description -l pl.UTF-8
W pełni sprawny, oparty o Pythona/GTK menedżer ustawień dla systemu
CompizConfig.

%prep
%setup -q

%build
python setup.py build \
	--prefix %{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
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
%{_desktopdir}/*.desktop
%{_datadir}/ccsm
%{_iconsdir}/*/scalable/apps/ccsm.svg
%{_pixmapsdir}/ccsm.png
%{py_sitescriptdir}/ccm
%{py_sitescriptdir}/%{name}*.egg-info
