
%global python3_pkgversion 3.11

Name:           python-irc
Version:        20.3.1
Release:        %autorelease
Summary:        IRC (Internet Relay Chat) protocol library for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jaraco/irc
Source:         %{pypi_source irc}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 56
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml]) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(jaraco-collections)
BuildRequires:  python%{python3_pkgversion}dist(jaraco-text) >= 3.10
BuildRequires:  python%{python3_pkgversion}dist(jaraco-logging)
BuildRequires:  python%{python3_pkgversion}dist(jaraco-functools) >= 1.20
BuildRequires:  python%{python3_pkgversion}dist(jaraco-stream)
BuildRequires:  python%{python3_pkgversion}dist(pytz)
BuildRequires:  python%{python3_pkgversion}dist(more-itertools)
BuildRequires:  python%{python3_pkgversion}dist(tempora) >= 1.6


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'irc' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-irc
Summary:        %{summary}

%description -n python%{python3_pkgversion}-irc %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n irc-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-irc -f %{pyproject_files}


%changelog
%autochangelog