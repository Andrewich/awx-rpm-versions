
%global python3_pkgversion 3.11

Name:           python-txaio
Version:        23.1.1
Release:        %autorelease
Summary:        Compatibility API between asyncio/Twisted/Trollius

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/crossbario/txaio
Source:         %{pypi_source txaio}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion}-twisted
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'txaio' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-txaio
Summary:        %{summary}

%description -n python%{python3_pkgversion}-txaio %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n txaio-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-txaio -f %{pyproject_files}


%changelog
%autochangelog