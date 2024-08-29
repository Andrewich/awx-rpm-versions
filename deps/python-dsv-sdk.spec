
%global python3_pkgversion 3.11

Name:           python-dsv-sdk
Version:        1.0.4
Release:        %autorelease
Summary:        The Delinea DevOps Secret Vault Python SDK

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/python-dsv-sdk/
Source:         %{pypi_source python-dsv-sdk}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  (python%{python3_pkgversion}dist(flit-core) < 4~~ with python%{python3_pkgversion}dist(flit-core) >= 2)
BuildRequires:  python%{python3_pkgversion}dist(requests) >= 2.22


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-dsv-sdk' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-python-dsv-sdk
Summary:        %{summary}

%description -n python%{python3_pkgversion}-python-dsv-sdk %_description


%prep
%autosetup -p1 -n python-dsv-sdk-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-python-dsv-sdk -f %{pyproject_files}


%changelog
%autochangelog