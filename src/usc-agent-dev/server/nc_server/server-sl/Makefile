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

NAME = netopeer-server-sl
VERSION = 0.6.0
IDGIT = "built from git $(shell git show --pretty=oneline | head -1 | cut -c -20)"
IDNOGIT = "released as version $(VERSION)"

srcdir = .
abs_srcdir = /home/test/usc-development/netopeer/server-sl
prefix = /usr/local
exec_prefix = ${prefix}
bindir = ${exec_prefix}/bin
readlink = readlink
libtool = ./libtool

SETBIT = 0
SETUSER = 
SETGROUP = 
INSTALL_BIN_OPTIONS = 
SERVERCFG_PATH = $(DESTDIR)//var/lib/libnetconf/server/
CC = gcc
LIBS = -levent  -lnetconf -L/usr/local/lib -lnetconf   
CFLAGS = -Wall -I/usr/local/include    -O3 -pthread
CPPFLAGS =  -DRCSID=\"$(IDGIT)\" -I../../src/ -DSERVERCFG_PATH=\"$(SERVERCFG_PATH)\" -DVERSION=\"$(VERSION)\"
INSTALL = /usr/bin/install -c
INSTALL_PROGRAM = ${INSTALL}
INSTALL_DATA = ${INSTALL} -m 644
CONFIGURE_ARGS = @CONFIGURE_ARGS@
LIBTOOL = $(libtool) --tag=CC --quiet

INSTALL_BIN_OPTIONS = 
ifeq ($(SETBIT), 1)
INSTALL_BIN_OPTIONS = --mode=4755 --owner=$(SETUSER)
endif
ifeq ($(SETBIT), 2)
INSTALL_BIN_OPTIONS = --mode=2575 --group=$(SETGROUP)
endif
ifeq ($(SETBIT), 3)
INSTALL_BIN_OPTIONS = --mode=6775 --owner=$(SETUSER) --group=$(SETGROUP)
endif

INCLUDES = 

ifeq "$(shell pwd)" "$(shell $(readlink) -f $(srcdir))"
OBJDIR= .obj
else
OBJDIR= .

endif

SRCS =  main.c 

HDRS = 

OBJS = $(SRCS:%.c=$(OBJDIR)/%.o)

MODULE = ./toaster/
.PHONY: $(MODULE)

all: $(NAME) $(MODULE)

$(MODULE): $(MODULE)/Makefile 
	$(MAKE) -C $@

$(NAME): $(OBJS)
	$(CC) $(CPPFLAGS) $(CFLAGS) $(OBJS) $(LIBS) -o $(NAME)
	@if test "$$(($(SETBIT) & 1))" = "1"; then \
		chmod u+s $(NAME); \
	fi;
	@if test "$$(($(SETBIT) & 2))" = "2"; then \
		chmod g+s $(NAME); \
	fi;

.PHONY: static
static: $(OBJS)
	$(CC) $(CPPFLAGS) $(CFLAGS) $(OBJS) libnetconf.a -levent -o $(NAME)

$(OBJDIR)/%.o: %.c
	@[ -d $$(dirname $@) ] || \
		(mkdir -p $$(dirname $@))
	$(CC) $(CFLAGS) $(INCLUDES) $(CPPFLAGS) -fPIC -c $< -o $@

.PHONY: install
install: $(NAME) $(MODULE)
	@[ -d $(DESTDIR)/$(bindir) ] || \
		(mkdir -p $(DESTDIR)/$(bindir); chmod 755 $(DESTDIR)/$(bindir))
	$(INSTALL_PROGRAM) $(INSTALL_BIN_OPTIONS) $(NAME) $(DESTDIR)/$(bindir)/;
	@[ -d $(SERVERCFG_PATH) ] || \
		mkdir -p $(SERVERCFG_PATH);
	chmod -R 700 $(SERVERCFG_PATH);
	$(LIBTOOL) --mode=install cp $(MODULE)/toaster.la $(SERVERCFG_PATH)/;
	$(INSTALL_DATA) $(MODULE)/toaster.yin $(SERVERCFG_PATH)/;
	$(INSTALL_DATA) $(MODULE)/toaster-data.rng $(SERVERCFG_PATH)/;
	$(INSTALL_DATA) $(MODULE)/toaster-gdefs.rng $(SERVERCFG_PATH)/;
	$(INSTALL_DATA) $(MODULE)/toaster-schematron.xsl $(SERVERCFG_PATH)/;
	if test "$$(($(SETBIT) & 1))" = "1"; then \
		if test -n "$(SETUSER)"; then \
			chown -R $(SETUSER) $(SERVERCFG_PATH) || \
				echo "WARNING: invalid group $(SETUSER)"; \
		fi; \
	fi; \
	if test "$$(($(SETBIT) & 2))" = "2"; then \
		chmod -R g+rwx $(SERVERCFG_PATH); \
		if test -n "$(SETGROUP)"; then \
			chown -R :$(SETGROUP) $(SERVERCFG_PATH) || \
				echo "WARNING: invalid group $(SETGROUP)"; \
		fi; \
	fi; \
	if test "$(SETBIT)" = "0"; then \
		chmod -R a+rwx $(SERVERCFG_PATH); \
	fi;

.PHONY: uninstall
uninstall:
	rm -f $(DESTDIR)/$(bindir)/$(NAME);

.PHONY: clean
clean:
	$(MAKE) -C $(MODULE) clean ;
	rm -rf $(NAME) .obj $(OBJS);
