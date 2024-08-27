
%global python3_pkgversion 3.11

Name:           python-pkgconfig
Version:        1.5.5
Release:        %autorelease
Summary:        Interface Python with pkg-config

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/matze/pkgconfig
Source:         %{pypi_source pkgconfig}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(poetry-core) >= 1


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pkgconfig' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pkgconfig
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pkgconfig %_description


%prep
%autosetup -p1 -n pkgconfig-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pkgconfig -f %{pyproject_files}


%changelog
%autochangelog