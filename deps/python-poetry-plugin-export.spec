
%global python3_pkgversion 3.11

Name:           python-poetry-plugin-export
Version:        1.8.0
Release:        %autorelease
Summary:        Poetry plugin to export the dependencies to various formats

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://python-poetry.org/
Source:         %{pypi_source poetry_plugin_export}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  (python%{python3_pkgversion}dist(poetry) < 3~~ with python%{python3_pkgversion}dist(poetry) >= 1.8)
BuildRequires:  (python%{python3_pkgversion}dist(poetry-core) < 3~~ with python%{python3_pkgversion}dist(poetry-core) >= 1.7)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'poetry-plugin-export' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-poetry-plugin-export
Summary:        %{summary}

%description -n python%{python3_pkgversion}-poetry-plugin-export %_description


%prep
%autosetup -p1 -n poetry_plugin_export-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-poetry-plugin-export -f %{pyproject_files}


%changelog
%autochangelog