
%global python3_pkgversion 3.11

Name:           python-ldap
Version:        3.4.4
Release:        %autorelease
Summary:        Python modules for implementing LDAP clients

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://www.python-ldap.org/
Source:         %{pypi_source python-ldap}

BuildArch:      x86_64

BuildRequires: openldap-devel
BuildRequires: gcc
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(pyasn1) >= 0.3.7
BuildRequires:  python%{python3_pkgversion}dist(pyasn1-modules) >= 0.1.5


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-ldap' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-python-ldap
Summary:        %{summary}

%description -n python%{python3_pkgversion}-python-ldap %_description


%prep
%autosetup -p1 -n python-ldap-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-python-ldap -f %{pyproject_files}


%changelog
%autochangelog