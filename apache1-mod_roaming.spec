Summary: Enables Netscape Communicator roaming profiles with Apache.
Name: mod_roaming
Version: 1.0.2
Release: 4
Group: System Environment/Daemons
URL: http://www.klomp.org/mod_roaming/
Source0: http://www.klomp.org/mod_roaming/%{name}-%{version}.tar.gz
Source1: roaming.conf
Copyright: BSD type
BuildRoot: %{_tmppath}/%{name}-root
BuildPrereq: apache-devel
Requires: webserver

%description 
With mod_roaming you can use your Apache web server as a Netscape
Roaming Access server. This allows you to store your Netscape
Communicator 4.5 preferences, bookmarks, address books, cookies
etc. on the server so that you can use (and update) the same settings
from any Netscape Communicator 4.5 that can access the server.

%prep
%setup -q

%build
%{_sbindir}/apxs -c -o mod_roaming.so -lc mod_roaming.c

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/apache
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/mod_roaming
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/
install -m 755 mod_roaming.so $RPM_BUILD_ROOT%{_libdir}/apache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config %{_sysconfdir}/httpd/conf/roaming.conf
%{_libdir}/apache/mod_roaming.so
%doc CHANGES INSTALL LICENSE README
%attr(-,apache,apache) %dir /var/lib/mod_roaming

%changelog
* Fri May 25 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Fri Nov 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment
- remove the bogus preun script
- fix permissions on /var/lib/mod_roaming

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Sun Jun 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.0.2
- call %{_sbindir}/apxs explicitly instead of expecting it to be in the PATH

* Sun Jun  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- update for new release (release 5)
- add URL: tag

* Mon Feb 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild for new Apache (release 4)

* Thu Feb 24 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild for 3.2 (revision 3)

* Thu May 06 1999 Preston Brown <pbrown@redhat.com>
- initial RPM for SWS 3.0
