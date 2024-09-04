
%global python3_pkgversion 3.11

Name:           python-twine
Version:        5.1.1
Release:        %autorelease
Summary:        Collection of utilities for publishing packages on PyPI

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://twine.readthedocs.io/
Source:         %{pypi_source twine}

Patch: twine-pkginfo-versionfix.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 61.2
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 6
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml]) >= 6
BuildRequires:  python%{python3_pkgversion}dist(readme-renderer) >= 35
BuildRequires:  python%{python3_pkgversion}dist(requests) >= 2.20
BuildRequires:  ((python%{python3_pkgversion}dist(requests-toolbelt) < 0.9 or python%{python3_pkgversion}dist(requests-toolbelt) > 0.9) with python%{python3_pkgversion}dist(requests-toolbelt) >= 0.8)
BuildRequires:  python%{python3_pkgversion}dist(urllib3) >= 1.26
BuildRequires:  python%{python3_pkgversion}dist(importlib-metadata) >= 3.6
BuildRequires:  python%{python3_pkgversion}dist(keyring) >= 15.1
BuildRequires:  python%{python3_pkgversion}dist(rfc3986) >= 1.4
BuildRequires:  python%{python3_pkgversion}dist(rich) >= 12
BuildRequires:  python%{python3_pkgversion}dist(pkginfo) <= 1.11.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'twine' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-twine
Summary:        %{summary}

%description -n python%{python3_pkgversion}-twine %_description


%prep
%autosetup -p1 -n twine-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/twine $RPM_BUILD_ROOT/usr/bin/twine%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/twine|/usr/bin/twine%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-twine -f %{pyproject_files}


%changelog
%autochangelog
