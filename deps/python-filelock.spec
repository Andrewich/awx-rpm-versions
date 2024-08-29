
%global python3_pkgversion 3.11

Name:           python-filelock
Version:        3.13.1
Release:        %autorelease
Summary:        A platform independent file lock.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/tox-dev/py-filelock
Source:         %{pypi_source filelock}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatch-vcs) >= 0.3
BuildRequires:  python%{python3_pkgversion}dist(hatchling) >= 1.18


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'filelock' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-filelock
Summary:        %{summary}

%description -n python%{python3_pkgversion}-filelock %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n filelock-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-filelock -f %{pyproject_files}


%changelog
%autochangelog