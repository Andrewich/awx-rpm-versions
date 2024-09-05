
%global python3_pkgversion 3.11

Name:           python-jsonschema
Version:        4.21.1
Release:        %autorelease
Summary:        An implementation of JSON Schema validation for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-jsonschema/jsonschema
Source:         %{pypi_source jsonschema}

Patch: 		jsonschema-deps.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)
BuildRequires:  python%{python3_pkgversion}dist(hatch-vcs)
BuildRequires:  python%{python3_pkgversion}dist(hatch-fancy-pypi-readme)
BuildRequires:  python%{python3_pkgversion}dist(attrs) >= 22.2
BuildRequires:  python%{python3_pkgversion}dist(jsonschema-specifications) >= 2023.3.6
BuildRequires:  python%{python3_pkgversion}dist(referencing) >= 0.28.4
BuildRequires:  python%{python3_pkgversion}dist(rpds-py) >= 0.7.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jsonschema' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-jsonschema
Summary:        %{summary}

%description -n python%{python3_pkgversion}-jsonschema %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n jsonschema-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/jsonschema $RPM_BUILD_ROOT/usr/bin/jsonschema%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/jsonschema|/usr/bin/jsonschema%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-jsonschema -f %{pyproject_files}


%changelog
%autochangelog