
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-azure-core
Version:        1.30.0
Release:        %autorelease
Summary:        Microsoft Azure Core Library for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core
Source:         %{pypi_source azure-core}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(requests) >= 2.21
BuildRequires:  python%{python3_pkgversion}dist(six) >= 1.11
BuildRequires:  python%{python3_pkgversion}dist(typing-extensions) >= 4.6
BuildRequires:  python%{python3_pkgversion}dist(aiohttp) >= 3


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'azure-core' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-azure-core
Summary:        %{summary}

%description -n python%{python3_pkgversion}-azure-core %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-azure-core+aio
Summary: Metapackage for python%{python3_pkgversion}-azure-core: aio extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(aiohttp) >= 3
Requires: python%{python3_pkgversion}-azure-core = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-azure-core+aio = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(azure-core[aio]) = 1.30

%description -n python%{python3_pkgversion}-azure-core+aio
This is a metapackage bringing in aio extras requires for python%{python3_pkgversion}-azure-core.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-azure-core+aio
%ghost %{python3__sitelib}/*.dist-info

%prep
%autosetup -p1 -n azure-core-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-azure-core -f %{pyproject_files}


%changelog
%autochangelog