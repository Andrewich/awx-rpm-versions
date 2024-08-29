
%global python3_pkgversion 3.11

Name:           python-msal-extensions
Version:        1.1.0
Release:        %autorelease
Summary:        Microsoft Authentication Library extensions (MSAL EX) provides a persistence API that can save your data on disk, encrypted on Windows, macOS and Linux. Concurrent data access will be coordinated by a file lock mechanism.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/msal-extensions/
Source:         %{pypi_source msal-extensions}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(msal) < 2~~ with python%{python3_pkgversion}dist(msal) >= 0.4.1)
BuildRequires:  python%{python3_pkgversion}dist(packaging)
BuildRequires:  (python%{python3_pkgversion}dist(portalocker) < 3~~ with python%{python3_pkgversion}dist(portalocker) >= 1)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'msal-extensions' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-msal-extensions
Summary:        %{summary}

%description -n python%{python3_pkgversion}-msal-extensions %_description


%prep
%autosetup -p1 -n msal-extensions-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-msal-extensions -f %{pyproject_files}


%changelog
%autochangelog