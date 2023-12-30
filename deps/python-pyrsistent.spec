Name:           python-pyrsistent
Version:        0.19.2
Release:        1%{?dist}
Summary:        Persistent/Functional/Immutable data structures

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/tobgu/pyrsistent/
Source:         %{pypi_source pyrsistent}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyrsistent' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-pyrsistent
Summary:        %{summary}

%description -n python3-pyrsistent %_description


%prep
%autosetup -p1 -n pyrsistent-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-pyrsistent -f %{pyproject_files}


%changelog
* Sat Dec 30 2023 Martin Juhl <m@rtinjuhl.dk> - 0.19.2-1
- Initial package