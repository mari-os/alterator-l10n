l10ndir=$(datadir)/alterator/l10n

install:
	for i in $(wildcard *.po) $(wildcard *.pot); do \
	install $$i -Dpm644 $(l10ndir)/$$i; \
	done
	cp -a help $(l10ndir)

check:
	for i in $(wildcard *.po) $(wildcard *.pot);do \
	    msgfmt $$i -o /dev/null || exit 1; \
	done
