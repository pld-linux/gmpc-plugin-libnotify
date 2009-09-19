%define		source_name gmpc-libnotify
Summary:	Libnotify plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka libnotify dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-libnotify
Version:	0.19.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	da1a96fbedb216976b1dae0bbd4bbcb2
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_LIBNOTIFY
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gmpc-devel >= 0.19.0
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	gmpc >= 0.19.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libnotify plugin sends to the notification daemon an announcement
on song change.

%description -l pl.UTF-8
Wtyczka libnotify wysyła do demona powiadomień informację o zmianie
utworu.

%prep
%setup -qn %{source_name}-%{version}

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
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/libnotifyplugin.so
