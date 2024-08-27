
%global python3_pkgversion 3.11

Name:           python-mdurl
Version:        0.1.2
Release:        %autorelease
Summary:        Markdown URL utilities

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/executablebooks/mdurl
Source:         %{pypi_source mdurl}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  (python%{python3_pkgversion}dist(flit-core) < 4~~ with python%{python3_pkgversion}dist(flit-core) >= 3.2)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mdurl' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-mdurl
Summary:        %{summary}

%description -n python%{python3_pkgversion}-mdurl %_description


%prep
%autosetup -p1 -n mdurl-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-mdurl -f %{pyproject_files}


%changelog
%autochangelog