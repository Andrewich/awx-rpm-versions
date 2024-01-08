Name:           python-boto3
Version:        1.26.102
Release:        1%{?dist}
Summary:        The AWS SDK for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/boto/boto3
Source:         %{pypi_source boto3}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'boto3' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-boto3
Summary:        %{summary}

%description -n python3-boto3 %_description


%prep
%autosetup -p1 -n boto3-%{version}


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


%files -n python3-boto3 -f %{pyproject_files}


%changelog
* Mon Jan 08 2024 Martin Juhl <m@rtinjuhl.dk> - 1.26.102-1
- Initial package