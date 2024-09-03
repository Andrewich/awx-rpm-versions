
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-aiohttp
Version:        3.9.5
Release:        %autorelease
Summary:        Async http client/server framework (asyncio)

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/aio-libs/aiohttp
Source:         %{pypi_source aiohttp}

BuildArch:      x86_64
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 46.4
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(aiosignal) >= 1.1.2
BuildRequires:  python%{python3_pkgversion}dist(attrs) >= 17.3
BuildRequires:  python%{python3_pkgversion}dist(frozenlist) >= 1.1.1
BuildRequires:  (python%{python3_pkgversion}dist(multidict) < 7~~ with python%{python3_pkgversion}dist(multidict) >= 4.5)
BuildRequires:  (python%{python3_pkgversion}dist(yarl) < 2~~ with python%{python3_pkgversion}dist(yarl) >= 1)
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'aiohttp' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-aiohttp
Summary:        %{summary}

%description -n python%{python3_pkgversion}-aiohttp %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-aiohttp+speedups
Summary: Metapackage for python%{python3_pkgversion}-aiohttp: speedups extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(aiodns)
Requires: python%{python3_pkgversion}dist(brotli)
Requires: python%{python3_pkgversion}-aiohttp = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-aiohttp+speedups = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}-aiohttp+speedups(x86-64) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(aiohttp[speedups]) = %{version}

%description -n python%{python3_pkgversion}-aiohttp+speedups
This is a metapackage bringing in speedups extras requires for python%{python3_pkgversion}-aiohttp.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-aiohttp+speedups
%ghost %{python3__sitelib}/*.dist-info


%prep
%autosetup -p1 -n aiohttp-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-aiohttp -f %{pyproject_files}


%changelog
%autochangelog