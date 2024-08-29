
%global python3_pkgversion 3.11

Name:           python-gitpython
Version:        3.1.42
Release:        %autorelease
Summary:        GitPython is a Python library used to interact with Git repositories

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/gitpython-developers/GitPython
Source:         %{pypi_source GitPython}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(gitdb) < 5~~ with python%{python3_pkgversion}dist(gitdb) >= 4.0.1)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'gitpython' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-gitpython
Summary:        %{summary}

%description -n python%{python3_pkgversion}-gitpython %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n GitPython-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-gitpython -f %{pyproject_files}


%changelog
%autochangelog