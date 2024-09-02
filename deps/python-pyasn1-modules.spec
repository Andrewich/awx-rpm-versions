
%global python3_pkgversion 3.11

Name:           python-pyasn1-modules
Version:        0.5.1
Release:        %autorelease
Summary:        A collection of ASN.1-based protocols modules

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pyasn1/pyasn1-modules
Source:         pyasn1_modules-0.3.0.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyasn1-modules' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pyasn1-modules
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyasn1-modules %_description


%prep
%autosetup -p1 -n pyasn1-modules-0.3.0


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pyasn1-modules -f %{pyproject_files}


%changelog
%autochangelog