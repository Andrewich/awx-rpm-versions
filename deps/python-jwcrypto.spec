
%global python3_pkgversion 3.11

Name:           python-jwcrypto
Version:        1.5.4
Release:        %autorelease
Summary:        Implementation of JOSE Web standards

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/latchset/jwcrypto
Source:         %{pypi_source jwcrypto}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(cryptography) >= 3.4
BuildRequires:  python%{python3_pkgversion}dist(typing-extensions) >= 4.5


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jwcrypto' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-jwcrypto
Summary:        %{summary}

%description -n python%{python3_pkgversion}-jwcrypto %_description


%prep
%autosetup -p1 -n jwcrypto-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-jwcrypto -f %{pyproject_files}


%changelog
%autochangelog