
%global python3_pkgversion 3.11

Name:           python-expandvars
Version:        0.12.0
Release:        %autorelease
Summary:        Expand system variables Unix style

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/sayanarijit/expandvars
Source:         %{pypi_source expandvars}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'expandvars' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-expandvars
Summary:        %{summary}

%description -n python%{python3_pkgversion}-expandvars %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n expandvars-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-expandvars -f %{pyproject_files}


%changelog
%autochangelog