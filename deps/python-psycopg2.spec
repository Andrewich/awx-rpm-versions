Name:           python-psycopg2
Version:        2.8.4
Release:        1%{?dist}
Summary:        psycopg2 - Python-PostgreSQL Database Adapter

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://psycopg.org/
Source:         %{pypi_source psycopg2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'psycopg2' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-psycopg2
Summary:        %{summary}

%description -n python3-psycopg2 %_description


%prep
%autosetup -p1 -n psycopg2-%{version}


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


%files -n python3-psycopg2 -f %{pyproject_files}


%changelog
* Tue May 09 2023 Martin Juhl <m@rtinjuhl.dk> - 2.8.4-1
- Initial package