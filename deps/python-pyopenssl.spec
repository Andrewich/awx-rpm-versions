
%global python3_pkgversion 3.11

Name:           python-pyopenssl
Version:        24.0.0
Release:        %autorelease
Summary:        Python wrapper module around the OpenSSL library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pyopenssl.org/
Source:         %{pypi_source pyOpenSSL}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(cryptography) < 43~~ with python%{python3_pkgversion}dist(cryptography) >= 41.0.5)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyopenssl' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pyopenssl
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyopenssl %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n pyOpenSSL-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pyopenssl -f %{pyproject_files}


%changelog
%autochangelog