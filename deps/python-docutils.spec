
%global python3_pkgversion 3.11

Name:           python-docutils
Version:        0.20.1
Release:        %autorelease
Summary:        Docutils -- Python Documentation Utilities

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://docutils.sourceforge.io/
Source:         %{pypi_source docutils}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(setuptools) >= 40.8
BuildRequires:  python%{python3_pkgversion}dist(wheel)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'docutils' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-docutils
Summary:        %{summary}

%description -n python%{python3_pkgversion}-docutils %_description


%prep
%autosetup -p1 -n docutils-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/docutils $RPM_BUILD_ROOT/usr/bin/docutils%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/rst2html.py $RPM_BUILD_ROOT/usr/bin/rst2html.py%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/rst2html4.py $RPM_BUILD_ROOT/usr/bin/rst2html4.py%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/rst2html5.py $RPM_BUILD_ROOT/usr/bin/rst2html5.py%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/rst2latex.py $RPM_BUILD_ROOT/usr/bin/rst2latex.py%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/rst2man.py $RPM_BUILD_ROOT/usr/bin/rst2man.py%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/rst2odt.py $RPM_BUILD_ROOT/usr/bin/rst2odt.py%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/rst2odt_prepstyles.py $RPM_BUILD_ROOT/usr/bin/rst2odt_prepstyles.py%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/rst2pseudoxml.py $RPM_BUILD_ROOT/usr/bin/rst2pseudoxml.py%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/rst2s5.py $RPM_BUILD_ROOT/usr/bin/rst2s5.py%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/rst2xetex.py $RPM_BUILD_ROOT/usr/bin/rst2xetex.py%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/rst2xml.py $RPM_BUILD_ROOT/usr/bin/rst2xml.py%{python3_pkgversion}
mv $RPM_BUILD_ROOT/usr/bin/rstpep2html.py $RPM_BUILD_ROOT/usr/bin/rstpep2html.py%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/docutils|/usr/bin/docutils%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/rst2html.py|/usr/bin/rst2html.py%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/rst2html4.py|/usr/bin/rst2html4.py%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/rst2html5.py|/usr/bin/rst2html5.py%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/rst2latex.py|/usr/bin/rst2latex.py%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/rst2man.py|/usr/bin/rst2man.py%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/rst2odt.py|/usr/bin/rst2odt.py%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/rst2odt_prepstyles.py|/usr/bin/rst2odt_prepstyles.py%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/rst2pseudoxml.py|/usr/bin/rst2pseudoxml.py%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/rst2s5.py|/usr/bin/rst2s5.py%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/rst2xetex.py|/usr/bin/rst2xetex.py%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/rst2xml.py|/usr/bin/rst2xml.py%{python3_pkgversion}|g" %{pyproject_files}
sed -i "s|/usr/bin/rstpep2html.py|/usr/bin/rstpep2html.py%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-docutils -f %{pyproject_files}


%changelog
%autochangelog