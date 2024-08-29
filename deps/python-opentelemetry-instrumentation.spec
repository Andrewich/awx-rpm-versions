
%global python3_pkgversion 3.11

Name:           python-opentelemetry-instrumentation
Version:        0.45~b0
Release:        %autorelease
Summary:        Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/opentelemetry-instrumentation
Source:         %{pypi_source opentelemetry_instrumentation 0.45b0}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)
BuildRequires:  (python%{python3_pkgversion}dist(opentelemetry-api) >= 1.4 with python%{python3_pkgversion}dist(opentelemetry-api) < 2)
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 16
BuildRequires:  (python%{python3_pkgversion}dist(wrapt) < 2~~ with python%{python3_pkgversion}dist(wrapt) >= 1)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opentelemetry-instrumentation' generated automatically by
pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-opentelemetry-instrumentation
Summary:        %{summary}

%description -n python%{python3_pkgversion}-opentelemetry-instrumentation %_description


%prep
%autosetup -p1 -n opentelemetry_instrumentation-0.45b0


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-opentelemetry-instrumentation -f %{pyproject_files}


%changelog
%autochangelog