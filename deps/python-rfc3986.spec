
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-rfc3986
Version:        2.0.0
Release:        %autorelease
Summary:        Validating URI References per RFC 3986

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://rfc3986.readthedocs.io
Source:         %{pypi_source rfc3986}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(idna)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'rfc3986' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-rfc3986
Summary:        %{summary}

%description -n python%{python3_pkgversion}-rfc3986 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-rfc3986+idna2008
Summary: Metapackage for python%{python3_pkgversion}-rfc3986: idna2008 extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(idna)
Requires: python%{python3_pkgversion}-rfc3986 = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-rfc3986+idna2008 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(rfc3986[idna2008]) = 2

%description -n python%{python3_pkgversion}-rfc3986+idna2008
This is a metapackage bringing in idna2008 extras requires for python%{python3_pkgversion}-rfc3986.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-rfc3986+idna2008
%ghost %{python3__sitelib}/*.dist-info

%prep
%autosetup -p1 -n rfc3986-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-rfc3986 -f %{pyproject_files}


%changelog
%autochangelog