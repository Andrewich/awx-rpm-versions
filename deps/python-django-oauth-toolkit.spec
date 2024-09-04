
%global python3_pkgversion 3.11

Name:           python-django-oauth-toolkit
Version:        1.7.1
Release:        %autorelease
Summary:        OAuth2 Provider for Django

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jazzband/django-oauth-toolkit
Source:         %{pypi_source django-oauth-toolkit}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  ((python%{python3_pkgversion}dist(django) < 4 or python%{python3_pkgversion}dist(django) > 4) with python%{python3_pkgversion}dist(django) >= 2.2)
BuildRequires:  python%{python3_pkgversion}dist(requests) >= 2.13
BuildRequires:  python%{python3_pkgversion}dist(oauthlib) >= 3.1
BuildRequires:  python%{python3_pkgversion}dist(jwcrypto) >= 0.8


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-oauth-toolkit' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-oauth-toolkit
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-oauth-toolkit %_description


%prep
%autosetup -p1 -n django-oauth-toolkit-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django-oauth-toolkit -f %{pyproject_files}


%changelog
%autochangelog