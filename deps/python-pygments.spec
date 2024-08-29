
%global python3_pkgversion 3.11

Name:           python-pygments
Version:        2.18.0
Release:        %autorelease
Summary:        Pygments is a syntax highlighting package written in Python.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pygments.org
Source:         %{pypi_source pygments}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pygments' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pygments
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pygments %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n pygments-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/pygmentize $RPM_BUILD_ROOT/usr/bin/pygmentize%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/pygmentize|/usr/bin/pygmentize%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pygments -f %{pyproject_files}


%changelog
%autochangelog