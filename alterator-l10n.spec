Name: alterator-l10n
Version: 0.5
Release: alt2

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch:	noarch

Source:%name-%version.tar

Summary: translations for all alterator modules
License: GPL
Group: System/Configuration/Other

Requires: alterator >= 3.4-alt2

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

