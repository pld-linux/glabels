Summary:	gLabels - a GNOME2 program to create labels and business cards
Summary(pl):	gLabels - program dla GNOME2 do tworzenia etykiet i wizytówek
Name:		glabels
Version:	1.91.1
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://snaught.com/glabels/source/%{name}-%{version}.tar.gz
# Source0-md5:	bd5bfd26c9e8c8f7741e255264ce2377
Patch0:		%{name}-libgnomeprint_fix.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-desktop.patch
URL:		http://snaught.com/glabels/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libgnome-devel >= 2.2
BuildRequires:	libgnomecanvas-devel >= 2.2
BuildRequires:	libgnomeprint-devel >= 2.2
BuildRequires:	libgnomeprintui-devel >= 2.2
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libtool
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
%patch1 -p1
%patch2 -p1

%build
rm -f missing
glib-gettextize --copy --force
%{__libtoolize}
intltoolize --copy --force
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/glabels
%dir %{_datadir}/glabels/ui
%{_datadir}/glabels/ui/glabels-ui.xml
%{_datadir}/glabels/predefined-labels.template
%{_pixmapsdir}/glabels
%{_desktopdir}/%{name}.desktop
