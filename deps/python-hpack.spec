
%global python3_pkgversion 3.11

Name:           python-hpack
Version:        4.0.0
Release:        %autorelease
Summary:        Pure-Python HPACK header compression

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-hyper/hpack
Source:         %{pypi_source hpack}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'hpack' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-hpack
Summary:        %{summary}

%description -n python%{python3_pkgversion}-hpack %_description


%prep
%autosetup -p1 -n hpack-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-hpack -f %{pyproject_files}


%changelog
%autochangelog