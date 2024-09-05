
%global python3_pkgversion 3.11

Name:           python-jaraco-logging
Version:        3.3.0
Release:        %autorelease
Summary:        Support for Python logging facility

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jaraco/jaraco.logging
Source:         %{pypi_source jaraco.logging}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 56
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml]) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(tempora)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jaraco-logging' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-jaraco-logging
Summary:        %{summary}
AutoProv: no
Provides: python%{python3_pkgversion}-jaraco-logging = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(jaraco-logging) = 3.3
Provides: python%{python3_pkgversion}dist(jaraco.logging) = 3.3

%description -n python%{python3_pkgversion}-jaraco-logging %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n jaraco.logging-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-jaraco-logging -f %{pyproject_files}


%changelog
%autochangelog