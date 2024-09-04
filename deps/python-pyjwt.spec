
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-pyjwt
Version:        2.8.0
Release:        %autorelease
Summary:        JSON Web Token implementation in Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jpadilla/pyjwt
Source:         %{pypi_source PyJWT}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(cryptography) >= 3.4


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyjwt' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pyjwt
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyjwt %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-pyjwt+crypto
Summary: Metapackage for python%{python3_pkgversion}-pyjwt: crypto extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(cryptography) >= 3.4
Requires: python%{python3_pkgversion}-pyjwt = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-pyjwt+crypto = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(pyjwt[crypto]) = 2.8

%description -n python%{python3_pkgversion}-pyjwt+crypto
This is a metapackage bringing in crypto extras requires for python%{python3_pkgversion}-pyjwt.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-pyjwt+crypto
%ghost %{python3__sitelib}/*.dist-info

%prep
%autosetup -p1 -n PyJWT-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pyjwt -f %{pyproject_files}


%changelog
%autochangelog