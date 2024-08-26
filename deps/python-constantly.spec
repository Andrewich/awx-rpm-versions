
%global python3_pkgversion 3.11

Name:           python-constantly
Version:        23.10.4
Release:        %autorelease
Summary:        Symbolic constants in Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/twisted/constantly
Source:         %{pypi_source constantly}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 68.2
BuildRequires:  python%{python3_pkgversion}dist(versioneer) = 0.29
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'constantly' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-constantly
Summary:        %{summary}

%description -n python%{python3_pkgversion}-constantly %_description


%prep
%autosetup -p1 -n constantly-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-constantly -f %{pyproject_files}


%changelog
%autochangelog