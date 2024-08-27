%global debug_package %{nil}
%global python3_pkgversion 3.11

Name:           python-psycopg
Version:        3.1.18
Release:        %autorelease
Summary:        PostgreSQL database adapter for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://psycopg.org/
Source:         %{pypi_source psycopg}
Patch:         psycopg-deps.patch

BuildArch:      x86_64
BuildRequires:  python%{python3_pkgversion}-devel libpq-devel gcc
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 49.2
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(typing-extensions) >= 4.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'psycopg' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-psycopg
Summary:        %{summary}

%description -n python%{python3_pkgversion}-psycopg %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n psycopg-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-psycopg -f %{pyproject_files}


%changelog
%autochangelog