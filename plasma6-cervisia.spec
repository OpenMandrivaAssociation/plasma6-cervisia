%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	CVS frontend for KDE
Name:		plasma6-cervisia
Version:	24.01.90
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/cervisia-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6Su)
BuildRequires:  qt6-qtbase-theme-gtk3
Requires:	cvs

%description
CVS frontend for KDE.

%files -f %{name}.lang -f cvsservice.lang
%{_bindir}/cervisia
%{_bindir}/cvsaskpass
%{_bindir}/cvsservice6
%{_libdir}/libkdeinit6_cervisia.so
%{_libdir}/libkdeinit6_cvsaskpass.so
%{_libdir}/libkdeinit6_cvsservice.so
%{_libdir}/qt6/plugins/cervisiapart6.so
%{_datadir}/applications/org.kde.cervisia.desktop
%{_datadir}/config.kcfg/cervisiapart.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.cervisia6.*
%{_datadir}/knotifications6/cervisia.notifyrc
%{_datadir}/kservices6/org.kde.cervisiapart6.desktop
%{_datadir}/kservices6/org.kde.cvsservice6.desktop
%{_datadir}/kxmlgui6/cervisia
%{_datadir}/kxmlgui6/cervisiapart
%{_datadir}/metainfo/org.kde.cervisia.appdata.xml
%{_datadir}/icons/*/*/*/vcs-*.*
%{_datadir}/icons/*/*/*/cervisia.*
%{_mandir}/man1/cervisia.1*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n cervisia-%{version}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-man --with-html
%find_lang cvsservice
