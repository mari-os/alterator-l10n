Name: alterator-l10n
Version: 0.9
Release: alt18

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch:	noarch

Source:%name-%version.tar

Summary: translations for all alterator modules
License: GPL
Group: System/Configuration/Other

Conflicts: alterator < 3.4-alt2

%description
translations for all alterator modules

%prep
%setup -q

%build
make check

%install
%makeinstall


%files
%_datadir/alterator/l10n


%changelog
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

