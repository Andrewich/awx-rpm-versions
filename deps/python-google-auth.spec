
%global python3_pkgversion 3.11

Name:           python-google-auth
Version:        2.28.1
Release:        %autorelease
Summary:        Google Authentication Library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/googleapis/google-auth-library-python
Source:         %{pypi_source google-auth}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(cachetools) < 6~~ with python%{python3_pkgversion}dist(cachetools) >= 2)
BuildRequires:  python%{python3_pkgversion}dist(pyasn1-modules) >= 0.2.1
BuildRequires:  (python%{python3_pkgversion}dist(rsa) < 5~~ with python%{python3_pkgversion}dist(rsa) >= 3.1.4)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'google-auth' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-google-auth
Summary:        %{summary}

%description -n python%{python3_pkgversion}-google-auth %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n google-auth-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-google-auth -f %{pyproject_files}


%changelog
%autochangelog