Name:           python-daemon
Version:        3.0.1
Release:        1%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pagure.io/python-daemon/
Source:         %{pypi_source python-daemon}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-daemon' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-python-daemon
Summary:        %{summary}

%description -n python3-python-daemon %_description


%prep
%autosetup -p1 -n python-daemon-%{version}


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


%files -n python3-python-daemon -f %{pyproject_files}


%changelog
* Mon Jan 08 2024 Martin Juhl <m@rtinjuhl.dk> - 3.0.1-1
- Initial package