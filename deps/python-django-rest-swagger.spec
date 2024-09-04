
%global python3_pkgversion 3.11

Name:           python-django-rest-swagger
Version:        2.2.0
Release:        %autorelease
Summary:        Swagger UI for Django REST Framework 3.5+

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/marcgibbons/django-rest-swagger
Source:         %{pypi_source django-rest-swagger}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(coreapi) >= 2.3
BuildRequires:  python%{python3_pkgversion}dist(openapi-codec) >= 1.3.1
BuildRequires:  python%{python3_pkgversion}dist(djangorestframework) >= 3.5.4
BuildRequires:  python%{python3_pkgversion}dist(simplejson)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-rest-swagger' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-rest-swagger
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-rest-swagger %_description


%prep
%autosetup -p1 -n django-rest-swagger-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django-rest-swagger -f %{pyproject_files}


%changelog
%autochangelog