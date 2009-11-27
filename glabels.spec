Summary:	gLabels - a GNOME2 program to create labels and business cards
Summary(pl.UTF-8):	gLabels - program dla GNOME2 do tworzenia etykiet i wizytówek
Name:		glabels
Version:	2.2.1
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/glabels/%{name}-%{version}.tar.gz
# Source0-md5:	0828bd732ba4c541616ca121407723f2
Patch0:		%{name}-desktop.patch
URL:		http://glabels.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	evolution-data-server-devel >= 1.2
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2.10.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.21
BuildRequires:	libbonobo-devel >= 2.8.1
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
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

%prep
%setup -q
%patch0 -p1

mv -f po/{zh_TW.Big5,zh_TW}.po
sed -i -e 's/zh_TW\.Big5/zh_TW/' configure.in

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

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_desktop_database_post

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/mime/packages/*
%{_mandir}/man1/*.1*
%{_pixmapsdir}/%{name}
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_gtkdocdir}/libglabels
%{_libdir}/lib*.la
%{_includedir}/libglabels
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
