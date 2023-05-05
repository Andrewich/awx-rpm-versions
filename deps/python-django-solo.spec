Name:           python-django-solo
Version:        2.0.0
Release:        1%{?dist}
Summary:        Django Solo helps working with singletons

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Creative Commons Attribution 3.0 Unported
URL:            https://github.com/lazybird/django-solo/
Source:         %{pypi_source django-solo}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-solo' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-django-solo
Summary:        %{summary}

%description -n python3-django-solo %_description


%prep
%autosetup -p1 -n django-solo-%{version}


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


%files -n python3-django-solo -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 2.0.0-1
- Initial package