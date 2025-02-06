%define relabel_files() restorecon -R /usr/libexec/fprintd;
%define selinux_policyver 41.31-1
%define version 1.0
%define release 1

Name:       fprintd_tod_selinux
Version:	%{version}
Release:	%{release}%{?dist}
Summary:	SELinux policy module for fprintd_tod

Group:	    System Environment/Base
License:	GPLv2+
URL:		https://github.com/ferdiu/fprintd_tod_selinux
Source0:	fprintd_tod.pp
Source1:	fprintd_tod.if
Source2:	fprintd_tod_selinux.8


Requires: policycoreutils-python-utils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils-python-utils
Requires(postun): policycoreutils-python-utils
BuildArch: noarch

%description
This package installs and sets up the  SELinux policy security module for fprintd_tod.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man8/fprintd_tod_selinux.8
install -d %{buildroot}/etc/selinux/targeted/contexts/users/


%post
semodule -n -i %{_datadir}/selinux/packages/fprintd_tod.pp

if [ $1 -eq 1 ]; then

fi
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files
fi;
exit 0

%postun
if [ $1 -eq 0 ]; then

    semodule -n -r fprintd_tod
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       %relabel_files
    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/fprintd_tod.pp
%{_datadir}/selinux/devel/include/contrib/fprintd_tod.if
%{_mandir}/man8/fprintd_tod_selinux.8.*


%changelog
* Thu Feb 5 2025 Federico Manzella <ferdiu.manzella@gmail.com> 1.0-1
- Initial version

