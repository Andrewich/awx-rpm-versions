
%global python3_pkgversion 3.11

Name:           python-lxml
Version:        4.9.4
Release:        %autorelease
Summary:        Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://lxml.de/
Source:         %{pypi_source lxml}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  gcc libxml2-devel libxslt-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'lxml' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-lxml
Summary:        %{summary}

%description -n python%{python3_pkgversion}-lxml %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n lxml-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-lxml -f %{pyproject_files}


%changelog
%autochangelog