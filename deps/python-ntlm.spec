%undefine __brp_python_bytecompile
%global python3_pkgversion 3.11

Name:           python-ntlm
Version:        1.1.0
Release:        %autorelease
Summary:        Python library that provides NTLM support, including an authentication handler for urllib2. Works with pass-the-hash in additon to password authentication.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://code.google.com/p/python-ntlm
Source:         %{pypi_source python-ntlm}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-ntlm' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-python-ntlm
Summary:        %{summary}

%description -n python%{python3_pkgversion}-python-ntlm %_description


%prep
%autosetup -p1 -n python-ntlm-%{version}


%build
%pyproject_wheel

%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/ntlm_example_extended $RPM_BUILD_ROOT/usr/bin/ntlm_example_extended%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/ntlm_example_simple $RPM_BUILD_ROOT/usr/bin/ntlm_example_simple%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/ntlm_example_extended|/usr/bin/ntlm_example_extended%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/ntlm_example_simple|/usr/bin/ntlm_example_simple%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2
sed -i "/HTTPNtlmAuthHandler.cpython-311{,.opt-?}.pyc/d" %{pyproject_files}
sed -i "/U32.cpython-311{,.opt-?}.pyc/d" %{pyproject_files}
sed -i "/des_c.cpython-311{,.opt-?}.pyc/d" %{pyproject_files}
sed -i "/ntlm.cpython-311{,.opt-?}.pyc/d" %{pyproject_files}
sed -i "/des_data.cpython-311{,.opt-?}.pyc/d" %{pyproject_files}

%check

%files -n python%{python3_pkgversion}-python-ntlm -f %{pyproject_files}

%changelog
%autochangelog