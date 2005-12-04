Summary:	X Cursor library
Summary(pl):	Biblioteka X Cursor
Name:		xorg-lib-libXcursor
Version:	1.1.5.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/lib/libXcursor-%{version}.tar.bz2
# Source0-md5:	ca793776537ce25422134f3dc7b7e55f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXrender-devel >= 0.8.2
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	XFree86-xcursor
Obsoletes:	libXcursor
Obsoletes:	xcursor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Cursor - client-side cursor loading library.

%description -l pl
X Cursor - kliencka biblioteka do wczytywania kursorów.

%package devel
Summary:	Header files libXcursor development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXcursor
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXrender-devel >= 0.8.2
Obsoletes:	XFree86-xcursor-devel
Obsoletes:	libXcursor-devel
Obsoletes:	xcursor-devel

%description devel
X Cursor - client-side cursor loading library.

This package contains the header files needed to develop programs that
use these libXcursor.

%description devel -l pl
X Cursor - kliencka biblioteka do wczytywania kursorów.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXcursor.

%package static
Summary:	Static libXcursor library
Summary(pl):	Biblioteka statyczna libXcursor
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	XFree86-xcursor-static
Obsoletes:	libXcursor-static
Obsoletes:	xcursor-static

%description static
X Cursor - client-side cursor loading library.

This package contains the static libXcursor library.

%description static -l pl
X Cursor - kliencka biblioteka do wczytywania kursorów.

Pakiet zawiera statyczn± bibliotekê libXcursor.

%prep
%setup -q -n libXcursor-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXcursor.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXcursor.so
%{_libdir}/libXcursor.la
%dir %{_includedir}/X11/Xcursor
%{_includedir}/X11/Xcursor/*.h
%{_pkgconfigdir}/xcursor.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXcursor.a
