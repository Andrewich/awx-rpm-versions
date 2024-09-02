
%global python3_pkgversion 3.11

Name:           python-zope-interface
Version:        6.2
Release:        %autorelease
Summary:        Interfaces for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/zopefoundation/zope.interface
Source:         %{pypi_source zope.interface}
Provides:       python%{python3_pkgversion}dist(zope-interface) = 6.2


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'zope-interface' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-zope-interface
Summary:        %{summary}

%description -n python%{python3_pkgversion}-zope-interface %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n zope.interface-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-zope-interface -f %{pyproject_files}


%changelog
%autochangelog