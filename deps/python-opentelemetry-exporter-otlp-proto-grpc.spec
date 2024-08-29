
%global python3_pkgversion 3.11

Name:           python-opentelemetry-exporter-otlp-proto-grpc
Version:        1.24.0
Release:        %autorelease
Summary:        OpenTelemetry Collector Protobuf over gRPC Exporter

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp-proto-grpc
Source:         %{pypi_source opentelemetry_exporter_otlp_proto_grpc}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)
BuildRequires:  python%{python3_pkgversion}dist(deprecated) >= 1.2.6
BuildRequires:  (python%{python3_pkgversion}dist(googleapis-common-protos) >= 1.52 with python%{python3_pkgversion}dist(googleapis-common-protos) < 2)
BuildRequires:  (python%{python3_pkgversion}dist(grpcio) < 2~~ with python%{python3_pkgversion}dist(grpcio) >= 1)
BuildRequires:  (python%{python3_pkgversion}dist(opentelemetry-api) >= 1.15 with python%{python3_pkgversion}dist(opentelemetry-api) < 2)
BuildRequires:  python%{python3_pkgversion}dist(opentelemetry-exporter-otlp-proto-common) = 1.24.0
BuildRequires:  python%{python3_pkgversion}dist(opentelemetry-proto) = 1.24.0
BuildRequires:  (python%{python3_pkgversion}dist(opentelemetry-sdk) >= 1.24 with python%{python3_pkgversion}dist(opentelemetry-sdk) < 1.25)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opentelemetry-exporter-otlp-proto-grpc' generated
automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-grpc
Summary:        %{summary}

%description -n python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-grpc %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n opentelemetry_exporter_otlp_proto_grpc-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-grpc -f %{pyproject_files}


%changelog
%autochangelog