
%global python3_pkgversion 3.11

Name:           python-frozenlist
Version:        1.4.1
Release:        %autorelease
Summary:        A list-like structure which implements collections.abc.MutableSequence

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/aio-libs/frozenlist
Source:         %{pypi_source frozenlist}

Patch:		frozenlist-deterministic.patch
BuildArch:      x86_64
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(expandvars)
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 47
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(cython)
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'frozenlist' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-frozenlist
Summary:        %{summary}

%description -n python%{python3_pkgversion}-frozenlist %_description


%prep
%autosetup -p1 -n frozenlist-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-frozenlist -f %{pyproject_files}


%changelog
%autochangelog