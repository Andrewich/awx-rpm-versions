
%global python3_pkgversion 3.11

Name:           python-daphne
Version:        3.0.2
Release:        %autorelease
Summary:        Django ASGI (HTTP/WebSocket) server

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/django/daphne
Source:         %{pypi_source daphne}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(pytest-runner)
BuildRequires:  python%{python3_pkgversion}dist(twisted) >= 18.7
BuildRequires:  python%{python3_pkgversion}dist(twisted[tls]) >= 18.7
BuildRequires:  python%{python3_pkgversion}dist(autobahn) >= 0.18
BuildRequires:  (python%{python3_pkgversion}dist(asgiref) < 4~~ with python%{python3_pkgversion}dist(asgiref) >= 3.2.10)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'daphne' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-daphne
Summary:        %{summary}

%description -n python%{python3_pkgversion}-daphne %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n daphne-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/daphne $RPM_BUILD_ROOT/usr/bin/daphne%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/daphne|/usr/bin/daphne%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-daphne -f %{pyproject_files}


%changelog
%autochangelog