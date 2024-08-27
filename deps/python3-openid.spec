
%global python3_pkgversion 3.11

Name:           python3-openid
Version:        3.2.0
Release:        %autorelease
Summary:        OpenID support for modern servers and consumers.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://github.com/necaris/python3-openid
Source:         %{pypi_source python3-openid}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(defusedxml)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python3-openid' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-python3-openid
Summary:        %{summary}

%description -n python%{python3_pkgversion}-python3-openid %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n python3-openid-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-python3-openid -f %{pyproject_files}


%changelog
%autochangelog