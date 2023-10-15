/*---------------------------------------------------------------
 * Copyright (c) 2021
 * Broadcom Corporation
 * All Rights Reserved.
 *---------------------------------------------------------------
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated
 * documentation files (the "Software"), to deal in the Software
 * without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute,
 * sublicense, and/or sell copies of the Software, and to permit
 * persons to whom the Software is furnished to do
 * so, subject to the following conditions:
 *
 *
 * Redistributions of source code must retain the above
 * copyright notice, this list of conditions and
 * the following disclaimers.
 *
 *
 * Redistributions in binary form must reproduce the above
 * copyright notice, this list of conditions and the following
 * disclaimers in the documentation and/or other materials
 * provided with the distribution.
 *
 *
 * Neither the name of Broadcom Coporation,
 * nor the names of its contributors may be used to endorse
 * or promote products derived from this Software without
 * specific prior written permission.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE CONTIBUTORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 * ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 * ________________________________________________________________
 *
 * gettcpinfo.c
 * Suppport for tcp info in a portable way
 *
 * by Robert J. McMahon (rjmcmahon@rjmcmahon.com, bob.mcmahon@broadcom.com)
 * -------------------------------------------------------------------
 */
#ifndef GETTCPINFO_H
#define GETTCPINFO_H

#include "headers.h"

#ifdef __cplusplus
extern "C" {
#endif

struct iperf_tcpstats {
    bool isValid;
    int rtt;
    double connecttime;
#if HAVE_TCP_STATS
    int cwnd;
    int rttvar;
    intmax_t retry;
    intmax_t retry_prev;
    intmax_t retry_tot;
    int mss_negotiated;
#endif
};

#if WIN32
void gettcpinfo(SOCKET sock, struct iperf_tcpstats *sample);
#else
void gettcpinfo(int sock, struct iperf_tcpstats *sample);
#endif
void tcpstats_copy (struct iperf_tcpstats *stats_dst, struct iperf_tcpstats *stats_src);

#ifdef __cplusplus
} /* end extern "C" */
#endif

#endif
