
%global python3_pkgversion 3.11

Name:           python-cffi
Version:        1.16.0
Release:        %autorelease
Summary:        Foreign Function Interface for Python calling C code.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://cffi.readthedocs.org
Source:         %{pypi_source cffi}

BuildArch:      x86_64
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 66.1
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(pycparser)
BuildRequires:  gcc
BuildRequires:  libffi-devel

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cffi' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-cffi
Summary:        %{summary}

%description -n python%{python3_pkgversion}-cffi %_description


%prep
%autosetup -p1 -n cffi-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-cffi -f %{pyproject_files}


%changelog
%autochangelog