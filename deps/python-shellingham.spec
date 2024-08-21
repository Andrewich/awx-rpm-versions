
%global python3_pkgversion 3.11

Name:           python-shellingham
Version:        1.5.4
Release:        %autorelease
Summary:        Tool to Detect Surrounding Shell

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/sarugaku/shellingham
Source:         %{pypi_source shellingham}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'shellingham' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-shellingham
Summary:        %{summary}

%description -n python%{python3_pkgversion}-shellingham %_description


%prep
%autosetup -p1 -n shellingham-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-shellingham -f %{pyproject_files}


%changelog
%autochangelog