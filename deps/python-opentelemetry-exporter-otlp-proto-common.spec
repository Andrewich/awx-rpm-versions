
%global python3_pkgversion 3.11

Name:           python-opentelemetry-exporter-otlp-proto-common
Version:        1.24.0
Release:        %autorelease
Summary:        OpenTelemetry Protobuf encoding

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp-proto-common
Source:         %{pypi_source opentelemetry_exporter_otlp_proto_common}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)
BuildRequires:  python%{python3_pkgversion}dist(opentelemetry-proto) = 1.24


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opentelemetry-exporter-otlp-proto-common' generated
automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-common
Summary:        %{summary}

%description -n python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-common %_description


%prep
%autosetup -p1 -n opentelemetry_exporter_otlp_proto_common-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-common -f %{pyproject_files}


%changelog
%autochangelog