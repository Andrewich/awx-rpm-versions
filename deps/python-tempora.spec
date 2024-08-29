
%global python3_pkgversion 3.11

Name:           python-tempora
Version:        5.5.1
Release:        %autorelease
Summary:        Objects and routines pertaining to date and time (tempora)

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jaraco/tempora
Source:         %{pypi_source tempora}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion}-pytest python%{python3_pkgversion}-freezegun
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 56
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(pytz)
BuildRequires:  python%{python3_pkgversion}dist(jaraco-functools) >= 1.20


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tempora' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-tempora
Summary:        %{summary}

%description -n python%{python3_pkgversion}-tempora %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n tempora-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files

# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/calc-prorate $RPM_BUILD_ROOT/usr/bin/calc-prorate%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/calc-prorate|/usr/bin/calc-prorate%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2

%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-tempora -f %{pyproject_files}


%changelog
%autochangelog