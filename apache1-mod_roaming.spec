%define 	apxs		/usr/sbin/apxs
%define		mod_name	roaming

Summary:	Enables Netscape Communicator roaming profiles with Apache
Summary(cs):	Modul podpory roamingových profilù Netscape Communicatora pro Apache
Summary(da):	Et apachemodul som lader webtjeneren håndtere profiler for Netscape Communicator
Summary(de):	Aktiviert den Netscape Communicator für das Profilroaming mit Apache
Summary(es):	Módulo de acceso roaming para navegación en red para Apache
Summary(fr):	Permet l'itinérance de profils Netscape Communicator avec Apache
Summary(it):	Abilita i profili di roaming di Netscape Communicator con Apache
Summary(no):	En apachemodul som lar webtjeneren håndtere profiler for Netscape Communicator
Summary(pl):	Modu³ Apache obs³uguj±cy przechodnie profile Netscape Communicatora
Summary(pt_BR):	Modulo "Netscape Roaming Access" para o Apache
Summary(sk):	WWW prehliadaè Netscape Navigator
Summary(sv):	Möjliggör Netscape Communicator reseprofiler med Apache
Name:		apache-mod_%{mod_name}
Version:	1.0.2
Release:	6
License:	BSD-like
Group:		Networking/Daemons
Source0:	http://www.klomp.org/mod_roaming/mod_%{mod_name}-%{version}.tar.gz
Source1:	%{name}.conf
URL:		http://www.klomp.org/mod_roaming/
BuildRequires:	apache(EAPI)-devel
BuildRequires:	%{apxs}
Requires(post,preun):	%{apxs}
Requires(post,preun):	grep
Requires(preun):	fileutils
Requires:	apache(EAPI)
Provides:	mod_roaming
Obsoletes:	mod_roaming
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With mod_roaming you can use your Apache web server as a Netscape
Roaming Access server. This allows you to store your Netscape
Communicator 4.5 preferences, bookmarks, address books, cookies etc.
on the server so that you can use (and update) the same settings from
any Netscape Communicator 4.5 that can access the server.

%description -l cs
Balíèek mod_roaming obsahuje modul pro podporu roamingových profilù
Netscape Communicatora pro Apache. Profily umo¾òují ulo¾it nastavení
Netscape 4.5 (bookmarky, adresáø, cookies, nastavení Netacspe apod.)
na server, tak¾e pøi spu¹tìní Netscape z libovolného místa na
Internetu budete mít stejné nastavení.

%description -l de
Mit mo_roaming können Sie Ihren Apache Web-Server als
Netscape-Roaming- Zugriffsserver verwenden. Auf diese Weise können Sie
Ihre Präferenzen für Netscape Communicator 4.5, Lesezeichen,
Adressbücher, Cookies etc. auf dem Server speichern, so dass Sie die
gleichen Einstellungen von jedem Netscape Communicator 4.5 verwenden
(und aktualisieren) können, die Zugriff auf den Server haben.

%description -l es
Con mod_roaming puede utilizar su servidor web apache como un servidor
Netscape Roaming Access. Esto le permite almacenar las preferencias de
su Netscape Communicator 4.5, los bookmarks, libros de direcciones,
cookies, etc. en el servidor de tal forma que puede utilizar (y
actualizar) las mismas opciones desde cualquier Netscape Communicator
4.5 que acceda al servidor.

%description -l fr
Mod_roaming vous permet d'utiliser le serveur Web Apache en tant que
Netscape pour accéder à un serveur Access. Cela vous permet de stocker
vos préférences Netscape Communicator 4.5, signets, carnets
d'adresses, cookies, etc. sur le serveur afin d'utiliser (et de mettre
à jour) les mêmes réglages depuis n'importe quel Netscapte
Communicator 4.5 ayant accès au serveur.

%description -l it
Grazie a mod_roaming è possibile utilizzare il server Web Apache come
un server Netscape Roaming Access. Questo consente di memorizzare le
preferenze, i segnalibri, le rubriche i cookie (e così via) di
Netscape Communicator 4.5 sul server, in modo da poter usare (e
aggiornare) le stesse impostazioni da qualsiasi Netscape Communicator
4.5 che possa accedere al server.

%description -l ja
mod_roaming ¤ò»ÈÍÑ¤¹¤ë¤È¡¢Apache Web ¥µ¡¼¥Ð¡¼¤ò Netscape Roaming
Access ¥µ¡¼¥Ð¡¼¤È¤·¤Æ»ÈÍÑ¤Ç¤­¤Þ¤¹¡£¤³¤ì¤Ë¤è¤Ã¤Æ Netscape Communicator
4.5 ¤Î¤ªµ¤¤ËÆþ¤ê¡¢¥Ö¥Ã¥¯¥Þ¡¼¥¯¡¢¥¢¥É¥ì¥¹
¥Ö¥Ã¥¯¡¢¥¯¥Ã¥­¡¼¤Ê¤É¤ò¥µ¡¼¥Ð¡¼¾å¤Ë³ÊÇ¼¤Ç¤­¡¢¥µ¡¼¥Ð¡¼¤Ë¥¢¥¯¥»¥¹¤Ç¤­¤ë¤É¤Î
¤Î Netscape Communicator 4.5 ¤«¤é¤Ç¤âÆ±¤¸ÀßÄê¤ò»ÈÍÑ (¤ª¤è¤Ó¹¹¿·)
¤Ç¤­¤ë ¤è¤¦¤Ë¤Ê¤ê¤Þ¤¹¡£

%description -l pl
Dziêki mod_roaming mo¿esz u¿ywaæ serwera Apache jako serwera Netscape
Roaming Access. Pozwala to na zapisywanie ustawieñ, bookmarków,
ksi±¿ek adresowych, cookie z Netscape Communicatora >= 4.5 na
serwerze, dziêki czemu mo¿esz u¿ywaæ (i uaktualniaæ) tych samych
ustawieñ z dowolnego Netscape Communicatora >= 4.5, który ma dostêp do
serwera.

%description -l pt_BR
Com o mod_roaming você pode usar o Apache como um servidor de "Roaming
Access" para o Netscape. Isto permite que você armazene preferências,
bookmarks, livros de acessos, cookies, etc, do Netscape Communicator
4.5 no servidor, sendo que com isso, você pode usar as mesmas
configurações para qualquer Netscape 4.5 que possa acessar este
servidor.

%description -l sv
Med mod_roaming kan du använda din webbserver Apache som en server för
Netscape reseprofiler. Detta låter dig lagra dina Netscape
Communicator 4.5 preferenser, bokmärken, adressbok, kakor, etc. på
servern så att du kan använda (och ändra) inställningarna från valfri
Netscape Communicator 4.5 som kan komma åt servern.

%prep
%setup -q -n mod_%{mod_name}-%{version}

%build
%{apxs} -c -o mod_roaming.so -lc mod_roaming.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/apache,%{_sysconfdir}/httpd,%{_var}/lib/mod_roaming}

install mod_%{mod_name}.so $RPM_BUILD_ROOT%{_libdir}/apache
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/mod_roaming.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{apxs} -e -a -n %{mod_name} %{_pkglibdir}/mod_%{mod_name}.so 1>&2
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*mod_%{mod_name}.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/mod_%{mod_name}.conf" >> /etc/httpd/httpd.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n %{mod_name} %{_pkglibdir}/mod_%{mod_name}.so 1>&2
	umask 027
	grep -v "^Include.*mod_%{mod_name}.conf" /etc/httpd/httpd.conf > \
		/etc/httpd/httpd.conf.tmp
	mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL LICENSE README
%attr(755,root,root) %{_libdir}/apache/mod_roaming.so
%attr(660,root,http) %dir %{_var}/lib/mod_roaming
%config(noreplace) %{_sysconfdir}/httpd/mod_roaming.conf
