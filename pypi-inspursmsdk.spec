#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-inspursmsdk
Version  : 1.2.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/24/7b/0228a7f4438858cf912de338c38fdb7940bc5c8bfbe937406af2068b0998/inspursmsdk-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/24/7b/0228a7f4438858cf912de338c38fdb7940bc5c8bfbe937406af2068b0998/inspursmsdk-1.2.0.tar.gz
Summary  : inspur server manager api
Group    : Development/Tools
License  : MIT
Requires: pypi-inspursmsdk-python = %{version}-%{release}
Requires: pypi-inspursmsdk-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jpype1)
BuildRequires : pypi(pycryptodome)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
BuildRequires : pypi(requests_toolbelt)

%description
inspursmsdk is a support tool for ansible.inspur.sm
        
        ## External requirements

%package python
Summary: python components for the pypi-inspursmsdk package.
Group: Default
Requires: pypi-inspursmsdk-python3 = %{version}-%{release}

%description python
python components for the pypi-inspursmsdk package.


%package python3
Summary: python3 components for the pypi-inspursmsdk package.
Group: Default
Requires: python3-core
Provides: pypi(inspursmsdk)
Requires: pypi(jpype1)
Requires: pypi(pycryptodome)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(requests_toolbelt)

%description python3
python3 components for the pypi-inspursmsdk package.


%prep
%setup -q -n inspursmsdk-1.2.0
cd %{_builddir}/inspursmsdk-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639063365
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
