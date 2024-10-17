%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	Reimplementation of the old game known as Tower Toppler or Nebulous
Name:		toppler
Version:	1.1.6
Release:	13
Source0:	https://sourceforge.net/projects/toppler/files/toppler/1.1.6/%{name}-%{version}.tar.gz
License:	GPL
URL:		https://toppler.sourceforge.net/
Group:		Games/Arcade
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(zlib)
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
export CXXFLAGS="%optflags -U HISCOREDIR -D HISCOREDIR=\\\"%{_localstatedir}/lib/games\\\" -U TOP_DATADIR -D TOP_DATADIR=\\\"%{_gamesdatadir}/%{name}\\\""
%configure2_5x	--bindir=%{_gamesbindir}
make

%install
%makeinstall_std pkglocalstatedir=%{_localstatedir}/lib/games pkgdatadir=%{_gamesdatadir}/%{name} pkgdocdir=%{_docdir}/%{name}-%{version}

rm -f %{buildroot}%{_datadir}/applications/%{name}.desktop
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Tower Toppler
Comment=%{Summary}
Exec=soundwrapper %{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

chmod a+w %{buildroot}%{_localstatedir}/lib/games/toppler.hsc

%find_lang %{name}

%clean

%post
%create_ghostfile %{_localstatedir}/lib/games/toppler.hsc root games 664

%files -f %{name}.lang
%defattr(-, root, root)
%doc %{_docdir}/%{name}-%{version}/*
%attr(664, root, games) %ghost %{_localstatedir}/lib/games/toppler.hsc
%attr(2755, root, games) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_mandir}/man?/%{name}*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-2mdv2011.0
+ Revision: 670722
- mass rebuild

* Fri Oct 01 2010 Funda Wang <fwang@mandriva.org> 1.1.4-1mdv2011.0
+ Revision: 582219
- new version 1.1.4

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-7mdv2010.1
+ Revision: 524232
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1.3-6mdv2010.0
+ Revision: 427428
- rebuild

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 1.1.3-5mdv2009.1
+ Revision: 366389
- fix str fmt

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.1.3-4mdv2009.0
+ Revision: 265767
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Mon Jun 02 2008 Olivier Blin <oblin@mandriva.com> 1.1.3-3mdv2009.0
+ Revision: 214227
- fix build with latest glibc (open with O_CREAT needs a third arg)

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-2mdv2008.1
+ Revision: 180339
- fix build
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Thu Aug 02 2007 Olivier Blin <oblin@mandriva.com> 1.1.3-1mdv2008.0
+ Revision: 58091
- use requires(post) instead of prereq
- 1.1.3


* Fri Nov 17 2006 Olivier Blin <oblin@mandriva.com> 1.1.2a-1mdv2007.0
+ Revision: 85258
- really pass directories, using CXXFLAGS
- fix top datadir
- xdg menu
- add desktop file and pixmap
- fix doc installation
- replace dir patches with cflags and make options
- 1.1.2a
- bunzip2 patches
- Import toppler

* Tue May 09 2006 Stefan van der Eijk <stefan@eijk.nu> 1.1.1-2mdk
- rebuild for sparc

* Tue Dec 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.1.1-1mdk
- 1.1.1

* Tue Dec 14 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.1.0-1mdk
- 1.1.0

* Thu Aug 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.0.6-3mdk
- Rebuild with new menu

* Sat Jun 05 2004 <lmontel@n2.mandrakesoft.com> 1.0.6-2mdk
- Rebuild

* Sun Feb 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.6-1mdk
- 1.0.6

* Mon Jan 26 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.5-1mdk
- 1.0.5

* Sun Jan 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.4-1mdk
- 1.0.4
- fix buildrequires (lib64..)
- add locales
- fix path to games data (P1)


