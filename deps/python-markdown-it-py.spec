
%global python3_pkgversion 3.11

Name:           python-markdown-it-py
Version:        3.0.0
Release:        %autorelease
Summary:        Python port of markdown-it. Markdown parsing, done right!

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/executablebooks/markdown-it-py
Source:         %{pypi_source markdown-it-py}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  (python%{python3_pkgversion}dist(flit-core) < 4~~ with python%{python3_pkgversion}dist(flit-core) >= 3.4)
BuildRequires:  (python%{python3_pkgversion}dist(mdurl) >= 0.1 with python%{python3_pkgversion}dist(mdurl) < 1)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'markdown-it-py' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-markdown-it-py
Summary:        %{summary}

%description -n python%{python3_pkgversion}-markdown-it-py %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n markdown-it-py-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/markdown-it $RPM_BUILD_ROOT/usr/bin/markdown-it%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/markdown-it|/usr/bin/markdown-it%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-markdown-it-py -f %{pyproject_files}


%changelog
%autochangelog