%define		source_name gmpc-libnotify
Summary:	Libnotify plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka libnotify dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-libnotify
Version:	0.18.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	eb2e9b8e0ef027095ae378e882c5aef0
URL:		http://gmpcwiki.sarine.nl/index.php?title=Libnotify
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gmpc-devel >= 0.18.0
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	libmpd-devel >= 0.18.0
BuildRequires:	libnotify-devel
BuildRequires:	libtool
Requires:	gmpc >= 0.17.0
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
