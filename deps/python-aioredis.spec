
%global python3_pkgversion 3.11

Name:           python-aioredis
Version:        1.3.1
Release:        %autorelease
Summary:        asyncio (PEP 3156) Redis support

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/aio-libs/aioredis
Source:         %{pypi_source aioredis}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(async-timeout)
BuildRequires:  python%{python3_pkgversion}dist(hiredis)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'aioredis' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-aioredis
Summary:        %{summary}

%description -n python%{python3_pkgversion}-aioredis %_description


%prep
%autosetup -p1 -n aioredis-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-aioredis -f %{pyproject_files}


%changelog
%autochangelog