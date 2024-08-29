
%global python3_pkgversion 3.11

Name:           python-django-pglocks
Version:        1.0.4
Release:        %autorelease
Summary:        django_pglocks provides useful context managers for advisory locks for PostgreSQL.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/Xof/django-pglocks
Source:         %{pypi_source django-pglocks}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(six) >= 1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-pglocks' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-pglocks
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-pglocks %_description


%prep
%autosetup -p1 -n django-pglocks-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django-pglocks -f %{pyproject_files}


%changelog
%autochangelog