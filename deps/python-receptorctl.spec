
%global python3_pkgversion 3.11

Name:           python-receptorctl
Version:        1.4.4
Release:        %autorelease
Summary:        "Receptorctl is a front-end CLI and importable Python library that interacts with Receptor over its control socket interface."

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://ansible.readthedocs.io/projects/receptor/
Source:         %{pypi_source receptorctl}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(python-dateutil)
BuildRequires:  python%{python3_pkgversion}dist(click)
BuildRequires:  python%{python3_pkgversion}dist(pyyaml)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'receptorctl' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-receptorctl
Summary:        %{summary}

%description -n python%{python3_pkgversion}-receptorctl %_description


%prep
%autosetup -p1 -n receptorctl-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/receptorctl $RPM_BUILD_ROOT/usr/bin/receptorctl%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/receptorctl|/usr/bin/receptorctl%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-receptorctl -f %{pyproject_files}


%changelog
%autochangelog