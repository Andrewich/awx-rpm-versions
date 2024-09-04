
%global python3_pkgversion 3.11

Name:           python-pytest-runner
Version:        6.0.1
Release:        %autorelease
Summary:        Invoke py.test as distutils command with dependency resolution

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pytest-dev/pytest-runner/
Source:         %{pypi_source pytest-runner}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 56
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml]) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pytest-runner' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pytest-runner
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pytest-runner %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n pytest-runner-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pytest-runner -f %{pyproject_files}


%changelog
%autochangelog