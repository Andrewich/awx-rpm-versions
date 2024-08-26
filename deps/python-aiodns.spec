
%global python3_pkgversion 3.11

Name:           python-aiodns
Version:        3.2.0
Release:        %autorelease
Summary:        Simple DNS resolver for asyncio

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/saghul/aiodns
Source:         %{pypi_source aiodns}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(pycares) >= 4



# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'aiodns' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-aiodns
Summary:        %{summary}

%description -n python%{python3_pkgversion}-aiodns %_description


%prep
%autosetup -p1 -n aiodns-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-aiodns -f %{pyproject_files}


%changelog
%autochangelog