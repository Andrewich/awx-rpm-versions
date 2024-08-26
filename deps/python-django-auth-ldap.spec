
%global python3_pkgversion 3.11

Name:           python-django-auth-ldap
Version:        4.8.0
Release:        %autorelease
Summary:        Django LDAP authentication backend

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/django-auth-ldap/django-auth-ldap
Source:         %{pypi_source django-auth-ldap}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 42
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 3.4
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml]) >= 3.4
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(django) >= 3.2
BuildRequires:  python%{python3_pkgversion}dist(python-ldap) >= 3.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-auth-ldap' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-auth-ldap
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-auth-ldap %_description


%prep
%autosetup -p1 -n django-auth-ldap-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django-auth-ldap -f %{pyproject_files}


%changelog
%autochangelog