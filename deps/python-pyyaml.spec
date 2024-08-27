%global debug_package %{nil}

%global python3_pkgversion 3.11

Name:           python-pyyaml
Version:        6.0.1
Release:        %autorelease
Summary:        YAML parser and emitter for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pyyaml.org/
Source:         %{pypi_source PyYAML}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(cython) < 3~~
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyyaml' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pyyaml
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyyaml %_description


%prep
%autosetup -p1 -n PyYAML-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pyyaml -f %{pyproject_files}


%changelog
%autochangelog