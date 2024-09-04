
%global python3_pkgversion 3.11

Name:           python-msrest
Version:        0.7.1
Release:        %autorelease
Summary:        AutoRest swagger generator Python client runtime.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/Azure/msrest-for-python
Source:         %{pypi_source msrest %{version} zip}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(requests) >= 2.16 with python%{python3_pkgversion}dist(requests) < 3)
BuildRequires:  python%{python3_pkgversion}dist(requests-oauthlib) >= 0.5
BuildRequires:  python%{python3_pkgversion}dist(isodate) >= 0.6
BuildRequires:  python%{python3_pkgversion}dist(certifi) >= 2017.4.17
BuildRequires:  python%{python3_pkgversion}dist(azure-core) >= 1.24
BuildRequires:  python%{python3_pkgversion}dist(aiohttp) >= 3
BuildRequires:  python%{python3_pkgversion}dist(aiodns)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'msrest' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-msrest
Summary:        %{summary}

%description -n python%{python3_pkgversion}-msrest %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-msrest async
%package -n python%{python3_pkgversion}-msrest+async
Summary: Metapackage for python%{python3_pkgversion}-msrest: async extras
Requires: python%{python3_pkgversion}-msrest = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-msrest+async = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(msrest[async]) = %{version}

%description -n python%{python3_pkgversion}-msrest+async
This is a metapackage bringing in async extras requires for python%{python3_pkgversion}-msrest.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-msrest+async
%ghost %{python3__sitelib}/*.dist-info

%prep
%autosetup -p1 -n msrest-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-msrest -f %{pyproject_files}


%changelog
%autochangelog