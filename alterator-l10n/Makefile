l10ndir=$(datadir)/alterator/l10n
new_l10ndir=$(datadir)/alterator/

install:
	for i in $(wildcard *.po) $(wildcard *.pot); do \
	  install $$i -Dpm644 $(l10ndir)/$$i; \
	done
	install -d $(l10ndir)/help $(new_l10ndir)/help
	cp -a old_help/* $(l10ndir)/help
	cp -a new_help/* $(new_l10ndir)/help
	PO_LOCALE_DIR=$(datadir)/locale ./utils/install_po

check:
	for i in $(wildcard *.po) $(wildcard *.pot);do \
	    msgfmt $$i -o /dev/null || exit 1; \
	done

