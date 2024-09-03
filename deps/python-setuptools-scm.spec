
%global python3_pkgversion 3.11

Name:           python-setuptools_scm
Version:        8.0.4
Release:        %autorelease
Summary:        the blessed package to manage your versions by scm tags

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/setuptools-scm/
Source:         %{pypi_source setuptools-scm}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 61
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(packaging) >= 20
BuildRequires:  python%{python3_pkgversion}dist(typing-extensions)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'setuptools-scm' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-setuptools_scm
Summary:        %{summary}

%description -n python%{python3_pkgversion}-setuptools_scm %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%python_extras_subpkg -n python%{python3_pkgversion}-setuptools_scm -i %{python3_sitelib}/*.dist-info toml


%prep
%autosetup -p1 -n setuptools-scm-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-setuptools_scm -f %{pyproject_files}


%changelog
%autochangelog