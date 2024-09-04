
%global python3_pkgversion 3.11

Name:           python-twilio
Version:        8.13.0
Release:        %autorelease
Summary:        Twilio API client and TwiML generator

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/twilio/twilio-python/
Source:         %{pypi_source twilio}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(requests) >= 2
BuildRequires:  (python%{python3_pkgversion}dist(pyjwt) < 3~~ with python%{python3_pkgversion}dist(pyjwt) >= 2)
BuildRequires:  python%{python3_pkgversion}dist(aiohttp) >= 3.8.4
BuildRequires:  python%{python3_pkgversion}dist(aiohttp-retry) >= 2.8.3


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'twilio' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-twilio
Summary:        %{summary}

%description -n python%{python3_pkgversion}-twilio %_description


%prep
%autosetup -p1 -n twilio-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-twilio -f %{pyproject_files}


%changelog
%autochangelog