%define debug_package %{nil}

Summary:	Quake-like pull-down console
Name:		yeahconsole
Version:	0.3.4
Release:	2
License:	GPLv2
Group:		Terminals
Url:		http://phrat.de/downloads.html
Source0:	http://phrat.de/%{name}-%{version}.tar.xz
Source1:	examples
BuildRequires:	pkgconfig(x11)
Requires:	xterm

%description
Yeahconsole puts an xterm window on top of your screen that behaves like a 
console found in many games (like Quake). Its visibility can be
toggled by a keyboard shortcut (Control+Alt+y).

Yeahconsole is configured by editing .Xdefaults.
Please read the examples file.

%prep
%setup -q
cp %{SOURCE1} .
sed -i 's|/usr/local|%{buildroot}%{_prefix}|' Makefile
sed -i 's| -o root -g root||' Makefile

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}
%makeinstall_std

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=YeahConsole
Comment=%{Summary}
Exec=%{_bindir}/%{name}
Icon=terminals_section.png
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-System-Terminals;
EOF

%files
%doc examples README LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop



%changelog
* Thu May 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.3.4-1
+ Revision: 800409
- imported package yeahconsole


* Tue Jul 28 2009 KDulcimer <kdulcimer@unity-linux.org> 0.3.4-1-unity2009
- Build yeahconsole
