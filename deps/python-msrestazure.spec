
%global python3_pkgversion 3.11

Name:           python-msrestazure
Version:        0.6.4
Release:        %autorelease
Summary:        AutoRest swagger generator Python client runtime. Azure-specific module.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/Azure/msrestazure-for-python
Source:         %{pypi_source msrestazure}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  (python%{python3_pkgversion}dist(msrest) < 2~~ with python%{python3_pkgversion}dist(msrest) >= 0.6)
BuildRequires:  (python%{python3_pkgversion}dist(adal) < 2~~ with python%{python3_pkgversion}dist(adal) >= 0.6)
BuildRequires:  python%{python3_pkgversion}dist(six)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'msrestazure' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-msrestazure
Summary:        %{summary}

%description -n python%{python3_pkgversion}-msrestazure %_description


%prep
%autosetup -p1 -n msrestazure-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-msrestazure -f %{pyproject_files}


%changelog
%autochangelog