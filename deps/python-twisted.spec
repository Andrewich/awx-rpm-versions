%bcond_without check
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-twisted
Version:        23.10.0
Release:        %autorelease
Summary:        An asynchronous networking framework written in Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://twistedmatrix.com/
Source:         %{pypi_source twisted}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion}-cryptography python%{python3_pkgversion}-bcrypt python%{python3_pkgversion}-pyasn1 python%{python3_pkgversion}-tkinter python%{python3_pkgversion}-pyhamcrest glibc-langpack-en
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling) >= 1.10
BuildRequires:  python%{python3_pkgversion}dist(hatch-fancy-pypi-readme) >= 22.5
BuildRequires:  python%{python3_pkgversion}dist(incremental) >= 22.10
BuildRequires:  python%{python3_pkgversion}dist(attrs) >= 21.3
BuildRequires:  python%{python3_pkgversion}dist(automat) >= 0.8
BuildRequires:  python%{python3_pkgversion}dist(constantly) >= 15.1
BuildRequires:  python%{python3_pkgversion}dist(hyperlink) >= 17.1.1
BuildRequires:  python%{python3_pkgversion}dist(incremental) >= 22.10
BuildRequires:  python%{python3_pkgversion}dist(typing-extensions) >= 4.2
BuildRequires:  python%{python3_pkgversion}dist(zope-interface) >= 5
BuildRequires:  (python%{python3_pkgversion}dist(h2) < 5~~ with python%{python3_pkgversion}dist(h2) >= 3)
BuildRequires:  (python%{python3_pkgversion}dist(priority) < 2~~ with python%{python3_pkgversion}dist(priority) >= 1.1)
BuildRequires:  python%{python3_pkgversion}dist(idna) >= 2.4
BuildRequires:  python%{python3_pkgversion}dist(pyopenssl) >= 21
BuildRequires:  python%{python3_pkgversion}dist(service-identity) >= 18.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'twisted' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-twisted
Summary:        %{summary}

%description -n python%{python3_pkgversion}-twisted %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-twisted+http2
Summary: Metapackage for python%{python3_pkgversion}-twisted: http2 extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: (python%{python3_pkgversion}dist(h2) < 5 with python%{python3_pkgversion}dist(h2) >= 3)
Requires: (python%{python3_pkgversion}dist(priority) < 2 with python%{python3_pkgversion}dist(priority) >= 1.1)
Requires: python%{python3_pkgversion}-twisted = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-twisted+http2 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(twisted[http2]) = 23.10

%description -n python%{python3_pkgversion}-twisted+http2
This is a metapackage bringing in http2 extras requires for python%{python3_pkgversion}-twisted.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-twisted+http2
%ghost %{python3__sitelib}/*.dist-info


%package -n python%{python3_pkgversion}-twisted+tls
Summary: Metapackage for python%{python3_pkgversion}-twisted: tls extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(idna) >= 2.4
Requires: python%{python3_pkgversion}dist(pyopenssl) >= 21
Requires: python%{python3_pkgversion}dist(service-identity) >= 18.1
Requires: python%{python3_pkgversion}-twisted = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-twisted+tls = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(twisted[tls]) = 23.10

%description -n python%{python3_pkgversion}-twisted+tls
This is a metapackage bringing in tls extras requires for python%{python3_pkgversion}-twisted.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-twisted+tls
%ghost %{python3__sitelib}/*.dist-info


%prep
%autosetup -p1 -n twisted-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/cftp $RPM_BUILD_ROOT/usr/bin/cftp%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/ckeygen $RPM_BUILD_ROOT/usr/bin/ckeygen%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/conch $RPM_BUILD_ROOT/usr/bin/conch%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/mailmail $RPM_BUILD_ROOT/usr/bin/mailmail%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/pyhtmlizer $RPM_BUILD_ROOT/usr/bin/pyhtmlizer%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/tkconch $RPM_BUILD_ROOT/usr/bin/tkconch%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/trial $RPM_BUILD_ROOT/usr/bin/trial%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/twist $RPM_BUILD_ROOT/usr/bin/twist%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/twistd $RPM_BUILD_ROOT/usr/bin/twistd%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/cftp$|/usr/bin/cftp%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/ckeygen$|/usr/bin/ckeygen%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/conch$|/usr/bin/conch%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/mailmail$|/usr/bin/mailmail%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/pyhtmlizer$|/usr/bin/pyhtmlizer%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/tkconch$|/usr/bin/tkconch%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/trial$|/usr/bin/trial%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/twist$|/usr/bin/twist%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/twistd$|/usr/bin/twistd%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-twisted -f %{pyproject_files}


%changelog
%autochangelog