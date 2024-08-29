
%global python3_pkgversion 3.11

Name:           python-django-debug-toolbar
Version:        4.4.2
Release:        %autorelease
Summary:        A configurable set of panels that display various debug information about the current request/response.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jazzband/django-debug-toolbar
Source:         %{pypi_source django_debug_toolbar}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)
BuildRequires:  python%{python3_pkgversion}dist(django) >= 4.2.9
BuildRequires:  python%{python3_pkgversion}dist(sqlparse) >= 0.2


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-debug-toolbar' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-debug-toolbar
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-debug-toolbar %_description


%prep
%autosetup -p1 -n django_debug_toolbar-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django-debug-toolbar -f %{pyproject_files}


%changelog
%autochangelog