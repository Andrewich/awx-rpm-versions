%global debug_package %{nil}

%global python3_pkgversion 3.11

Name:           python-pydantic-core
Version:        2.14.1
Release:        %autorelease
Summary:        ...

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pydantic/pydantic-core
Source:         %{pypi_source pydantic_core}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  (python%{python3_pkgversion}dist(maturin) < 2~~ with python%{python3_pkgversion}dist(maturin) >= 1)
BuildRequires:  ((python%{python3_pkgversion}dist(typing-extensions) < 4.7 or python%{python3_pkgversion}dist(typing-extensions) > 4.7) with python%{python3_pkgversion}dist(typing-extensions) >= 4.6)
BuildRequires:  gcc
BuildRequires:  rust
BuildRequires:  cargo

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pydantic-core' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pydantic-core
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pydantic-core %_description


%prep
%autosetup -p1 -n pydantic_core-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pydantic-core -f %{pyproject_files}


%changelog
%autochangelog