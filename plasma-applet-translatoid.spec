%define oname translatoid

Name:		plasma-applet-%{oname}
Version:	1.4
Release:	2
Summary:	Plasma widget to translate text using Google Translate
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://kde-look.org/content/show.php/translatoid?content=97511
Source0:	http://212.158.157.7/translatoid/%{oname}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(QJson)
Provides:	plasma-applet

%description
A plasma widget to translate text using Google Translate.

%files
%doc licence.txt
%{_kde_libdir}/kde4/plasma_applet_translatoid.so
%{_kde_services}/plasma-applet-translatoid.desktop
%{_kde_iconsdir}/*/*/*/translator.*
%{_kde_iconsdir}/kbflags/*
%{_kde_appsdir}/translatoid/translatoid.db

%prep
%setup -q -n %{oname}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# We really don't need it
rm -f %{buildroot}%{_kde_appsdir}/cmake/modules/FindQJSON.cmake