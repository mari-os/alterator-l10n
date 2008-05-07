Name: alterator-l10n
Version: 0.1
Release: alt10

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch:	noarch

Source:%name-%version.tar

Summary: translations for all alterator modules
License: GPL
Group: System/Configuration/Other

%description
translations for all alterator modules

%prep
%setup -q

%install
%makeinstall


%files
%_datadir/alterator/l10n


%changelog
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

