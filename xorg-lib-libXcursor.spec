Summary:	libXcursor - X Window System Cursor management library
Summary(pl.UTF-8):	Biblioteka libXcursor do zarządzania kursorami w systemie X Window
Name:		xorg-lib-libXcursor
Version:	1.1.12
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXcursor-%{version}.tar.bz2
# Source0-md5:	a93b5a6f5b05976d2c0d3f8a07f6ac6a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXrender-devel >= 0.8.2
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXrender >= 0.8.2
Obsoletes:	XFree86-xcursor
Obsoletes:	libXcursor
Obsoletes:	xcursor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libXcursor - X Window System Cursor management library.

%description -l pl.UTF-8
Biblioteka libXcursor do zarządzania kursorami w systemie X Window.

%package devel
Summary:	Header files for libXcursor library
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki libXcursor
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXrender-devel >= 0.8.2
Obsoletes:	XFree86-xcursor-devel
Obsoletes:	libXcursor-devel
Obsoletes:	xcursor-devel

%description devel
libXcursor - X Window System Cursor management library.

This package contains the header files needed to develop programs that
use libXcursor.

%description devel -l pl.UTF-8
Biblioteka libXcursor do zarządzania kursorami w systemie X Window.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXcursor.

%package static
Summary:	Static libXcursor library
Summary(pl.UTF-8):	Biblioteka statyczna libXcursor
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	XFree86-xcursor-static
Obsoletes:	libXcursor-static
Obsoletes:	xcursor-static

%description static
libXcursor - X Window System Cursor management library.

This package contains the static libXcursor library.

%description static -l pl.UTF-8
Biblioteka libXcursor do zarządzania kursorami w systemie X Window.

Pakiet zawiera statyczną bibliotekę libXcursor.

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXcursor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXcursor.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXcursor.so
%{_libdir}/libXcursor.la
%dir %{_includedir}/X11/Xcursor
%{_includedir}/X11/Xcursor/Xcursor.h
%{_pkgconfigdir}/xcursor.pc
%{_mandir}/man3/Xcursor*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXcursor.a
