
%global python3_pkgversion 3.11

Name:           python-itypes
Version:        1.2.0
Release:        %autorelease
Summary:        Simple immutable types for python.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://github.com/PavanTatikonda/itypes
Source:         %{pypi_source itypes}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'itypes' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-itypes
Summary:        %{summary}

%description -n python%{python3_pkgversion}-itypes %_description


%prep
%autosetup -p1 -n itypes-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-itypes -f %{pyproject_files}


%changelog
%autochangelog