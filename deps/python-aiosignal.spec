
%global python3_pkgversion 3.11

Name:           python-aiosignal
Version:        1.3.1
Release:        %autorelease
Summary:        aiosignal: a list of registered asynchronous callbacks

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/aio-libs/aiosignal
Source:         %{pypi_source aiosignal}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 51
BuildRequires:  python%{python3_pkgversion}dist(wheel) >= 0.36
BuildRequires:  python%{python3_pkgversion}dist(frozenlist) >= 1.1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'aiosignal' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-aiosignal
Summary:        %{summary}

%description -n python%{python3_pkgversion}-aiosignal %_description


%prep
%autosetup -p1 -n aiosignal-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-aiosignal -f %{pyproject_files}


%changelog
%autochangelog