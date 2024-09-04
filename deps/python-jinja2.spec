
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-jinja2
Version:        3.1.3
Release:        %autorelease
Summary:        A very fast and expressive template engine.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://palletsprojects.com/p/jinja/
Source:         %{pypi_source Jinja2}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(markupsafe) >= 2
BuildRequires:  python%{python3_pkgversion}dist(babel) >= 2.7


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jinja2' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-jinja2
Summary:        %{summary}

%description -n python%{python3_pkgversion}-jinja2 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-jinja2+i18n
Summary: Metapackage for python%{python3_pkgversion}-jinja2: i18n extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}dist(babel) >= 2.7
Requires: python%{python3_pkgversion}-jinja2 = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-jinja2+i18n = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(jinja2[i18n]) = %{version}

%description -n python%{python3_pkgversion}-jinja2+i18n
This is a metapackage bringing in i18n extras requires for python%{python3_pkgversion}-jinja2.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-jinja2+i18n
%ghost %{python3__sitelib}/*.dist-info


%prep
%autosetup -p1 -n Jinja2-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-jinja2 -f %{pyproject_files}


%changelog
%autochangelog