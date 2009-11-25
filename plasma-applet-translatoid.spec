%define shortname translatoid-1.1
%define version 1.1
%define svn svn20091125
%define release %mkrel 0.%{svn}.1

Name:		plasma-applet-translatoid
Version:	%version
Release:	%release
Summary:	Plasma widget to translate text using Google Translate
Source0:	http://thecorpo.fr/sacha/translatoid/%{shortname}-%{svn}.tar.gz
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

%build
%cmake_kde4

%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
%__rm -rf %{buildroot}
