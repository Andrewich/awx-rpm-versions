
%global python3_pkgversion 3.11

Name:           python-isodate
Version:        0.6.1
Release:        %autorelease
Summary:        An ISO 8601 date/time/duration parser and formatter

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/gweis/isodate/
Source:         %{pypi_source isodate}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(six)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'isodate' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-isodate
Summary:        %{summary}

%description -n python%{python3_pkgversion}-isodate %_description


%prep
%autosetup -p1 -n isodate-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-isodate -f %{pyproject_files}


%changelog
%autochangelog