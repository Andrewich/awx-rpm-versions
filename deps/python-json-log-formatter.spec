
%global python3_pkgversion 3.11

Name:           python-json-log-formatter
Version:        0.5.2
Release:        %autorelease
Summary:        JSON log formatter

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/marselester/json-log-formatter
Source:         %{pypi_source JSON-log-formatter}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'json-log-formatter' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-json-log-formatter
Summary:        %{summary}

%description -n python%{python3_pkgversion}-json-log-formatter %_description


%prep
%autosetup -p1 -n JSON-log-formatter-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-json-log-formatter -f %{pyproject_files}


%changelog
%autochangelog