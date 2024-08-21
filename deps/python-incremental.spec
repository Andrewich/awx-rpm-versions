
%global python3_pkgversion 3.11

Name:           python-incremental
Version:        22.10.0
Release:        %autorelease
Summary:        "A small library that versions your Python projects."

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/twisted/incremental
Source:         %{pypi_source incremental}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 44.1.1
BuildRequires:  python%{python3_pkgversion}dist(wheel) >= 0.36.2


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'incremental' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-incremental
Summary:        %{summary}

%description -n python%{python3_pkgversion}-incremental %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n incremental-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-incremental -f %{pyproject_files}


%changelog
%autochangelog