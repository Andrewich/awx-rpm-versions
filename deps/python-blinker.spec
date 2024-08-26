
%global python3_pkgversion 3.11

Name:           python-blinker
Version:        1.8.2
Release:        %autorelease
Summary:        Fast, simple object-to-object and broadcast signaling

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/blinker/
Source:         %{pypi_source blinker}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(flit-core) < 4~~


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'blinker' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-blinker
Summary:        %{summary}

%description -n python%{python3_pkgversion}-blinker %_description


%prep
%autosetup -p1 -n blinker-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-blinker -f %{pyproject_files}


%changelog
%autochangelog