
%global python3_pkgversion 3.11

Name:           python-azure-identity
Version:        1.15.0
Release:        %autorelease
Summary:        Microsoft Azure Identity Library for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity
Source:         %{pypi_source azure-identity}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(azure-core) < 2~~ with python%{python3_pkgversion}dist(azure-core) >= 1.23)
BuildRequires:  python%{python3_pkgversion}dist(cryptography) >= 2.5
BuildRequires:  (python%{python3_pkgversion}dist(msal) < 2~~ with python%{python3_pkgversion}dist(msal) >= 1.24)
BuildRequires:  (python%{python3_pkgversion}dist(msal-extensions) < 2~~ with python%{python3_pkgversion}dist(msal-extensions) >= 0.3)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'azure-identity' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-azure-identity
Summary:        %{summary}

%description -n python%{python3_pkgversion}-azure-identity %_description


%prep
%autosetup -p1 -n azure-identity-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-azure-identity -f %{pyproject_files}


%changelog
%autochangelog