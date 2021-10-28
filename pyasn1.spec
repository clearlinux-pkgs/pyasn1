#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyasn1
Version  : 0.4.8
Release  : 86
URL      : https://files.pythonhosted.org/packages/a4/db/fffec68299e6d7bad3d504147f9094830b704527a7fc098b721d38cc7fa7/pyasn1-0.4.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/a4/db/fffec68299e6d7bad3d504147f9094830b704527a7fc098b721d38cc7fa7/pyasn1-0.4.8.tar.gz
Summary  : ASN.1 types and codecs
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pyasn1-license = %{version}-%{release}
Requires: pyasn1-python = %{version}-%{release}
Requires: pyasn1-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : py
BuildRequires : pytest

%description
ASN.1 library for Python
------------------------
[![PyPI](https://img.shields.io/pypi/v/pyasn1.svg?maxAge=2592000)](https://pypi.org/project/pyasn1)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyasn1.svg)](https://pypi.org/project/pyasn1/)
[![Build status](https://travis-ci.org/etingof/pyasn1.svg?branch=master)](https://secure.travis-ci.org/etingof/pyasn1)
[![Coverage Status](https://img.shields.io/codecov/c/github/etingof/pyasn1.svg)](https://codecov.io/github/etingof/pyasn1)
[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/etingof/pyasn1/master/LICENSE.txt)

%package license
Summary: license components for the pyasn1 package.
Group: Default

%description license
license components for the pyasn1 package.


%package python
Summary: python components for the pyasn1 package.
Group: Default
Requires: pyasn1-python3 = %{version}-%{release}

%description python
python components for the pyasn1 package.


%package python3
Summary: python3 components for the pyasn1 package.
Group: Default
Requires: python3-core
Provides: pypi(pyasn1)

%description python3
python3 components for the pyasn1 package.


%prep
%setup -q -n pyasn1-0.4.8
cd %{_builddir}/pyasn1-0.4.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603399665
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyasn1
cp %{_builddir}/pyasn1-0.4.8/LICENSE.rst %{buildroot}/usr/share/package-licenses/pyasn1/7f822087024e192164d73581d9fba060445de7e8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyasn1/7f822087024e192164d73581d9fba060445de7e8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
