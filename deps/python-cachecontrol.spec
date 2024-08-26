
%global python3_pkgversion 3.11

Name:           python-cachecontrol
Version:        0.14.0
Release:        %autorelease
Summary:        httplib2 caching for requests

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/CacheControl/
Source:         %{pypi_source cachecontrol}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  (python%{python3_pkgversion}dist(flit-core) < 4~~ with python%{python3_pkgversion}dist(flit-core) >= 3.2)
BuildRequires:  python%{python3_pkgversion}dist(requests) >= 2.16
BuildRequires:  (python%{python3_pkgversion}dist(msgpack) < 2~~ with python%{python3_pkgversion}dist(msgpack) >= 0.5.2)
BuildRequires:  python%{python3_pkgversion}dist(filelock) >= 3.8


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cachecontrol' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-cachecontrol
Summary:        %{summary}

%description -n python%{python3_pkgversion}-cachecontrol %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-cachecontrol filecache 


%prep
%autosetup -p1 -n cachecontrol-%{version}



%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/doesitcache $RPM_BUILD_ROOT/usr/bin/doesitcache%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/doesitcache|/usr/bin/doesitcache%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-cachecontrol -f %{pyproject_files}


%changelog
%autochangelog