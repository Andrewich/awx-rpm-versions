
%global python3_pkgversion 3.11

Name:           python-opentelemetry-semantic-conventions
Version:        0.45~b0
Release:        %autorelease
Summary:        OpenTelemetry Semantic Conventions

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-semantic-conventions
Source:         %{pypi_source opentelemetry_semantic_conventions 0.45b0}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(hatchling)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opentelemetry-semantic-conventions' generated automatically by
pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-opentelemetry-semantic-conventions
Summary:        %{summary}

%description -n python%{python3_pkgversion}-opentelemetry-semantic-conventions %_description


%prep
%autosetup -p1 -n opentelemetry_semantic_conventions-0.45b0


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-opentelemetry-semantic-conventions -f %{pyproject_files}


%changelog
%autochangelog