%global debug_package %{nil}
%global python3_pkgversion 3.11

Name:           python-bcrypt
Version:        4.1.3
Release:        %autorelease
Summary:        Modern password hashing for your software and your servers

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/bcrypt/
Source:         %{pypi_source bcrypt}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 42
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-rust)
BuildRequires:  ((python%{python3_pkgversion}dist(pytest) < 3.3 or python%{python3_pkgversion}dist(pytest) > 3.3) with python%{python3_pkgversion}dist(pytest) >= 3.2.1)
BuildRequires:  python%{python3_pkgversion}dist(mypy)
BuildRequires:  gcc
BuildRequires:  rust
BuildRequires:  cargo

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'bcrypt' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-bcrypt
Summary:        %{summary}

%description -n python%{python3_pkgversion}-bcrypt %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-bcrypt tests,typecheck


%prep
%autosetup -p1 -n bcrypt-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-bcrypt -f %{pyproject_files}


%changelog
%autochangelog