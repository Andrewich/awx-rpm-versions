
%global python3_pkgversion 3.11

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
%pyproject_extras_subpkg -n python%{python3_pkgversion}-azure-core aio


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