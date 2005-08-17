
#
Summary:	X Cursor library
Summary(pl):	Biblioteka X Cursor
Name:		xorg-lib-libXcursor
Version:	1.1.3
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXcursor-%{version}.tar.bz2
# Source0-md5:	c794209ce7dcbbdca5d6cb9e5c24a5dd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
Obsoletes:	XFree86-xcursor
Obsoletes:	libXcursor
Obsoletes:	xcursor
BuildRoot:	%{tmpdir}/libXcursor-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
X Cursor - client-side cursor loading library.

%description -l pl
X Cursor - kliencka biblioteka do wczytywania kursorów.


%package devel
Summary:	Header files libXcursor development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXcursor
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXcursor = %{version}-%{release}
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXrender-devel
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
Summary:	Static libXcursor libraries
Summary(pl):	Biblioteki statyczne libXcursor
Group:		Development/Libraries
Requires:	xorg-lib-libXcursor-devel = %{version}-%{release}
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
%doc AUTHORS ChangeLog
%attr(755,root,wheel) %{_libdir}/libXcursor.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/Xcursor/*.h
%{_libdir}/libXcursor.la
%attr(755,root,wheel) %{_libdir}/libXcursor.so
%{_pkgconfigdir}/xcursor.pc
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXcursor.a
