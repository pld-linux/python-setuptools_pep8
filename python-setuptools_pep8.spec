#
# Conditional build:
%bcond_with	tests	# unit tests (fixtures missing in pypi tarball)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	pep8 command for setuptools
Summary(pl.UTF-8):	Polecenie pep8 dla setuptools
Name:		python-setuptools_pep8
Version:	0.9.0
Release:	4
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
This package exposes the pep8 style guide checker as a sub-command of
setup.py.

%description -l pl.UTF-8
Ten pakiet udostępnia sprawdzanie stylu wg pep8 jako podpolecenie
setup.py.

%package -n python3-setuptools_pep8
Summary:	pep8 command for setuptools
Summary(pl.UTF-8):	Polecenie pep8 dla setuptools
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-setuptools_pep8
This package exposes the pep8 style guide checker as a sub-command of
setup.py.

%description -n python3-setuptools_pep8 -l pl.UTF-8
Ten pakiet udostępnia sprawdzanie stylu wg pep8 jako podpolecenie
setup.py.

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
