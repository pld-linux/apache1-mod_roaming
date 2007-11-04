# TODO
# - mod_roaming.conf points to htpasswd file in /var, shouldn't it be in /etc
#   (and don't forget trigger to move old possibly existing htpasswd in /var when fixing it)
%define		mod_name	roaming
%define 	apxs		/usr/sbin/apxs1
Summary:	Enables Netscape Communicator roaming profiles with Apache
Summary(cs.UTF-8):	Modul podpory roamingových profilů Netscape Communicatora pro Apache
Summary(da.UTF-8):	Et apachemodul som lader webtjeneren håndtere profiler for Netscape Communicator
Summary(de.UTF-8):	Aktiviert den Netscape Communicator für das Profilroaming mit Apache
Summary(es.UTF-8):	Módulo de acceso roaming para navegación en red para Apache
Summary(fr.UTF-8):	Permet l'itinérance de profils Netscape Communicator avec Apache
Summary(it.UTF-8):	Abilita i profili di roaming di Netscape Communicator con Apache
Summary(nb.UTF-8):	En apachemodul som lar webtjeneren håndtere profiler for Netscape Communicator
Summary(pl.UTF-8):	Moduł Apache obsługujący przechodnie profile Netscape Communicatora
Summary(pt_BR.UTF-8):	Modulo "Netscape Roaming Access" para o Apache
Summary(sk.UTF-8):	WWW prehliadač Netscape Navigator
Summary(sv.UTF-8):	Möjliggör Netscape Communicator reseprofiler med Apache
Name:		apache1-mod_%{mod_name}
Version:	1.0.2
Release:	3
License:	BSD-like
Group:		Networking/Daemons
Source0:	http://www.klomp.org/mod_roaming/mod_%{mod_name}-%{version}.tar.gz
# Source0-md5:	226c0ce2daf276072079590b5560f022
Source1:	%{name}.conf
URL:		http://www.klomp.org/mod_roaming/
BuildRequires:	apache1-devel >= 1.3.39
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(triggerpostun):	%{apxs}
Requires(triggerpostun):	grep
Requires(triggerpostun):	sed >= 4.0
Requires:	apache1(EAPI)
Obsoletes:	apache-mod_roaming <= 1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)

%description
With mod_roaming you can use your Apache web server as a Netscape
Roaming Access server. This allows you to store your Netscape
Communicator 4.5 preferences, bookmarks, address books, cookies etc.
on the server so that you can use (and update) the same settings from
any Netscape Communicator 4.5 that can access the server.

%description -l cs.UTF-8
Balíček mod_roaming obsahuje modul pro podporu roamingových profilů
Netscape Communicatora pro Apache. Profily umožňují uložit nastavení
Netscape 4.5 (bookmarky, adresář, cookies, nastavení Netacspe apod.)
na server, takže při spuštění Netscape z libovolného místa na
Internetu budete mít stejné nastavení.

%description -l de.UTF-8
Mit mo_roaming können Sie Ihren Apache Web-Server als
Netscape-Roaming- Zugriffsserver verwenden. Auf diese Weise können Sie
Ihre Präferenzen für Netscape Communicator 4.5, Lesezeichen,
Adressbücher, Cookies etc. auf dem Server speichern, so dass Sie die
gleichen Einstellungen von jedem Netscape Communicator 4.5 verwenden
(und aktualisieren) können, die Zugriff auf den Server haben.

%description -l es.UTF-8
Con mod_roaming puede utilizar su servidor web apache como un servidor
Netscape Roaming Access. Esto le permite almacenar las preferencias de
su Netscape Communicator 4.5, los bookmarks, libros de direcciones,
cookies, etc. en el servidor de tal forma que puede utilizar (y
actualizar) las mismas opciones desde cualquier Netscape Communicator
4.5 que acceda al servidor.

%description -l fr.UTF-8
Mod_roaming vous permet d'utiliser le serveur Web Apache en tant que
Netscape pour accéder à un serveur Access. Cela vous permet de stocker
vos préférences Netscape Communicator 4.5, signets, carnets
d'adresses, cookies, etc. sur le serveur afin d'utiliser (et de mettre
à jour) les mêmes réglages depuis n'importe quel Netscapte
Communicator 4.5 ayant accès au serveur.

%description -l it.UTF-8
Grazie a mod_roaming è possibile utilizzare il server Web Apache come
un server Netscape Roaming Access. Questo consente di memorizzare le
preferenze, i segnalibri, le rubriche i cookie (e così via) di
Netscape Communicator 4.5 sul server, in modo da poter usare (e
aggiornare) le stesse impostazioni da qualsiasi Netscape Communicator
4.5 che possa accedere al server.

%description -l ja.UTF-8
mod_roaming を使用すると、Apache Web サーバーを Netscape Roaming
Access サーバーとして使用できます。これによって Netscape Communicator
4.5 のお気に入り、ブックマーク、アドレス
ブック、クッキーなどをサーバー上に格納でき、サーバーにアクセスできるどの
の Netscape Communicator 4.5 からでも同じ設定を使用 (および更新)
できる ようになります。

%description -l pl.UTF-8
Dzięki mod_roaming możesz używać serwera Apache jako serwera Netscape
Roaming Access. Pozwala to na zapisywanie ustawień, bookmarków,
książek adresowych, cookie z Netscape Communicatora >= 4.5 na
serwerze, dzięki czemu możesz używać (i uaktualniać) tych samych
ustawień z dowolnego Netscape Communicatora >= 4.5, który ma dostęp do
serwera.

%description -l pt_BR.UTF-8
Com o mod_roaming você pode usar o Apache como um servidor de "Roaming
Access" para o Netscape. Isto permite que você armazene preferências,
bookmarks, livros de acessos, cookies, etc, do Netscape Communicator
4.5 no servidor, sendo que com isso, você pode usar as mesmas
configurações para qualquer Netscape 4.5 que possa acessar este
servidor.

%description -l sv.UTF-8
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
install -d $RPM_BUILD_ROOT{%{_pkglibdir},%{_sysconfdir}/conf.d,%{_var}/lib/mod_roaming}

install mod_%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/90_mod_%{mod_name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q apache restart

%postun
if [ "$1" = "0" ]; then
	%service -q apache restart
fi

%triggerpostun -- %{name} < 1.0.2-1.1
if grep -q '^Include conf\.d/\*\.conf' /etc/apache/apache.conf; then
	%{apxs} -e -A -n %{mod_name} %{_pkglibdir}/mod_%{mod_name}.so 1>&2
	sed -i -e '
		/^Include.*mod_%{mod_name}\.conf/d
	' /etc/apache/apache.conf
else
	# they're still using old apache.conf
	sed -i -e '
		s,^Include.*mod_%{mod_name}\.conf,Include %{_sysconfdir}/conf.d/*_mod_%{mod_name}.conf,
	' /etc/apache/apache.conf
fi
%service -q apache restart

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL LICENSE README
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_%{mod_name}.conf
%attr(755,root,root) %{_pkglibdir}/*
%attr(770,root,http) %dir %{_var}/lib/mod_roaming
