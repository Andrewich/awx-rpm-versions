Name:           python-drf-yasg
Version:        1.21.7
Release:        1%{?dist}
Summary:        Automated generation of real Swagger/OpenAPI 2.0 schemas from Django Rest Framework code.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/axnsan12/drf-yasg
Source:         %{pypi_source drf-yasg}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'drf_yasg' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-drf-yasg
Summary:        %{summary}

%description -n python3-drf-yasg %_description


%prep
%autosetup -p1 -n drf-yasg-%{version}


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


%files -n python3-drf-yasg -f %{pyproject_files}


%changelog
* Tue Jan 02 2024 Martin Juhl <m@rtinjuhl.dk> - 1.21.7-1
- Initial package