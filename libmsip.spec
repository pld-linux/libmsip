#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	libmsip - C++ implementation of the SIP (RFC3261) protocol
Summary(pl.UTF-8):   libmsip - implementacja w C++ protokołu SIP (RFC3261)
Name:		libmsip
Version:	0.3.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.minisip.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	4960049a61128adef1debdccfdd7936a
URL:		http://www.minisip.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libmnetutil-devel >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmsip implements the Session Initiation Protocol, in a C++ library.
The SIP protocol is used mostly to initialize Voice over IP calls.

%description -l pl.UTF-8
libmsip to biblioteka C++ implementująca protokół Session Initiation
Protocol. Protokół SIP jest używany głównie do nawiązywnia połączeń
Voice over IP.

%package devel
Summary:	Header files for libmsip library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libmsip
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libmnetutil-devel >= %{version}

%description devel
Header files for libmsip library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmsip.

%package static
Summary:	Static libmsip library
Summary(pl.UTF-8):   Statyczna biblioteka libmsip
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmsip library.

%description static -l pl.UTF-8
Statyczna biblioteka libmsip.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libmsip.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmsip.so
%{_libdir}/libmsip.la
%{_includedir}/libmsip

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmsip.a
%endif
