Summary:	gLabels - a GNOME2 program to create labels and business cards
Summary(pl):	gLabels - program dla GNOME2 do tworzenia etykiet i wizytówek
Name:		glabels
Version:	1.93.3
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	29abf3f91ea9e8aec194744302175c02
Patch0:		%{name}-desktop.patch
URL:		http://glabels.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common
BuildRequires:	intltool >= 0.21
BuildRequires:	libbonobo-devel >= 2.4.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.23
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gLabels is a small stand-alone program for creating labels and
business cards.

%description -l pl
gLabels jest ma³ym, samodzielnym programem do tworzenia etykiet i
wizytówek.

%package libs
Summary:	glabels shared libraries
Summary(pl):	Biblioteki wspó³dzielone glabels
Group:		Libraries

%description libs
glabels shared libraries.

%description libs -l pl
Biblioteki wspó³dzielone glabels.

%package devel
Summary:	Header files for glabels
Summary(pl):	Pliki nag³ówkowe glabels
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for glabels.

%description devel -l pl
Pliki nag³ówkowe glabels.

%package static
Summary:	glabels static library
Summary(pl):	Statyczna biblioteka glabels
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
glabels staic library.

%description static -l pl
Statyczna biblioteka glabels.

%prep
%setup -q
%patch0 -p1

mv -f po/{zh_TW.Big5,zh_TW}.po
%{__perl} -pi -e 's/zh_TW\.Big5/zh_TW/' configure.in

%build
glib-gettextize --copy --force
%{__libtoolize}
intltoolize --copy --force
gnome-doc-common --copy
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-platform-gnome-2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/scrollkeeper-update
%postun	-p /usr/bin/scrollkeeper-update

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/application-registry/*
%{_datadir}/mime-info/*
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
%{_libdir}/lib*.la
%{_includedir}/libglabels

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
