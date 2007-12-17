%define	name	toppler
%define	version	1.1.3
%define	release	%mkrel 1
%define	Summary	Reimplementation of the old game known as Tower Toppler or Nebulous

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://heanet.dl.sourceforge.net/sourceforge/toppler/%{name}-%{version}.tar.bz2
License:	GPL
URL:		http://toppler.sourceforge.net/
Group:		Games/Arcade
BuildRequires:	SDL-devel SDL_mixer-devel zlib-devel
Requires(post):	rpm-helper

%description
It is an almost complete reimplementation of the old game known as Tower
Toppler or Nebulous. This game was available at least for PC, Atari, C64
and now the PC version is abandonware.

The goal of the game is to reach the target door of each of the 8 towers
in currently 2 missions with this little green animal. This door is
usually at the very top of the tower.

But finding the way by using elevators and walking trough a maze of doors
and platforms is not the only problem you have to solve. There are a bunch
of other creatures living on the tower that will hinder you to reach your
target by pushing you over the edge of the platforms.

The only weapon of defence you have is to throw a little snowball. But
most of the other creatures just don't care about this. So you must avoid
them.

%prep
%setup -q

%build
export CXXFLAGS="%optflags -U HISCOREDIR -D HISCOREDIR=\\\"%{_localstatedir}/games\\\" -U TOP_DATADIR -D TOP_DATADIR=\\\"%{_gamesdatadir}/%{name}\\\""
%configure2_5x	--bindir=%{_gamesbindir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std} pkglocalstatedir=%{_localstatedir}/games pkgdatadir=%{_gamesdatadir}/%{name} pkgdocdir=%{_docdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Tower Toppler
Comment=%{Summary}
Exec=soundwrapper %{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

chmod a+w $RPM_BUILD_ROOT%{_localstatedir}/games/toppler.hsc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
%create_ghostfile %{_localstatedir}/games/toppler.hsc root games 664

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-, root, root)
%doc %{_docdir}/%{name}-%{version}/*
%attr(664, root, games) %ghost %{_localstatedir}/games/toppler.hsc
%attr(2755, root, games) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_mandir}/man?/%{name}*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm


