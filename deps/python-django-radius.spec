
%global python3_pkgversion 3.11

Name:           python-django-radius
Version:        1.5.1
Release:        %autorelease
Summary:        Django authentication backend for RADIUS

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://robgolding63.github.com/django-radius/
Source:         %{pypi_source django-radius}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(asgiref) >= 3.6
BuildRequires:  python%{python3_pkgversion}dist(django) >= 3.2


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-radius' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-radius
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-radius %_description


%prep
%autosetup -p1 -n django-radius-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django-radius -f %{pyproject_files}


%changelog
%autochangelog