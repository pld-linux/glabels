Summary:	gLabels - a GNOME program to create labels and business cards
Summary(pl.UTF-8):	gLabels - program dla GNOME do tworzenia etykiet i wizytówek
Name:		glabels
Version:	3.0.0
Release:	2
License:	GPL v3
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glabels/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	823531d597a5483c30486f1b22ee07bf
Patch0:		%{name}-link.patch
URL:		http://www.glabels.org/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	barcode-devel >= 0.98
BuildRequires:	docbook-dtd412-xml
BuildRequires:	evolution-data-server-devel >= 3.0.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.2
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.0.9
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	iec16022-devel >= 0.2.4
BuildRequires:	intltool >= 0.40.0
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.7.8
BuildRequires:	pkgconfig
BuildRequires:	qrencode-devel >= 3.1.0
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	zint-devel >= 2.4.0
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gLabels is a small stand-alone program for creating labels and
business cards.

%description -l pl.UTF-8
gLabels jest małym, samodzielnym programem do tworzenia etykiet i
wizytówek.

%package libs
Summary:	glabels shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone glabels
License:	LGPL v3
Group:		Libraries

%description libs
glabels shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone glabels.

%package devel
Summary:	Header files for glabels
Summary(pl.UTF-8):	Pliki nagłówkowe glabels
License:	LGPL v3
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.2
Requires:	libxml2-devel >= 1:2.7.8
Requires:	pango-devel

%description devel
Header files for glabels.

%description devel -l pl.UTF-8
Pliki nagłówkowe glabels.

%package static
Summary:	glabels static library
Summary(pl.UTF-8):	Statyczna biblioteka glabels
License:	LGPL v3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
glabels staic library.

%description static -l pl.UTF-8
Statyczna biblioteka glabels.

%package apidocs
Summary:	glabels library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki glabels
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
glabels library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki glabels.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__gnome_doc_common}
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-schemas-compile \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}-3.0 --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_mime_database
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}-3.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/glabels-3
%attr(755,root,root) %{_bindir}/glabels-3-batch
%{_datadir}/glabels-3.0
%{_datadir}/glib-2.0/schemas/org.gnome.glabels-3.gschema.xml
%{_datadir}/mime/packages/glabels-3.0.xml
%{_mandir}/man1/*.1*
%{_desktopdir}/glabels-3.0.desktop
%{_iconsdir}/hicolor/*/*/*.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglabels-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglabels-3.0.so.8
%attr(755,root,root) %{_libdir}/libglbarcode-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglbarcode-3.0.so.0
%{_datadir}/libglabels-3.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglabels-3.0.so
%attr(755,root,root) %{_libdir}/libglbarcode-3.0.so
%{_includedir}/libglabels-3.0
%{_includedir}/libglbarcode-3.0
%{_pkgconfigdir}/libglabels-3.0.pc
%{_pkgconfigdir}/libglbarcode-3.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libglabels-3.0.a
%{_libdir}/libglbarcode-3.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libglabels-3.0
%{_gtkdocdir}/libglbarcode-3.0
