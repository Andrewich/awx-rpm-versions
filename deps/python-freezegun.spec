
%global python3_pkgversion 3.11

Name:           python-freezegun
Version:        1.5.1
Release:        %autorelease
Summary:        Let your Python tests travel through time

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/spulec/freezegun
Source:         %{pypi_source freezegun}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(python-dateutil) >= 2.7


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'freezegun' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-freezegun
Summary:        %{summary}

%description -n python%{python3_pkgversion}-freezegun %_description


%prep
%autosetup -p1 -n freezegun-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-freezegun -f %{pyproject_files}


%changelog
%autochangelog