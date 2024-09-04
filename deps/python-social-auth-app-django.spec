
%global python3_pkgversion 3.11

Name:           python-social-auth-app-django
Version:        5.4.0
Release:        %autorelease
Summary:        Python Social Authentication, Django integration.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-social-auth/social-app-django
Source:         %{pypi_source social-auth-app-django}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(django) >= 3.2
BuildRequires:  python%{python3_pkgversion}dist(social-auth-core) >= 4.4.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'social-auth-app-django' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-social-auth-app-django
Summary:        %{summary}

%description -n python%{python3_pkgversion}-social-auth-app-django %_description


%prep
%autosetup -p1 -n social-auth-app-django-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-social-auth-app-django -f %{pyproject_files}


%changelog
%autochangelog