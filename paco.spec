Summary:	Paco is a source code package organizer for Unix/Linux systems
Summary(pl):	Paco to manager paczek ¼ród³owych dla systemów Unix/Linux
Name:		paco
Version:	1.10.2
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/paco/%{name}-%{version}.tar.bz2
# Source0-md5:	b3cc9a1bd7bf218adf38ee23eecb48dd
Patch0:		%{name}-Makefile.patch
URL:		http://paco.sourceforge.net/
BuildRequires:	gtk+2 => 2:2.6.0
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When installing a package from sources, paco wraps the "make install"
command (or whatever is needed to install the files into the system),
and generates a log containing the list of all installed files.

%description -l pl
Przy instalacji programów ze ¼róde³ paco przechwytuje "make install"
(lub inne komendy które s± potrzebne do zainstalowania danego
programu) i tworzy log zawieraj±cy listê wszystkich instalowanych
plików, umo¿liwiaj±c w przysz³o¶ci ³atwe i skuteczne odinstalowanie
pakietu.

%package gui
Summary:	Gtk+2 frontend to paco
Summary(pl):	Nak³adka na paco w Gtk+2
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.6.0

%description gui
Gtk+2 gui for paco.

%description gui -l pl
Graficzny interfejs dla paco w Gtk+2

%package scripts
Summary:	Addtional scripts for paco
Summary:	Dodatkowe skrypty dla paco
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description scripts
Addtional scripts for paco.
    - a2paco: Create paco logs from a local dpkg or rpm database.
    - superpaco: Installs Debian, RPM or tgz packages with paco.
    - pacoball: Creates binary packages from installed (and logged by paco)
      packages.

%description scripts -l pl
Dodatkowe skrypty dla paco.
    - a2paco: Tworzy logi z lokalnych baz dpkg lub rpm.
    - superpaco: Instalacja pakietów deb, rpm, lub tgz z paco.
    - pacoball: Tworzy pakiety binarne z instalowanych programów.

%prep
%setup -q
%patch0 -p1
sed -i -e 's#Categories=Application;System;#Categories=GTK;Application;System;#' \
	doc/gpaco.desktop

%build
./configure \
	--enable-a2paco \
	--enable-pacoball \
	--enable-superpaco \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/{man5,man8}}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_prefix}/man/man5/* $RPM_BUILD_ROOT%{_mandir}/man5
mv $RPM_BUILD_ROOT%{_prefix}/man/man8/* $RPM_BUILD_ROOT%{_mandir}/man8
install -d $RPM_BUILD_ROOT/var/log/paco

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pacorc
%attr(755,root,root) %{_bindir}/paco
%doc AUTHORS ChangeLog README
%dir /var/log/paco
%{_libdir}/*.so
%{_libdir}/libpaco*
%{_mandir}/man5/pacorc*
%{_mandir}/man8/paco*

%files scripts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/a2paco
%attr(755,root,root) %{_bindir}/superpaco
%attr(755,root,root) %{_bindir}/pacoball
%{_mandir}/man8/a2paco*
%{_mandir}/man8/superpaco*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpaco
%{_pixmapsdir}/*.png
%{_datadir}/*/*/*/paco.mo
%{_desktopdir}/*.desktop
