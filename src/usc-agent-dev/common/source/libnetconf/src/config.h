/**
 * \file config.h
 * \author Radek Krejci <rkrejci@cesnet.cz>
 * \brief Various configuration settings.
 *
 * Copyright (c) 2012-2014 CESNET, z.s.p.o.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in
 *    the documentation and/or other materials provided with the
 *    distribution.
 * 3. Neither the name of the Company nor the names of its contributors
 *    may be used to endorse or promote products derived from this
 *    software without specific prior written permission.
 *
 * ALTERNATIVELY, provided that this notice is retained in full, this
 * product may be distributed under the terms of the GNU General Public
 * License (GPL) version 2 or later, in which case the provisions
 * of the GPL apply INSTEAD OF those given above.
 *
 * This software is provided ``as is, and any express or implied
 * warranties, including, but not limited to, the implied warranties of
 * merchantability and fitness for a particular purpose are disclaimed.
 * In no event shall the company or contributors be liable for any
 * direct, indirect, incidental, special, exemplary, or consequential
 * damages (including, but not limited to, procurement of substitute
 * goods or services; loss of use, data, or profits; or business
 * interruption) however caused and on any theory of liability, whether
 * in contract, strict liability, or tort (including negligence or
 * otherwise) arising in any way out of the use of this software, even
 * if advised of the possibility of such damage.
 *
 */

#ifndef NC_CONFIG_H_
#define NC_CONFIG_H_

/*
 * If the compiler supports attribute to mark objects as hidden, mark all
 * objects as hidden and export only objects explicitly marked to be part of
 * the public API.
 */
#define API __attribute__((visibility("default")))

#ifndef DISABLE_LIBSSH
/*
 * libssh2_session_startup() is deprecated in libssh2 >= 1.2.8 and replaced by
 * libssh2_session_handshake(). This macro is automatically set by configure
 * script and appropriate function according to the current (in a compilation
 * time) libssh2 version is used.
 */
#define LIBSSH2_SESSION_HANDSHAKE(session,socket) libssh2_session_handshake(session,socket)

/*
 * libssh2_session_set_timeout() is available since libssh2 1.2.9
 */
#define LIBSSH2_SET_TIMEOUT(session,timeout) 

#else /* DISABLE_LIBSSH */

/* set path to the used ssh(1) application */
#define SSH_PROG ""

#endif /* not DISABLE_LIBSSH */

/*
 * Path for storing libnetconf's Event stream files
 */
//#define NCNTF_STREAMS_PATH "/var/lib/libnetconf//streams/"
#define NCNTF_STREAMS_PATH_ENV "LIBNETCONF_STREAMS"

/*
 * NACM
 */
#define NACM_RECOVERY_UID 0

/*
 * Compatibility section
 */
#define HAVE_EACCESS
#ifndef HAVE_EACCESS
int eaccess(const char *pathname, int mode);
#endif

#define HAVE_UTMPX_H

#define HAVE_XMLDOMWRAPRECONCILENAMESPACE

#endif /* NC_CONFIG_H_ */
