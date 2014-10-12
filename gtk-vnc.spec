Summary:	A GTK widget for VNC clients
Name:		gtk-vnc
Version:	0.5.3
Release:	3
License:	LGPL
Group:		Development/Libraries
Source0:	http://ftp.acc.umu.se/pub/GNOME/sources/gtk-vnc/0.5/%{name}-%{version}.tar.xz
# Source0-md5:	1dccd918a4d633020e4afaf6c9352cde
URL:		http://live.gnome.org/gtk-vnc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnutls-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRequires:	vala
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-vnc is a VNC viewer widget for GTK. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

%package devel
Summary:	Libraries, includes, etc. to compile with the gtk-vnc library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries, includes, etc. to compile with the gtk-vnc library

%package capture
Summary:	VNC screenshot capture
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description capture
Captures a screenshot of the VNC desktop.

%prep
%setup -q

%build
install -d build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
cd build
../%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-gtk=3.0		\
	--without-sasl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgtk-vnc-2.0.so.0
%attr(755,root,root) %ghost %{_libdir}/libgvnc-1.0.so.0
%attr(755,root,root) %ghost %{_libdir}/libgvncpulse-1.0.so.0
%attr(755,root,root) %{_libdir}/libgtk-vnc-2.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libgvnc-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libgvncpulse-1.0.so.*.*.*
%{_libdir}/girepository-1.0/GVnc-1.0.typelib
%{_libdir}/girepository-1.0/GVncPulse-1.0.typelib
%{_libdir}/girepository-1.0/GtkVnc-2.0.typelib

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_includedir}/gtk-vnc-2.0
%{_includedir}/gvnc-1.0
%{_includedir}/gvncpulse-1.0
%{_pkgconfigdir}/gtk-vnc-2.0.pc
%{_pkgconfigdir}/gvnc-1.0.pc
%{_pkgconfigdir}/gvncpulse-1.0.pc
%{_datadir}/gir-1.0/GVnc-1.0.gir
%{_datadir}/gir-1.0/GVncPulse-1.0.gir
%{_datadir}/gir-1.0/GtkVnc-2.0.gir
%{_datadir}/vala/vapi/gtk-vnc-2.0.deps
%{_datadir}/vala/vapi/gtk-vnc-2.0.vapi
%{_datadir}/vala/vapi/gvnc-1.0.vapi
%{_datadir}/vala/vapi/gvncpulse-1.0.vapi

%files capture
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvnccapture
%{_mandir}/man1/gvnccapture.1*

