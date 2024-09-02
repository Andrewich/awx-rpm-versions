
%global python3_pkgversion 3.11

Name:           python-virtualenv
Version:        20.26.3
Release:        %autorelease
Summary:        Virtual Python Environment builder

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pypa/virtualenv
Source:         %{pypi_source virtualenv}

Patch: 		virtualenv-deps.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatch-vcs) >= 0.3
BuildRequires:  python%{python3_pkgversion}dist(hatchling) >= 1.17.1
BuildRequires:  (python%{python3_pkgversion}dist(distlib) < 1~~ with python%{python3_pkgversion}dist(distlib) >= 0.3.7)
BuildRequires:  (python%{python3_pkgversion}dist(filelock) < 4~~ with python%{python3_pkgversion}dist(filelock) >= 3.12.2)
BuildRequires:  (python%{python3_pkgversion}dist(platformdirs) < 5~~ with python%{python3_pkgversion}dist(platformdirs) >= 3.9.1)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'virtualenv' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-virtualenv
Summary:        %{summary}

%description -n python%{python3_pkgversion}-virtualenv %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n virtualenv-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-virtualenv -f %{pyproject_files}


%changelog
%autochangelog