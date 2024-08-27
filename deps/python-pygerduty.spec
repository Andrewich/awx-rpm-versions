
%global python3_pkgversion 3.11

Name:           python-pygerduty
Version:        0.38.3
Release:        %autorelease
Summary:        Python Client Library for PagerDuty's REST API

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/dropbox/pygerduty
Source:         %{pypi_source pygerduty}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(six)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pygerduty' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pygerduty
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pygerduty %_description


%prep
%autosetup -p1 -n pygerduty-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/grab_oncall.py $RPM_BUILD_ROOT/usr/bin/grab_oncall.py%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/grab_oncall.py|/usr/bin/grab_oncall.py%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pygerduty -f %{pyproject_files}


%changelog
%autochangelog