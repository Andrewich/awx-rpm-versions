
%global python3_pkgversion 3.11

Name:           python-urllib3
Version:        1.26.18
Release:        %autorelease
Summary:        HTTP library with thread-safe connection pooling, file post, and more.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://urllib3.readthedocs.io/
Source:         %{pypi_source urllib3}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion}-python-ntlm
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'urllib3' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-urllib3
Summary:        %{summary}

%description -n python%{python3_pkgversion}-urllib3 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n urllib3-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-urllib3 -f %{pyproject_files}


%changelog
%autochangelog