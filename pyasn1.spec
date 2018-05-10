#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyasn1
Version  : 0.4.2
Release  : 46
URL      : https://pypi.debian.net/pyasn1/pyasn1-0.4.2.tar.gz
Source0  : https://pypi.debian.net/pyasn1/pyasn1-0.4.2.tar.gz
Summary  : ASN.1 types and codecs
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pyasn1-python3
Requires: pyasn1-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
ASN.1 library for Python
------------------------
[![PyPI](https://img.shields.io/pypi/v/pyasn1.svg?maxAge=2592000)](https://pypi.python.org/pypi/pyasn1)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyasn1.svg)](https://pypi.python.org/pypi/pyasn1/)
[![Build status](https://travis-ci.org/etingof/pyasn1.svg?branch=master)](https://secure.travis-ci.org/etingof/pyasn1)
[![Coverage Status](https://img.shields.io/codecov/c/github/etingof/pyasn1.svg)](https://codecov.io/github/etingof/pyasn1)
[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/etingof/pyasn1/master/LICENSE.txt)

%package legacypython
Summary: legacypython components for the pyasn1 package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pyasn1 package.


%package python
Summary: python components for the pyasn1 package.
Group: Default
Requires: pyasn1-python3

%description python
python components for the pyasn1 package.


%package python3
Summary: python3 components for the pyasn1 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyasn1 package.


%prep
%setup -q -n pyasn1-0.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519345745
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1519345745
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
