%global debug_package %{nil}
%global python3_pkgversion 3.11

Name:           python-pydantic
Version:        2.5.0
Release:        %autorelease
Summary:        Data validation using Python type hints

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pydantic/pydantic
Source:         %{pypi_source pydantic}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)
BuildRequires:  python%{python3_pkgversion}dist(hatch-fancy-pypi-readme) >= 22.5
BuildRequires:  python%{python3_pkgversion}dist(annotated-types) >= 0.4
BuildRequires:  python%{python3_pkgversion}dist(pydantic-core) = 2.14.1
BuildRequires:  python%{python3_pkgversion}dist(typing-extensions) >= 4.6.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pydantic' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pydantic
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pydantic %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n pydantic-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pydantic -f %{pyproject_files}


%changelog
%autochangelog