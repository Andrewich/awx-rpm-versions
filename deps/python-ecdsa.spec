
%global python3_pkgversion 3.11

Name:           python-ecdsa
Version:        0.18.0
Release:        %autorelease
Summary:        ECDSA cryptographic signature library (pure python)

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://github.com/tlsfuzzer/python-ecdsa
Source:         %{pypi_source ecdsa}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(six) >= 1.9


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ecdsa' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-ecdsa
Summary:        %{summary}

%description -n python%{python3_pkgversion}-ecdsa %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n ecdsa-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-ecdsa -f %{pyproject_files}


%changelog
%autochangelog