
%global python3_pkgversion 3.11

Name:           python-ansible-runner
Version:        2.4.0
Release:        %autorelease
Summary:        "Consistent Ansible Python API and CLI with container and process isolation runtime capabilities"

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://ansible-runner.readthedocs.io
Source:         %{pypi_source ansible-runner}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  (python%{python3_pkgversion}dist(setuptools) <= 69.0.2 with python%{python3_pkgversion}dist(setuptools) >= 45)
BuildRequires:  (python%{python3_pkgversion}dist(setuptools-scm) <= 8.0.4 with python%{python3_pkgversion}dist(setuptools-scm) >= 6.2)
BuildRequires:  (python%{python3_pkgversion}dist(setuptools-scm[toml]) <= 8.0.4 with python%{python3_pkgversion}dist(setuptools-scm[toml]) >= 6.2)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(pexpect) >= 4.5
BuildRequires:  python%{python3_pkgversion}dist(packaging)
BuildRequires:  python%{python3_pkgversion}dist(python-daemon)
BuildRequires:  python%{python3_pkgversion}dist(pyyaml)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ansible_runner' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-ansible-runner
Summary:        %{summary}

%description -n python%{python3_pkgversion}-ansible-runner %_description


%prep
%autosetup -p1 -n ansible-runner-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-ansible-runner -f %{pyproject_files}


%changelog
%autochangelog