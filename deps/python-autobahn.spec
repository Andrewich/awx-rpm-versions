
%global python3_pkgversion 3.11
%_binaries_in_noarch_packages_terminate_build   0

Name:           python-autobahn
Version:        23.6.2
Release:        %autorelease
Summary:        WebSocket client & server library, WAMP real-time framework

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/crossbario/autobahn-python
Source:         %{pypi_source autobahn}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(txaio) >= 21.2.1
BuildRequires:  python%{python3_pkgversion}dist(cryptography) >= 3.4.6
BuildRequires:  python%{python3_pkgversion}dist(hyperlink) >= 21


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'autobahn' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-autobahn
Summary:        %{summary}

%description -n python%{python3_pkgversion}-autobahn %_description


%prep
%autosetup -p1 -n autobahn-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/wamp $RPM_BUILD_ROOT/usr/bin/wamp%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/xbrnetwork $RPM_BUILD_ROOT/usr/bin/xbrnetwork%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/xbrnetwork-ui $RPM_BUILD_ROOT/usr/bin/xbrnetwork-ui%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/wamp|/usr/bin/wamp%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/xbrnetwork$|/usr/bin/xbrnetwork%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/xbrnetwork-ui$|/usr/bin/xbrnetwork-ui%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-autobahn -f %{pyproject_files}


%changelog
%autochangelog