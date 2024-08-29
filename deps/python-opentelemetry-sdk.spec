
%global python3_pkgversion 3.11

Name:           python-opentelemetry-sdk
Version:        1.24.0
Release:        %autorelease
Summary:        OpenTelemetry Python SDK

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-sdk
Source:         %{pypi_source opentelemetry_sdk}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)
BuildRequires:  python%{python3_pkgversion}dist(opentelemetry-api) = 1.24
BuildRequires:  python%{python3_pkgversion}dist(opentelemetry-semantic-conventions) = 0.45~b0
BuildRequires:  python%{python3_pkgversion}dist(typing-extensions) >= 3.7.4


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opentelemetry-sdk' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-opentelemetry-sdk
Summary:        %{summary}

%description -n python%{python3_pkgversion}-opentelemetry-sdk %_description


%prep
%autosetup -p1 -n opentelemetry_sdk-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-opentelemetry-sdk -f %{pyproject_files}


%changelog
%autochangelog