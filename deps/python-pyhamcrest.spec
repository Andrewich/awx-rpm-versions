
%global python3_pkgversion 3.11

Name:           python-pyhamcrest
Version:        2.1.0
Release:        %autorelease
Summary:        Hamcrest framework for matcher objects

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/PyHamcrest/
Source:         %{pypi_source pyhamcrest}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)
BuildRequires:  python%{python3_pkgversion}dist(hatch-vcs)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyhamcrest' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pyhamcrest
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyhamcrest %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n pyhamcrest-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pyhamcrest -f %{pyproject_files}


%changelog
%autochangelog