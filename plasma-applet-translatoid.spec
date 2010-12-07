%define shortname translatoid-1.1
%define version 1.1
%define svn svn20091215
%define release %mkrel -c %svn 3

Name:		plasma-applet-translatoid
Version:	%version
Release:	%release
Summary:	Plasma widget to translate text using Google Translate
Source0:	http://thecorpo.fr/sacha/translatoid/%{shortname}-%{svn}.tar.bz2
Patch0:		translatoid-1.1-fix-translation-text-parsing.patch
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://kde-look.org/content/show.php/translatoid?content=97511
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	kdelibs4-devel
BuildRequires:	libqjson-devel
Provides:	plasma-applet

%description
A plasma widget to translate text using Google Translate

%files
%defattr(-,root,root)
%doc README licence.txt
%{_kde_libdir}/kde4/plasma_applet_translatoid.so
%{_kde_services}/plasma-applet-translatoid.desktop
%{_kde_iconsdir}/*/*/*/translator.*
%{_kde_iconsdir}/kbflags/*
%{_kde_appsdir}/translatoid/translatoid.db
%{_kde_appsdir}/cmake/modules/FindQJSON.cmake

%prep
%setup -q -n %{shortname}
%patch0 -p0 -b .parsing

%build
%cmake_kde4

%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
