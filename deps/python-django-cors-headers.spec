
%global python3_pkgversion 3.11

Name:           python-django-cors-headers
Version:        4.3.1
Release:        %autorelease
Summary:        django-cors-headers is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/django-cors-headers/
Source:         %{pypi_source django-cors-headers}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(asgiref) >= 3.6
BuildRequires:  python%{python3_pkgversion}dist(django) >= 3.2


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-cors-headers' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-cors-headers
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-cors-headers %_description


%prep
%autosetup -p1 -n django-cors-headers-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django-cors-headers -f %{pyproject_files}


%changelog
%autochangelog