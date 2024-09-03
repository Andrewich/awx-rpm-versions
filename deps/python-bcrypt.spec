%global debug_package %{nil}
%global python3_pkgversion 3.11
%global python3__sitelib64 /usr/lib64/python%{python3_pkgversion}/site-packages

Name:           python-bcrypt
Version:        4.1.3
Release:        %autorelease
Summary:        Modern password hashing for your software and your servers

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/bcrypt/
Source:         %{pypi_source bcrypt}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 42
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-rust)
BuildRequires:  ((python%{python3_pkgversion}dist(pytest) < 3.3 or python%{python3_pkgversion}dist(pytest) > 3.3) with python%{python3_pkgversion}dist(pytest) >= 3.2.1)
BuildRequires:  python%{python3_pkgversion}dist(mypy)
BuildRequires:  gcc
BuildRequires:  rust
BuildRequires:  cargo

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'bcrypt' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-bcrypt
Summary:        %{summary}

%description -n python%{python3_pkgversion}-bcrypt %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-bcrypt+tests
Summary: Metapackage for python%{python3_pkgversion}-bcrypt: tests extras
AutoReq: no
Requires: ((python%{python3_pkgversion}dist(pytest) < 3.3 or python%{python3_pkgversion}dist(pytest) > 3.3) with python%{python3_pkgversion}dist(pytest) >= 3.2.1)
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}-bcrypt = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-bcrypt+tests = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}-bcrypt+tests(x86-64) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(bcrypt[tests]) = %{version}

%description -n python%{python3_pkgversion}-bcrypt+tests
This is a metapackage bringing in tests extras requires for python%{python3_pkgversion}-bcrypt.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-bcrypt+tests
%ghost %{python3__sitelib64}/*.dist-info


%package -n python%{python3_pkgversion}-bcrypt+typecheck
Summary: Metapackage for python%{python3_pkgversion}-bcrypt: typecheck extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}-bcrypt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: python%{python3_pkgversion}dist(mypy)
AutoProv: no
Provides: python%{python3_pkgversion}-bcrypt+typecheck = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}-bcrypt+typecheck(x86-64) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(bcrypt[typecheck]) = %{version}

%description -n python%{python3_pkgversion}-bcrypt+typecheck
This is a metapackage bringing in typecheck extras requires for python%{python3_pkgversion}-bcrypt.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-bcrypt+typecheck
%ghost %{python3__sitelib64}/*.dist-info

%prep
%autosetup -p1 -n bcrypt-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-bcrypt -f %{pyproject_files}


%changelog
%autochangelog