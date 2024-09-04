
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-social-auth-core
Version:        4.4.2
Release:        %autorelease
Summary:        Python social authentication made simple.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-social-auth/social-core
Source:         %{pypi_source social-auth-core}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(requests) >= 2.9.1
BuildRequires:  python%{python3_pkgversion}dist(oauthlib) >= 1.0.3
BuildRequires:  python%{python3_pkgversion}dist(requests-oauthlib) >= 0.6.1
BuildRequires:  python%{python3_pkgversion}dist(pyjwt) >= 2
BuildRequires:  python%{python3_pkgversion}dist(cryptography) >= 1.4
BuildRequires:  python%{python3_pkgversion}dist(defusedxml) >= 0.5~rc1
BuildRequires:  python%{python3_pkgversion}dist(python3-openid) >= 3.0.10
BuildRequires:  python%{python3_pkgversion}dist(python-jose) >= 3
BuildRequires:  python%{python3_pkgversion}dist(python3-saml) >= 1.5
BuildRequires:  python%{python3_pkgversion}dist(cryptography) >= 2.1.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'social-auth-core' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-social-auth-core
Summary:        %{summary}

%description -n python%{python3_pkgversion}-social-auth-core %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-social-auth-core+all
Summary: Metapackage for python%{python3_pkgversion}-social-auth-core: all extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(cryptography) >= 2.1.1
Requires: python%{python3_pkgversion}dist(python-jose) >= 3
Requires: python%{python3_pkgversion}dist(python3-saml) >= 1.5
Requires: python%{python3_pkgversion}-social-auth-core = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-social-auth-core+all = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(social-auth-core[all]) = %{version}

%description -n python%{python3_pkgversion}-social-auth-core+all
This is a metapackage bringing in all extras requires for python%{python3_pkgversion}-social-auth-core.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-social-auth-core+all
%ghost %{python3__sitelib}/*.dist-info


%package -n python%{python3_pkgversion}-social-auth-core+allpy3
Summary: Metapackage for python%{python3_pkgversion}-social-auth-core: allpy3 extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(cryptography) >= 2.1.1
Requires: python%{python3_pkgversion}dist(python-jose) >= 3
Requires: python%{python3_pkgversion}dist(python3-saml) >= 1.5
Requires: python%{python3_pkgversion}-social-auth-core = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-social-auth-core+allpy3 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(social-auth-core[allpy3]) = %{version}

%description -n python%{python3_pkgversion}-social-auth-core+allpy3
This is a metapackage bringing in allpy3 extras requires for python%{python3_pkgversion}-social-auth-core.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-social-auth-core+allpy3
%ghost %{python3__sitelib}/*.dist-info


%package -n python%{python3_pkgversion}-social-auth-core+azuread
Summary: Metapackage for python%{python3_pkgversion}-social-auth-core: azuread extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(cryptography) >= 2.1.1
Requires: python%{python3_pkgversion}-social-auth-core = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-social-auth-core+azuread = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(social-auth-core[azuread]) = %{version}

%description -n python%{python3_pkgversion}-social-auth-core+azuread
This is a metapackage bringing in azuread extras requires for python%{python3_pkgversion}-social-auth-core.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-social-auth-core+azuread
%ghost %{python3__sitelib}/*.dist-info


%package -n python%{python3_pkgversion}-social-auth-core+openidconnect
Summary: Metapackage for python%{python3_pkgversion}-social-auth-core: openidconnect extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(python-jose) >= 3
Requires: python%{python3_pkgversion}-social-auth-core = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-social-auth-core+openidconnect = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(social-auth-core[openidconnect]) = %{version}

%description -n python%{python3_pkgversion}-social-auth-core+openidconnect
This is a metapackage bringing in openidconnect extras requires for python%{python3_pkgversion}-social-auth-core.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-social-auth-core+openidconnect
%ghost %{python3__sitelib}/*.dist-info


%package -n python%{python3_pkgversion}-social-auth-core+saml
Summary: Metapackage for python%{python3_pkgversion}-social-auth-core: saml extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(python3-saml) >= 1.5
Requires: python%{python3_pkgversion}-social-auth-core = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-social-auth-core+saml = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(social-auth-core[saml]) = %{version}

%description -n python%{python3_pkgversion}-social-auth-core+saml
This is a metapackage bringing in saml extras requires for python%{python3_pkgversion}-social-auth-core.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-social-auth-core+saml
%ghost %{python3__sitelib}/*.dist-info


%prep
%autosetup -p1 -n social-auth-core-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-social-auth-core -f %{pyproject_files}


%changelog
%autochangelog