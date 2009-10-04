%define		source_name gmpc-tagedit
Summary:	Add to GMPC an editor for song tags
Summary(pl.UTF-8):Wtyczka edycji znaczników dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-tagedit
Version:	0.19.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	be84d0be7ac2e4a11649d944ee06bd39
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_TAGEDIT
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.16
BuildRequires:	gmpc-devel >= 0.19.0
BuildRequires:	gob2 >= 2.0.10
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	intltool >= 0.21
BuildRequires:	libmpd-devel >= 0.19.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	taglib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tagedit plugin for GMPC adds a editor panel for editing song tags. With the
plugin enabled, you are able to queue one or more songs to the Tag editor from
the playlist or song browser. You may then enter the Tag editor panel and
modify the tags of the queued songs one by one or by groups. The changes are
recorded when you hit the Save button. If you made a mistake while editing
tags, you may discard the changes you made to one song or a group of songs.

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

install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%find_lang gmpc-tagedit

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gmpc-tagedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/*.so
