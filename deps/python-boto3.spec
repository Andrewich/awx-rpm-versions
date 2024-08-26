
%global python3_pkgversion 3.11

Name:           python-boto3
Version:        1.34.47
Release:        %autorelease
Summary:        The AWS SDK for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/boto/boto3
Source:         %{pypi_source boto3}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(botocore) < 1.35~~ with python%{python3_pkgversion}dist(botocore) >= 1.34.47)
BuildRequires:  (python%{python3_pkgversion}dist(jmespath) < 2~~ with python%{python3_pkgversion}dist(jmespath) >= 0.7.1)
BuildRequires:  (python%{python3_pkgversion}dist(s3transfer) < 0.11~~ with python%{python3_pkgversion}dist(s3transfer) >= 0.10)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'boto3' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-boto3
Summary:        %{summary}

%description -n python%{python3_pkgversion}-boto3 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n boto3-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-boto3 -f %{pyproject_files}


%changelog
%autochangelog