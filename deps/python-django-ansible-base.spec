
%global python3_pkgversion 3.11
%global python3__sitelib /usr/lib/python%{python3_pkgversion}/site-packages

Name:           python-django-ansible-base
Version:        20240701
Release:        %autorelease
Summary:        Reserved package

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/django-ansible-base/
Source:         https://github.com/ansible/django-ansible-base/releases/download/2024.7.1/django_ansible_base-2024.7.1.tar.gz 
Patch:		django-ansible-base-versionfix.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 64
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(cryptography)
BuildRequires:  (python%{python3_pkgversion}dist(django) < 4.3~~ with python%{python3_pkgversion}dist(django) >= 4.2.5)
BuildRequires:  python%{python3_pkgversion}dist(djangorestframework)
BuildRequires:  python%{python3_pkgversion}dist(django-crum)
BuildRequires:  python%{python3_pkgversion}dist(django-split-settings)
BuildRequires:  python%{python3_pkgversion}dist(inflection)
BuildRequires:  python%{python3_pkgversion}dist(pyjwt)
BuildRequires:  python%{python3_pkgversion}dist(requests)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-ansible-base' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-ansible-base
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-ansible-base %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%package -n python%{python3_pkgversion}-django-ansible-base+rest_filters
Summary: Metapackage for python%{python3_pkgversion}-django-ansible-base: rest_filters extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}-django-ansible-base = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-django-ansible-base+rest_filters = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(django-ansible-base[rest_filters]) = 2024.7.1

%description -n python%{python3_pkgversion}-django-ansible-base+rest_filters
This is a metapackage bringing in rest_filters extras requires for python%{python3_pkgversion}-django-ansible-base.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-django-ansible-base+rest_filters
%ghost %{python3__sitelib}/*.dist-info


%package -n python%{python3_pkgversion}-django-ansible-base+jwt_consumer
Summary: Metapackage for python%{python3_pkgversion}-django-ansible-base: jwt_consumer extras
AutoReq: no
Requires: python(abi) = %{python3_pkgversion}
Requires: python%{python3_pkgversion}-django-ansible-base = %{?epoch:%{epoch}:}%{version}-%{release}
AutoProv: no
Provides: python%{python3_pkgversion}-django-ansible-base+jwt_consumer = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: python%{python3_pkgversion}dist(django-ansible-base[jwt_consumer]) = 2024.7.1

%description -n python%{python3_pkgversion}-django-ansible-base+jwt_consumer
This is a metapackage bringing in jwt_consumer extras requires for python%{python3_pkgversion}-django-ansible-base.
It contains no code, just makes sure the dependencies are installed.

%files -n python%{python3_pkgversion}-django-ansible-base+jwt_consumer
%ghost %{python3__sitelib}/*.dist-info

%prep
%autosetup -p1 -n django_ansible_base-2024.7.1


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django-ansible-base -f %{pyproject_files}


%changelog
%autochangelog
