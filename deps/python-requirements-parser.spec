
%global python3_pkgversion 3.11

Name:           python-requirements-parser
Version:        0.9.0
Release:        %autorelease
Summary:        This is a small Python module for parsing Pip requirement files.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/madpah/requirements-parser/#readme
Source:         %{pypi_source requirements_parser}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(poetry-core) >= 1
BuildRequires:  python%{python3_pkgversion}dist(types-setuptools) >= 69.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'requirements-parser' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-requirements-parser
Summary:        %{summary}

%description -n python%{python3_pkgversion}-requirements-parser %_description


%prep
%autosetup -p1 -n requirements_parser-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-requirements-parser -f %{pyproject_files}


%changelog
%autochangelog