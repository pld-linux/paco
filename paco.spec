Summary:	Paco - a source code package organizer for Unix/Linux systems
Summary(pl.UTF-8):   Paco - zarządca pakietów źródłowych dla systemów Unix/Linux
Name:		paco
Version:	1.10.2
Release:	0.3
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/paco/%{name}-%{version}.tar.bz2
# Source0-md5:	b3cc9a1bd7bf218adf38ee23eecb48dd
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://paco.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When installing a package from sources, paco wraps the "make install"
command (or whatever is needed to install the files into the system),
and generates a log containing the list of all installed files.

%description -l pl.UTF-8
Przy instalacji programów ze źródeł paco przechwytuje "make install"
(lub inne polecenia, które są potrzebne do zainstalowania danego
programu) i tworzy log zawierający listę wszystkich instalowanych
plików, umożliwiając w przyszłości łatwe i skuteczne odinstalowanie
pakietu.

%package gui
Summary:	GTK+2 frontend to paco
Summary(pl.UTF-8):   Nakładka na paco w GTK+2
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description gui
GTK+2 GUI for paco.

%description gui -l pl.UTF-8
Graficzny interfejs GTK+2 dla paco.

%package scripts
Summary:	Addtional scripts for paco
Summary(pl.UTF-8):   Dodatkowe skrypty dla paco
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description scripts
Addtional scripts for paco.
- a2paco: Create paco logs from a local dpkg or rpm database.
- superpaco: Installs Debian, RPM or tgz packages with paco.
- pacoball: Creates binary packages from installed (and logged by paco)
  packages.

%description scripts -l pl.UTF-8
Dodatkowe skrypty dla paco.
- a2paco: Tworzy logi z lokalnych baz dpkg lub rpm.
- superpaco: Instalacja pakietów deb, rpm, lub tgz z paco.
- pacoball: Tworzy pakiety binarne z instalowanych programów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--enable-a2paco \
	--enable-pacoball \
	--enable-superpaco
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/log/paco

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README
%attr(755,root,root) %{_bindir}/paco
%attr(755,root,root) %{_libdir}/libpaco*.so.*.*.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pacorc
%dir /var/log/paco
%{_mandir}/man5/pacorc*
%{_mandir}/man8/paco*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpaco
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

%files scripts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/a2paco
%attr(755,root,root) %{_bindir}/superpaco
%attr(755,root,root) %{_bindir}/pacoball
%{_mandir}/man8/a2paco*
%{_mandir}/man8/superpaco*
