
%global python3_pkgversion 3.11

Name:           python-ansiconv
Version:        1.0.0
Release:        %autorelease
Summary:        Converts ANSI coded text and converts it to either plain text or to HTML.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://bitbucket.org/dhrrgn/ansiconv
Source:         %{pypi_source ansiconv %{version} zip}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ansiconv' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-ansiconv
Summary:        %{summary}

%description -n python%{python3_pkgversion}-ansiconv %_description


%prep
%autosetup -p1 -n ansiconv-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-ansiconv -f %{pyproject_files}


%changelog
%autochangelog