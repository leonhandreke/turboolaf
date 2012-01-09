install:
	cp turboolaf /usr/bin
	xdg-mime install data/text_olaf-invoice.xml
	xdg-desktop-menu install --novendor data/turboolaf.desktop
	# run `xdg-mime default data/turboolaf.desktop text/olaf-invoice` in case you want to set the default application explicitly
