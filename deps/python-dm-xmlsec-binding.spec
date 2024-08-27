
%global python3_pkgversion 3.11

Name:           python-dm-xmlsec-binding
Version:        3.0
Release:        %autorelease
Summary:        Cython/lxml based binding for the XML security library -- for lxml 3.x

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/dm.xmlsec.binding
Source:         %{pypi_source dm.xmlsec.binding}

BuildArch:      x86_64
BuildRequires:  python%{python3_pkgversion}-devel libxml2-devel xmlsec1-openssl-devel xmlsec1-devel gcc libtool-ltdl-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(lxml) >= 3


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'dm-xmlsec-binding' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-dm-xmlsec-binding
Summary:        %{summary}

%description -n python%{python3_pkgversion}-dm-xmlsec-binding %_description


%prep
%autosetup -p1 -n dm.xmlsec.binding-%{version}
sed -i '/Md5/d' src/_xmlsec.c
sed -i '/Sha1/d' src/_xmlsec.c


%build
%pyproject_wheel

%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-dm-xmlsec-binding -f %{pyproject_files}


%changelog
%autochangelog