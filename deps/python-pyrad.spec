
%global python3_pkgversion 3.11

Name:           python-pyrad
Version:        2.4
Release:        %autorelease
Summary:        RADIUS tools

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pyradius/pyrad
Source:         %{pypi_source pyrad}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion}-poetry
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(poetry) >= 1
BuildRequires:  (python%{python3_pkgversion}dist(netaddr) < 0.9~~ with python%{python3_pkgversion}dist(netaddr) >= 0.8)
BuildRequires:  (python%{python3_pkgversion}dist(six) < 2~~ with python%{python3_pkgversion}dist(six) >= 1.15)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyrad' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pyrad
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyrad %_description


%prep
%autosetup -p1 -n pyrad-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pyrad -f %{pyproject_files}


%changelog
%autochangelog