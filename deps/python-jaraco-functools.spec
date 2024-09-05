
%global python3_pkgversion 3.11

Name:           python-jaraco-functools
Version:        4.0.0
Release:        %autorelease
Summary:        Functools like those found in stdlib

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jaraco/jaraco.functools
Source:         %{pypi_source jaraco.functools}

BuildArch:      noarch

AutoProv: no
Provides: python%{python3_pkgversion}-jaraco-functools = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(jaraco-functools) = 4
Provides: python%{python3_pkgversion}dist(jaraco.functools) = 4

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 56
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml]) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(more-itertools)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jaraco-functools' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-jaraco-functools
Summary:        %{summary}

%description -n python%{python3_pkgversion}-jaraco-functools %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n jaraco.functools-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-jaraco-functools -f %{pyproject_files}


%changelog
%autochangelog