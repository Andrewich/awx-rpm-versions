
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-drf-yasg
Version:        1.21.7
Release:        %autorelease
Summary:        Automated generation of real Swagger/OpenAPI 2.0 schemas from Django Rest Framework code.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/axnsan12/drf-yasg
Source:         %{pypi_source drf-yasg}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.6.3
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 3.0.3
BuildRequires:  python%{python3_pkgversion}dist(djangorestframework) >= 3.10.3
BuildRequires:  python%{python3_pkgversion}dist(django) >= 2.2.16
BuildRequires:  python%{python3_pkgversion}dist(pyyaml) >= 5.1
BuildRequires:  python%{python3_pkgversion}dist(inflection) >= 0.3.1
BuildRequires:  python%{python3_pkgversion}dist(packaging) >= 21
BuildRequires:  python%{python3_pkgversion}dist(pytz) >= 2021.1
BuildRequires:  python%{python3_pkgversion}dist(uritemplate) >= 3
BuildRequires:  python%{python3_pkgversion}dist(coreapi) >= 2.3.3
BuildRequires:  python%{python3_pkgversion}dist(coreschema) >= 0.0.4
BuildRequires:  python%{python3_pkgversion}dist(swagger-spec-validator) >= 2.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'drf_yasg' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-drf-yasg
Summary:        %{summary}

%description -n python%{python3_pkgversion}-drf-yasg %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-drf-yasg+coreapi
Summary: Metapackage for python%{python3_pkgversion}-drf-yasg: coreapi extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(coreapi) >= 2.3.3
Requires: python%{python3_pkgversion}dist(coreschema) >= 0.0.4
Requires: python%{python3_pkgversion}-drf-yasg = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-drf-yasg+coreapi = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(drf-yasg[coreapi]) = %{version}

%description -n python%{python3_pkgversion}-drf-yasg+coreapi
This is a metapackage bringing in coreapi extras requires for python%{python3_pkgversion}-drf-yasg.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-drf-yasg+coreapi
%ghost %{python3__sitelib}/*.dist-info


%package -n python%{python3_pkgversion}-drf-yasg+validation
Summary: Metapackage for python%{python3_pkgversion}-drf-yasg: validation extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(swagger-spec-validator) >= 2.1
Requires: python%{python3_pkgversion}-drf-yasg = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-drf-yasg+validation = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(drf-yasg[validation]) = %{version}

%description -n python%{python3_pkgversion}-drf-yasg+validation
This is a metapackage bringing in validation extras requires for python%{python3_pkgversion}-drf-yasg.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-drf-yasg+validation
%ghost %{python3__sitelib}/*.dist-info


%prep
%autosetup -p1 -n drf-yasg-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-drf-yasg -f %{pyproject_files}


%changelog
%autochangelog