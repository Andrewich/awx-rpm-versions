Name:           python-pytz
Version:        2021.3
Release:        1%{?dist}
Summary:        World timezone definitions, modern and historical

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://pythonhosted.org/pytz
Source:         %{pypi_source pytz}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pytz' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-pytz
Summary:        %{summary}

%description -n python3-pytz %_description


%prep
%autosetup -p1 -n pytz-%{version}


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


%files -n python3-pytz -f %{pyproject_files}


%changelog
* Tue May 09 2023 Martin Juhl <m@rtinjuhl.dk> - 2021.3-1
- Initial package