Summary:	Enables Netscape Communicator roaming profiles with Apache
Summary(pl):	Modu³ Apache obs³uguj±cy przechodnie profile Netscape Communicatora
Name:		mod_roaming
Version:	1.0.2
Release:	4
License:	BSD type
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://www.klomp.org/mod_roaming/%{name}-%{version}.tar.gz
Source1:	roaming.conf
URL:		http://www.klomp.org/mod_roaming/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	apache-devel
Requires:	webserver

%description 
With mod_roaming you can use your Apache web server as a Netscape
Roaming Access server. This allows you to store your Netscape
Communicator 4.5 preferences, bookmarks, address books, cookies etc.
on the server so that you can use (and update) the same settings from
any Netscape Communicator 4.5 that can access the server.

%description -l pl
Dziêki mod_roaming mo¿esz u¿ywaæ serwera Apache jako serwera Netscape
Roaming Access. Pozwala to na zapisywanie ustawieñ, bookmarków,
ksi±¿ek adresowych, cookie z Netscape Communicatora >= 4.5 na
serwerze, dziêki czemu mo¿esz u¿ywaæ (i uaktualniaæ) tych samych
ustawieñ z dowolnego Netscape Communicatora >= 4.5, który ma dostêp do
serwera.

%prep
%setup -q

%build
%{_sbindir}/apxs -c -o mod_roaming.so -lc mod_roaming.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/apache,%{_sysconfdir}/httpd,%{_var}/lib/mod_roaming}

install mod_roaming.so $RPM_BUILD_ROOT%{_libdir}/apache
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd

gzip -9nf CHANGES INSTALL LICENSE README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES* INSTALL* LICENSE* README*
%attr(755,root,root) %{_libdir}/apache/mod_roaming.so
%attr(660,root,http) %dir %{_var}/lib/mod_roaming
%config %{_sysconfdir}/httpd/roaming.conf
