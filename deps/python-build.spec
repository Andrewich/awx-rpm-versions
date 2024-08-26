
%global python3_pkgversion 3.11

Name:           python-build
Version:        1.2.1
Release:        %autorelease
Summary:        A simple, correct Python build frontend

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/build/
Source:         %{pypi_source build}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(flit-core) >= 3.8
BuildRequires:  python%{python3_pkgversion}dist(packaging) >= 19.1
BuildRequires:  python%{python3_pkgversion}dist(pyproject-hooks)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'build' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-build
Summary:        %{summary}

%description -n python%{python3_pkgversion}-build %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n build-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/pyproject-build $RPM_BUILD_ROOT/usr/bin/pyproject-build%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/pyproject-build|/usr/bin/pyproject-build%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-build -f %{pyproject_files}


%changelog
%autochangelog