%define nsusr nagios
%define nsgrp nagios
%define cmdusr apache
%define cmdgrp apache

Summary:	Host/service/network monitoring program plugins for Nagios
Name:		nagios-plugins
Version:	1.5
Release:	2
License:	GPLv2+
Group:		Monitoring
URL:		http://nagiosplug.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/nagiosplug/%{name}-%{version}.tar.gz
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

Patch6:		nagios-plugins-check_ping-socket-filter-warning.diff
# http://sourceforge.net/tracker/index.php?func=detail&aid=1854415&group_id=29880&atid=397599
Patch21:	nagios-plugins-1.4.15-check_dhcp-roguedhcpservercheck.patch
# http://sourceforge.net/tracker/?func=detail&atid=397599&aid=2430999&group_id=29880
Patch22:	nagios-plugins-1.5-check_ldap_certificate.patch
Patch23:	nagios-plugins-1.5-automake-1.14.patch
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRequires:	cvs
BuildRequires:	mysql-devel
BuildRequires:	bind-utils
BuildRequires:	fping
BuildRequires:	gettext-devel
BuildRequires:	sasl-devel
BuildRequires:	net-snmp-utils
BuildRequires:	ntp
BuildRequires:	nut
BuildRequires:	openldap-devel
BuildRequires:	openssh-clients
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel
BuildRequires:	python
BuildRequires:	radiusclient-ng-devel
BuildRequires:	samba-client
BuildRequires:	shadow-utils
BuildRequires:	traceroute
BuildRequires:	zlib-devel
BuildRequires:	dbi-devel
Epoch:		1

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
Requires:   nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_breeze
This plugin reports the signal strength of a Breezecom wireless equipment

%package -n	nagios-check_by_ssh
Summary:	The check_by_ssh plugin for nagios
Group:		Networking/Other
Requires:	nagios-check_disk
Requires:   nagios-plugins

%description -n	nagios-check_by_ssh
This plugin uses SSH to execute commands on a remote host.

%package -n	nagios-check_cluster
Summary:	The check_cluster plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_cluster
This package contains the check_cluster plugin for nagios.

%package -n nagios-check_dbi
Summary:    The check_dbi plugin for nagios
Group:		Networking/Other

%description -n nagios-check_dbi
This package contains the check_dbi plugin for nagios.

%package -n	nagios-check_dhcp
Summary:	The check_dhcp plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_dhcp
This plugin tests the availability of DHCP servers on a network.

%package -n	nagios-check_dig
Summary:	The check_dig plugin for nagios
Group:		Networking/Other
Requires:	bind-utils
Requires:   nagios-plugins

%description -n	nagios-check_dig
This plugin test the DNS service on the specified host using dig

%package -n	nagios-check_disk
Summary:	The check_disk plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_disk
This plugin checks the amount of used disk space on a mounted file system and
generates an alert if free space is less than one of the threshold values

%package -n	nagios-check_disk_smb
Summary:	The check_disk_smb plugin for nagios
Group:		Networking/Other
Requires:	samba-client
Requires:   nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_disk_smb
Perl Check SMB Disk plugin for Nagios

%package -n	nagios-check_dns
Summary:	The check_dns plugin for nagios
Group:		Networking/Other
Requires:	bind-utils
Requires:   nagios-plugins

%description -n	nagios-check_dns
This plugin uses the nslookup program to obtain the IP address for the given
host/domain query. An optional DNS server to use may be specified. If no DNS
server is specified, the default server(s) specified in /etc/resolv.conf will
be used.

%package -n	nagios-check_dummy
Summary:	The check_dummy plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_dummy
This plugin will simply return the state corresponding to the numeric value
of the <state> argument with optional text

%package -n	nagios-check_file_age
Summary:	The check_file_age plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_file_age
This package contains the check_file_age plugin for nagios.

%package -n	nagios-check_flexlm
Summary:	The check_flexlm plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_flexlm
Check available flexlm license managers.

%package -n	nagios-check_fping
Summary:	The check_fping plugin for nagios
Group:		Networking/Other
Requires:	fping
Requires:   nagios-plugins

%description -n	nagios-check_fping
This plugin will use the fping command to ping the specified host for a fast
check Note that it is necessary to set the suid flag on fping.

%package -n	nagios-check_game
Summary:	The check_game plugin for nagios
Group:		Networking/Other
Requires:	qstat
Requires:   nagios-plugins

%description -n	nagios-check_game
This plugin tests game server connections with the specified host.

%package -n	nagios-check_hpjd
Summary:	The check_hpjd plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Requires:   nagios-plugins

%description -n	nagios-check_hpjd
This plugin tests the STATUS of an HP printer with a JetDirect card. Net-snmp
must be installed on the computer running the plugin.

%package -n	nagios-check_http
Summary:	The check_http plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_http
This plugin tests the HTTP service on the specified host. It can test normal
(http) and secure (https) servers, follow redirects, search for strings and
regular expressions, check connection times, and report on certificate
expiration times.

%package -n	nagios-check_icmp
Summary:	The check_icmp plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_icmp
This package contains the check_icmp plugin for nagios.

%package -n	nagios-check_ide_smart
Summary:	The check_ide_smart plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_ide_smart
This plugin checks a local hard drive with the (Linux specific) SMART interface
[http://smartlinux.sourceforge.net/smart/index.php].

%package -n	nagios-check_ifoperstatus
Summary:	The check_ifoperstatus plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_ifoperstatus
check_ifoperstatus plugin for Nagios monitors operational status of a
particular network interface on the target host.

%package -n	nagios-check_ifstatus
Summary:	The check_ifstatus plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_ifstatus
check_ifstatus plugin for Nagios monitors operational status of each network
interface on the target host.

%package -n	nagios-check_ircd
Summary:	The check_ircd plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_ircd
Perl Check IRCD plugin for Nagios

%package -n	nagios-check_ldap
Summary:	The check_ldap plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_ldap
This package contains the check_ldap plugin for nagios.

%package -n	nagios-check_load
Summary:	The check_load plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_load
This plugin tests the current system load average.

%package -n	nagios-check_log
Summary:	The check_log plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_log
Log file pattern detector plugin for Nagios

%package -n	nagios-check_mailq
Summary:	The check_mailq plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_mailq
Checks the number of messages in the mail queue (supports multiple sendmail
queues, qmail)

%package -n	nagios-check_mysql
Summary:	The check_mysql plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_mysql
This program tests connections to a mysql server.

%package -n	nagios-check_mysql_query
Summary:	The check_mysql_query plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_mysql_query
This program checks a query result against threshold levels.

%package -n	nagios-check_nagios
Summary:	The check_nagios plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_nagios
This plugin checks the status of the Nagios process on the local machine. The
plugin will check to make sure the Nagios status log is no older than the
number of minutes specified by the expires option. It also checks the process
table for a process matching the command argument.

%package -n	nagios-check_nt
Summary:	The check_nt plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_nt
This plugin collects data from the NSClient service running on a Windows(tm)
NT/2000/XP/2003 server.

%package -n	nagios-check_ntp
Summary:	The check_ntp plugin for nagios
Group:		Networking/Other
Requires:	ntp
Requires:   nagios-plugins

%description -n	nagios-check_ntp
This plugin checks the selected ntp server.

%package -n	nagios-check_ntp_peer
Summary:	The check_ntp_peer plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_ntp_peer
This plugin checks the selected ntp server.

%package -n	nagios-check_ntp_time
Summary:	The check_ntp_time plugin for nagios
Group:		Networking/Other
Requires:	ntp
Requires:   nagios-plugins

%description -n	nagios-check_ntp_time
This plugin checks the clock offset with the ntp server.

%package -n	nagios-check_nwstat
Summary:	The check_nwstat plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_nwstat
This plugin attempts to contact the MRTGEXT NLM running on a Novell server
to gather the requested system information.

%package -n	nagios-check_oracle
Summary:	The check_oracle plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_oracle
Check Oracle status.

%package -n	nagios-check_overcr
Summary:	The check_overcr plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_overcr
This plugin attempts to contact the Over-CR collector daemon running on the
remote UNIX server in order to gather the requested system information.

%package -n	nagios-check_pgsql
Summary:	The check_pgsql plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_pgsql
Test whether a PostgreSQL Database is accepting connections.

%package -n	nagios-check_ping
Summary:	The check_ping plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_ping
Use ping to check connection statistics for a remote host.

%package -n	nagios-check_procs
Summary:	The check_procs plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_procs
Checks all processes and generates WARNING or CRITICAL states if the specified
metric is outside the required threshold ranges. The metric defaults to number
of processes.  Search filters can be applied to limit the processes to check.

%package -n	nagios-check_radius
Summary:	The check_radius plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_radius
Tests to see if a radius server is accepting connections.

%package -n	nagios-check_real
Summary:	The check_real plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_real
This plugin tests the REAL service on the specified host.

%package -n	nagios-check_rpc
Summary:	The check_rpc plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_rpc
Check if a rpc service is registered and running using:
rpcinfo -H host -C rpc_command 

%package -n	nagios-check_sensors
Summary:	The check_sensors plugin for nagios
Group:		Networking/Other
Requires:	lm_sensors
Requires:   nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_sensors
This plugin checks hardware status using the lm_sensors package.

%package -n	nagios-check_smtp
Summary:	The check_smtp plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_smtp
This plugin will attempt to open an SMTP connection with the host.

%package -n	nagios-check_snmp
Summary:	The check_snmp plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Requires:   nagios-plugins

%description -n	nagios-check_snmp
Check status of remote machines and obtain sustem information via SNMP.

%package -n	nagios-check_ssh
Summary:	The check_ssh plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_ssh
Try to connect to an SSH server at specified server and port.

%package -n	nagios-check_swap
Summary:	The check_swap plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_swap
Check swap space on local machine.

%package -n	nagios-check_tcp
Summary:	The check_tcp plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_tcp
This plugin tests TCP connections with the specified host (or unix socket).

%package -n	nagios-check_time
Summary:	The check_time plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_time
This plugin will check the time on the specified host.

%package -n	nagios-check_ups
Summary:	The check_ups plugin for nagios
Group:		Networking/Other
Requires:	nut
Requires:   nagios-plugins

%description -n	nagios-check_ups
This plugin tests the UPS service on the specified host.Network UPS Tools 
from www.networkupstools.org must be running for thisplugin to work.

%package -n	nagios-check_users
Summary:	The check_users plugin for nagios
Group:		Networking/Other
Requires:   nagios-plugins

%description -n	nagios-check_users
This plugin checks the number of users currently logged in on the local
system and generates an error if the number exceeds the thresholds specified.

%package -n	nagios-check_wave
Summary:	The check_wave plugin for nagios
Group:		Networking/Other
Requires:	nagios-plugins = %{epoch}:%{version}-%{release}

%description -n	nagios-check_wave
This package contains the check_wave plugin for nagios.

%prep
%setup -q
%patch6 -p0
%patch21 -p1
%patch22 -p1
%patch23 -p1

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

# anti recheck hack
touch *

export CPPFLAGS="-I%{_includedir}/ldap -I%{_includedir}/mysql -I%{_includedir}/pgsql -I%{_includedir}/openssl"

make

make -C plugins \
    check_ide_smart check_ldap check_pgsql check_radius

%install
install -d -m0755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
%makeinstall_std MKDIR_P="/bin/mkdir -p"

install -m0755 plugins/check_pgsql %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 plugins/check_radius %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 plugins/check_ide_smart %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 plugins-root/check_dhcp %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 plugins-root/check_icmp %{buildroot}%{_libdir}/nagios/plugins/

# magic by anssi
pushd %{buildroot}%{_sysconfdir}/nagios/plugins.d
%{expand:%(for i in {101..124}; do echo "install -m 644 %%SOURCE$i ."; done)}
%{expand:%(for i in {127..152}; do echo "install -m 644 %%SOURCE$i ."; done)}
popd

perl -pi -e 's|\@libexecdir\@|%{_libdir}/nagios/plugins|g' \
    %{buildroot}%{_sysconfdir}/nagios/plugins.d/*

# fix bad paths (again!)
for i in check_breeze check_disk_smb check_file_age check_flexlm check_ifoperstatus \
    check_ifstatus check_ircd check_mailq check_ntp check_rpc check_wave; do
    perl -pi -e "s|\"nagios/plugins\"|\"%{_libdir}/nagios/plugins\"|g" \
    %{buildroot}%{_libdir}/nagios/plugins/$i
done

%find_lang %{name}

# make noarch pluginds installable under %{_datadir} also
install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
pushd %{buildroot}%{_datadir}/nagios/plugins
ln -sf ../../../%{_lib}/nagios/plugins/utils.pm .
ln -sf ../../../%{_lib}/nagios/plugins/utils.sh .
popd

# delete unusable plugins
rm -f %{buildroot}%{_libdir}/nagios/plugins/check_apt
rm -f %{buildroot}%{_libdir}/nagios/plugins/check_mrtg
rm -f %{buildroot}%{_libdir}/nagios/plugins/check_mrtgtraf

%pre
%{_sbindir}/useradd -r -M -s /bin/sh -d /var/log/nagios -c "system user for %{nsusr}" %{nsusr} >/dev/null 2>&1 || :
%{_bindir}/gpasswd -a %{cmdusr} %{nsgrp} >/dev/null 2>&1 || :

%postun
%_postun_userdel %{nsusr}

%files -f %{name}.lang
%doc AUTHORS CODING ChangeLog FAQ LEGAL NEWS README* REQUIREMENTS SUPPORT
%dir %{_libdir}/nagios
%dir %{_libdir}/nagios/plugins
%{_libdir}/nagios/plugins/negate
%{_libdir}/nagios/plugins/urlize
%{_libdir}/nagios/plugins/utils.pm
%{_libdir}/nagios/plugins/utils.sh
%{_datadir}/nagios/plugins

%files -n nagios-check_breeze
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_breeze.cfg
%{_libdir}/nagios/plugins/check_breeze

%files -n nagios-check_by_ssh
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_by_ssh.cfg
%{_libdir}/nagios/plugins/check_by_ssh

%files -n nagios-check_cluster
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_cluster.cfg
%{_libdir}/nagios/plugins/check_cluster

%files -n nagios-check_dbi
%{_libdir}/nagios/plugins/check_dbi

%files -n nagios-check_dhcp
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_dhcp.cfg
%attr(4550,root,nagios) %{_libdir}/nagios/plugins/check_dhcp

%files -n nagios-check_dig
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_dig.cfg
%{_libdir}/nagios/plugins/check_dig

%files -n nagios-check_disk
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_disk.cfg
%{_libdir}/nagios/plugins/check_disk

%files -n nagios-check_disk_smb
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_disk_smb.cfg
%{_libdir}/nagios/plugins/check_disk_smb

%files -n nagios-check_dns
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_dns.cfg
%{_libdir}/nagios/plugins/check_dns

%files -n nagios-check_dummy
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_dummy.cfg
%{_libdir}/nagios/plugins/check_dummy

%files -n nagios-check_file_age
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_file_age.cfg
%{_libdir}/nagios/plugins/check_file_age

%files -n nagios-check_flexlm
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_flexlm.cfg
%{_libdir}/nagios/plugins/check_flexlm

%files -n nagios-check_fping
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_fping.cfg
%{_libdir}/nagios/plugins/check_fping

%files -n nagios-check_game
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_game.cfg
%{_libdir}/nagios/plugins/check_game

%files -n nagios-check_hpjd
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_hpjd.cfg
%{_libdir}/nagios/plugins/check_hpjd

%files -n nagios-check_http
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_http.cfg
%{_libdir}/nagios/plugins/check_http

%files -n nagios-check_icmp
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_icmp.cfg
%attr(4550,root,nagios) %{_libdir}/nagios/plugins/check_icmp

%files -n nagios-check_ide_smart
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_ide_smart.cfg
%{_libdir}/nagios/plugins/check_ide_smart

%files -n nagios-check_ifoperstatus
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_ifoperstatus.cfg
%{_libdir}/nagios/plugins/check_ifoperstatus

%files -n nagios-check_ifstatus
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_ifstatus.cfg
%{_libdir}/nagios/plugins/check_ifstatus

%files -n nagios-check_ircd
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_ircd.cfg
%{_libdir}/nagios/plugins/check_ircd

%files -n nagios-check_ldap
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_ldap.cfg
%{_libdir}/nagios/plugins/check_ldap
%{_libdir}/nagios/plugins/check_ldaps

%files -n nagios-check_load
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_load.cfg
%{_libdir}/nagios/plugins/check_load

%files -n nagios-check_log
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_log.cfg
%{_libdir}/nagios/plugins/check_log

%files -n nagios-check_mailq
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_mailq.cfg
%{_libdir}/nagios/plugins/check_mailq

%files -n nagios-check_mysql
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_mysql.cfg
%{_libdir}/nagios/plugins/check_mysql

%files -n nagios-check_mysql_query
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_mysql_query.cfg
%{_libdir}/nagios/plugins/check_mysql_query

%files -n nagios-check_nagios
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_nagios.cfg
%{_libdir}/nagios/plugins/check_nagios

%files -n nagios-check_nt
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_nt.cfg
%{_libdir}/nagios/plugins/check_nt

%files -n nagios-check_ntp
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_ntp.cfg
%{_libdir}/nagios/plugins/check_ntp

%files -n nagios-check_ntp_peer
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_ntp_peer.cfg
%{_libdir}/nagios/plugins/check_ntp_peer

%files -n nagios-check_ntp_time
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_ntp_time.cfg
%{_libdir}/nagios/plugins/check_ntp_time

%files -n nagios-check_nwstat
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_nwstat.cfg
%{_libdir}/nagios/plugins/check_nwstat

%files -n nagios-check_oracle
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_oracle.cfg
%{_libdir}/nagios/plugins/check_oracle

%files -n nagios-check_overcr
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_overcr.cfg
%{_libdir}/nagios/plugins/check_overcr

%files -n nagios-check_pgsql
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_pgsql.cfg
%{_libdir}/nagios/plugins/check_pgsql

%files -n nagios-check_ping
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_ping.cfg
%{_libdir}/nagios/plugins/check_ping

%files -n nagios-check_procs
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_procs.cfg
%{_libdir}/nagios/plugins/check_procs

%files -n nagios-check_radius
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_radius.cfg
%{_libdir}/nagios/plugins/check_radius

%files -n nagios-check_real
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_real.cfg
%{_libdir}/nagios/plugins/check_real

%files -n nagios-check_rpc
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_rpc.cfg
%{_libdir}/nagios/plugins/check_rpc

%files -n nagios-check_sensors
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_sensors.cfg
%{_libdir}/nagios/plugins/check_sensors

%files -n nagios-check_smtp
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_smtp.cfg
%{_libdir}/nagios/plugins/check_smtp

%files -n nagios-check_snmp
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp.cfg
%{_libdir}/nagios/plugins/check_snmp

%files -n nagios-check_ssh
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_ssh.cfg
%{_libdir}/nagios/plugins/check_ssh

%files -n nagios-check_swap
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_swap.cfg
%{_libdir}/nagios/plugins/check_swap

%files -n nagios-check_tcp
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_tcp.cfg
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
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_time.cfg
%{_libdir}/nagios/plugins/check_time

%files -n nagios-check_ups
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_ups.cfg
%{_libdir}/nagios/plugins/check_ups

%files -n nagios-check_users
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_users.cfg
%{_libdir}/nagios/plugins/check_users

%files -n nagios-check_wave
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_wave.cfg
%{_libdir}/nagios/plugins/check_wave
