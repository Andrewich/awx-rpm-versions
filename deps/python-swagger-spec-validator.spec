
%global python3_pkgversion 3.11

Name:           python-swagger-spec-validator
Version:        3.0.4
Release:        %autorelease
Summary:        Validation of Swagger specifications

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://github.com/Yelp/swagger_spec_validator
Source:         %{pypi_source swagger_spec_validator}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(jsonschema)
BuildRequires:  python%{python3_pkgversion}dist(pyyaml)
BuildRequires:  python%{python3_pkgversion}dist(typing-extensions)
BuildRequires:  python%{python3_pkgversion}dist(importlib-resources) >= 1.3


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'swagger-spec-validator' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-swagger-spec-validator
Summary:        %{summary}

%description -n python%{python3_pkgversion}-swagger-spec-validator %_description


%prep
%autosetup -p1 -n swagger_spec_validator-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-swagger-spec-validator -f %{pyproject_files}


%changelog
%autochangelog