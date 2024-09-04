
%global python3_pkgversion 3.11

Name:           python-jsonschema-specifications
Version:        2023.12.1
Release:        %autorelease
Summary:        The JSON Schema meta-schemas and vocabularies, exposed as a Registry

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-jsonschema/jsonschema-specifications
Source:         %{pypi_source jsonschema_specifications}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)
BuildRequires:  python%{python3_pkgversion}dist(hatch-vcs)
BuildRequires:  python%{python3_pkgversion}dist(referencing) >= 0.31


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jsonschema-specifications' generated automatically by
pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-jsonschema-specifications
Summary:        %{summary}

%description -n python%{python3_pkgversion}-jsonschema-specifications %_description


%prep
%autosetup -p1 -n jsonschema_specifications-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-jsonschema-specifications -f %{pyproject_files}


%changelog
%autochangelog