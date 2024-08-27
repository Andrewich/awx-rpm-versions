
%global python3_pkgversion 3.11

Name:           python-pluggy
Version:        1.5.0
Release:        %autorelease
Summary:        plugin and hook calling mechanisms for python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pytest-dev/pluggy
Source:         %{pypi_source pluggy}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 45
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 6.2.3
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pluggy' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pluggy
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pluggy %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n pluggy-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pluggy -f %{pyproject_files}


%changelog
%autochangelog