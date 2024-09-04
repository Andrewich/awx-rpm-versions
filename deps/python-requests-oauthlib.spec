
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-requests-oauthlib
Version:        1.3.1
Release:        %autorelease
Summary:        OAuthlib authentication support for Requests.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/requests/requests-oauthlib
Source:         %{pypi_source requests-oauthlib}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(requests) >= 2
BuildRequires:  python%{python3_pkgversion}dist(oauthlib) >= 3


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'requests-oauthlib' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-requests-oauthlib
Summary:        %{summary}

%description -n python%{python3_pkgversion}-requests-oauthlib %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-requests-oauthlib+rsa
Summary: Metapackage for python%{python3_pkgversion}-requests-oauthlib: rsa extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(oauthlib) >= 3
Requires: python%{python3_pkgversion}dist(oauthlib[signedtoken]) >= 3
Requires: python%{python3_pkgversion}-requests-oauthlib = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-requests-oauthlib+rsa = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(requests-oauthlib[rsa]) = %{version}

%description -n python%{python3_pkgversion}-requests-oauthlib+rsa
This is a metapackage bringing in rsa extras requires for python%{python3_pkgversion}-requests-oauthlib.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-requests-oauthlib+rsa
%ghost %{python3__sitelib}/*.dist-info


%prep
%autosetup -p1 -n requests-oauthlib-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-requests-oauthlib -f %{pyproject_files}


%changelog
%autochangelog