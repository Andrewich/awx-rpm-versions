
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-oauthlib
Version:        3.2.2
Release:        %autorelease
Summary:        A generic, spec-compliant, thorough implementation of the OAuth request-signing logic

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/oauthlib/oauthlib
Source:         %{pypi_source oauthlib}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(cryptography) >= 3
BuildRequires:  python%{python3_pkgversion}dist(blinker) >= 1.4
BuildRequires:  (python%{python3_pkgversion}dist(pyjwt) < 3~~ with python%{python3_pkgversion}dist(pyjwt) >= 2)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'oauthlib' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-oauthlib
Summary:        %{summary}

%description -n python%{python3_pkgversion}-oauthlib %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-oauthlib+rsa
Summary: Metapackage for python%{python3_pkgversion}-oauthlib: rsa extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(cryptography) >= 3
Requires: python%{python3_pkgversion}-oauthlib = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-oauthlib+rsa = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(oauthlib[rsa]) = %{version}

%description -n python%{python3_pkgversion}-oauthlib+rsa
This is a metapackage bringing in rsa extras requires for python%{python3_pkgversion}-oauthlib.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-oauthlib+rsa
%ghost %{python3__sitelib}/*.dist-info


%package -n python%{python3_pkgversion}-oauthlib+signals
Summary: Metapackage for python%{python3_pkgversion}-oauthlib: signals extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(blinker) >= 1.4
Requires: python%{python3_pkgversion}-oauthlib = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-oauthlib+signals = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(oauthlib[signals]) = %{version}

%description -n python%{python3_pkgversion}-oauthlib+signals
This is a metapackage bringing in signals extras requires for python%{python3_pkgversion}-oauthlib.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-oauthlib+signals
%ghost %{python3__sitelib}/*.dist-info


%package -n python%{python3_pkgversion}-oauthlib+signedtoken
Summary: Metapackage for python%{python3_pkgversion}-oauthlib: signedtoken extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(cryptography) >= 3
Requires: python%{python3_pkgversion}-oauthlib = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-oauthlib+signedtoken = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(oauthlib[signedtoken]) = %{version}

%description -n python%{python3_pkgversion}-oauthlib+signedtoken
This is a metapackage bringing in signedtoken extras requires for python%{python3_pkgversion}-oauthlib.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-oauthlib+signedtoken
%ghost %{python3__sitelib}/*.dist-info


%prep
%autosetup -p1 -n oauthlib-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-oauthlib -f %{pyproject_files}


%changelog
%autochangelog