
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-prometheus-client
Version:        0.20.0
Release:        %autorelease
Summary:        Python client for the Prometheus monitoring system.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/prometheus/client_python
Source:         %{pypi_source prometheus_client}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(twisted)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'prometheus-client' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-prometheus-client
Summary:        %{summary}

%description -n python%{python3_pkgversion}-prometheus-client %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-prometheus-client+twisted
Summary: Metapackage for python%{python3_pkgversion}-prometheus-client: twisted extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(twisted)
Requires: python%{python3_pkgversion}-prometheus-client = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-prometheus-client+twisted = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(prometheus-client[twisted]) = 0.20

%description -n python%{python3_pkgversion}-prometheus-client+twisted
This is a metapackage bringing in twisted extras requires for python%{python3_pkgversion}-prometheus-client.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-prometheus-client+twisted
%ghost %{python3__sitelib}/*.dist-info

%prep
%autosetup -p1 -n prometheus_client-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-prometheus-client -f %{pyproject_files}


%changelog
%autochangelog