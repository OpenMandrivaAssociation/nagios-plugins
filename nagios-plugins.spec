# Just a wild guess...
%define _requires_exceptions perl(English)\\|perl(SNMP)\\|perl(a)

%define snap	20041220

%define nsusr nagios
%define nsgrp nagios
%define cmdusr apache
%define cmdgrp apache

Summary:	Host/service/network monitoring program plugins for Nagios
Name:		nagios-plugins
Version:	1.4.13
Release:	%mkrel 9
License:	GPL
Group:		Networking/Other
URL:		http://nagiosplug.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/nagiosplug/%{name}-%{version}.tar.gz
Source1:	http://www.consol.com/fileadmin/opensource/Nagios/check_mysql_perf-1.3.tar.gz
Source2:	nagios-plugins.cfg_do_not_use
Source101:	check_breeze.cfg
Source102:	check_by_ssh.cfg
Source103:	check_cluster.cfg
Source104:	check_dhcp.cfg
Source105:	check_dig.cfg
Source106:	check_disk.cfg
Source107:	check_disk_smb.cfg
Source108:	check_dns.cfg
Source109:	check_dummy.cfg
Source110:	check_file_age.cfg
Source111:	check_flexlm.cfg
Source112:	check_fping.cfg
Source113:	check_game.cfg
Source114:	check_hpjd.cfg
Source115:	check_http.cfg
Source116:	check_icmp.cfg
Source117:	check_ide_smart.cfg
Source118:	check_ifoperstatus.cfg
Source119:	check_ifstatus.cfg
Source120:	check_ircd.cfg
Source121:	check_ldap.cfg
Source122:	check_load.cfg
Source123:	check_log.cfg
Source124:	check_mailq.cfg
Source125:	check_mrtg.cfg
Source126:	check_mrtgtraf.cfg
Source127:	check_mysql.cfg
Source128:	check_mysql_query.cfg
Source129:	check_nagios.cfg
Source130:	check_nt.cfg
Source131:	check_ntp.cfg
Source132:	check_ntp_peer.cfg
Source133:	check_ntp_time.cfg
Source134:	check_nwstat.cfg
Source135:	check_oracle.cfg
Source136:	check_overcr.cfg
Source137:	check_pgsql.cfg
Source138:	check_ping.cfg
Source139:	check_procs.cfg
Source140:	check_radius.cfg
Source141:	check_real.cfg
Source142:	check_rpc.cfg
Source143:	check_sensors.cfg
Source144:	check_smtp.cfg
Source145:	check_snmp.cfg
Source146:	check_ssh.cfg
Source147:	check_swap.cfg
Source148:	check_tcp.cfg
Source149:	check_time.cfg
Source150:	check_ups.cfg
Source151:	check_users.cfg
Source152:	check_wave.cfg
#
Source200:	check_adptraid.cfg
Source201:	check_apache.cfg
Source202:	check_apc_ups.cfg
Source203:	check_appletalk.cfg
Source204:	check_arping.cfg
Source205:	check_asterisk.cfg
Source206:	check_axis.cfg
Source207:	check_backup.cfg
Source208:	check_bgp.cfg
Source209:	check_bgpstate.cfg
Source210:	check_ciscotemp.cfg
Source211:	check_cluster2.cfg
Source212:	check_compaq_insight.cfg
Source213:	check_digitemp.cfg
Source214:	check_dlswcircuit.cfg
Source215:	check_dns_random.cfg
Source216:	check_email_loop.cfg
Source217:	check_frontpage.cfg
Source218:	check_hprsc.cfg
Source219:	check_hw.cfg
Source220:	check_ica_master_browser.cfg
Source221:	check_ica_metaframe_pub_apps.cfg
Source222:	check_ica_program_neigbourhood.cfg
Source223:	check_inodes.cfg
Source224:	check_ipxping.cfg
Source225:	check_javaproc.cfg
Source226:	check_linux_raid.cfg
Source227:	check_log2.cfg
Source228:	check_lotus.cfg
Source229:	check_maxchannels.cfg
Source230:	check_maxwanstate.cfg
Source231:	check_mem.cfg
Source232:	check_mrtgext.cfg
Source233:	check_ms_spooler.cfg
Source234:	check_mssql.cfg
Source235:	check_netapp.cfg
Source236:	check_nmap.cfg
Source237:	check_pcpmetric.cfg
Source238:	check_pfstate.cfg
Source239:	check_qmailq.cfg
Source240:	check_rbl.cfg
Source241:	check_remote_nagios_status.cfg
Source242:	check_sendim.cfg
Source243:	check_smart.cfg
Source244:	check_smb.cfg
Source245:	check_snmp_disk_monitor.cfg
Source246:	check_snmp_printer.cfg
Source247:	check_snmp_process_monitor.cfg
Source248:	check_snmp_procs.cfg
Source249:	check_sockets.cfg
Source250:	check_timeout.cfg
Source251:	check_traceroute.cfg
Source252:	check_uptime.cfg
Source253:	check_wins.cfg
#
Source300:	check_mysql_perf.cfg
#
Patch0:		nagios-plugins-1.4.13-no-buggy-locales.diff
Patch1:		nagios-plugins-check_compaq_insight.diff
Patch2:		nagios-plugins-wireshark.diff
Patch3:		nagios-plugins-contrib-API.patch
Patch4:		nagios-plugins-check_ipxping.diff
Patch5:		command.cfg.diff
Patch6:		nagios-plugins-check_ping-socket-filter-warning.diff
Patch7:		nagios-plugins-command.cfg.in.typo.diff
Patch8:		nagios-plugins-command.cfg.in.bindir.diff
Patch9:		nagios-plugins-check_backup.pl_fix.diff
Patch10:	nagios-plugins-check_email_loop.pl_fix.diff
Patch11:	nagios-plugins-check_ica_program_neigbourhood.pl_fix.diff
Patch12:	nagios-plugins-check_log2.pl_fix.diff
Patch13:	nagios-plugins-check_ms_spooler.pl_fix.diff
Patch14:	nagios-plugins-check_traceroute.pl_fix.diff
Patch15:	nagios-plugins-check_appletalk.pl_fix.diff
Patch16:	nagios-plugins-check_mssql.sh_fix.diff
Patch17:	nagios-plugins-check_nmap.py_fix.diff
Patch18:	nagios-plugins-check_inodes.pl_fix.diff
Patch19:	nagios-plugins-utils.pm_fix.diff
# http://sourceforge.net/tracker/index.php?func=detail&aid=1854415&group_id=29880&atid=397599
Patch21:	nagios-plugins-1.4.13-check_dhcp-roguedhcpservercheck.diff
# http://sourceforge.net/tracker/?func=detail&atid=397599&aid=2430999&group_id=29880
Patch22:	nagios-plugins-1.4.13-check_ldap_certificate.patch
# http://sourceforge.net/tracker/index.php?func=detail&aid=1939022&group_id=29880&atid=397599
Patch23:	nagios-plugins-1.4.13-sni-support.patch
#
Patch300:	nagios-plugins-check_mysql_perf.diff
Patch301:	check_mysql_perf-no_buggy_locales.diff
Requires(post): rpm-helper
Requires(preun): rpm-helper
# we seem to need zillions of requires and buildrequires, 
# well fine as long as it does the trick...
Requires:	coreutils
Requires:	gawk
Requires:	grep
Requires:	perl
Requires:	shadow-utils
BuildRequires:	cvs
BuildRequires:	mysql-devel
BuildRequires:	autoconf2.5
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	bind-utils
BuildRequires:	coreutils
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
BuildRequires:	traceroute
BuildRequires:	zlib-devel
BuildRequires:	file
Epoch:		1
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Nagios is a program that will monitor hosts and services on your network, and
to email or page you when a problem arises or is resolved. Nagios runs on a
Unix server as a background or daemon process, intermittently running checks on
various services that you specify. The actual service checks are performed by
separate "plugin" programs which return the status of the checks to Nagios.

This package contains the basic plugins necessary for use with the Nagios
package.  This package should install cleanly on almost any RPM-based system.

%package -n	nagios-check_breeze
Summary:	The check_breeze plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_breeze
This plugin reports the signal strength of a Breezecom wireless equipment

%package -n	nagios-check_by_ssh
Summary:	The check_by_ssh plugin for nagios
Group:		Networking/Other
Requires:	nagios-check_disk
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_by_ssh
This plugin uses SSH to execute commands on a remote host.

%package -n	nagios-check_cluster
Summary:	The check_cluster plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_cluster
This package contains the check_cluster plugin for nagios.

%package -n	nagios-check_dhcp
Summary:	The check_dhcp plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_dhcp
This plugin tests the availability of DHCP servers on a network.

%package -n	nagios-check_dig
Summary:	The check_dig plugin for nagios
Group:		Networking/Other
Requires:	bind-utils
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_dig
This plugin test the DNS service on the specified host using dig

%package -n	nagios-check_disk
Summary:	The check_disk plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_disk
This plugin checks the amount of used disk space on a mounted file system and
generates an alert if free space is less than one of the threshold values

%package -n	nagios-check_disk_smb
Summary:	The check_disk_smb plugin for nagios
Group:		Networking/Other
Requires:	samba-client
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_disk_smb
Perl Check SMB Disk plugin for Nagios

%package -n	nagios-check_dns
Summary:	The check_dns plugin for nagios
Group:		Networking/Other
Requires:	bind-utils
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_dns
This plugin uses the nslookup program to obtain the IP address for the given
host/domain query. An optional DNS server to use may be specified. If no DNS
server is specified, the default server(s) specified in /etc/resolv.conf will
be used.

%package -n	nagios-check_dummy
Summary:	The check_dummy plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_dummy
This plugin will simply return the state corresponding to the numeric value
of the <state> argument with optional text

%package -n	nagios-check_file_age
Summary:	The check_file_age plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_file_age
This package contains the check_file_age plugin for nagios.

%package -n	nagios-check_flexlm
Summary:	The check_flexlm plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_flexlm
Check available flexlm license managers.

%package -n	nagios-check_fping
Summary:	The check_fping plugin for nagios
Group:		Networking/Other
Requires:	fping
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_fping
This plugin will use the fping command to ping the specified host for a fast
check Note that it is necessary to set the suid flag on fping.

%package -n	nagios-check_game
Summary:	The check_game plugin for nagios
Group:		Networking/Other
Requires:	qstat
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_game
This plugin tests game server connections with the specified host.

%package -n	nagios-check_hpjd
Summary:	The check_hpjd plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_hpjd
This plugin tests the STATUS of an HP printer with a JetDirect card. Net-snmp
must be installed on the computer running the plugin.

%package -n	nagios-check_http
Summary:	The check_http plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_http
This plugin tests the HTTP service on the specified host. It can test normal
(http) and secure (https) servers, follow redirects, search for strings and
regular expressions, check connection times, and report on certificate
expiration times.

%package -n	nagios-check_icmp
Summary:	The check_icmp plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_icmp
This package contains the check_icmp plugin for nagios.

%package -n	nagios-check_ide_smart
Summary:	The check_ide_smart plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ide_smart
This plugin checks a local hard drive with the (Linux specific) SMART interface
[http://smartlinux.sourceforge.net/smart/index.php].

%package -n	nagios-check_ifoperstatus
Summary:	The check_ifoperstatus plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ifoperstatus
check_ifoperstatus plugin for Nagios monitors operational status of a
particular network interface on the target host.

%package -n	nagios-check_ifstatus
Summary:	The check_ifstatus plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ifstatus
check_ifstatus plugin for Nagios monitors operational status of each network
interface on the target host.

%package -n	nagios-check_ircd
Summary:	The check_ircd plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ircd
Perl Check IRCD plugin for Nagios

%package -n	nagios-check_ldap
Summary:	The check_ldap plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ldap
This package contains the check_ldap plugin for nagios.

%package -n	nagios-check_load
Summary:	The check_load plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_load
This plugin tests the current system load average.

%package -n	nagios-check_log
Summary:	The check_log plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_log
Log file pattern detector plugin for Nagios

%package -n	nagios-check_mailq
Summary:	The check_mailq plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_mailq
Checks the number of messages in the mail queue (supports multiple sendmail
queues, qmail)

%package -n	nagios-check_mrtg
Summary:	The check_mrtg plugin for nagios
Group:		Networking/Other
Requires:	mrtg
Obsoletes:	nagios-mrtg
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_mrtg
This plugin will check either the average or maximum value of one of the two
variables recorded in an MRTG log file.

%package -n	nagios-check_mrtgtraf
Summary:	The check_mrtgtraf plugin for nagios
Group:		Networking/Other
Requires:	mrtg
Obsoletes:	nagios-mrtg
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_mrtgtraf
This plugin will check the incoming/outgoing transfer rates of a router,
switch, etc recorded in an MRTG log. If the newest log entry is older than
<expire_minutes>, a WARNING status is returned. If either the incoming or
outgoing rates exceed the <icl> or <ocl> thresholds (in Bytes/sec), a CRITICAL
status results. If either of the rates exceed the <iwl> or <owl> thresholds
(in Bytes/sec), a WARNING status results.

%package -n	nagios-check_mysql
Summary:	The check_mysql plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_mysql
This program tests connections to a mysql server.

%package -n	nagios-check_mysql_query
Summary:	The check_mysql_query plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_mysql_query
This program checks a query result against threshold levels.

%package -n	nagios-check_nagios
Summary:	The check_nagios plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_nagios
This plugin checks the status of the Nagios process on the local machine. The
plugin will check to make sure the Nagios status log is no older than the
number of minutes specified by the expires option. It also checks the process
table for a process matching the command argument.

%package -n	nagios-check_nt
Summary:	The check_nt plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_nt
This plugin collects data from the NSClient service running on a Windows(tm)
NT/2000/XP/2003 server.

%package -n	nagios-check_ntp
Summary:	The check_ntp plugin for nagios
Group:		Networking/Other
Requires:	ntp
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ntp
This plugin checks the selected ntp server.

%package -n	nagios-check_ntp_peer
Summary:	The check_ntp_peer plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ntp_peer
This plugin checks the selected ntp server.

%package -n	nagios-check_ntp_time
Summary:	The check_ntp_time plugin for nagios
Group:		Networking/Other
Requires:	ntp
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ntp_time
This plugin checks the clock offset with the ntp server.

%package -n	nagios-check_nwstat
Summary:	The check_nwstat plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_nwstat
This plugin attempts to contact the MRTGEXT NLM running on a Novell server
to gather the requested system information.

%package -n	nagios-check_oracle
Summary:	The check_oracle plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_oracle
Check Oracle status.

%package -n	nagios-check_overcr
Summary:	The check_overcr plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_overcr
This plugin attempts to contact the Over-CR collector daemon running on the
remote UNIX server in order to gather the requested system information.

%package -n	nagios-check_pgsql
Summary:	The check_pgsql plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_pgsql
Test whether a PostgreSQL Database is accepting connections.

%package -n	nagios-check_ping
Summary:	The check_ping plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ping
Use ping to check connection statistics for a remote host.

%package -n	nagios-check_procs
Summary:	The check_procs plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_procs
Checks all processes and generates WARNING or CRITICAL states if the specified
metric is outside the required threshold ranges. The metric defaults to number
of processes.  Search filters can be applied to limit the processes to check.

%package -n	nagios-check_radius
Summary:	The check_radius plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_radius
Tests to see if a radius server is accepting connections.

%package -n	nagios-check_real
Summary:	The check_real plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_real
This plugin tests the REAL service on the specified host.

%package -n	nagios-check_rpc
Summary:	The check_rpc plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_rpc
Check if a rpc service is registered and running using:
rpcinfo -H host -C rpc_command 

%package -n	nagios-check_sensors
Summary:	The check_sensors plugin for nagios
Group:		Networking/Other
Requires:	lm_sensors
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_sensors
This plugin checks hardware status using the lm_sensors package.

%package -n	nagios-check_smtp
Summary:	The check_smtp plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_smtp
This plugin will attempt to open an SMTP connection with the host.

%package -n	nagios-check_snmp
Summary:	The check_snmp plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_snmp
Check status of remote machines and obtain sustem information via SNMP.

%package -n	nagios-check_ssh
Summary:	The check_ssh plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ssh
Try to connect to an SSH server at specified server and port.

%package -n	nagios-check_swap
Summary:	The check_swap plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_swap
Check swap space on local machine.

%package -n	nagios-check_tcp
Summary:	The check_tcp plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_tcp
This plugin tests TCP connections with the specified host (or unix socket).

%package -n	nagios-check_time
Summary:	The check_time plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_time
This plugin will check the time on the specified host.

%package -n	nagios-check_ups
Summary:	The check_ups plugin for nagios
Group:		Networking/Other
Requires:	nut
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ups
This plugin tests the UPS service on the specified host.Network UPS Tools 
from www.networkupstools.org must be running for thisplugin to work.

%package -n	nagios-check_users
Summary:	The check_users plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_users
This plugin checks the number of users currently logged in on the local
system and generates an error if the number exceeds the thresholds specified.

%package -n	nagios-check_wave
Summary:	The check_wave plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_wave
This package contains the check_wave plugin for nagios.

%package -n	nagios-check_adptraid
Summary:	The check_adptraid plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_adptraid
This plugin checks alarm status of Adaptec 3200S RAID controller.

%package -n	nagios-check_apache
Summary:	The check_apache plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_apache
This plugin checks the apache HTTP service on the specified host. It uses the
mod_status facilities provided by the apache server. The monitoring server must
be authorized in httpd.conf.

%package -n	nagios-check_apc_ups
Summary:	The check_apc_ups plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_apc_ups
This plugin reports the status of an APC UPS equipped with an SNMP management
module.

%package -n	nagios-check_appletalk
Summary:	The check_appletalk plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_appletalk
Check if an atalkhost responds to an atalk echo using:

aecho -c <packets> <atalkhost>

%package -n	nagios-check_arping
Summary:	The check_arping plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_arping
check_arping pings hosts that normally wouldn't allow ICMP packets but are
still on the local network.

%package -n	nagios-check_asterisk
Summary:	The check_asterisk plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_asterisk
The check_asterisk plugin for nagios.

%package -n	nagios-check_axis
Summary:	The check_axis plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_axis
Check_axis checks the status of LPT ports on Axis print servers.

%package -n	nagios-check_backup
Summary:	The check_backup plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_backup
Checks a directory to see if at least one file was created within a specified
period of time that is of equal to or greater than a given size.

%package -n	nagios-check_bgp
Summary:	The check_bgp plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_bgp
Cisco BGP Session Checker. This little perl script logs into a Cisco router and
does a "sh ip bgp summary" to collect te bgp session status. (This script works
only if you use the "aaa newmodel athentification")

%package -n	nagios-check_bgpstate
Summary:	The check_bgpstate plugin for nagios
Group:		Networking/Other
Requires:	whois
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_bgpstate
Perl bgpstate plugin for Nagios. Monitors all BGP sessions

%package -n	nagios-check_ciscotemp
Summary:	The check_ciscotemp plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ciscotemp
Perl envmon temperature plugin for Nagios.

%package -n	nagios-check_cluster2
Summary:	The check_cluster2 plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_cluster2
Host/Service Cluster Plugin for Nagios.

%package -n	nagios-check_compaq_insight
Summary:	The check_compaq_insight plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_compaq_insight
This plugin checks the Compaq Insight Management agents system status via SNMP
on the specified host.

%package -n	nagios-check_digitemp
Summary:	The check_digitemp plugin for nagios
Group:		Networking/Other
Requires:	digitemp
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_digitemp
This is a Nagios plugin script to check the temperature on a local machine.
Remote usage may be possible with SSH.

%package -n	nagios-check_dlswcircuit
Summary:	The check_dlswcircuit plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_dlswcircuit
Missing arguments!
Perl Check Cisco Dlsw Circuit State plugin for Nagios.

%package -n	nagios-check_dns_random
Summary:	The check_dns_random plugin for nagios
Group:		Networking/Other
Requires:	nagios-check_dns
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_dns_random
This script will check to see if dns resolves hosts randomly from a list using
the check_dns plugin. 

%package -n	nagios-check_email_loop
Summary:	The check_email_loop plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_email_loop
This script sends a mail with a specific id in the subject via an given
smtp-server to a given email-adress. When the script is run again, it checks
for this Email (with its unique id) on a given pop3 account and sends another
mail.

%package -n	nagios-check_frontpage
Summary:	The check_frontpage plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_frontpage
Check that FrontPage extensions appear to be working on a specified host.
Currently only checks that the hit counter is not returning an error.

Probably not a good idea to use this on a host that someone's counting the hits
on, so create a separate vhost for frontpage extensions testing, or just
install the extensions on the default/root host for your server, and point it
against that hostname, running it against all vhosts on a server is probably
rather wasteful.

FrontPage remains a copyright/trademark of Microsoft Corporation.

%package -n	nagios-check_hprsc
Summary:	The check_hprsc plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_hprsc
Nagios plug-in that monitors the resources on an HP-UX machine by querying the
SNMP daemon.

%package -n	nagios-check_hw
Summary:	The check_hw plugin for nagios
Group:		Networking/Other
Requires:	hwinfo
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_hw
This plugin checks hardware changes.

%package -n	nagios-check_ica_master_browser
Summary:	The check_ica_master_browser plugin for nagios
Group:		Networking/Other
Requires:	tshark
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ica_master_browser
Perl Check Citrix Master Browser plugin for Nagios.

%package -n	nagios-check_ica_metaframe_pub_apps
Summary:	The check_ica_metaframe_pub_apps plugin for nagios
Group:		Networking/Other
Requires:	tshark
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ica_metaframe_pub_apps
Perl Check Citrix plugin for Nagios.

%package -n	nagios-check_ica_program_neigbourhood
Summary:	The check_ica_program_neigbourhood plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ica_program_neigbourhood
Check the Citrix Metaframe XP service by completing an HTTP dialogue with a
Program Neigbourhood server (pn_server) that returns an ICA server in the named
Server farm hosting the specified applications (an ICA server in a farm which
runs some MS app).

%package -n	nagios-check_inodes
Summary:	The check_inodes plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_inodes
This plugin uses df to gather filesystem statistics and check the percent used
of inodes.

%package -n	nagios-check_ipxping
Summary:	The check_ipxping plugin for nagios
Group:		Networking/Other
Requires:	ipxping
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ipxping
This plugin will use the ipxping command to ping the specified host using the
IPX protocol. IPX support must be compiled into the kernel and your host must
be correctly configured to use IPX before this plugin will work!

%package -n	nagios-check_javaproc
Summary:	The check_javaproc plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_javaproc
Perl Check java processes plugin for Nagios.

%package -n	nagios-check_linux_raid
Summary:	The check_linux_raid plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_linux_raid
The check_linux_raid plugin for nagios.

%package -n	nagios-check_log2
Summary:	The check_log2 plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_log2
Scan arbitrary log files for regular expression matches.

%package -n	nagios-check_lotus
Summary:	The check_lotus plugin for nagios
Group:		Networking/Other
Requires:	tshark
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_lotus
Perl Check Lotus Notes plugin for Nagios.

%package -n	nagios-check_maxchannels
Summary:	The check_maxchannels plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_maxchannels
Perl Check maxchannels plugin for Nagios. Monitors ISDN lines and modems on
Ascend MAX 2000/4000/6000/TNT

%package -n	nagios-check_maxwanstate
Summary:	The check_maxwanstate plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_maxwanstate
Perl Check maxwanstate plugin for Nagios. Monitors E1/T1 interface status.

%package -n	nagios-check_mem
Summary:	The check_mem plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_mem
The check_mem plugin for nagios.

%package -n	nagios-check_mrtgext
Summary:	The check_mrtgext plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_mrtgext
A UNIX counterpart to Jim Drews' MRTG Extension for netware servers Mimics
output of mrtgext.nlm using output of various standard UNIX programs (df,
uptime, and uname)

%package -n	nagios-check_ms_spooler
Summary:	The check_ms_spooler plugin for nagios
Group:		Networking/Other
Requires:	samba-client
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_ms_spooler
Primitive and in need of refinement test of MS spooler (with smbclient)

%package -n	nagios-check_mssql
Summary:	The check_mssql plugin for nagios
Group:		Networking/Other
Requires:	freetds
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_mssql
Checks Microsoft(tm) SQL Server connectivity. It works with versions 7 and
2000.

%package -n	nagios-check_netapp
Summary:	The check_netapp plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_netapp
Perl NetApp filer plugin for Nagios.

%package -n	nagios-check_nmap
Summary:	The check_nmap plugin for nagios
Group:		Networking/Other
Requires:	nmap
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_nmap
Does a nmap scan, compares open ports to those given on command-line. Reports
warning for closed that should be open and error for open that should be
closed. If optional ports are given, no warning is given if they are closed and
they are included in the list of valid ports.

%package -n	nagios-check_pcpmetric
Summary:	The check_pcpmetric plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_pcpmetric
Nagios client for checking Performance Co-Pilot metrics.

%package -n	nagios-check_pfstate
Summary:	The check_pfstate plugin for nagios
Group:		Networking/Other
Requires:	openssh-clients
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_pfstate
This plugin checks the number of state table entries on a PF-enabled OpenBSD
system.

%package -n	nagios-check_qmailq
Summary:	The check_qmailq plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_qmailq
This plugin allows you to check the number of Mails in a qmail-queue.

%package -n	nagios-check_rbl
Summary:	The check_rbl plugin for nagios
Group:		Networking/Other
Requires:	bind-utils
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_rbl
This plugin uses dig to test whether the specified host is on any RBL lists.

%package -n	nagios-check_remote_nagios_status
Summary:	The check_remote_nagios_status plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_remote_nagios_status
This plugin parses through the Nagios status log and will return a Critical,
Warning, or Unknown state depending on the number of Critical, Warning,
and/or Unknown services found in the log (or Down/Unreachable hosts when
matching against hosts)  

%package -n	nagios-check_sendim
Summary:	The check_sendim plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_sendim
Nagios plugin to send notifications using instant messages through a jabber
server.

%package -n	nagios-check_smart
Summary:	The check_smart plugin for nagios
Group:		Networking/Other
Requires:	smartmontools
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_smart
Check S.M.A.R.T. enabled disks status. This uses smartmontools to check for
disk status.

%package -n	nagios-check_smb
Summary:	The check_smb plugin for nagios
Group:		Networking/Other
Requires:	samba-client
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_smb
Samba status check.

%package -n	nagios-check_snmp_disk_monitor
Summary:	The check_snmp_disk_monitor plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_snmp_disk_monitor
SNMP Disk Monitor plugin for Nagios.

%package -n	nagios-check_snmp_printer
Summary:	The check_snmp_printer plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_snmp_printer
check_snmp_printer - check for printer status via snmp. Supports both standard
PRINT-MIB (RFC-1759) and HP Enterprise print-mib that is supported by some of
the older JetDirect interfaces.

%package -n	nagios-check_snmp_process_monitor
Summary:	The check_snmp_process_monitor plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_snmp_process_monitor
SNMP Process Monitor plugin for Nagios.

%package -n	nagios-check_snmp_procs
Summary:	The check_snmp_procs plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_snmp_procs
Check if processes are running on a host via snmp.

%package -n	nagios-check_sockets
Summary:	The check_sockets plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_sockets
This script will check to see how may open sockets a server has and waron
respectivly.

%package -n	nagios-check_timeout
Summary:	The check_timeout plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_timeout
This 'plugin' - if you want to call it that - doesn't do anything. It just
stays in a loop forever and never exits, and is therefore useful for testing
service and host check timeouts in Nagios. You must supply at least one
argument on the command line in order to activate the loop.

%package -n	nagios-check_traceroute
Summary:	The check_traceroute plugin for nagios
Group:		Networking/Other
Requires:	traceroute
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_traceroute
This plugin checks whether traceroute to the destination succeeds and if so
that the route string option (-R) matches the list of routers returned by
traceroute.

%package -n	nagios-check_uptime
Summary:	The check_uptime plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_uptime
This plugin parses the output from "uptime", tokenizing it with ',' as the
delimiter. Returning only the number of days and/or the hours and minutes a
machine has been up and running.

%package -n	nagios-check_wins
Summary:	The check_wins plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-plugins < 1:1.4.11-3

%description -n	nagios-check_wins
Perl Check WINS plugin for Nagios.

%package -n	nagios-check_mysql_perf
Summary:	The check_mysql_perf plugin for nagios
Group:		Networking/Other
URL:		http://www.consol.com/opensource/nagios/check-mysql-perf

%description -n	nagios-check_mysql_perf
A plugin for Nagios that allows you to monitor various performance-related
characteristics of a MySQL database.

%prep

%setup -q -n %{name}-%{version} -a1
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p0
%patch12 -p0
%patch13 -p0
%patch14 -p0
%patch15 -p0
%patch16 -p0
%patch17 -p0
%patch18 -p0
%patch19 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

%patch300 -p0
pushd check_mysql_perf*
%patch301 -p0
cp -p plugins/check_mysql_perf.c plugins/my_utils.h ../plugins/
popd

# fix strange perms
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

# unpack the extra (not all) contrib packages
mkdir -p extra-plugins
pushd extra-plugins
tar -zxf ../contrib/tarballs/check_bgp-1.0.tar.gz
popd


%build
autoreconf -fi

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
    --with-ping6-command="%{_bindir}/ping6 -n -U -w %d -c %d %s" \
    --with-ps-command="/bin/ps axwo 'stat uid pid ppid vsz rss pcpu etime comm args'" \
    --with-ps-format="%s %d %d %d %d %d %f %s %s %n" \
    --with-ps-varlist='procstat,&procuid,&procpid,&procppid,&procvsz,&procrss,&procpcpu,&procetime,procprog,&pos' \
    --with-ps-cols=10 \
    --with-ipv6

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
	s|^use lib  \"\"utils\.pm\"\"|use lib \"%{_libdir}/nagios/plugins/utils\.pm\"|g;\
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

make \
    CPPFLAGS="-I%{_includedir}/ldap -I%{_includedir}/mysql -I%{_includedir}/pgsql -I%{_includedir}/openssl" \
    CFLAGS="$CFLAGS" \
    LDFLAGS="-L. -L%{_libdir}"

make -C plugins \
    CPPFLAGS="-I%{_includedir}/ldap -I%{_includedir}/mysql -I%{_includedir}/pgsql -I%{_includedir}/openssl" \
    CFLAGS="$CFLAGS" \
    LDFLAGS="-L. -L%{_libdir}" check_ide_smart check_ldap check_pgsql check_radius

gcc $CFLAGS -Llib -I. -Igl -Iplugins -Ilib -o contrib/check_cluster2 contrib/check_cluster2.c

gcc $CFLAGS -Llib -I. -Igl -Iplugins -Ilib -o contrib/check_rbl contrib/check_rbl.c \
    plugins/popen.o plugins/utils.o lib/utils_base.o plugins/netutils.o   

gcc $CFLAGS -Llib -I. -Igl -Iplugins -Ilib -o contrib/check_ipxping contrib/check_ipxping.c \
    plugins/popen.o plugins/utils.o lib/utils_base.o plugins/netutils.o   

gcc $CFLAGS -Llib -I. -Igl -Iplugins -Ilib -o contrib/check_timeout contrib/check_timeout.c

gcc $CFLAGS -Llib -I. -Igl -Iplugins -Ilib -o contrib/check_uptime contrib/check_uptime.c \
    plugins/popen.o plugins/utils.o lib/utils_base.o plugins/netutils.o   

%install
rm -rf %{buildroot}

install -d -m0755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
install -d -m0755 %{buildroot}%{_libdir}/nagios/plugins/contrib

make AM_INSTALL_PROGRAM_FLAGS="" DESTDIR=%{buildroot} install

install -m0755 plugins/check_pgsql %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 plugins/check_radius %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 plugins/check_ide_smart %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 plugins-root/check_dhcp %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 plugins-root/check_icmp %{buildroot}%{_libdir}/nagios/plugins/

# scripts
install -m0755 contrib/check_adptraid.sh %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_apache.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_apc_ups.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_appletalk.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_arping.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_asterisk.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_axis.sh %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_backup.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_bgpstate.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/checkciscotemp.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/check_ciscotemp.pl
install -m0755 contrib/check_compaq_insight.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_digitemp.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_dlswcircuit.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_dns_random.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_email_loop.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_frontpage %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_hprsc.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_hw.sh %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_ica_program_neigbourhood.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_inodes.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_javaproc.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_linux_raid.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_log2.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_maxchannels.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_maxwanstate.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_mem.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_ms_spooler.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_mssql.sh %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_netapp.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_nmap.py %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_pcpmetric.py %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_pfstate %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_qmailq.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_remote_nagios_status.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_smart.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_smb.sh %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_snmp_disk_monitor.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_snmp_printer.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_snmp_process_monitor.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_snmp_procs.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_sockets.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_traceroute.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_wins.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/mrtgext.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/check_mrtgext.pl
install -m0755 contrib/nagios_sendim.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/check_sendim.pl
install -m0755 contrib/utils.py %{buildroot}%{_libdir}/nagios/plugins/contrib/utils.py

# these uses packet_utils.pm
install -m0755 contrib/check_ica_master_browser.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_ica_metaframe_pub_apps.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_lotus.pl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/packet_utils.pm %{buildroot}%{_libdir}/nagios/plugins/contrib/

# binaries
install -m0755 contrib/check_cluster2 %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_ipxping %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_rbl %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_timeout %{buildroot}%{_libdir}/nagios/plugins/contrib/
install -m0755 contrib/check_uptime %{buildroot}%{_libdir}/nagios/plugins/contrib/

# install the extra plugins
pushd extra-plugins
    install -m0755 check-bgp-1.0/check_bgp %{buildroot}%{_libdir}/nagios/plugins/contrib/
    cp check-bgp-1.0/README ../README.check-bgp
popd
cp contrib/README.TXT .

# instead of a patch
install -m0755 plugins-scripts/utils.sh %{buildroot}%{_libdir}/nagios/plugins/contrib/utils.sh

# install the config files
install -m0644 command.cfg %{buildroot}%{_sysconfdir}/nagios/command-old-style.cfg

# magic by anssi
pushd %{buildroot}%{_sysconfdir}/nagios/plugins.d
%{expand:%(for i in {101..152}; do echo "install -m 644 %%SOURCE$i ."; done)}
%{expand:%(for i in {200..253}; do echo "install -m 644 %%SOURCE$i ."; done)}
%{expand:%(for i in {300..300}; do echo "install -m 644 %%SOURCE$i ."; done)}
install -m 644 %{SOURCE2} .
popd

perl -pi -e 's|\@libexecdir\@|%{_libdir}/nagios/plugins|g' \
    %{buildroot}%{_sysconfdir}/nagios/plugins.d/*

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

# fix bad subst script generated crap...
find %{buildroot}%{_libdir}/nagios/plugins/contrib/ | xargs perl -pi -e "s|# autoconf-derived\;|\;|g"

# fix other issues
perl -pi -e "s|\"check_dns\"|\"%{_libdir}/nagios/plugins/contrib/check_dns\"|g" %{buildroot}%{_libdir}/nagios/plugins/contrib/check_dns_random.pl
cat > %{buildroot}%{_sysconfdir}/nagios/domains.list << EOF
google.com
yahoo.com
EOF

%find_lang %{name}

cat > README.urpmi << EOF
IMPORTANT!

Since nagios-plugins-1.4.11-4mdv2008.1 *ALL* check_* modules has been split into
own sub packages. This means the older configuration file located here:
%{_sysconfdir}/nagios/plugins.d/%{name}.cfg is not valid anymore. The file has 
been renamed to %{_sysconfdir}/nagios/plugins.d/%{name}.cfg_do_not_use and all 
command related configuration per plugin has been put in the related plugin sub
package, for example the nagios-check_by_ssh package contains only this:

%{_sysconfdir}/nagios/plugins.d/check_by_ssh.cfg
%{_libdir}/nagios/plugins/check_by_ssh

EOF

# make noarch pluginds installable under %{_datadir} also
install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
pushd %{buildroot}%{_datadir}/nagios/plugins
ln -sf ../../../%_lib/nagios/plugins/utils.pm .
ln -sf ../../../%_lib/nagios/plugins/utils.sh .
popd

# delete unusable plugins
rm -f %{buildroot}%{_libdir}/nagios/plugins/check_apt

%pre
%{_sbindir}/useradd -r -M -s /bin/sh -d /var/log/nagios -c "system user for %{nsusr}" %{nsusr} >/dev/null 2>&1 || :
%{_bindir}/gpasswd -a %{cmdusr} %{nsgrp} >/dev/null 2>&1 || :

if [ -f %{_sysconfdir}/nagios/plugins.d/%{name}.cfg ]; then
    mv %{_sysconfdir}/nagios/plugins.d/%{name}.cfg %{_sysconfdir}/nagios/plugins.d/%{name}.cfg_do_not_use
fi

%postun
%_postun_userdel %{nsusr}

%if %mdkversion < 200900

%post -n nagios-check_breeze
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_breeze
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_by_ssh
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_by_ssh
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_cluster
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_cluster
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_dhcp
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_dhcp
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_dig
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_dig
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_disk
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_disk
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_disk_smb
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_disk_smb
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_dns
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_dns
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_dummy
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_dummy
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_file_age
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_file_age
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_flexlm
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_flexlm
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_fping
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_fping
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_game
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_game
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_hpjd
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_hpjd
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_http
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_http
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_icmp
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_icmp
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ide_smart
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ide_smart
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ifoperstatus
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ifoperstatus
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ifstatus
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ifstatus
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ircd
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ircd
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ldap
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ldap
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_load
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_load
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_log
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_log
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_mailq
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_mailq
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_mrtg
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_mrtg
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_mrtgtraf
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_mrtgtraf
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_mysql
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_mysql
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_mysql_query
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_mysql_query
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_nagios
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_nagios
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_nt
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_nt
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ntp
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ntp
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ntp_peer
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ntp_peer
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ntp_time
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ntp_time
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_nwstat
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_nwstat
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_oracle
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_oracle
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_overcr
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_overcr
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_pgsql
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_pgsql
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ping
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ping
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_procs
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_procs
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_radius
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_radius
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_real
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_real
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_rpc
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_rpc
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_sensors
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_sensors
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_smtp
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_smtp
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ssh
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ssh
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_swap
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_swap
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_tcp
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_tcp
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_time
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_time
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ups
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ups
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_users
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_users
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_wave
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_wave
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_adptraid
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_adptraid
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_apache
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_apache
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_apc_ups
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_apc_ups
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_appletalk
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_appletalk
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_arping
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_arping
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_asterisk
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_asterisk
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_axis
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_axis
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_backup
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_backup
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_bgp
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_bgp
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_bgpstate
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_bgpstate
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ciscotemp
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ciscotemp
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_cluster2
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_cluster2
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_compaq_insight
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_compaq_insight
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_digitemp
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_digitemp
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_dlswcircuit
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_dlswcircuit
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_dns_random
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_dns_random
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_email_loop
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_email_loop
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_frontpage
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_frontpage
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_hprsc
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_hprsc
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_hw
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_hw
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ica_master_browser
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ica_master_browser
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ica_metaframe_pub_apps
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ica_metaframe_pub_apps
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ica_program_neigbourhood
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ica_program_neigbourhood
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_inodes
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_inodes
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ipxping
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ipxping
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_javaproc
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_javaproc
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_linux_raid
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_linux_raid
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_log2
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_log2
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_lotus
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_lotus
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_maxchannels
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_maxchannels
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_maxwanstate
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_maxwanstate
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_mem
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_mem
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_mrtgext
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_mrtgext
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_ms_spooler
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_ms_spooler
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_mssql
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_mssql
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_netapp
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_netapp
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_nmap
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_nmap
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_pcpmetric
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_pcpmetric
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_pfstate
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_pfstate
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_qmailq
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_qmailq
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_rbl
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_rbl
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_remote_nagios_status
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_remote_nagios_status
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_sendim
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_sendim
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_smart
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_smart
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_smb
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_smb
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_disk_monitor
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_disk_monitor
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_printer
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_printer
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_process_monitor
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_process_monitor
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_procs
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_procs
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_sockets
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_sockets
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_timeout
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_timeout
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_traceroute
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_traceroute
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_uptime
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_uptime
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_wins
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_wins
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_mysql_perf
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_mysql_perf
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS CODING ChangeLog FAQ LEGAL NEWS README* REQUIREMENTS SUPPORT README.urpmi
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/command-old-style.cfg
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/%{name}.cfg_do_not_use
%defattr(0755,root,root)
%dir %{_libdir}/nagios
%dir %{_libdir}/nagios/plugins
%dir %{_libdir}/nagios/plugins/contrib
%{_libdir}/nagios/plugins/negate
%{_libdir}/nagios/plugins/urlize
%{_libdir}/nagios/plugins/utils.pm
%{_libdir}/nagios/plugins/utils.sh
# check_ica_master_browser.pl, check_ica_metaframe_pub_apps.pl and check_lotus.pl uses packet_utils.pm
%{_libdir}/nagios/plugins/contrib/packet_utils.pm
%{_libdir}/nagios/plugins/contrib/utils.py
%{_libdir}/nagios/plugins/contrib/utils.sh
%{_datadir}/nagios/plugins

%files -n nagios-check_breeze
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_breeze.cfg
%{_libdir}/nagios/plugins/check_breeze

%files -n nagios-check_by_ssh
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_by_ssh.cfg
%{_libdir}/nagios/plugins/check_by_ssh

%files -n nagios-check_cluster
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_cluster.cfg
%{_libdir}/nagios/plugins/check_cluster

%files -n nagios-check_dhcp
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_dhcp.cfg
%attr(4550,root,nagios) %{_libdir}/nagios/plugins/check_dhcp

%files -n nagios-check_dig
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_dig.cfg
%{_libdir}/nagios/plugins/check_dig

%files -n nagios-check_disk
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_disk.cfg
%{_libdir}/nagios/plugins/check_disk

%files -n nagios-check_disk_smb
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_disk_smb.cfg
%{_libdir}/nagios/plugins/check_disk_smb

%files -n nagios-check_dns
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_dns.cfg
%{_libdir}/nagios/plugins/check_dns

%files -n nagios-check_dummy
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_dummy.cfg
%{_libdir}/nagios/plugins/check_dummy

%files -n nagios-check_file_age
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_file_age.cfg
%{_libdir}/nagios/plugins/check_file_age

%files -n nagios-check_flexlm
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_flexlm.cfg
%{_libdir}/nagios/plugins/check_flexlm

%files -n nagios-check_fping
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_fping.cfg
%{_libdir}/nagios/plugins/check_fping

%files -n nagios-check_game
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_game.cfg
%{_libdir}/nagios/plugins/check_game

%files -n nagios-check_hpjd
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_hpjd.cfg
%{_libdir}/nagios/plugins/check_hpjd

%files -n nagios-check_http
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_http.cfg
%{_libdir}/nagios/plugins/check_http

%files -n nagios-check_icmp
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_icmp.cfg
%attr(4550,root,nagios) %{_libdir}/nagios/plugins/check_icmp

%files -n nagios-check_ide_smart
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ide_smart.cfg
%{_libdir}/nagios/plugins/check_ide_smart

%files -n nagios-check_ifoperstatus
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ifoperstatus.cfg
%{_libdir}/nagios/plugins/check_ifoperstatus

%files -n nagios-check_ifstatus
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ifstatus.cfg
%{_libdir}/nagios/plugins/check_ifstatus

%files -n nagios-check_ircd
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ircd.cfg
%{_libdir}/nagios/plugins/check_ircd

%files -n nagios-check_ldap
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ldap.cfg
%{_libdir}/nagios/plugins/check_ldap
%{_libdir}/nagios/plugins/check_ldaps

%files -n nagios-check_load
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_load.cfg
%{_libdir}/nagios/plugins/check_load

%files -n nagios-check_log
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_log.cfg
%{_libdir}/nagios/plugins/check_log

%files -n nagios-check_mailq
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_mailq.cfg
%{_libdir}/nagios/plugins/check_mailq

%files -n nagios-check_mrtg
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_mrtg.cfg
%{_libdir}/nagios/plugins/check_mrtg

%files -n nagios-check_mrtgtraf
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_mrtgtraf.cfg
%{_libdir}/nagios/plugins/check_mrtgtraf

%files -n nagios-check_mysql
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_mysql.cfg
%{_libdir}/nagios/plugins/check_mysql

%files -n nagios-check_mysql_query
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_mysql_query.cfg
%{_libdir}/nagios/plugins/check_mysql_query

%files -n nagios-check_nagios
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_nagios.cfg
%{_libdir}/nagios/plugins/check_nagios

%files -n nagios-check_nt
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_nt.cfg
%{_libdir}/nagios/plugins/check_nt

%files -n nagios-check_ntp
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ntp.cfg
%{_libdir}/nagios/plugins/check_ntp

%files -n nagios-check_ntp_peer
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ntp_peer.cfg
%{_libdir}/nagios/plugins/check_ntp_peer

%files -n nagios-check_ntp_time
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ntp_time.cfg
%{_libdir}/nagios/plugins/check_ntp_time

%files -n nagios-check_nwstat
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_nwstat.cfg
%{_libdir}/nagios/plugins/check_nwstat

%files -n nagios-check_oracle
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_oracle.cfg
%{_libdir}/nagios/plugins/check_oracle

%files -n nagios-check_overcr
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_overcr.cfg
%{_libdir}/nagios/plugins/check_overcr

%files -n nagios-check_pgsql
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_pgsql.cfg
%{_libdir}/nagios/plugins/check_pgsql

%files -n nagios-check_ping
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ping.cfg
%{_libdir}/nagios/plugins/check_ping

%files -n nagios-check_procs
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_procs.cfg
%{_libdir}/nagios/plugins/check_procs

%files -n nagios-check_radius
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_radius.cfg
%{_libdir}/nagios/plugins/check_radius

%files -n nagios-check_real
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_real.cfg
%{_libdir}/nagios/plugins/check_real

%files -n nagios-check_rpc
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_rpc.cfg
%{_libdir}/nagios/plugins/check_rpc

%files -n nagios-check_sensors
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_sensors.cfg
%{_libdir}/nagios/plugins/check_sensors

%files -n nagios-check_smtp
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_smtp.cfg
%{_libdir}/nagios/plugins/check_smtp

%files -n nagios-check_snmp
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp.cfg
%{_libdir}/nagios/plugins/check_snmp

%files -n nagios-check_ssh
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ssh.cfg
%{_libdir}/nagios/plugins/check_ssh

%files -n nagios-check_swap
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_swap.cfg
%{_libdir}/nagios/plugins/check_swap

%files -n nagios-check_tcp
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_tcp.cfg
%{_libdir}/nagios/plugins/check_tcp
%{_libdir}/nagios/plugins/check_imap
%{_libdir}/nagios/plugins/check_spop
%{_libdir}/nagios/plugins/check_simap
%{_libdir}/nagios/plugins/check_udp
%{_libdir}/nagios/plugins/check_pop
%{_libdir}/nagios/plugins/check_nntp
%{_libdir}/nagios/plugins/check_jabber
%{_libdir}/nagios/plugins/check_clamd
%{_libdir}/nagios/plugins/check_ftp
%{_libdir}/nagios/plugins/check_ssmtp
%{_libdir}/nagios/plugins/check_nntps

%files -n nagios-check_time
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_time.cfg
%{_libdir}/nagios/plugins/check_time

%files -n nagios-check_ups
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ups.cfg
%{_libdir}/nagios/plugins/check_ups

%files -n nagios-check_users
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_users.cfg
%{_libdir}/nagios/plugins/check_users

%files -n nagios-check_wave
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_wave.cfg
%{_libdir}/nagios/plugins/check_wave

%files -n nagios-check_adptraid
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_adptraid.cfg
%{_libdir}/nagios/plugins/contrib/check_adptraid.sh

%files -n nagios-check_apache
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_apache.cfg
%{_libdir}/nagios/plugins/contrib/check_apache.pl

%files -n nagios-check_apc_ups
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_apc_ups.cfg
%{_libdir}/nagios/plugins/contrib/check_apc_ups.pl

%files -n nagios-check_appletalk
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_appletalk.cfg
%{_libdir}/nagios/plugins/contrib/check_appletalk.pl

%files -n nagios-check_arping
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_arping.cfg
%attr(4550,root,nagios) %{_libdir}/nagios/plugins/contrib/check_arping.pl

%files -n nagios-check_asterisk
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_asterisk.cfg
%{_libdir}/nagios/plugins/contrib/check_asterisk.pl

%files -n nagios-check_axis
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_axis.cfg
%{_libdir}/nagios/plugins/contrib/check_axis.sh

%files -n nagios-check_backup
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_backup.cfg
%{_libdir}/nagios/plugins/contrib/check_backup.pl

%files -n nagios-check_bgp
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_bgp.cfg
%{_libdir}/nagios/plugins/contrib/check_bgp

%files -n nagios-check_bgpstate
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_bgpstate.cfg
%{_libdir}/nagios/plugins/contrib/check_bgpstate.pl

%files -n nagios-check_ciscotemp
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ciscotemp.cfg
%{_libdir}/nagios/plugins/contrib/check_ciscotemp.pl

%files -n nagios-check_cluster2
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_cluster2.cfg
%{_libdir}/nagios/plugins/contrib/check_cluster2

%files -n nagios-check_compaq_insight
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_compaq_insight.cfg
%{_libdir}/nagios/plugins/contrib/check_compaq_insight.pl

%files -n nagios-check_digitemp
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_digitemp.cfg
%{_libdir}/nagios/plugins/contrib/check_digitemp.pl

%files -n nagios-check_dlswcircuit
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_dlswcircuit.cfg
%{_libdir}/nagios/plugins/contrib/check_dlswcircuit.pl

%files -n nagios-check_dns_random
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/domains.list
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_dns_random.cfg
%{_libdir}/nagios/plugins/contrib/check_dns_random.pl

%files -n nagios-check_email_loop
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_email_loop.cfg
%{_libdir}/nagios/plugins/contrib/check_email_loop.pl

%files -n nagios-check_frontpage
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_frontpage.cfg
%{_libdir}/nagios/plugins/contrib/check_frontpage

%files -n nagios-check_hprsc
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_hprsc.cfg
%{_libdir}/nagios/plugins/contrib/check_hprsc.pl

%files -n nagios-check_hw
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_hw.cfg
%{_libdir}/nagios/plugins/contrib/check_hw.sh

%files -n nagios-check_ica_master_browser
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ica_master_browser.cfg
%{_libdir}/nagios/plugins/contrib/check_ica_master_browser.pl

%files -n nagios-check_ica_metaframe_pub_apps
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ica_metaframe_pub_apps.cfg
%{_libdir}/nagios/plugins/contrib/check_ica_metaframe_pub_apps.pl

%files -n nagios-check_ica_program_neigbourhood
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ica_program_neigbourhood.cfg
%{_libdir}/nagios/plugins/contrib/check_ica_program_neigbourhood.pl

%files -n nagios-check_inodes
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_inodes.cfg
%{_libdir}/nagios/plugins/contrib/check_inodes.pl

%files -n nagios-check_ipxping
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ipxping.cfg
%{_libdir}/nagios/plugins/contrib/check_ipxping

%files -n nagios-check_javaproc
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_javaproc.cfg
%{_libdir}/nagios/plugins/contrib/check_javaproc.pl

%files -n nagios-check_linux_raid
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_linux_raid.cfg
%{_libdir}/nagios/plugins/contrib/check_linux_raid.pl

%files -n nagios-check_log2
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_log2.cfg
%{_libdir}/nagios/plugins/contrib/check_log2.pl

%files -n nagios-check_lotus
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_lotus.cfg
%{_libdir}/nagios/plugins/contrib/check_lotus.pl

%files -n nagios-check_maxchannels
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_maxchannels.cfg
%{_libdir}/nagios/plugins/contrib/check_maxchannels.pl

%files -n nagios-check_maxwanstate
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_maxwanstate.cfg
%{_libdir}/nagios/plugins/contrib/check_maxwanstate.pl

%files -n nagios-check_mem
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_mem.cfg
%{_libdir}/nagios/plugins/contrib/check_mem.pl

%files -n nagios-check_mrtgext
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_mrtgext.cfg
%{_libdir}/nagios/plugins/contrib/check_mrtgext.pl

%files -n nagios-check_ms_spooler
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_ms_spooler.cfg
%{_libdir}/nagios/plugins/contrib/check_ms_spooler.pl

%files -n nagios-check_mssql
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_mssql.cfg
%{_libdir}/nagios/plugins/contrib/check_mssql.sh

%files -n nagios-check_netapp
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_netapp.cfg
%{_libdir}/nagios/plugins/contrib/check_netapp.pl

%files -n nagios-check_nmap
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_nmap.cfg
%{_libdir}/nagios/plugins/contrib/check_nmap.py

%files -n nagios-check_pcpmetric
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_pcpmetric.cfg
%{_libdir}/nagios/plugins/contrib/check_pcpmetric.py

%files -n nagios-check_pfstate
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_pfstate.cfg
%{_libdir}/nagios/plugins/contrib/check_pfstate

%files -n nagios-check_qmailq
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_qmailq.cfg
%{_libdir}/nagios/plugins/contrib/check_qmailq.pl

%files -n nagios-check_rbl
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_rbl.cfg
%{_libdir}/nagios/plugins/contrib/check_rbl

%files -n nagios-check_remote_nagios_status
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_remote_nagios_status.cfg
%{_libdir}/nagios/plugins/contrib/check_remote_nagios_status.pl

%files -n nagios-check_sendim
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_sendim.cfg
%{_libdir}/nagios/plugins/contrib/check_sendim.pl

%files -n nagios-check_smart
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_smart.cfg
%{_libdir}/nagios/plugins/contrib/check_smart.pl

%files -n nagios-check_smb
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_smb.cfg
%{_libdir}/nagios/plugins/contrib/check_smb.sh

%files -n nagios-check_snmp_disk_monitor
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_disk_monitor.cfg
%{_libdir}/nagios/plugins/contrib/check_snmp_disk_monitor.pl

%files -n nagios-check_snmp_printer
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_printer.cfg
%{_libdir}/nagios/plugins/contrib/check_snmp_printer.pl

%files -n nagios-check_snmp_process_monitor
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_process_monitor.cfg
%{_libdir}/nagios/plugins/contrib/check_snmp_process_monitor.pl

%files -n nagios-check_snmp_procs
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_procs.cfg
%{_libdir}/nagios/plugins/contrib/check_snmp_procs.pl

%files -n nagios-check_sockets
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_sockets.cfg
%{_libdir}/nagios/plugins/contrib/check_sockets.pl

%files -n nagios-check_timeout
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_timeout.cfg
%{_libdir}/nagios/plugins/contrib/check_timeout

%files -n nagios-check_traceroute
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_traceroute.cfg
%{_libdir}/nagios/plugins/contrib/check_traceroute.pl

%files -n nagios-check_uptime
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_uptime.cfg
%{_libdir}/nagios/plugins/contrib/check_uptime

%files -n nagios-check_wins
%defattr(-,root,root)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_wins.cfg
%{_libdir}/nagios/plugins/contrib/check_wins.pl

%files -n nagios-check_mysql_perf
%defattr(-,root,root)
%doc check_mysql_perf-*/README
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_mysql_perf.cfg
%{_libdir}/nagios/plugins/check_mysql_perf
