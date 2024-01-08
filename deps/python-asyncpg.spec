Name:           python-asyncpg
Version:        0.27.0
Release:        1%{?dist}
Summary:        An asyncio PostgreSQL driver

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/asyncpg/
Source:         %{pypi_source asyncpg}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'asyncpg' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-asyncpg
Summary:        %{summary}

%description -n python3-asyncpg %_description


%prep
%autosetup -p1 -n asyncpg-%{version}


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


%files -n python3-asyncpg -f %{pyproject_files}


%changelog
* Mon Jan 08 2024 Martin Juhl <m@rtinjuhl.dk> - 0.27.0-1
- Initial package