
%global python3_pkgversion 3.11

Name:           python-versioneer
Version:        0.29
Release:        %autorelease
Summary:        Easy VCS-based management of project version strings

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-versioneer/python-versioneer
Source:         %{pypi_source versioneer}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'versioneer' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-versioneer
Summary:        %{summary}

%description -n python%{python3_pkgversion}-versioneer %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-versioneer toml


%prep
%autosetup -p1 -n versioneer-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-versioneer -f %{pyproject_files}


%changelog
%autochangelog