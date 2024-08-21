
%global python3_pkgversion 3.11

Name:           python-markupsafe
Version:        2.1.5
Release:        %autorelease
Summary:        Safely add untrusted strings to HTML/XML markup.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://palletsprojects.com/p/markupsafe/
Source:         %{pypi_source MarkupSafe}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'markupsafe' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-markupsafe
Summary:        %{summary}

%description -n python%{python3_pkgversion}-markupsafe %_description


%prep
%autosetup -p1 -n MarkupSafe-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-markupsafe -f %{pyproject_files}


%changelog
%autochangelog