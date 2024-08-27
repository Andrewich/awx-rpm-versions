%global debug_package %{nil}
%global python3_pkgversion 3.11

Name:           python-mypy
Version:        1.10.1
Release:        %autorelease
Summary:        Optional static typing for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://www.mypy-lang.org/
Source:         %{pypi_source mypy}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.6.2
BuildRequires:  python%{python3_pkgversion}dist(wheel) >= 0.30
BuildRequires:  python%{python3_pkgversion}dist(typing-extensions) >= 4.1
BuildRequires:  python%{python3_pkgversion}dist(mypy-extensions) >= 1
BuildRequires:  python%{python3_pkgversion}dist(types-psutil)
BuildRequires:  python%{python3_pkgversion}dist(types-setuptools)
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mypy' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-mypy
Summary:        %{summary}

%description -n python%{python3_pkgversion}-mypy %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n mypy-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-mypy -f %{pyproject_files}


%changelog
%autochangelog