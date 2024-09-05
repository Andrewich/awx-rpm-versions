
%global python3_pkgversion 3.11

Name:           python-django-guid
Version:        3.2.1
Release:        %autorelease
Summary:        Middleware that enables single request-response cycle tracing by injecting a unique ID into project logs

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/snok/django-guid
Source:         %{pypi_source django-guid}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(poetry) >= 0.12
BuildRequires:  (python%{python3_pkgversion}dist(django) < 5~~ with python%{python3_pkgversion}dist(django) >= 3.1.1)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-guid' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-guid
Summary:        %{summary}
AutoReq: no
Requires: (python%{python3_pkgversion}dist(django) < 5 with python%{python3_pkgversion}dist(django) >= 3.1.1)
Requires: python(abi) = %{python3_pkgversion}

%description -n python%{python3_pkgversion}-django-guid %_description


%prep
%autosetup -p1 -n django-guid-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django-guid -f %{pyproject_files}


%changelog
%autochangelog