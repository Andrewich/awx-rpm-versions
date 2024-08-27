
%global python3_pkgversion 3.11

Name:           python-pyparsing
Version:        3.1.2
Release:        %autorelease
Summary:        pyparsing module - Classes and methods to define and execute parsing grammars

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pyparsing/pyparsing/
Source:         %{pypi_source pyparsing}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  (python%{python3_pkgversion}dist(flit-core) < 4~~ with python%{python3_pkgversion}dist(flit-core) >= 3.2)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyparsing' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pyparsing
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyparsing %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n pyparsing-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pyparsing -f %{pyproject_files}


%changelog
%autochangelog