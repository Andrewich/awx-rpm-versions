
%global python3_pkgversion 3.11

Name:           python-distro
Version:        1.9.0
Release:        %autorelease
Summary:        Distro - an OS platform information API

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-distro/distro
Source:         %{pypi_source distro}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'distro' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-distro
Summary:        %{summary}

%description -n python%{python3_pkgversion}-distro %_description


%prep
%autosetup -p1 -n distro-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/distro $RPM_BUILD_ROOT/usr/bin/distro%{python3_pkgversion}
%endif
%pyproject_save_files '*' +auto
sed -i "s|/usr/bin/distro|/usr/bin/distro%{python3_pkgversion}|g" %{pyproject_files}

%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-distro -f %{pyproject_files}


%changelog
%autochangelog