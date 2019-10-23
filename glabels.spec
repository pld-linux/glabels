Summary:	gLabels - a GNOME program to create labels and business cards
Summary(pl.UTF-8):	gLabels - program dla GNOME do tworzenia etykiet i wizytówek
Name:		glabels
Version:	3.4.1
Release:	1
License:	GPL v3+ (libraries: LGPL v3+)
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glabels/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	095105ac95872bd9a767764fa60d5152
Patch0:		%{name}-link.patch
URL:		http://www.glabels.org/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	barcode-devel >= 0.98
BuildRequires:	cairo-devel >= 1.14.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	evolution-data-server-devel >= 3.12.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.42.0
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	iec16022-devel >= 0.2.4
BuildRequires:	intltool >= 0.40.0
BuildRequires:	librsvg-devel >= 2.39.0
BuildRequires:	libtool >= 2:2
BuildRequires:	libxml2-devel >= 1:2.9.0
BuildRequires:	pango-devel >= 1:1.36.0
BuildRequires:	pkgconfig
BuildRequires:	qrencode-devel >= 3.1.0
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
BuildRequires:	zint-devel >= 2.4.0
Requires(post,postun):	glib2 >= 1:2.42.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	barcode >= 0.98
Requires:	evolution-data-server-libs >= 3.12.0
Requires:	gtk+3 >= 3.14.0
Requires:	hicolor-icon-theme
Requires:	iec16022 >= 0.2.4
Requires:	librsvg >= 2.39.0
Requires:	qrencode-libs >= 3.1.0
Requires:	zint >= 2.4.0
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
License:	LGPL v3+
Group:		Libraries
Requires:	cairo >= 1.14.0
Requires:	glib2 >= 1:2.42.0
Requires:	libxml2 >= 1:2.9.0
Requires:	pango >= 1:1.36.0

%description libs
glabels shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone glabels.

%package devel
Summary:	Header files for glabels
Summary(pl.UTF-8):	Pliki nagłówkowe glabels
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cairo-devel >= 1.14.0
Requires:	glib2-devel >= 1:2.42.0
Requires:	libxml2-devel >= 1:2.9.0
Requires:	pango-devel >= 1:1.36.0

%description devel
Header files for glabels.

%description devel -l pl.UTF-8
Pliki nagłówkowe glabels.

%package static
Summary:	glabels static library
Summary(pl.UTF-8):	Statyczna biblioteka glabels
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
glabels staic library.

%description static -l pl.UTF-8
Statyczna biblioteka glabels.

%package apidocs
Summary:	glabels library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki glabels
License:	CC-BY-SA v3.0
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
glabels library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki glabels.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile \
	--disable-silent-rules \
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
%doc AUTHORS COPYING-TEMPLATES COPYING.README_FIRST ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/glabels-3
%attr(755,root,root) %{_bindir}/glabels-3-batch
%{_datadir}/appdata/glabels-3.appdata.xml
%{_datadir}/glabels-3.0
%{_datadir}/glib-2.0/schemas/org.gnome.glabels-3.gschema.xml
%{_datadir}/mime/packages/glabels-3.0.xml
%{_mandir}/man1/glabels-3.1*
%{_mandir}/man1/glabels-3-batch.1*
%{_desktopdir}/glabels-3.0.desktop
%{_iconsdir}/hicolor/*x*/apps/glabels-3.0.png
%{_iconsdir}/hicolor/48x48/mimetypes/application-x-glabels.png
%{_iconsdir}/hicolor/scalable/apps/glabels-3.0.svg
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-glabels.svg

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
