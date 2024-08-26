
%global python3_pkgversion 3.11

Name:           python-cleo
Version:        2.1.0
Release:        %autorelease
Summary:        Cleo allows you to create beautiful and testable command-line interfaces.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-poetry/cleo
Source:         %{pypi_source cleo}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(poetry-core) >= 1.1
BuildRequires:  (python%{python3_pkgversion}dist(crashtest) < 0.5~~ with python%{python3_pkgversion}dist(crashtest) >= 0.4.1)
BuildRequires:  (python%{python3_pkgversion}dist(rapidfuzz) < 4~~ with python%{python3_pkgversion}dist(rapidfuzz) >= 3)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cleo' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-cleo
Summary:        %{summary}

%description -n python%{python3_pkgversion}-cleo %_description


%prep
%autosetup -p1 -n cleo-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-cleo -f %{pyproject_files}


%changelog
%autochangelog