#
# Conditional build:
%bcond_with	tests	# unit tests (fixtures missing in pypi tarball)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Setuptools revision control system plugin for Git
Summary(pl.UTF-8):	Wtyczka setuptools do systemu kontroli wersji Git
Name:		python-setuptools_pep8
Version:	0.9.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/setuptools-pep8/
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools-pep8/setuptools-pep8-%{version}.tar.gz
# Source0-md5:	8d21d3dbee4e82652b15b1873e789e6c
URL:		https://pypi.org/project/setuptools-pep8/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pep8 >= 1.4.6
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pep8 >= 1.4.6
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a plugin for setuptools that enables pep8 integration. Once
installed, Setuptools can be told to include in a package distribution
all the files tracked by pep8. This is an alternative to explicit
inclusion specifications with MANIFEST.in.

%description -l pl.UTF-8
Ten pakiet zawiera wtyczkę do setuptools włączającą integrację z
pep8em. Po zainstalowaniu jej, setuptools można przekazać, żeby
dołączyć do dystrybucji pakietu wszystkie pliki śledzone przez pep8a -
jest to alternatywa dla jawnego określenia plików w MANIFEST.in.

%package -n python3-setuptools_pep8
Summary:	Setuptools revision control system plugin for Git
Summary(pl.UTF-8):	Wtyczka setuptools do systemu kontroli wersji Git
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-setuptools_pep8
This is a plugin for setuptools that enables pep8 integration. Once
installed, Setuptools can be told to include in a package distribution
all the files tracked by pep8. This is an alternative to explicit
inclusion specifications with MANIFEST.in.

%description -n python3-setuptools_pep8 -l pl.UTF-8
Ten pakiet zawiera wtyczkę do setuptools włączającą integrację z
pep8em. Po zainstalowaniu jej, setuptools można przekazać, żeby
dołączyć do dystrybucji pakietu wszystkie pliki śledzone przez pep8a -
jest to alternatywa dla jawnego określenia plików w MANIFEST.in.

%prep
%setup -q -n setuptools-pep8-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python} src/tests/test_pep8_command.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} src/tests/test_pep8_command.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/tests
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS.rst README.rst
%{py_sitescriptdir}/setuptools_pep8
%{py_sitescriptdir}/setuptools_pep8-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-setuptools_pep8
%defattr(644,root,root,755)
%doc NEWS.rst README.rst
%{py3_sitescriptdir}/setuptools_pep8
%{py3_sitescriptdir}/setuptools_pep8-%{version}-py*.egg-info
%endif
