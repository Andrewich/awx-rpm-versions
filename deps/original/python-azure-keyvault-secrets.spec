
%global python3_pkgversion 3.11

Name:           python-azure-keyvault-secrets
Version:        4.7.0
Release:        %autorelease
Summary:        Microsoft Azure Key Vault Secrets Client Library for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/keyvault/azure-keyvault-secrets
Source:         %{pypi_source azure-keyvault-secrets %{version} zip}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'azure-keyvault-secrets' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-azure-keyvault-secrets
Summary:        %{summary}

%description -n python%{python3_pkgversion}-azure-keyvault-secrets %_description


%prep
%autosetup -p1 -n azure-keyvault-secrets-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-azure-keyvault-secrets -f %{pyproject_files}


%changelog
%autochangelog