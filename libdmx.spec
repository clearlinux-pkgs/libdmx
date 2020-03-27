#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : libdmx
Version  : 1.1.4
Release  : 15
URL      : http://xorg.freedesktop.org/releases/individual/lib/libdmx-1.1.4.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libdmx-1.1.4.tar.gz
Source99 : http://xorg.freedesktop.org/releases/individual/lib/libdmx-1.1.4.tar.gz.sig
Summary  : X11 Distributed Multihead extension library
Group    : Development/Tools
License  : MIT
Requires: libdmx-lib = %{version}-%{release}
Requires: libdmx-license = %{version}-%{release}
BuildRequires : libX11-dev
BuildRequires : libX11-lib
BuildRequires : pkgconfig(dmxproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)

%description
libdmx - X Window System DMX (Distributed Multihead X) extension library
All questions regarding this software should be directed at the
Xorg mailing list:

%package dev
Summary: dev components for the libdmx package.
Group: Development
Requires: libdmx-lib = %{version}-%{release}
Provides: libdmx-devel = %{version}-%{release}
Requires: libdmx = %{version}-%{release}

%description dev
dev components for the libdmx package.


%package lib
Summary: lib components for the libdmx package.
Group: Libraries
Requires: libdmx-license = %{version}-%{release}

%description lib
lib components for the libdmx package.


%package license
Summary: license components for the libdmx package.
Group: Default

%description license
license components for the libdmx package.


%prep
%setup -q -n libdmx-1.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557077123
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557077123
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libdmx
cp COPYING %{buildroot}/usr/share/package-licenses/libdmx/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/dmxext.h
/usr/lib64/libdmx.so
/usr/lib64/pkgconfig/dmx.pc
/usr/share/man/man3/DMX.3
/usr/share/man/man3/DMXAddInput.3
/usr/share/man/man3/DMXAddScreen.3
/usr/share/man/man3/DMXChangeDesktopAttributes.3
/usr/share/man/man3/DMXChangeScreensAttributes.3
/usr/share/man/man3/DMXForceWindowCreation.3
/usr/share/man/man3/DMXGetDesktopAttributes.3
/usr/share/man/man3/DMXGetInputAttributes.3
/usr/share/man/man3/DMXGetInputCount.3
/usr/share/man/man3/DMXGetScreenAttributes.3
/usr/share/man/man3/DMXGetScreenCount.3
/usr/share/man/man3/DMXGetWindowAttributes.3
/usr/share/man/man3/DMXQueryExtension.3
/usr/share/man/man3/DMXQueryVersion.3
/usr/share/man/man3/DMXRemoveInput.3
/usr/share/man/man3/DMXRemoveScreen.3
/usr/share/man/man3/DMXSync.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdmx.so.1
/usr/lib64/libdmx.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libdmx/COPYING
