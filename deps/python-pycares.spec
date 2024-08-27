
%global python3_pkgversion 3.11

Name:           python-pycares
Version:        4.4.0
Release:        %autorelease
Summary:        Python interface for c-ares

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://github.com/saghul/pycares
Source:         %{pypi_source pycares}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(cffi) >= 1.5
BuildRequires:  python%{python3_pkgversion}dist(idna) >= 2.1
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pycares' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pycares
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pycares %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-pycares idna


%prep
%autosetup -p1 -n pycares-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pycares -f %{pyproject_files}


%changelog
%autochangelog