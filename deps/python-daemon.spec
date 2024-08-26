
%global python3_pkgversion 3.11

Name:           python-daemon
Version:        3.0.1
Release:        %autorelease
Summary:        Library to implement a well-behaved Unix daemon process.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pagure.io/python-daemon/
Source:         %{pypi_source python-daemon}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 62.4
BuildRequires:  python%{python3_pkgversion}dist(docutils)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(lockfile) >= 0.10


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-daemon' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-python-daemon
Summary:        %{summary}

%description -n python%{python3_pkgversion}-python-daemon %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n python-daemon-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-python-daemon -f %{pyproject_files}


%changelog
%autochangelog