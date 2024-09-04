
%global python3_pkgversion 3.11

Name:           python-setuptools-twine
Version:        0.1.3
Release:        %autorelease
Summary:        Adds twine_check and twine_upload commands to setuptools.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/cchurch/setuptools-twine
Source:         %{pypi_source setuptools-twine}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(twine)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'setuptools-twine' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-setuptools-twine
Summary:        %{summary}

%description -n python%{python3_pkgversion}-setuptools-twine %_description


%prep
%autosetup -p1 -n setuptools-twine-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-setuptools-twine -f %{pyproject_files}


%changelog
%autochangelog