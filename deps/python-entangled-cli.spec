Name:           python-entangled-cli
Version:        2.0.2
Release:        %autorelease
Summary:        Literate Programming toolbox

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://entangled.github.io/
Source:         %{pypi_source entangled_cli}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'entangled-cli' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-entangled-cli
Summary:        %{summary}

%description -n python3-entangled-cli %_description


%prep
%autosetup -p1 -n entangled_cli-%{version}


%generate_buildrequires
%pyproject_buildrequires -x rich


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-entangled-cli -f %{pyproject_files}


%changelog
%autochangelog
