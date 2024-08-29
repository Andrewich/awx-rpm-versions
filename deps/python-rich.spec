
%global python3_pkgversion 3.11

Name:           python-rich
Version:        13.7.1
Release:        %autorelease
Summary:        Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/Textualize/rich
Source:         %{pypi_source rich}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(poetry-core) >= 1
BuildRequires:  python%{python3_pkgversion}dist(markdown-it-py) >= 2.2
BuildRequires:  (python%{python3_pkgversion}dist(pygments) < 3~~ with python%{python3_pkgversion}dist(pygments) >= 2.13)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'rich' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-rich
Summary:        %{summary}

%description -n python%{python3_pkgversion}-rich %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n rich-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-rich -f %{pyproject_files}


%changelog
%autochangelog