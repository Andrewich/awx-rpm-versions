
%global python3_pkgversion 3.11

Name:           python-inflect
Version:        7.0.0
Release:        %autorelease
Summary:        Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jaraco/inflect
Source:         %{pypi_source inflect}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 56
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml]) >= 3.4.1
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(pydantic) >= 1.9.1
BuildRequires:  python%{python3_pkgversion}dist(typing-extensions)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'inflect' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-inflect
Summary:        %{summary}

%description -n python%{python3_pkgversion}-inflect %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n inflect-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-inflect -f %{pyproject_files}


%changelog
%autochangelog