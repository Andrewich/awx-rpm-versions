
%global python3_pkgversion 3.11

Name:           python-azure-keyvault
Version:        4.2.0
Release:        %autorelease
Summary:        Microsoft Azure Key Vault Client Libraries for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/keyvault/azure-keyvault
Source:         %{pypi_source azure-keyvault %{version} zip}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(azure-keyvault-certificates) >= 4.4 with python%{python3_pkgversion}dist(azure-keyvault-certificates) < 5)
BuildRequires:  (python%{python3_pkgversion}dist(azure-keyvault-secrets) >= 4.4 with python%{python3_pkgversion}dist(azure-keyvault-secrets) < 5)
BuildRequires:  (python%{python3_pkgversion}dist(azure-keyvault-keys) >= 4.5 with python%{python3_pkgversion}dist(azure-keyvault-keys) < 5)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'azure-keyvault' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-azure-keyvault
Summary:        %{summary}

%description -n python%{python3_pkgversion}-azure-keyvault %_description


%prep
%autosetup -p1 -n azure-keyvault-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-azure-keyvault -f %{pyproject_files}


%changelog
%autochangelog