
%global python3_pkgversion 3.11

Name:           python-jaraco-context
Version:        4.3.0
Release:        %autorelease
Summary:        Context managers by jaraco

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jaraco/jaraco.context
Source:         %{pypi_source jaraco.context}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 56
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml]) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jaraco-context' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-jaraco-context
Summary:        %{summary}
AutoProv: no
Provides: python%{python3_pkgversion}-jaraco-context = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(jaraco-context) = 4.3
Provides: python%{python3_pkgversion}dist(jaraco.context) = 4.3

%description -n python%{python3_pkgversion}-jaraco-context %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n jaraco.context-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-jaraco-context -f %{pyproject_files}


%changelog
%autochangelog