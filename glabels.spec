Summary:	gLabels - a GNOME2 program to create labels and business cards
Summary(pl):	gLabels - program dla GNOME2 do tworzenia etykiet i wizytówek
Name:		glabels
Version:	1.93.2
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f748f43805763b03567c5a2c2505ab1b
Patch0:		%{name}-desktop.patch
URL:		http://glabels.sf.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	libbonobo-devel >= 2.4.0
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.23
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gLabels is a small stand-alone program for creating labels and
business cards.

%description -l pl
gLabels jest ma³ym, samodzielnym programem do tworzenia etykiet i
wizytówek.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
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

%post		-p /usr/bin/scrollkeeper-update
%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/application-registry/*
%{_datadir}/mime-info/*
%{_pixmapsdir}/%{name}
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/%{name}
