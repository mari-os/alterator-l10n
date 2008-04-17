install:
	for i in $(wildcard *.po) $(wildcard *.pot); do \
	install $$i -Dpm644 $(datadir)/alterator/l10n/$$i; \
	done
