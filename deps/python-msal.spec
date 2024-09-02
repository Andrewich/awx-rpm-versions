
%global python3_pkgversion 3.11

Name:           python-msal
Version:        1.26.0
Release:        %autorelease
Summary:        The Microsoft Authentication Library (MSAL) for Python library enables your app to access the Microsoft Cloud by supporting authentication of users with Microsoft Azure Active Directory accounts (AAD) and Microsoft Accounts (MSA) using industry standard OAuth2 and OpenID Connect.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/AzureAD/microsoft-authentication-library-for-python
Source:         %{pypi_source msal}

Patch: 		msal-deps.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(requests) < 3~~ with python%{python3_pkgversion}dist(requests) >= 2)
BuildRequires:  (python%{python3_pkgversion}dist(pyjwt) < 3~~ with python%{python3_pkgversion}dist(pyjwt) >= 1)
BuildRequires:  (python%{python3_pkgversion}dist(cryptography) < 44~~ with python%{python3_pkgversion}dist(cryptography) >= 0.6)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'msal' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-msal
Summary:        %{summary}

%description -n python%{python3_pkgversion}-msal %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-msal broker


%prep
%autosetup -p1 -n msal-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-msal -f %{pyproject_files}


%changelog
%autochangelog