Summary:	libXcursor - X Window System Cursor management library
Summary(pl.UTF-8):	Biblioteka libXcursor do zarządzania kursorami w systemie X Window
Name:		xorg-lib-libXcursor
Version:	1.2.3
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXcursor-%{version}.tar.xz
# Source0-md5:	5ce55e952ec2d84d9817169d5fdb7865
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXrender-devel >= 0.8.2
BuildRequires:	xorg-proto-fixesproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libXrender >= 0.8.2
Obsoletes:	XFree86-xcursor < 4.4
Obsoletes:	libXcursor < 1.2
Obsoletes:	xcursor < 1.1
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
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXrender-devel >= 0.8.2
Obsoletes:	XFree86-xcursor-devel < 4.4
Obsoletes:	libXcursor-devel < 1.2
Obsoletes:	xcursor-devel < 1.1

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
Obsoletes:	XFree86-xcursor-static < 4.4
Obsoletes:	libXcursor-static < 1.2
Obsoletes:	xcursor-static < 1.1

%description static
libXcursor - X Window System Cursor management library.

This package contains the static libXcursor library.

%description static -l pl.UTF-8
Biblioteka libXcursor do zarządzania kursorami w systemie X Window.

Pakiet zawiera statyczną bibliotekę libXcursor.

%prep
%setup -q -n libXcursor-%{version}

# support __libmansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__libmansuffix__/,.so man3/,' man/*.man

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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXcursor.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXcursor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXcursor.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXcursor.so
%dir %{_includedir}/X11/Xcursor
%{_includedir}/X11/Xcursor/Xcursor.h
%{_pkgconfigdir}/xcursor.pc
%{_mandir}/man3/Xcursor*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXcursor.a
