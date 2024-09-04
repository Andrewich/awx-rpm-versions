
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-kubernetes
Version:        29.0.0
Release:        %autorelease
Summary:        Kubernetes python client

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/kubernetes-client/python
Source:         %{pypi_source kubernetes}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(certifi) >= 14.5.14
BuildRequires:  python%{python3_pkgversion}dist(six) >= 1.9
BuildRequires:  python%{python3_pkgversion}dist(python-dateutil) >= 2.5.3
BuildRequires:  python%{python3_pkgversion}dist(pyyaml) >= 5.4.1
BuildRequires:  python%{python3_pkgversion}dist(google-auth) >= 1.0.1
BuildRequires:  ((python%{python3_pkgversion}dist(websocket-client) < 0.40 or python%{python3_pkgversion}dist(websocket-client) > 0.40) with (python%{python3_pkgversion}dist(websocket-client) < 0.41~~ or python%{python3_pkgversion}dist(websocket-client) >= 0.42) with (python%{python3_pkgversion}dist(websocket-client) < 0.42~~ or python%{python3_pkgversion}dist(websocket-client) >= 0.43) with python%{python3_pkgversion}dist(websocket-client) >= 0.32)
BuildRequires:  python%{python3_pkgversion}dist(requests)
BuildRequires:  python%{python3_pkgversion}dist(requests-oauthlib)
BuildRequires:  python%{python3_pkgversion}dist(oauthlib) >= 3.2.2
BuildRequires:  python%{python3_pkgversion}dist(urllib3) >= 1.24.2
BuildRequires:  python%{python3_pkgversion}dist(adal) >= 1.0.2


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'kubernetes' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-kubernetes
Summary:        %{summary}

%description -n python%{python3_pkgversion}-kubernetes %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-kubernetes+adal
Summary: Metapackage for python%{python3_pkgversion}-kubernetes: adal extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}-kubernetes = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: python%{python3_pkgversion}dist(adal) >= 1.0.2
AutoProv: no
Provides: python%{python3_pkgversion}-kubernetes+adal = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(kubernetes[adal]) = 29

%description -n python%{python3_pkgversion}-kubernetes+adal
This is a metapackage bringing in adal extras requires for python%{python3_pkgversion}-kubernetes.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-kubernetes+adal
%ghost %{python3__sitelib}/*.dist-info


%prep
%autosetup -p1 -n kubernetes-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-kubernetes -f %{pyproject_files}


%changelog
%autochangelog