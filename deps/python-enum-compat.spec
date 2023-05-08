Name:           python-enum-compat
Version:        0.0.3
Release:        1%{?dist}
Summary:        enum/enum34 compatibility package

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jstasiak/enum-compat
Source:         %{pypi_source enum-compat}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'enum-compat' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-enum-compat
Summary:        %{summary}

%description -n python3-enum-compat %_description


%prep
%autosetup -p1 -n enum-compat-%{version}


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


%files -n python3-enum-compat -f %{pyproject_files}


%changelog
* Tue May 09 2023 Martin Juhl <m@rtinjuhl.dk> - 0.0.3-1
- Initial package