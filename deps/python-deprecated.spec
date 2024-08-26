
%global python3_pkgversion 3.11

Name:           python-deprecated
Version:        1.2.14
Release:        %autorelease
Summary:        Python @deprecated decorator to deprecate old python classes, functions or methods.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/tantale/deprecated
Source:         %{pypi_source Deprecated}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(wrapt) < 2~~ with python%{python3_pkgversion}dist(wrapt) >= 1.10)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'deprecated' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-deprecated
Summary:        %{summary}

%description -n python%{python3_pkgversion}-deprecated %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n Deprecated-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-deprecated -f %{pyproject_files}


%changelog
%autochangelog