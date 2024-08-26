
%global python3_pkgversion 3.11

Name:           python-cryptography
Version:        41.0.7
Release:        %autorelease
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/cryptography/
Source:         %{pypi_source cryptography}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 61
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(cffi) >= 1.12
BuildRequires:  python%{python3_pkgversion}dist(setuptools-rust) >= 0.11.4
BuildRequires:	openssl-devel
BuildRequires:  gcc
BuildRequires:  rust
BuildRequires:  cargo


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cryptography' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-cryptography
Summary:        %{summary}

%description -n python%{python3_pkgversion}-cryptography %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n cryptography-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-cryptography -f %{pyproject_files}


%changelog
%autochangelog