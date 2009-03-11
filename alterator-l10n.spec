Name: alterator-l10n
Version: 2.0
Release: alt2

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch:	noarch

Source:%name-%version.tar

Summary: translations for all alterator modules
License: GPL
Group: System/Configuration/Other

Conflicts: alterator                      < 4.7-alt1
Conflicts: alterator-ahttpd               < 0.5-alt4
Conflicts: alterator-alternatives         < 1.1-alt1
Conflicts: alterator-dhcp                 < 0.3-alt6
Conflicts: alterator-dovecot              < 0.4-alt9
Conflicts: alterator-fbi                  < 5.5-alt1
Conflicts: alterator-groups               < 0.4-alt4
Conflicts: alterator-lilo                 < 1.1-alt6
Conflicts: alterator-mirror               < 0.1-alt3
Conflicts: alterator-net-eth              < 3.3-alt1
Conflicts: alterator-net-pptp             < 0.7-alt6
Conflicts: alterator-net-pppoe            < 0.6.1-alt6
Conflicts: alterator-net-iptables         < 0.4-alt3
Conflicts: alterator-net-wifi             < 0.6-alt8
Conflicts: alterator-notes                < 1.1-alt9
Conflicts: alterator-pkg                  < 2.0-alt2
Conflicts: alterator-postfix-restrictions < 0.5-alt4
Conflicts: alterator-root                 < 0.5-alt1
Conflicts: alterator-samba                < 0.6-alt2
Conflicts: alterator-services             < 1.5-alt6
Conflicts: alterator-spamassassin         < 0.7-alt4
Conflicts: alterator-squid                < 0.4-alt6
Conflicts: alterator-sysconfig            < 1.0-alt1
Conflicts: alterator-sysinfo              < 0.6-alt1
Conflicts: alterator-tzone                < 1.0-alt6
Conflicts: alterator-ulogd                < 0.5-alt5
Conflicts: alterator-users                < 9.3-alt3
Conflicts: alterator-vsftpd               < 0.6-alt1
Conflicts: alterator-x11                  < 0.21-alt4
Conflicts: alterator-xinetd               < 1.4-alt4
Conflicts: alterator-xkb                  < 2.1-alt2
Conflicts: alterator-wizardface           < 1.0-alt1
Conflicts: alterator-lookout              < 1.6-alt1
Conflicts: alterator-datetime             < 1.0-alt1

%description
translations for all alterator modules

%prep
%setup -q

%build
make check

%install
%makeinstall

%files
%lang(en) %_datadir/alterator/help/en_US/*.html
%lang(ru) %_datadir/alterator/help/ru_RU/*.html
%lang(uk) %_datadir/alterator/help/uk_UA/*.html
%lang(pt_BR) %_datadir/alterator/help/pt_BR/*.html

%lang(ru) %_datadir/locale/ru/LC_MESSAGES/*.mo
%lang(uk) %_datadir/locale/uk/LC_MESSAGES/*.mo
%lang(pt_BR) %_datadir/locale/pt_BR/LC_MESSAGES/*.mo

%changelog
* Wed Mar 04 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt2
- add alterator-net-domain
- update translations: alterator, alterator-net-eth, alterator-office-server

* Fri Feb 27 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- move to new schema: alterator-standalone, alterator-mailman, alterator-logs
- remove old help
- don't install compendum

* Thu Feb 26 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt10
- add alterator-office-server

* Wed Feb 25 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt9
- alterator-ahttpd: update translations

* Tue Feb 24 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt8
- alterator-ahttpd: update help
- alterator-net-iptables: fix typo
- add translations for alterator-firsttime

* Thu Feb 19 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt7
- update translations for alterator-updates

* Tue Feb 17 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt6
- update translations for alterator-pkg and alterator-root

* Mon Feb 16 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt5
- move alterator-net-eth to new schema

* Fri Feb 13 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.6-alt4
- rewrite ru help for new alterator-net-iptables

* Wed Feb 11 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt3
- update translations for alterator-mirror

* Wed Feb 11 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt2
- add alterator-updates

* Tue Feb 10 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt1
- move alterator-pkg to new schema
- remove files for alterator-tzone

* Mon Feb 09 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt8
- alterator-net-iptables: fix label

* Fri Feb 06 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt7
- alterator-net-iptables: fix translation

* Fri Feb 06 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt6
- update translations for alterator-net-iptables

* Mon Feb 02 2009 Stanislav Ievlev <inger@altlinux.org> 1.5-alt5
- update translations for alterator-datetime
- move to new schema: alterator-control

* Fri Jan 30 2009 Stanislav Ievlev <inger@altlinux.org> 1.5-alt4
- update translations for new alterator-datetime

* Fri Jan 30 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt3
- add pt_BR po-files (by fmartini@)

* Fri Jan 30 2009 Stanislav Ievlev <inger@altlinux.org> 1.5-alt2
- move to new schema: alterator-datetime

* Thu Jan 29 2009 Stanislav Ievlev <inger@altlinux.org> 1.5-alt1
- move to new schema: alterator-wizardface, alterator-lookout, alterator-tzone, alterator-fbi

* Wed Jan 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt3
- move UA and EN help for alterator-dovecot to new_help dir
- remove old help for alterator-groups (new help is already in new_help dir)

* Wed Jan 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt2
- move help for alterator-openldap back to old_help dir

* Wed Jan 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt1
- update_module script: using dictionary from module directory when
  one in alterator-l10n does not exists yet
- add translations and new-style help for modules:
  + alterator-users
  + alterator-ulogd
  + alterator-dovecot
- move help to new_help dir for alterator-notes
- ru help fixes (by azol@):
  + services: add restart note
  + ahttpd-server: add signature section
  + openldap, samba, vsftpd, xinetd, dhcp, dovecot,
    postfix-restrictions, squid, ulogd: add service restart warning

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt2
- update translations for alterator-vsftpd

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt1
- add new-style dictionaries and help for modules:
 + alterator-dhcp
 + alterator-groups
 + alterator-net-{pptp,pppoe,iptables}
 + alterator-postfix-restrictions
 + alterator-squid
 + alterator-xkb
- update Conflicts and modules.list
- fix some po-files

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt3
- fix help for alterator-ahttpd-server
- fix help for alterator-chronograph (by manowar@)

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt2
- remove alterator-ahttpd translations (module does not exists)
- update conflicts for alterator-{vsftpd,alternatives,root}

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt1
- add new ru help (by azol@)
  + ahttpd-server
  + office-server-net
  + mirror
- move po-files for modules to alterator-l10n:
  + alterator-spamassassin
  + alterator-net-wifi
  + alterator-notes
  + alterator-notes
  + alterator-mirror
  + alterator-ahttpd
  + alterator
- move help to new-style directory:
  + alterator (notfound.html)
  + alterator-spamassassin
- for modules converted to new-style help and po keepping:
  + add conflicts on old versions
  + remove modules from modules.list
- add utils/get_po_transl script (moved from altertator:build/msggrep)
- move install_po script to utils dir
- fix update_desktop util: work with alterator itself, remove unused code

* Mon Jan 26 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt4
- move alterator-vsftpd to new schema

* Mon Jan 26 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt3
- move alterator-alternatives to new schema

* Mon Jan 26 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt2
- move alterator-root to new schema

* Mon Jan 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt1
- add update_desktop script

* Fri Jan 23 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt3
- new-style help and po for alterator-xinetd and alterator-services
- fix update_module script

* Fri Jan 23 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt2
- add alterator-samba dictionary
- update alterator-samba help (by manowar@)
- update alterator-lilo dictionary

* Thu Jan 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- New style po files keeping!
  keep and install separate dictionary for each module
- add alterator-lilo and alterator-x11 dictionaries

* Thu Jan 22 2009 Stanislav Ievlev <inger@altlinux.org> 0.17-alt1
- move to new help: alterator-pkg
- update translations for alterator-pkg

* Wed Jan 21 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.16-alt1
- merge with azol@ (new help for alterator-office-server-root)
- add help for chronograph and openldap (by manowar@)

* Thu Jan 15 2009 Stanislav Ievlev <inger@altlinux.org> 0.15-alt1
- move to new help: tzone acc-html
- update translations for alterator-fbi
- remove obsolete help: timezone

* Thu Jan 15 2009 Stanislav Ievlev <inger@altlinux.org> 0.14-alt1
- move to new_help: net-eth, sysconfig-base
- remove obsolete help: sysconfig-lang, sysconfig-kbd

* Thu Dec 11 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.13-alt4
- update pt_BR.po

* Thu Dec 11 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.13-alt3
- install some help files in /usr/share/alterator/help/ directory

* Tue Dec 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.12-alt2
- fix ru help (auth dhcp net-eth nut-devices postfix-restrictions spamassassin ulogd)
  (by bertis@)

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.12-alt1
- update ru help (by azol@):
  + acc-html
  + auth
  + datetime
  + dhcp
  + dovecot
  + lightsquid (NEW)
  + logs
  + net-eth
  + net-iptables
  + net-pppoe
  + net-pptp
  + notes-license
  + notes-release-notes
  + nut-devices (NEW)
  + pkg-groups
  + pkg-register
  + pkg-sources
  + pkg-upgrade
  + postfix-restrictions
  + root
  + samba
  + services
  + spamassassin
  + squid
  + sysconfig-kbd
  + sysconfig-language
  + sysconfig
  + sysinfo
  + tzone
  + ulogd (NEW)
  + users
  + vsftpd
  + xinetd

* Thu Dec 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.11-alt2
- add pt_BR

* Tue Dec 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.11-alt1
- fix ru help files (by azol@):
  + notes-release-notes
  + notes-license
  + users
  + root
  + net-iptables
  + sysinfo
  + acc-html
  + tzone (move from module)

* Mon Nov 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.10-alt4
- add english help for: logs, samba, dovecot, acc-html, root
- minor help improvements (inger@, azol@)

* Thu Nov 20 2008 Stanislav Ievlev <inger@altlinux.org> 0.10-alt3
- update translations for alterator-sysconfig

* Thu Nov 20 2008 Stanislav Ievlev <inger@altlinux.org> 0.10-alt2
- add alterator-mirror

* Mon Nov 17 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.10-alt1
- ru help for sysinfo, services, logs, pkg (by azol@)

* Wed Nov 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt19
- fix translation for alterator-x11

* Thu Oct 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt18
- add alterator-dhcp

* Wed Oct 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt17
- add alterator-mailman

* Tue Oct 14 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt16
- fix update_archive and update_po

* Tue Oct 14 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt15
- update translations for alterator-x11

* Thu Oct 09 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt14
- update translations for alterator-postfix-restrictions and alterator-dovecot

* Wed Oct 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt13
- add alterator-postfix-restrictions

* Fri Oct 03 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt12
- add alterator-samba

* Fri Sep 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt11
- add alterator-squid

* Mon Sep 22 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt10
- alterator-lilo: minor spelling fix (by mike@)

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt9
- update po for auth

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt8.2
- hotfix2

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt8.1
- hotfix

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt8
- update po for users

* Fri Sep 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt7
- fix uk.po

* Fri Sep 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt6
- changes for alterator-lilo, alterator-xkb, alterator-notes desktop labels

* Wed Sep 17 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt5
- roughly half of uk.po reviewed/updated/translated (mike@)
- fix some English phrases (mike@)
- update translations for new alterator and alterator-fbi

* Mon Sep 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt4
- update alterator translations

* Fri Sep 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt3
- update Ukrainian translation (port from 4.0 branch)

* Mon Sep 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt2
- update translation for alterator-net-eth

* Tue Sep 02 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- merge with cas@
- add helps
- replace po_head_repl script with fix_po
- fix package deps

* Thu Aug 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- add translations for alterator-net-iptables

* Mon Aug 25 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt6
- update translations for acl feature

* Mon Aug 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt5
- update translations for alterator-xkb

* Fri Aug 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt4
- add alterator-xkb
- update Ukrainian translation

* Wed Aug 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt3
- update translations for alterator (comments for desktop directories)

* Wed Jul 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt2
- update translations for alterator-groups

* Wed Jul 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- improve update-po script
- add translations for acc groups
- update Ukrainian translation

* Fri Jul 25 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt8
- add alterator-postfix-sasl

* Fri Jul 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt7
- add alterator-groups

* Fri Jul 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt6
- update translations for alterator-control

* Fri Jul 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt5
- update translations for alterator-xinetd

* Tue Jul 01 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt4
- fix labels for alterator-lilo

* Tue Jul 01 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt3
- update translations for new alterator-lilo

* Tue Jul 01 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt2
- update translations for new alterator-lilo

* Mon Jun 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- add alterator-fbi

* Wed Jun 25 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt12
- update translations for alterator-users

* Wed Jun 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt11
- new labels in alterator-lilo (fix #16161)

* Tue Jun 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt10
- update translations for alterator-root, alterator-root

* Tue Jun 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt9
- update translations for new alterator-lilo

* Mon Jun 23 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt8
- update translations for new alterator-lilo

* Wed Jun 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt7
- update translations for new alterator-lilo

* Tue Jun 17 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt6
- add alterator-net-pppoe

* Mon Jun 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt5
- add alterator-net-pptp

* Mon Jun 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt4
- update translations for new alterator-pkg again

* Wed Jun 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- rebuild

* Wed Jun 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- update translations for new alterator-pkg

* Mon Jun 09 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- add translations for desktop files

* Fri Jun 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt12
- add some translations for new alterator-lilo

* Tue Jun 03 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt11
- clear pot-file before merging
- fix some translations

* Tue Jun 03 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt10
- update alterator-ahttpd translations

* Fri May 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt9
- add alterator-lookout, alterator-pkg

* Thu May 29 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt8
- add alterator-standalone

* Wed May 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt7
- add alterator-dovecot

* Wed May 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt6
- add alterator
- add alterator-net-wifi

* Mon May 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt5
- add alterator-sysconfig

* Fri May 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- update for new alterator-lilo
- add alterator-wizardface

* Thu May 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt2
- modify with new alterator-lilo

* Tue May 13 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- add alterator-datetime
- add alterator-control
- improve po-file generation

* Tue May 13 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt6
- fix ru.po
- fix uk.po
- add make check

* Mon May 12 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt5
- add alterator-lilo

* Thu May 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt4
- add alterator-xinetd

* Thu May 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt3
- fix alterator-logs (s,Fist,First)

* Thu May 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt2
- add po_head_repl script

* Thu May 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt2
- add alterator-notes

* Thu May 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- ru.po: fix "Reset" translation
- add uk.po (resurrected from existing translations)

* Wed May 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt10
- add alterator-services

* Wed May 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt9
- add alterator-ahttpd
- add alterator-logs

* Tue May 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt8
- update alterator-x11

* Sun May 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt7
- add alterator-root

* Wed Apr 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- add alterator-vsftpd

* Wed Apr 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- add alterator-net-eth

* Wed Apr 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- add alterator-x11

* Tue Apr 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- add alterator-auth

* Sat Apr 19 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- add alterator-spamassassin

* Thu Apr 17 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build

