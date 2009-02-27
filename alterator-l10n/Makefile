PO_LOCALEDIR=$(datadir)/locale

l10ndir=$(datadir)/alterator/l10n
new_l10ndir=$(datadir)/alterator/

install: install-po install-tzone-po install-country-po
	for i in $(wildcard *.po) $(wildcard *.pot); do \
	  install $$i -Dpm644 $(l10ndir)/$$i; \
	done
	install -d $(datadir)/alterator/help
	cp -a help/* $(datadir)/alterator/help

check:
	for i in $(wildcard *.po) $(wildcard *.pot);do \
	    msgfmt $$i -o /dev/null || exit 1; \
	done

install-tzone-po:
	cd tzone-po ; \
	for i in *.po; do \
	    install -d $(PO_LOCALEDIR)/$${i%%.po}/LC_MESSAGES; \
	    msgfmt -o $(PO_LOCALEDIR)/$${i%%.po}/LC_MESSAGES/alterator-tzone-tz.mo $$i || exit 1;\
	done; \
	cd -

install-country-po:
	cd country-po ; \
	for i in *.po; do \
	    install -d $(PO_LOCALEDIR)/$${i%%.po}/LC_MESSAGES; \
	    msgfmt -o $(PO_LOCALEDIR)/$${i%%.po}/LC_MESSAGES/alterator-tzone-co.mo $$i || exit 1;\
	done; \
	cd -

install-po:
	for i in po/*; do \
	    lang=$${i##po/}; \
	    echo "Installing $$lang language:"; \
	    install -d $(PO_LOCALEDIR)/$$lang/LC_MESSAGES; \
	    for j in $$i/*.po; do \
		name=$$(basename $$j .po); \
		echo "* $$name"; \
		msgmerge --update --sort-output --backup=off \
			--compendium="$$lang.po" "$$j" "$$j" &>/dev/null || exit 1; \
		msgfmt -o "$(PO_LOCALEDIR)/$$lang/LC_MESSAGES/$$name.mo" "$$j" || exit 1; \
	    done ; \
	done
