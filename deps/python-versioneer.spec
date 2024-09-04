
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-versioneer
Version:        0.29
Release:        %autorelease
Summary:        Easy VCS-based management of project version strings

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-versioneer/python-versioneer
Source:         %{pypi_source versioneer}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'versioneer' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-versioneer
Summary:        %{summary}

%description -n python%{python3_pkgversion}-versioneer %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-versioneer+toml
Summary: Metapackage for python%{python3_pkgversion}-versioneer: toml extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}-versioneer = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-versioneer+toml = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(versioneer[toml]) = %{version}

%description -n python%{python3_pkgversion}-versioneer+toml
This is a metapackage bringing in toml extras requires for python%{python3_pkgversion}-versioneer.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-versioneer+toml
%ghost %{python3__sitelib}/*.dist-info


%prep
%autosetup -p1 -n versioneer-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-versioneer -f %{pyproject_files}


%changelog
%autochangelog