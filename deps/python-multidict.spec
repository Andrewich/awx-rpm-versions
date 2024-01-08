Name:           python-multidict
Version:        6.0.2
Release:        1%{?dist}
Summary:        multidict implementation

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/aio-libs/multidict
Source:         %{pypi_source multidict}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'multidict' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-multidict
Summary:        %{summary}

%description -n python3-multidict %_description


%prep
%autosetup -p1 -n multidict-%{version}


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


%files -n python3-multidict -f %{pyproject_files}


%changelog
* Mon Jan 08 2024 Martin Juhl <m@rtinjuhl.dk> - 6.0.2-1
- Initial package