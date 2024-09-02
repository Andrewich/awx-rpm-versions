
%global python3_pkgversion 3.11

Name:           python-poetry
Version:        1.8.3
Release:        %autorelease
Summary:        Python dependency management and packaging made easy.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://python-poetry.org/
Source:         %{pypi_source poetry}
Patch: poetry-circular-dep-fix.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(poetry-core) >= 1.5
BuildRequires:  (python%{python3_pkgversion}dist(build) < 2~~ with python%{python3_pkgversion}dist(build) >= 1.0.3)
BuildRequires:  (python%{python3_pkgversion}dist(cachecontrol) < 0.15~~ with python%{python3_pkgversion}dist(cachecontrol) >= 0.14)
BuildRequires:  (python%{python3_pkgversion}dist(cleo) < 3~~ with python%{python3_pkgversion}dist(cleo) >= 2.1)
BuildRequires:  (python%{python3_pkgversion}dist(crashtest) < 0.5~~ with python%{python3_pkgversion}dist(crashtest) >= 0.4.1)
BuildRequires:  (python%{python3_pkgversion}dist(dulwich) < 0.22~~ with python%{python3_pkgversion}dist(dulwich) >= 0.21.2)
BuildRequires:  (python%{python3_pkgversion}dist(fastjsonschema) < 3~~ with python%{python3_pkgversion}dist(fastjsonschema) >= 2.18)
BuildRequires:  (python%{python3_pkgversion}dist(installer) < 0.8~~ with python%{python3_pkgversion}dist(installer) >= 0.7)
BuildRequires:  (python%{python3_pkgversion}dist(keyring) < 25~~ with python%{python3_pkgversion}dist(keyring) >= 24)
BuildRequires:  python%{python3_pkgversion}dist(packaging) >= 23.1
BuildRequires:  (python%{python3_pkgversion}dist(pexpect) < 5~~ with python%{python3_pkgversion}dist(pexpect) >= 4.7)
BuildRequires:  (python%{python3_pkgversion}dist(pkginfo) < 2~~ with python%{python3_pkgversion}dist(pkginfo) >= 1.10)
BuildRequires:  (python%{python3_pkgversion}dist(platformdirs) < 5~~ with python%{python3_pkgversion}dist(platformdirs) >= 3)
BuildRequires:  python%{python3_pkgversion}dist(poetry-core) = 1.9
BuildRequires:  (python%{python3_pkgversion}dist(pyproject-hooks) < 2~~ with python%{python3_pkgversion}dist(pyproject-hooks) >= 1)
BuildRequires:  (python%{python3_pkgversion}dist(requests) < 3~~ with python%{python3_pkgversion}dist(requests) >= 2.26)
BuildRequires:  (python%{python3_pkgversion}dist(requests-toolbelt) < 2~~ with python%{python3_pkgversion}dist(requests-toolbelt) >= 1)
BuildRequires:  (python%{python3_pkgversion}dist(shellingham) < 2~~ with python%{python3_pkgversion}dist(shellingham) >= 1.5)
BuildRequires:  (python%{python3_pkgversion}dist(tomlkit) < 1~~ with python%{python3_pkgversion}dist(tomlkit) >= 0.11.4)
BuildRequires:  python%{python3_pkgversion}dist(trove-classifiers) >= 2022.5.19
BuildRequires:  (python%{python3_pkgversion}dist(virtualenv) < 21~~ with python%{python3_pkgversion}dist(virtualenv) >= 20.23)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'poetry' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-poetry
Summary:        %{summary}

%description -n python%{python3_pkgversion}-poetry %_description


%prep
%autosetup -p1 -n poetry-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-poetry -f %{pyproject_files}


%changelog
%autochangelog