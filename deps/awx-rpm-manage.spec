%define  debug_package %{nil}

Summary: Ansible AWX-RPM Management Tools
Name: awx-rpm-manage
Version: 1.2.0
Release: 6%{dist}
Source0: awx-rpm-manage-1.2.0.tar.gz
License: GPLv3
Group: AWX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

BuildRequires: python3 
Requires: python3 

%description
%{summary}

%prep
%setup -n awx-rpm-manage-%version
%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/ $RPM_BUILD_ROOT/usr/share/doc/awx-rpm-manage
cp awx-rpm-manage $RPM_BUILD_ROOT/usr/bin/awx-rpm-manage
cp README.md $RPM_BUILD_ROOT/usr/share/doc/awx-rpm-manage/README.md

%pre
/usr/bin/getent group awx >/dev/null || /usr/sbin/groupadd --system awx
/usr/bin/getent passwd awx >/dev/null || /usr/sbin/useradd --no-create-home --system -g awx --home-dir /opt/awx-rpm -s /bin/bash awx
/usr/sbin/usermod -s /bin/bash awx

%clean

%files
%defattr(0755, awx, awx, 0755)
/usr/bin/awx-rpm-manage
/usr/share/doc/awx-rpm-manage/README.md

%changelog
* Thu Apr 11 2024 02:34:52 PM CEST +0200 Martin Juhl <m@rtinjuhl.dk> 1.2.0
- New version build: 1.2.0

