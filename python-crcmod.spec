# $Revision: 1.7 $ $Date: 2008-10-03 17:47:40 $

%define 	module	crcmod

Summary:	crcmod - Python module for creating functions computing CRC
Summary(pl.UTF-8):	crcmod - moduł Python umożliwiający generowanie funkcji liczących CRC
Name:		python-%{module}
Version:	1.2
Release:	2
License:	BSD-like
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/crcmod/%{module}-%{version}.tar.gz
# Source0-md5:	be98002a7bab37ca4a10fa59bc48aef9
URL:		http://crcmod.sourceforge.net/
BuildRequires:	python-devel >= 1:2.3
Requires:	python >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
crcmod is a Python module for creating functions computing the Cyclic
Redundancy Check (CRC). Any generating polynomial producing 8, 16, 32,
or 64 bit CRCs is allowed. Generated functions can be used in Python
or C/C++ source code can be generated.

%description -l pl.UTF-8
crcmod jest modułem Pythona umożliwiającym tworzenie funkcji
obliczających sumę kontrolną CRC. crcmod pozwala na użycie dowolnego
wielomianu generującego 8-, 16-, 32-, lub 64-bitową sumę CRC.
Wygenerowane funkcje mogą być używane w programach Pythona, jak
również odpowiedni kod w C/C++ do użycia w tych językach może zostać
stworzony.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
cd extmod
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

cd extmod
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitedir}

cp -a ../crcmod.py ../_crcfunpy.py $RPM_BUILD_ROOT%{py_sitedir}

%{py_comp} $RPM_BUILD_ROOT%{py_sitedir}
%{py_ocomp} $RPM_BUILD_ROOT%{py_sitedir}

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_crcfunext.so
%{py_sitedir}/*.py[oc]
%doc README
