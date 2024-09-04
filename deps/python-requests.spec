
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-requests
Version:        2.31.0
Release:        %autorelease
Summary:        Python HTTP for Humans.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://requests.readthedocs.io
Source:         %{pypi_source requests}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(charset-normalizer) < 4~~ with python%{python3_pkgversion}dist(charset-normalizer) >= 2)
BuildRequires:  (python%{python3_pkgversion}dist(idna) < 4~~ with python%{python3_pkgversion}dist(idna) >= 2.5)
BuildRequires:  (python%{python3_pkgversion}dist(urllib3) < 3~~ with python%{python3_pkgversion}dist(urllib3) >= 1.21.1)
BuildRequires:  python%{python3_pkgversion}dist(certifi) >= 2017.4.17
BuildRequires:  ((python%{python3_pkgversion}dist(pysocks) < 1.5.7 or python%{python3_pkgversion}dist(pysocks) > 1.5.7) with python%{python3_pkgversion}dist(pysocks) >= 1.5.6)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'requests' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-requests
Summary:        %{summary}

%description -n python%{python3_pkgversion}-requests %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-requests+socks
Summary: Metapackage for python%{python3_pkgversion}-requests: socks extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: ((python%{python3_pkgversion}dist(pysocks) < 1.5.7 or python%{python3_pkgversion}dist(pysocks) > 1.5.7) with python%{python3_pkgversion}dist(pysocks) >= 1.5.6)
Requires: python%{python3_pkgversion}-requests = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-requests+socks = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(requests[socks]) = 2.31

%description -n python%{python3_pkgversion}-requests+socks
This is a metapackage bringing in socks extras requires for python%{python3_pkgversion}-requests.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-requests+socks
%ghost %{python3__sitelib}/*.dist-info


%prep
%autosetup -p1 -n requests-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-requests -f %{pyproject_files}


%changelog
%autochangelog