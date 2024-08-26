
%global python3_pkgversion 3.11

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
%pyproject_extras_subpkg -n python%{python3_pkgversion}-aiohttp speedups


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