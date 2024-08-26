
%global python3_pkgversion 3.11

Name:           python-annotated-types
Version:        0.6.0
Release:        %autorelease
Summary:        Reusable constraint types to use with typing.Annotated

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/annotated-types/
Source:         %{pypi_source annotated_types}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'annotated-types' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-annotated-types
Summary:        %{summary}

%description -n python%{python3_pkgversion}-annotated-types %_description


%prep
%autosetup -p1 -n annotated_types-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-annotated-types -f %{pyproject_files}


%changelog
%autochangelog