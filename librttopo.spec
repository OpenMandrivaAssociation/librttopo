%define major 1
%define libname %mklibname rttopo
%define devname %mklibname rttopo -d

Name: librttopo
Version: 1.1.0
Release: 2
Source0: https://git.osgeo.org/gitea/rttopo/librttopo/archive/librttopo-%{version}.tar.gz
Summary: RT Topology Library
URL: https://git.osgeo.org/gitea/rttopo/librttopo
License: GPLv2
Group: System/Libraries
BuildRequires: pkgconfig(geos)

%description
The RT Topology Library exposes an API to create and manage standard
(ISO 13249 aka SQL/MM) topologies using user-provided data stores

%package -n %{libname}
Summary: RT Topology Library
Group: System/Libraries

%description -n %{libname}
The RT Topology Library exposes an API to create and manage standard
(ISO 13249 aka SQL/MM) topologies using user-provided data stores

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

The RT Topology Library exposes an API to create and manage standard
(ISO 13249 aka SQL/MM) topologies using user-provided data stores

%prep
%autosetup -p1 -n %{name}
[ -e configure ] || ./autogen.sh
%configure

%build
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
