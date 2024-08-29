
%global python3_pkgversion 3.11

Name:           python-gitdb
Version:        4.0.11
Release:        %autorelease
Summary:        Git Object Database

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/gitpython-developers/gitdb
Source:         %{pypi_source gitdb}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(smmap) < 6~~ with python%{python3_pkgversion}dist(smmap) >= 3.0.1)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'gitdb' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-gitdb
Summary:        %{summary}

%description -n python%{python3_pkgversion}-gitdb %_description


%prep
%autosetup -p1 -n gitdb-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-gitdb -f %{pyproject_files}


%changelog
%autochangelog