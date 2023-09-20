Name:           python-ntlm
Version:        1.1.0
Release:        1%{?dist}
Summary:        Python library that provides NTLM support, including an authentication handler for urllib2. Works with pass-the-hash in additon to password authentication.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://code.google.com/p/python-ntlm
Source:         %{pypi_source python-ntlm}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-ntlm' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-python-ntlm
Summary:        %{summary}

%description -n python3-python-ntlm %_description


%prep
%autosetup -p1 -n python-ntlm-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-python-ntlm -f %{pyproject_files}


%changelog
* Wed Sep 20 2023 Martin Juhl <m@rtinjuhl.dk> - 1.1.0-1
- Initial package