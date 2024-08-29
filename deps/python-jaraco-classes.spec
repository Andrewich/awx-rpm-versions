
%global python3_pkgversion 3.11

Name:           python-jaraco-classes
Version:        3.4.0
Release:        %autorelease
Summary:        Utility functions for Python class constructs

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jaraco/jaraco.classes
Source:         %{pypi_source jaraco.classes}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 56
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(more-itertools)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jaraco-classes' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-jaraco-classes
Summary:        %{summary}

%description -n python%{python3_pkgversion}-jaraco-classes %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n jaraco.classes-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-jaraco-classes -f %{pyproject_files}


%changelog
%autochangelog