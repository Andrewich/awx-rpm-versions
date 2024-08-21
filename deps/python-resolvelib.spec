
%global python3_pkgversion 3.11

Name:           python-resolvelib
Version:        1.0.1
Release:        %autorelease
Summary:        Resolve abstract dependencies into concrete ones

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/sarugaku/resolvelib
Source:         %{pypi_source resolvelib}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 36.2.2
BuildRequires:  python%{python3_pkgversion}dist(wheel) >= 0.28
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'resolvelib' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-resolvelib
Summary:        %{summary}

%description -n python%{python3_pkgversion}-resolvelib %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n resolvelib-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-resolvelib -f %{pyproject_files}


%changelog
%autochangelog