Name:           python-pygerduty
Version:        0.38.2
Release:        1%{?dist}
Summary:        Python Client Library for PagerDuty's REST API

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/dropbox/pygerduty
Source:         %{pypi_source pygerduty}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pygerduty' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-pygerduty
Summary:        %{summary}

%description -n python3-pygerduty %_description


%prep
%autosetup -p1 -n pygerduty-%{version}


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


%files -n python3-pygerduty -f %{pyproject_files}


%changelog
* Tue May 09 2023 Martin Juhl <m@rtinjuhl.dk> - 0.38.2-1
- Initial package