
%global python3_pkgversion 3.11

Name:           python-dateutil
Version:        2.9.0^post0
Release:        %autorelease
Summary:        Extensions to the standard Python datetime module

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/dateutil/dateutil
Source:         %{pypi_source python-dateutil 2.9.0.post0}

Patch: 		dateutil-deps.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm)
BuildRequires:  python%{python3_pkgversion}dist(six) >= 1.5


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-dateutil' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-python-dateutil
Summary:        %{summary}

%description -n python%{python3_pkgversion}-python-dateutil %_description


%prep
%autosetup -p1 -n python-dateutil-2.9.0.post0


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-python-dateutil -f %{pyproject_files}


%changelog
%autochangelog