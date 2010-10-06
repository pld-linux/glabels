Summary:	gLabels - a GNOME program to create labels and business cards
Summary(pl.UTF-8):	gLabels - program dla GNOME do tworzenia etykiet i wizytówek
Name:		glabels
Version:	2.2.8
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glabels/2.2/%{name}-%{version}.tar.bz2
# Source0-md5:	8e0ac4b19de68d55e33aef6a5544f0e5
Patch0:		%{name}-desktop.patch
URL:		http://glabels.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	evolution-data-server-devel >= 1.2
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2.10.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.21
BuildRequires:	libbonobo-devel >= 2.8.1
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.7.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires:	%{name}-libs = %{version}-%{release}
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
Group:		Libraries

%description libs
glabels shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone glabels.

%package devel
Summary:	Header files for glabels
Summary(pl.UTF-8):	Pliki nagłówkowe glabels
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.0
Requires:	libxml2-devel >= 1:2.7.0

%description devel
Header files for glabels.

%description devel -l pl.UTF-8
Pliki nagłówkowe glabels.

%package static
Summary:	glabels static library
Summary(pl.UTF-8):	Statyczna biblioteka glabels
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
%{__libtoolize}
%{__intltoolize}
%{__gnome_doc_common}
%{__gtkdocize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-update-desktopdb \
	--disable-update-mimedb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/{mime-info,application-registry}

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_desktop_database_post
%update_mime_database

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_mime_database

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/glabels
%attr(755,root,root) %{_bindir}/glabels-batch
%{_datadir}/%{name}
%{_datadir}/mime/packages/glabels.xml
%{_mandir}/man1/*.1*
%{_pixmapsdir}/%{name}
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglabels.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglabels.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglabels.so
%{_libdir}/libglabels.la
%{_includedir}/libglabels
%{_pkgconfigdir}/libglabels.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libglabels.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libglabels
