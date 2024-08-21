
%global python3_pkgversion 3.11

Name:           python-pbr
Version:        6.0.0
Release:        %autorelease
Summary:        Python Build Reasonableness

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://docs.openstack.org/pbr/latest/
Source:         %{pypi_source pbr}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pbr' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pbr
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pbr %_description


%prep
%autosetup -p1 -n pbr-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/pbr $RPM_BUILD_ROOT/usr/bin/pbr%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/pbr|/usr/bin/pbr%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pbr -f %{pyproject_files}


%changelog
%autochangelog