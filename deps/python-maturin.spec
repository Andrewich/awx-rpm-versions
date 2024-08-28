
%global python3_pkgversion 3.11
%define  debug_package %{nil}

Name:           python-maturin
Version:        1.6.0
Release:        %autorelease
Summary:        Build and publish crates with pyo3, cffi and uniffi bindings as well as rust binaries as python packages

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pyo3/maturin
Source:         %{pypi_source maturin}
Patch:		maturin-pythonver.patch

BuildArch:      x86_64
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel) >= 0.36.2
BuildRequires:  python%{python3_pkgversion}dist(setuptools-rust) >= 1.4
BuildRequires:	rust cargo


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'maturin' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-maturin
Summary:        %{summary}

%description -n python%{python3_pkgversion}-maturin %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n maturin-%{version}


%build
sed -i "s|¤PYTHON_VER¤|%{python3_pkgversion}|g" maturin/__init__.py 
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/maturin $RPM_BUILD_ROOT/usr/bin/maturin%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/maturin|/usr/bin/maturin%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-maturin -f %{pyproject_files}


%changelog
%autochangelog