Name: alterator-l10n
Version: 0.1
Release: alt2

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
* Sat Apr 19 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- add alterator-spamassassin

* Thu Apr 17 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build

