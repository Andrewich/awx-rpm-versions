
%global python3_pkgversion 3.11

Name:           python-hyperlink
Version:        21.0.0
Release:        %autorelease
Summary:        A featureful, immutable, and correct URL for Python.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-hyper/hyperlink
Source:         %{pypi_source hyperlink}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(idna) >= 2.5


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'hyperlink' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-hyperlink
Summary:        %{summary}

%description -n python%{python3_pkgversion}-hyperlink %_description


%prep
%autosetup -p1 -n hyperlink-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-hyperlink -f %{pyproject_files}


%changelog
%autochangelog