
%global python3_pkgversion 3.11

Name:           python-grpcio
Version:        1.64.1
Release:        %autorelease
Summary:        HTTP/2-based RPC framework

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://grpc.io
Source:         %{pypi_source grpcio}


BuildRequires: gcc-c++
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'grpcio' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-grpcio
Summary:        %{summary}

%description -n python%{python3_pkgversion}-grpcio %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n grpcio-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-grpcio -f %{pyproject_files}


%changelog
%autochangelog