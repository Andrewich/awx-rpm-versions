Name:           python-django
Version:        4.2.6
Release:        1%{?dist}
Summary:        A high-level Python web framework that encourages rapid development and clean, pragmatic design.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://www.djangoproject.com/
Source:         %{pypi_source Django}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-django
Summary:        %{summary}

%description -n python3-django %_description


%prep
%autosetup -p1 -n Django-%{version}


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


%files -n python3-django -f %{pyproject_files}


%changelog
* Mon Jan 08 2024 Martin Juhl <m@rtinjuhl.dk> - 4.2.6-1
- Initial package