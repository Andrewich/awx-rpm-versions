
%global python3_pkgversion 3.11

Name:           python-readme-renderer
Version:        43.0
Release:        %autorelease
Summary:        readme_renderer is a library for rendering readme descriptions for Warehouse

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/readme-renderer/
Source:         %{pypi_source readme_renderer}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(nh3) >= 0.2.14
BuildRequires:  python%{python3_pkgversion}dist(docutils) >= 0.13.1
BuildRequires:  python%{python3_pkgversion}dist(pygments) >= 2.5.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'readme-renderer' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-readme-renderer
Summary:        %{summary}

%description -n python%{python3_pkgversion}-readme-renderer %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n readme_renderer-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-readme-renderer -f %{pyproject_files}


%changelog
%autochangelog