%global python3_pkgversion 3.11

Name:           python-enum34
Version:        1.1.10
Release:        %autorelease
Summary:        Python 3.4 Enum backported to 3.3, 3.2, 3.1, 2.7, 2.6, 2.5, and 2.4

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        bsd
URL:            https://bitbucket.org/stoneleaf/enum34
Source:         %{pypi_source enum34}

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'enum34' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-enum34
Summary:        %{summary}

%description -n python%{python3_pkgversion}-enum34 %_description


%prep
%autosetup -p1 -n enum34-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-enum34 -f %{pyproject_files}


%changelog
%autochangelog