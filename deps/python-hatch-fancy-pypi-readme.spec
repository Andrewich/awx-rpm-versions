
%global python3_pkgversion 3.11

Name:           python-hatch-fancy-pypi-readme
Version:        24.1.0
Release:        %autorelease
Summary:        Fancy PyPI READMEs with Hatch

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/hatch-fancy-pypi-readme/
Source:         %{pypi_source hatch_fancy_pypi_readme}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'hatch-fancy-pypi-readme' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-hatch-fancy-pypi-readme
Summary:        %{summary}

%description -n python%{python3_pkgversion}-hatch-fancy-pypi-readme %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n hatch_fancy_pypi_readme-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/hatch-fancy-pypi-readme $RPM_BUILD_ROOT/usr/bin/hatch-fancy-pypi-readme%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/hatch-fancy-pypi-readme|/usr/bin/hatch-fancy-pypi-readme%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-hatch-fancy-pypi-readme -f %{pyproject_files}


%changelog
%autochangelog