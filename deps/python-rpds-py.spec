%global debug_package %{nil}
%global python3_pkgversion 3.11

Name:           python-rpds-py
Version:        0.18.0
Release:        %autorelease
Summary:        Python bindings to Rust's persistent data structures (rpds)

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/crate-py/rpds
Source:         %{pypi_source rpds_py}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  (python%{python3_pkgversion}dist(maturin) < 2~~ with python%{python3_pkgversion}dist(maturin) >= 1)
BuildRequires:  gcc
BuildRequires:	rust
BuildRequires:	cargo

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'rpds-py' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-rpds-py
Summary:        %{summary}

%description -n python%{python3_pkgversion}-rpds-py %_description


%prep
%autosetup -p1 -n rpds_py-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-rpds-py -f %{pyproject_files}


%changelog
%autochangelog