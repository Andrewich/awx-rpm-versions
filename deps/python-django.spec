%undefine __brp_mangle_shebangs
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-django
Version:        4.2.10
Release:        %autorelease
Summary:        A high-level Python web framework that encourages rapid development and clean, pragmatic design.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://www.djangoproject.com/
Source:         %{pypi_source Django}

Patch: 		django-deps.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(asgiref) < 4~~ with python%{python3_pkgversion}dist(asgiref) >= 3.6)
BuildRequires:  python%{python3_pkgversion}dist(sqlparse) >= 0.3.1
BuildRequires:  python%{python3_pkgversion}dist(bcrypt)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-django+bcrypt
Summary: Metapackage for python%{python3_pkgversion}-django: bcrypt extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(bcrypt)
Requires: python%{python3_pkgversion}-django = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-django+bcrypt = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(django[bcrypt]) = %{version}

%description -n python%{python3_pkgversion}-django+bcrypt
This is a metapackage bringing in bcrypt extras requires for python%{python3_pkgversion}-django.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-django+bcrypt
%ghost %{python3__sitelib}/*.dist-info


%prep
%autosetup -p1 -n Django-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/django-admin $RPM_BUILD_ROOT/usr/bin/django-admin%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/django-admin|/usr/bin/django-admin%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django -f %{pyproject_files}


%changelog
%autochangelog