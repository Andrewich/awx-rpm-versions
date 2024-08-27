
%global python3_pkgversion 3.11

Name:           python-idna
Version:        3.6
Release:        %autorelease
Summary:        Internationalized Domain Names in Applications (IDNA)

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/idna/
Source:         %{pypi_source idna}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  (python%{python3_pkgversion}dist(flit-core) < 4~~ with python%{python3_pkgversion}dist(flit-core) >= 3.2)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'idna' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-idna
Summary:        %{summary}

%description -n python%{python3_pkgversion}-idna %_description


%prep
%autosetup -p1 -n idna-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-idna -f %{pyproject_files}


%changelog
%autochangelog