
%global python3_pkgversion 3.11

Name:           python-django-crum
Version:        0.7.9
Release:        %autorelease
Summary:        Django middleware to capture current request and user.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/ninemoreminutes/django-crum/
Source:         %{pypi_source django-crum}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(pytest-runner)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-twine)
BuildRequires:  python%{python3_pkgversion}dist(django) >= 1.8


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-crum' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-crum
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-crum %_description


%prep
%autosetup -p1 -n django-crum-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django-crum -f %{pyproject_files}


%changelog
%autochangelog