
%global python3_pkgversion 3.11

Name:           python-openapi-codec
Version:        1.3.2
Release:        %autorelease
Summary:        An OpenAPI codec for Core API.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://github.com/core-api/python-openapi-codec/
Source:         %{pypi_source openapi-codec}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(coreapi) >= 2.2


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'openapi-codec' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-openapi-codec
Summary:        %{summary}

%description -n python%{python3_pkgversion}-openapi-codec %_description


%prep
%autosetup -p1 -n openapi-codec-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-openapi-codec -f %{pyproject_files}


%changelog
%autochangelog