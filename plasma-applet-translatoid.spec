%define shortname translatoid

Name:		plasma-applet-translatoid
Version:	1.0
Release:	%mkrel 0.rc1.1
Summary:	Plasma widget to translate text using Google Translate
Source0:	http://thecorpo.fr/sacha/translatoid/%{shortname}%{version}.tar.gz
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://kde-look.org/content/show.php/translatoid?content=97511
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	kdelibs4-devel
Provides:	plasma-applet

%description
A plasma widget to translate text using Google Translate

%files
%defattr(-,root,root)
%doc README licence.txt
%{_kde_libdir}/kde4/plasma_applet_translatoid.so
%{_kde_datadir}/kde4/services/plasma-applet-translatoid.desktop
%{_kde_iconsdir}/*/*/*/translator.*
%{_kde_iconsdir}/kbflags/*

%prep
%setup -q -n %{shortname}

%build
%cmake_kde4

%make

%install
rm -Rf %{buildroot}
cd build
%{makeinstall_std}

%clean
rm -rf %buildroot
