%global python3_pkgversion 3.11
%global python3_sitelib /usr/lib64/python%{python3_pkgversion}/site-packages

Name:           python-uwsgi
Version:        2.0.26
Release:        %autorelease
Summary:        The uWSGI server

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://uwsgi-docs.readthedocs.io/en/latest/
Source:         %{pypi_source uwsgi}

BuildArch:      x86_64

BuildRequires:  python%{python3_pkgversion}-devel gcc
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'uwsgi' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-uwsgi
Summary:        %{summary}

%description -n python%{python3_pkgversion}-uwsgi %_description


%prep
%autosetup -p1 -n uwsgi-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
#touch $RPM_BUILD_ROOT/usr/lib/python%{python3_pkgversion}/site-packages/uWSGI-%{version}.dist-info/RECORD
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/uwsgi $RPM_BUILD_ROOT/usr/bin/uwsgi%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/uwsgi|/usr/bin/uwsgi%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-uwsgi -f %{pyproject_files}
/usr/lib/python%{python3_pkgversion}/site-packages/__pycache__/uwsgidecorators*

%changelog
%autochangelog