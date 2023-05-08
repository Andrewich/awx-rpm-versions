Name:           python-idna
Version:        2.9
Release:        1%{?dist}
Summary:        Internationalized Domain Names in Applications (IDNA)

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/idna/
Source:         %{pypi_source idna}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'idna' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-idna
Summary:        %{summary}

%description -n python3-idna %_description


%prep
%autosetup -p1 -n idna-%{version}


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


%files -n python3-idna -f %{pyproject_files}


%changelog
* Tue May 09 2023 Martin Juhl <m@rtinjuhl.dk> - 2.9-1
- Initial package