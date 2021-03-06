#
# Copyright (c) 2011-2013 CESNET
#
# LICENSE TERMS
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the Company nor the names of its contributors
#    may be used to endorse or promote products derived from this
#    software without specific prior written permission.
#
# ALTERNATIVELY, provided that this notice is retained in full, this
# product may be distributed under the terms of the GNU General Public
# License (GPL) version 2 or later, in which case the provisions
# of the GPL apply INSTEAD OF those given above.
#
# This software is provided ``as is'', and any express or implied
# warranties, including, but not limited to, the implied warranties of
# merchantability and fitness for a particular purpose are disclaimed.
# In no event shall the company or contributors be liable for any
# direct, indirect, incidental, special, exemplary, or consequential
# damages (including, but not limited to, procurement of substitute
# goods or services; loss of use, data, or profits; or business
# interruption) however caused and on any theory of liability, whether
# in contract, strict liability, or tort (including negligence or
# otherwise) arising in any way out of the use of this software, even
# if advised of the possibility of such damage.
#

NAME = netopeer-cli
VERSION = 0.6.0
RELEASE = 1

IDGIT = "built from git $(shell git show --pretty=oneline | head -1 | cut -c -20)"
IDNOGIT = "released as version $(VERSION)"

srcdir = .
abs_srcdir = /home/ravi/netopeer/cli
prefix = /usr/local
exec_prefix = ${prefix}
bindir = ${exec_prefix}/bin
datarootdir = ${prefix}/share
mandir = ${datarootdir}/man
readlink = readlink

CC = gcc
LIBS = -lxml2 -lreadline -lnetconf  
CFLAGS = -Wall -I/usr/include/libxml2  -g -O0 -DDEBUG -pthread 
CPPFLAGS =  -DRCSID=\"$(IDGIT)\" -DENABLE_TLS -DVERSION=\"$(VERSION)\"
INSTALL = /usr/bin/install -c
INSTALL_PROGRAM = ${INSTALL}
INSTALL_DATA = ${INSTALL} -m 644

RPMBUILD = no
RPMDIR = RPMBUILD

INCLUDES=

ifeq "$(shell pwd)" "$(shell $(readlink) -f $(srcdir))"
OBJDIR= .obj
else
OBJDIR= .

endif

SRCS =  main.c \
	commands.c \
	configuration.c \
	mreadline.c

HDRS = 	commands.h \
	configuration.h \
	mreadline.h

OBJS = $(SRCS:%.c=$(OBJDIR)/%.o)

MANPAGES = doc/netopeer-cli.1
MANHTMLS = $(MANPAGES:%=%.html)

MANPATH=$(DESTDIR)$(mandir)/man$(subst .,,$(suffix $(1)))
define MANINSTALL
[ -d $(call MANPATH,$(1)) ] || \
	(mkdir -p $(call MANPATH,$(1)); \
	chmod 755 $(call MANPATH,$(1))); \
$(INSTALL_DATA) $(1) $(call MANPATH,$(1))/;
endef

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CPPFLAGS) $(CFLAGS) $(OBJS) $(LIBS) -o $(NAME)

.PHONY: static
static: $(OBJS)
	$(CC) $(CPPFLAGS) $(CFLAGS) $(OBJS) /home/test/usc-development/libnetconf/.libs/libnetconf.a -lreadline -lxml2 -lcurl -lssh2 -lxslt /home/test/usc-development/openssl/libssl.a  /home/test/usc-development/openssl/libcrypto.a -o $(NAME)

$(OBJDIR)/%.o: %.c
	@[ -d $$(dirname $@) ] || \
		(mkdir -p $$(dirname $@))
	$(CC) $(CFLAGS) $(INCLUDES) $(CPPFLAGS) -fPIC -c $< -o $@

%.1.html: %.1
	@if [ "no" = "no" ]; then \
		echo "Missing roff2html"; \
	else \
		no $< > $@; \
	fi

.PHONY: doc
doc: $(MANHTMLS)

.PHONY: tarball
tarball: $(SRCS) $(HEADERS) $(MANHTMLS)
	@rm -rf $(NAME)-$(VERSION);
	@mkdir $(NAME)-$(VERSION);
	for i in $(SRCS) $(HDRS) $(MANPAGES) $(MANHTMLS) configure.in configure \
	    Makefile.in VERSION $(NAME).spec.in \
	    install-sh config.sub config.guess; do \
	    [ -d $(NAME)-$(VERSION)/$$(dirname $$i) ] || (mkdir -p $(NAME)-$(VERSION)/$$(dirname $$i)); \
		cp $$i $(NAME)-$(VERSION)/$$i; \
	done; \
	@rm -rf $(RPMDIR)/SOURCES/; \
	mkdir -p $(RPMDIR)/SOURCES/; \
	tar -c -z -f $(RPMDIR)/SOURCES/$(NAME)-$(VERSION)-$(RELEASE).tar.gz \
	    $(NAME)-$(VERSION); \
	rm -rf $(NAME)-$(VERSION);

.PHONY: rpm
rpm: tarball
	if [ "$(RPMBUILD)" != "no" ]; then \
		mkdir -p $(RPMDIR)/BUILD $(RPMDIR)/RPMS $(RPMDIR)/SRPMS; \
		$(RPMBUILD) -ba $(NAME).spec \
			--define "_topdir `pwd`/$(RPMDIR)"; \
	else \
		echo "Missing rpmbuild"; \
		exit 1; \
	fi

.PHONY: install
install: $(NAME) $(MANPAGES) $(MANHTMLS)
	[ -d $(DESTDIR)/$(bindir) ] || \
		(mkdir -p $(DESTDIR)/$(bindir); chmod 755 $(DESTDIR)/$(bindir))
	$(INSTALL_PROGRAM) $(NAME) $(DESTDIR)/$(bindir)/;
	$(foreach man,$(MANPAGES),$(call MANINSTALL,$(man)))
	if test -n "$(MANHTMLS)"; then \
		[ -d $(DESTDIR)/$(datarootdir)/netopeer/ ] || \
			(mkdir -p $(DESTDIR)/$(datarootdir)/netopeer/; chmod 755 $(DESTDIR)/$(datarootdir)/netopeer/); \
	fi
	$(foreach man,$(MANHTMLS),$(INSTALL_DATA) $(man) $(DESTDIR)/$(datarootdir)/netopeer/)

.PHONY: uninstall
uninstall:
	rm -f $(DESTDIR)/$(bindir)/$(NAME);
	$(foreach man,$(MANPAGES),rm -rf $(call MANPATH,$(man))/$(notdir $(man)))
	$(foreach man,$(MANHTMLS),rm -rf $(DESTDIR)/$(datarootdir)/netopeer/$(notdir $(man)))

.PHONY: clean
clean:
	rm -rf $(NAME) .obj $(OBJS);

.PHONY: cleandoc
cleandoc:
	rm -rf $(MANHTMLS);
