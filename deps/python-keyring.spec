
%global python3_pkgversion 3.11

Name:           python-keyring
Version:        24.3.1
Release:        %autorelease
Summary:        Store and access your passwords safely.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jaraco/keyring
Source:         %{pypi_source keyring}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 56
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml]) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(jaraco.classes)
BuildRequires:  python%{python3_pkgversion}dist(importlib-metadata) >= 4.11.4
BuildRequires:  python%{python3_pkgversion}dist(secretstorage) >= 3.2
BuildRequires:  python%{python3_pkgversion}dist(jeepney) >= 0.4.2


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'keyring' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-keyring
Summary:        %{summary}

%description -n python%{python3_pkgversion}-keyring %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n keyring-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/keyring $RPM_BUILD_ROOT/usr/bin/keyring%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/keyring|/usr/bin/keyring%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-keyring -f %{pyproject_files}


%changelog
%autochangelog