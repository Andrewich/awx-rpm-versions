
%global python3_pkgversion 3.11

Name:           python3-saml
Version:        1.16.0
Release:        %autorelease
Summary:        Saml Python Toolkit. Add SAML support to your Python software using this library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/SAML-Toolkits/python3-saml
Source:         %{pypi_source python3-saml}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(poetry) >= 1.1.15
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.1
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(isodate) >= 0.6.1
BuildRequires:  ((python%{python3_pkgversion}dist(lxml) < 4.7 or python%{python3_pkgversion}dist(lxml) > 4.7) with python%{python3_pkgversion}dist(lxml) >= 4.6.5)
BuildRequires:  python%{python3_pkgversion}dist(xmlsec) >= 1.3.9


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python3-saml' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-python3-saml
Summary:        %{summary}

%description -n python%{python3_pkgversion}-python3-saml %_description


%prep
%autosetup -p1 -n python3-saml-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-python3-saml -f %{pyproject_files}


%changelog
%autochangelog