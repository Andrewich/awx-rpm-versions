
%global python3_pkgversion 3.11

Name:           python-cython
Version:        0.29.37
Release:        %autorelease
Summary:        The Cython compiler for writing C extensions for the Python language.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://cython.org/
Source:         %{pypi_source Cython}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cython' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-cython
Summary:        %{summary}

%description -n python%{python3_pkgversion}-cython %_description


%prep
%autosetup -p1 -n Cython-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files

# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/cython $RPM_BUILD_ROOT/usr/bin/cython%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/cygdb $RPM_BUILD_ROOT/usr/bin/cygdb%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/cythonize $RPM_BUILD_ROOT/usr/bin/cythonize%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/cython$|/usr/bin/cython%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/cygdb$|/usr/bin/cygdb%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/cythonize$|/usr/bin/cythonize%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2




%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-cython -f %{pyproject_files}


%changelog
%autochangelog