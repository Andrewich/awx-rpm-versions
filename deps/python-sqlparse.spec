
%global python3_pkgversion 3.11

Name:           python-sqlparse
Version:        0.4.4
Release:        %autorelease
Summary:        A non-validating SQL parser.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/sqlparse/
Source:         %{pypi_source sqlparse}
Patch:		sqlparse-python-explicit.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  (python%{python3_pkgversion}dist(flit-core) < 4~~ with python%{python3_pkgversion}dist(flit-core) >= 3.2)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sqlparse' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-sqlparse
Summary:        %{summary}

%description -n python%{python3_pkgversion}-sqlparse %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n sqlparse-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/sqlformat $RPM_BUILD_ROOT/usr/bin/sqlformat%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/sqlformat|/usr/bin/sqlformat%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-sqlparse -f %{pyproject_files}


%changelog
%autochangelog