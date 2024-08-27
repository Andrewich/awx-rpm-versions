
%global python3_pkgversion 3.11

Name:           python-googleapis-common-protos
Version:        1.63.0
Release:        %autorelease
Summary:        Common protobufs used in Google APIs

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/googleapis/python-api-common-protos
Source:         %{pypi_source googleapis-common-protos}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  ((python%{python3_pkgversion}dist(protobuf) < 3.20 or python%{python3_pkgversion}dist(protobuf) > 3.20) with (python%{python3_pkgversion}dist(protobuf) < 3.20.1 or python%{python3_pkgversion}dist(protobuf) > 3.20.1) with (python%{python3_pkgversion}dist(protobuf) < 4.21.1 or python%{python3_pkgversion}dist(protobuf) > 4.21.1) with (python%{python3_pkgversion}dist(protobuf) < 4.21.2 or python%{python3_pkgversion}dist(protobuf) > 4.21.2) with (python%{python3_pkgversion}dist(protobuf) < 4.21.3 or python%{python3_pkgversion}dist(protobuf) > 4.21.3) with (python%{python3_pkgversion}dist(protobuf) < 4.21.4 or python%{python3_pkgversion}dist(protobuf) > 4.21.4) with (python%{python3_pkgversion}dist(protobuf) < 4.21.5 or python%{python3_pkgversion}dist(protobuf) > 4.21.5) with python%{python3_pkgversion}dist(protobuf) < 5~~dev0 with python%{python3_pkgversion}dist(protobuf) >= 3.19.5)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'googleapis-common-protos' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-googleapis-common-protos
Summary:        %{summary}

%description -n python%{python3_pkgversion}-googleapis-common-protos %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n googleapis-common-protos-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-googleapis-common-protos -f %{pyproject_files}


%changelog
%autochangelog