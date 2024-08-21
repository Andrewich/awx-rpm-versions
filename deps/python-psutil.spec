
%global python3_pkgversion 3.11

Name:           python-psutil
Version:        5.9.8
Release:        %autorelease
Summary:        Cross-platform lib for process and system monitoring in Python.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/giampaolo/psutil
Source:         %{pypi_source psutil}

BuildArch:      x86_64
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 43
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'psutil' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-psutil
Summary:        %{summary}

%description -n python%{python3_pkgversion}-psutil %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n psutil-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-psutil -f %{pyproject_files}


%changelog
%autochangelog