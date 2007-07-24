# Just a wild guess...
%define _requires_exceptions perl(English)\\|perl(SNMP)\\|perl(a)

%define snap	20041220

%define nsusr nagios
%define nsgrp nagios

Summary:	Host/service/network monitoring program plugins for Nagios
Name:		nagios-plugins
Version:	1.4.9
Release:	%mkrel 2
License:	GPL
Group:		Networking/Other
URL:		http://nagiosplug.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/nagiosplug/%{name}-%{version}.tar.gz
Patch0:		nagios-plugins-no_buggy_locales.diff
Patch1:		nagios-plugins-check_nmap_random_fix.diff
Patch2:		nagios-plugins-check_compaq_insight.diff
Patch3:		nagios-plugins-wireshark.diff
Patch4:		nagios-plugins-radiusclient-ng.diff
Patch5:		nagios-plugins-check_ide_smart.diff
Patch6:		nagios-plugins-contrib-API.patch
Patch7:		check_ipxping.diff
Patch8:		command.cfg.diff
Patch9:		nagios-plugins-check_ping-socket-filter-warning.diff
Requires(post): rpm-helper
Requires(preun): rpm-helper
# we seem to need zillions of requires and buildrequires, 
# well fine as long as it does the trick...
Requires:	apt
Requires:	bind-utils
Requires:	fileutils
Requires:	fping
Requires:	gawk
Requires:	grep
Requires:	net-snmp-utils
Requires:	ntp
Requires:	nut
Requires:	perl
Requires:	python
Requires:	samba-client
Requires:	shadow-utils
Requires:	textutils
Requires:	traceroute
Requires:	mrtg
Requires:	qstat
Requires:	tshark
Requires:	ipxping
BuildRequires:	cvs
BuildRequires:	MySQL-devel
BuildRequires:	autoconf2.5
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	bind-utils
BuildRequires:	fileutils
BuildRequires:	fping
BuildRequires:	gawk
BuildRequires:	gettext-devel
BuildRequires:	grep
BuildRequires:	libsasl-devel
BuildRequires:	net-snmp-utils
BuildRequires:	ntp
BuildRequires:	nut
BuildRequires:	openldap-devel
BuildRequires:	openssh-clients
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	postgresql-devel
BuildRequires:	python
BuildRequires:	radiusclient-ng-devel
BuildRequires:	samba-client
BuildRequires:	shadow-utils
BuildRequires:	textutils
BuildRequires:	traceroute
BuildRequires:	zlib-devel
BuildRequires:	file
BuildRequires:	nagios
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a Unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This package contains the basic plugins necessary for use with the
Nagios package.  This package should install cleanly on almost any
RPM-based system.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p0
%patch6 -p1
%patch7 -p0
%patch8 -p0
%patch9 -p0

# fix strange perms
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

# unpack the extra (not all) contrib packages
mkdir -p extra-plugins
pushd extra-plugins
tar -zxf ../contrib/tarballs/check_bgp-1.0.tar.gz
popd

%build
export WANT_AUTOCONF_2_5="1"
autopoint --force; aclocal -I gl/m4 -I m4; autoheader; automake --add-missing --force-missing --copy; autoconf

export PATH_TO_DIG=/usr/bin/dig
export PATH_TO_FPING=/bin/fping
export PATH_TO_HOST=/usr/bin/host
export PATH_TO_LMSTAT=
export PATH_TO_LSPS=
export PATH_TO_MAILQ=/usr/bin/mailq
export PATH_TO_NSLOOKUP=/usr/bin/nslookup
export PATH_TO_PING=/bin/ping
export PATH_TO_PING6=/usr/bin/ping6
export PATH_TO_PS=/bin/ps
export PATH_TO_QMAIL_QSTAT=/var/qmail/bin/qmail-qstat
export PATH_TO_QSTAT=/usr/bin/qstat-quake
export PATH_TO_QUAKESTAT=
export PATH_TO_RPCINFO=/usr/sbin/rpcinfo
export PATH_TO_SMBCLIENT=/usr/bin/smbclient
export PATH_TO_SNMPGET=/usr/bin/snmpget
export PATH_TO_SNMPGETNEXT=/usr/bin/snmpgetnext
export PATH_TO_SSH=/usr/bin/ssh
export PATH_TO_SWAP=
export PATH_TO_SWAPINFO=
export PATH_TO_UPTIME=/usr/bin/uptime
export PATH_TO_WHO=/usr/bin/who
export PATH_TO_APTGET=/usr/bin/apt-get

%serverbuild

%configure2_5x \
    --libexecdir=%{_libdir}/nagios/plugins \
    --disable-rpath \
    --with-cgiurl=/nagios/cgi-bin \
    --with-trusted-path="/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin" \
    --with-openssl=%{_prefix} \
    --with-pgsql=%{_prefix} \
    --with-mysql=%{_prefix} \
    --with-ping-command="/bin/ping -n -U -w %d -c %d %s" \
    --with-ping6-command="%{_bindir}/ping6 -n -U -w %d -c %d %s"

find . -type f -name "Makefile" -exec /usr/bin/perl -pi -e "s|-L/usr/lib|-L%{_libdir}|g" \{\} \;

# replace some bad paths
for i in `find contrib/ -type f`; do
    gawk -f `pwd`/plugins-scripts/subst $i > $i.sub
    mv $i.sub $i
    perl -pi -e "s|^#!/usr/local/bin/perl|#!%{_bindir}/perl|g;\
	s|^#!/bin/perl|#!%{_bindir}/perl|g;\
	s|^#!/nyet/bin/perl|#!%{_bindir}/perl|g;\
	s|^use lib \"%{_sbindir}/nagios\"|use lib \"%{_libdir}/nagios/plugins\"|g;\
	s|^use lib \"\"%{_libdir}/nagios/plugins\"\"|use lib \"%{_libdir}/nagios/plugins\"|g;\
	s|^use lib \"nagios/plugins\"|use lib \"%{_libdir}/nagios/plugins\"|g;\
	s|^use lib \"\"nagios/plugins\"\"|use lib \"%{_libdir}/nagios/plugins\"|g;\
	s|^use lib  \"\"nagios/plugins\"\"|use lib \"%{_libdir}/nagios/plugins\"|g;\
	s|\"nagios/plugins/\"|\"%{_libdir}/nagios/plugins/\"|g;\
	s|/opt/nagios/libexec|%{_libdir}/nagios/plugins|g;\
	s|/opt/nagios/etc|/etc/nagios|g;\
	s|/usr/libexec/nagios/plugins|%{_libdir}/nagios/plugins|g;\
	s|/usr/lib/nagios/plugins|%{_libdir}/nagios/plugins|g;\
	s|/usr/local/bin|%{_bindir}|g;\
	s|%{_sbindir}/nagios/plugins|%{_libdir}/nagios/plugins|g;\
	s|/usr/local/libexec/nagios|%{_libdir}/nagios/plugins|g;\
	s|/usr/local/nagios/bin/nagios|%{_bindir}/nagios|g;\
	s|/usr/local/nagios/etc|%{_sysconfdir}/nagios|g;\
	s|/usr/local/nagios/libexec|%{_libdir}/nagios/plugins|g;\
	s|/usr/local/nagios|%{_prefix}|g;\
	s|/usr/local/nagios/var|%{_var}/log/nagios|g;\
	s|/usr/local/netsaint/etc/tmp|/tmp|g;\
	s|/usr/local/netsaint/etc|/etc|g;\
	s|require \'nagios/plugins/utils.pm\'|require \'%{_libdir}/nagios/plugins/utils.pm\'|g" $i
done

#    --without-included-gettext \
#    --with-libintl-prefix=%{_prefix}

# anti recheck hack
touch *

# do this the hard way as it is not fool proof as is...
cat >> config.h << EOF
#define USE_IPV6 1
#define PING6_COMMAND "/usr/bin/ping6 -n -U -c %d %s"
#define PING6_PACKETS_FIRST 1
#define PING_COMMAND "/bin/ping -n -U -w %d -c %d %s"
#define PING_HAS_TIMEOUT 1
#define PING_PACKETS_FIRST 1
#define PS_COLS 8
#define PS_COMMAND "/bin/ps axwo 'stat uid ppid vsz rss pcpu comm args'"
#define PS_FORMAT "%s %d %d %d %d %f %s %n"
#define PS_VARLIST procstat,&procuid,&procppid,&procvsz,&procrss,&procpcpu,procprog,&pos
EOF

make \
    CPPFLAGS="-I%{_includedir}/ldap -I%{_includedir}/mysql -I%{_includedir}/pgsql -I%{_includedir}/openssl" \
    CFLAGS="$CFLAGS" \
    LDFLAGS="-L. -L%{_libdir}"

make -C plugins \
    CPPFLAGS="-I%{_includedir}/ldap -I%{_includedir}/mysql -I%{_includedir}/pgsql -I%{_includedir}/openssl" \
    CFLAGS="$CFLAGS" \
    LDFLAGS="-L. -L%{_libdir}" check_ide_smart check_ldap check_pgsql check_radius

gcc $CFLAGS -Llib -I. -Igl -Iplugins -Ilib -o contrib/check_cluster contrib/check_cluster2.c

gcc $CFLAGS -Llib -I. -Igl -Iplugins -Ilib -o contrib/check_rbl contrib/check_rbl.c \
    plugins/popen.o plugins/utils.o lib/utils_base.o plugins/netutils.o   

gcc $CFLAGS -Llib -I. -Igl -Iplugins -Ilib -o contrib/check_ipxping contrib/check_ipxping.c \
    plugins/popen.o plugins/utils.o lib/utils_base.o plugins/netutils.o   

gcc $CFLAGS -Llib -I. -Igl -Iplugins -Ilib -o contrib/check_timeout contrib/check_timeout.c

gcc $CFLAGS -Llib -I. -Igl -Iplugins -Ilib -o contrib/check_uptime contrib/check_uptime.c \
    plugins/popen.o plugins/utils.o lib/utils_base.o plugins/netutils.o   

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d -m0755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
install -d -m0755 %{buildroot}%{_libdir}/nagios/plugins/contrib

make AM_INSTALL_PROGRAM_FLAGS="" DESTDIR=%{buildroot} install

install -m0755 contrib/check* %{buildroot}%{_libdir}/nagios/plugins/contrib/
#install -m0755 plugins-scripts/check_oracle %{buildroot}%{_libdir}/nagios/plugins/contrib/

install -m0755 plugins/check_pgsql %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 plugins/check_radius %{buildroot}%{_libdir}/nagios/plugins/

# install the extra plugins
pushd extra-plugins
    install -m0755 check-bgp-1.0/check_bgp %{buildroot}%{_libdir}/nagios/plugins/contrib/
    cp check-bgp-1.0/README ../README.check-bgp
popd
cp contrib/README.TXT .

install -m0755 contrib/check_cluster %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_rbl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_ipxping %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_timeout %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_uptime %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 plugins/check_ide_smart %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 plugins-root/check_dhcp %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 plugins-root/check_icmp %{buildroot}%{_libdir}/nagios/plugins/

# forgotten
install -m0755 contrib/utils.py %{buildroot}%{_libdir}/nagios/plugins/contrib/utils.py
install -m0755 contrib/packet_utils.pm %{buildroot}%{_libdir}/nagios/plugins/contrib/

# instead of a patch
install -m0755 plugins-scripts/utils.sh %{buildroot}%{_libdir}/nagios/plugins/contrib/utils.sh

# install the config file
install -m0644 command.cfg %{buildroot}%{_sysconfdir}/nagios/command-old-style.cfg
%{_sbindir}/convertcfg command.cfg commands > %{buildroot}%{_sysconfdir}/nagios/plugins.d/%{name}.cfg

# don't ship dev files
rm %{buildroot}%{_libdir}/nagios/plugins/contrib/*.c

# house cleaning...
# we don't have any oracle stuff in Mandriva, so don't ship none...
rm -f %{buildroot}%{_libdir}/nagios/plugins/contrib/check_ora_table_space.pl
rm -f %{buildroot}%{_libdir}/nagios/plugins/contrib/check_oracle_instance.pl
rm -f %{buildroot}%{_libdir}/nagios/plugins/contrib/check_oracle.sh
rm -f %{buildroot}%{_libdir}/nagios/plugins/contrib/check_oracle_tbs
rm -f %{buildroot}%{_libdir}/nagios/plugins/contrib/check_cluster2.README

# this one is outdated
rm -f %{buildroot}%{_libdir}/nagios/plugins/contrib/check_rrd_data.pl

# these requires a "snmputil.pm" file that is no where to be found
rm -f %{buildroot}%{_libdir}/nagios/plugins/contrib/check_fan_cpq_present
rm -f %{buildroot}%{_libdir}/nagios/plugins/contrib/check_fan_fsc_present

# fix bad paths (again!)
for i in check_breeze check_disk_smb check_file_age check_flexlm check_ifoperstatus \
    check_ifstatus check_ircd check_mailq check_ntp check_rpc check_wave; do
    perl -pi -e "s|\"nagios/plugins\"|\"%{_libdir}/nagios/plugins\"|g" \
    %{buildroot}%{_libdir}/nagios/plugins/$i
done

# fix three remaining plugins
perl -pi -e "s|^use lib qw\(%{_libdir}/nagios/plugins\)|use lib qw\(%{_libdir}/nagios/plugins %{_libdir}/nagios/plugins/contrib\)|g" \
    %{buildroot}%{_libdir}/nagios/plugins/contrib/check_ica_metaframe_pub_apps.pl \
    %{buildroot}%{_libdir}/nagios/plugins/contrib/check_lotus.pl \
    %{buildroot}%{_libdir}/nagios/plugins/contrib/check_ica_master_browser.pl

%find_lang %{name}

%pre
%_pre_useradd %{nsusr} /var/log/nagios /bin/sh

%postun
%_postun_userdel %{nsusr}

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS CODING ChangeLog FAQ LEGAL NEWS README* REQUIREMENTS SUPPORT
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/command-old-style.cfg
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/%{name}.cfg
%defattr(0755,root,root)
%dir %{_libdir}/nagios/plugins
%dir %{_libdir}/nagios/plugins/contrib
# list them all so it's easier to see what's new/missing while building
%{_libdir}/nagios/plugins/check_apt
%{_libdir}/nagios/plugins/check_breeze
%{_libdir}/nagios/plugins/check_by_ssh
%{_libdir}/nagios/plugins/check_cluster
%{_libdir}/nagios/plugins/check_dig
%{_libdir}/nagios/plugins/check_disk
%{_libdir}/nagios/plugins/check_disk_smb
%{_libdir}/nagios/plugins/check_dns
%{_libdir}/nagios/plugins/check_dummy
%{_libdir}/nagios/plugins/check_file_age
%{_libdir}/nagios/plugins/check_flexlm
%{_libdir}/nagios/plugins/check_fping
%{_libdir}/nagios/plugins/check_ftp
%{_libdir}/nagios/plugins/check_hpjd
%{_libdir}/nagios/plugins/check_http
%{_libdir}/nagios/plugins/check_ide_smart
%{_libdir}/nagios/plugins/check_ifoperstatus
%{_libdir}/nagios/plugins/check_ifstatus
%{_libdir}/nagios/plugins/check_imap
%{_libdir}/nagios/plugins/check_ircd
%{_libdir}/nagios/plugins/check_jabber
%{_libdir}/nagios/plugins/check_ldap
%{_libdir}/nagios/plugins/check_ldaps
%{_libdir}/nagios/plugins/check_load
%{_libdir}/nagios/plugins/check_log
%{_libdir}/nagios/plugins/check_mailq
%{_libdir}/nagios/plugins/check_mrtg
%{_libdir}/nagios/plugins/check_mrtgtraf
%{_libdir}/nagios/plugins/check_mysql
%{_libdir}/nagios/plugins/check_nagios
%{_libdir}/nagios/plugins/check_nntp
%{_libdir}/nagios/plugins/check_nntps
%{_libdir}/nagios/plugins/check_nt
%{_libdir}/nagios/plugins/check_ntp
%{_libdir}/nagios/plugins/check_nwstat
%{_libdir}/nagios/plugins/check_oracle
%{_libdir}/nagios/plugins/check_overcr
%{_libdir}/nagios/plugins/check_pgsql
%{_libdir}/nagios/plugins/check_ping
%{_libdir}/nagios/plugins/check_pop
%{_libdir}/nagios/plugins/check_procs
%{_libdir}/nagios/plugins/check_radius
%{_libdir}/nagios/plugins/check_real
%{_libdir}/nagios/plugins/check_rpc
%{_libdir}/nagios/plugins/check_sensors
%{_libdir}/nagios/plugins/check_simap
%{_libdir}/nagios/plugins/check_smtp
%{_libdir}/nagios/plugins/check_snmp
%{_libdir}/nagios/plugins/check_spop
%{_libdir}/nagios/plugins/check_ssh
%{_libdir}/nagios/plugins/check_ssmtp
%{_libdir}/nagios/plugins/check_swap
%{_libdir}/nagios/plugins/check_tcp
%{_libdir}/nagios/plugins/check_time
%{_libdir}/nagios/plugins/check_udp
%{_libdir}/nagios/plugins/check_ups
%{_libdir}/nagios/plugins/check_users
%{_libdir}/nagios/plugins/check_wave
%{_libdir}/nagios/plugins/check_clamd
%{_libdir}/nagios/plugins/check_game
%{_libdir}/nagios/plugins/check_mysql_query
%{_libdir}/nagios/plugins/negate
%{_libdir}/nagios/plugins/urlize
%{_libdir}/nagios/plugins/utils.pm
%{_libdir}/nagios/plugins/utils.sh
%{_libdir}/nagios/plugins/contrib/check_adptraid.sh
%{_libdir}/nagios/plugins/contrib/check_apache.pl
%{_libdir}/nagios/plugins/contrib/check_apc_ups.pl
%{_libdir}/nagios/plugins/contrib/check_appletalk.pl
%{_libdir}/nagios/plugins/contrib/check_axis.sh
%{_libdir}/nagios/plugins/contrib/check_backup.pl
%{_libdir}/nagios/plugins/contrib/check_bgp
%{_libdir}/nagios/plugins/contrib/check_bgpstate.pl
%{_libdir}/nagios/plugins/contrib/check_breeze.pl
%{_libdir}/nagios/plugins/contrib/check_cluster
%{_libdir}/nagios/plugins/contrib/check_compaq_insight.pl
%{_libdir}/nagios/plugins/contrib/check_digitemp.pl
%{_libdir}/nagios/plugins/contrib/check_dlswcircuit.pl
%{_libdir}/nagios/plugins/contrib/check_dns_random.pl
%{_libdir}/nagios/plugins/contrib/check_email_loop.pl
%{_libdir}/nagios/plugins/contrib/check_flexlm.pl
%{_libdir}/nagios/plugins/contrib/check_hprsc.pl
%{_libdir}/nagios/plugins/contrib/check_hw.sh
%{_libdir}/nagios/plugins/contrib/check_inodes-freebsd.pl
%{_libdir}/nagios/plugins/contrib/check_inodes.pl
%{_libdir}/nagios/plugins/contrib/check_javaproc.pl
%{_libdir}/nagios/plugins/contrib/check_joy.sh
%{_libdir}/nagios/plugins/contrib/check_linux_raid.pl
%{_libdir}/nagios/plugins/contrib/check_lmmon.pl
%{_libdir}/nagios/plugins/contrib/check_log2.pl
%{_libdir}/nagios/plugins/contrib/check_maxchannels.pl
%{_libdir}/nagios/plugins/contrib/check_maxwanstate.pl
%{_libdir}/nagios/plugins/contrib/check_mem.pl
%{_libdir}/nagios/plugins/contrib/check_ms_spooler.pl
%{_libdir}/nagios/plugins/contrib/check_mssql.sh
%{_libdir}/nagios/plugins/contrib/check_nagios.pl
%{_libdir}/nagios/plugins/contrib/check_nagios_db.pl
%{_libdir}/nagios/plugins/contrib/check_nagios_db_pg.pl
%{_libdir}/nagios/plugins/contrib/check_netapp.pl
%{_libdir}/nagios/plugins/contrib/check_nmap.py
%{_libdir}/nagios/plugins/contrib/utils.py
%{_libdir}/nagios/plugins/contrib/utils.sh
%{_libdir}/nagios/plugins/contrib/check_qmailq.pl
%{_libdir}/nagios/plugins/contrib/check_remote_nagios_status.pl
%{_libdir}/nagios/plugins/contrib/check_sap.sh
%{_libdir}/nagios/plugins/contrib/check_smb.sh
%{_libdir}/nagios/plugins/contrib/check_snmp_disk_monitor.pl
%{_libdir}/nagios/plugins/contrib/check_snmp_printer.pl
%{_libdir}/nagios/plugins/contrib/check_snmp_process_monitor.pl
%{_libdir}/nagios/plugins/contrib/check_snmp_procs.pl
%{_libdir}/nagios/plugins/contrib/check_sockets.pl
%{_libdir}/nagios/plugins/contrib/check_vcs.pl
%{_libdir}/nagios/plugins/contrib/check_wave.pl
%{_libdir}/nagios/plugins/contrib/check_wins.pl
%{_libdir}/nagios/plugins/contrib/checkciscotemp.pl
%{_libdir}/nagios/plugins/contrib/check_arping.pl
%{_libdir}/nagios/plugins/contrib/check_asterisk.pl
#%{_libdir}/nagios/plugins/contrib/check_fan_cpq_present
#%{_libdir}/nagios/plugins/contrib/check_fan_fsc_present
%{_libdir}/nagios/plugins/contrib/check_frontpage
%{_libdir}/nagios/plugins/contrib/check_ica_master_browser.pl
%{_libdir}/nagios/plugins/contrib/check_ica_metaframe_pub_apps.pl
%{_libdir}/nagios/plugins/contrib/check_ica_program_neigbourhood.pl
%{_libdir}/nagios/plugins/contrib/check_lotus.pl
%{_libdir}/nagios/plugins/contrib/check_pcpmetric.py
%{_libdir}/nagios/plugins/contrib/check_pfstate
%{_libdir}/nagios/plugins/contrib/check_smart.pl
%{_libdir}/nagios/plugins/contrib/check_temp_cpq
%{_libdir}/nagios/plugins/contrib/check_temp_fsc
%{_libdir}/nagios/plugins/contrib/check_traceroute-pure_perl.pl
%{_libdir}/nagios/plugins/contrib/check_traceroute.pl
%{_libdir}/nagios/plugins/contrib/check_rbl
%{_libdir}/nagios/plugins/contrib/check_ipxping
%{_libdir}/nagios/plugins/contrib/check_timeout
%{_libdir}/nagios/plugins/contrib/check_uptime
%{_libdir}/nagios/plugins/contrib/packet_utils.pm
#%{_libdir}/nagios/plugins/contrib/check_ora_table_space.pl
#%{_libdir}/nagios/plugins/contrib/check_oracle_instance.pl
#%{_libdir}/nagios/plugins/contrib/check_oracle
#%{_libdir}/nagios/plugins/contrib/check_oracle_tbs
%attr(4550,root,root) %{_libdir}/nagios/plugins/check_dhcp
%attr(4550,root,root) %{_libdir}/nagios/plugins/check_icmp
