
%global python3_pkgversion 3.11

Name:           python-jaraco-stream
Version:        3.0.3
Release:        %autorelease
Summary:        routines for dealing with data streams

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jaraco/jaraco.stream
Source:         %{pypi_source jaraco.stream}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 56
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml]) >= 3.4.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jaraco-stream' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-jaraco-stream
Summary:        %{summary}

%description -n python%{python3_pkgversion}-jaraco-stream %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n jaraco.stream-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-jaraco-stream -f %{pyproject_files}


%changelog
%autochangelog