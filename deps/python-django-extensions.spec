
%global python3_pkgversion 3.11

Name:           python-django-extensions
Version:        3.2.3
Release:        %autorelease
Summary:        Extensions for Django

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/django-extensions/django-extensions
Source:         %{pypi_source django-extensions}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(django) >= 3.2


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-extensions' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-extensions
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-extensions %_description


%prep
%autosetup -p1 -n django-extensions-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django-extensions -f %{pyproject_files}


%changelog
%autochangelog