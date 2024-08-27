
%global python3_pkgversion 3.11

Name:           python-rsa
Version:        4.9
Release:        %autorelease
Summary:        Pure-Python RSA implementation

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://stuvel.eu/rsa
Source:         %{pypi_source rsa}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(poetry-core) >= 1
BuildRequires:  python%{python3_pkgversion}dist(pyasn1) >= 0.1.3


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'rsa' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-rsa
Summary:        %{summary}

%description -n python%{python3_pkgversion}-rsa %_description


%prep
%autosetup -p1 -n rsa-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/pyrsa-decrypt $RPM_BUILD_ROOT/usr/bin/pyrsa-decrypt%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/pyrsa-encrypt $RPM_BUILD_ROOT/usr/bin/pyrsa-encrypt%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/pyrsa-keygen $RPM_BUILD_ROOT/usr/bin/pyrsa-keygen%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/pyrsa-priv2pub $RPM_BUILD_ROOT/usr/bin/pyrsa-priv2pub%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/pyrsa-sign $RPM_BUILD_ROOT/usr/bin/pyrsa-sign%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/pyrsa-verify $RPM_BUILD_ROOT/usr/bin/pyrsa-verify%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/pyrsa-decrypt|/usr/bin/pyrsa-decrypt%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/pyrsa-encrypt|/usr/bin/pyrsa-encrypt%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/pyrsa-keygen|/usr/bin/pyrsa-keygen%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/pyrsa-priv2pub|/usr/bin/pyrsa-priv2pub%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/pyrsa-sign|/usr/bin/pyrsa-sign%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/pyrsa-verify|/usr/bin/pyrsa-verify%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-rsa -f %{pyproject_files}


%changelog
%autochangelog