
%global python3_pkgversion 3.11

Name:           python-service-identity
Version:        24.1.0
Release:        %autorelease
Summary:        Service identity verification for pyOpenSSL & cryptography.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/service-identity/
Source:         %{pypi_source service_identity}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion}-pyasn1 python%{python3_pkgversion}-pyasn1-modules
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)
BuildRequires:  python%{python3_pkgversion}dist(hatch-vcs)
BuildRequires:  python%{python3_pkgversion}dist(hatch-fancy-pypi-readme)
BuildRequires:  python%{python3_pkgversion}dist(attrs) >= 19.1
BuildRequires:  python%{python3_pkgversion}dist(cryptography)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'service-identity' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-service-identity
Summary:        %{summary}

%description -n python%{python3_pkgversion}-service-identity %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n service_identity-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-service-identity -f %{pyproject_files}


%changelog
%autochangelog