Name:		schedtool
Version:	1.3.0
Release:	%mkrel 2
Summary:	Tool for setting and querying scheduling parameters
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://freequaos.host.sk/schedtool/
Source:		%name-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
schedtool can set all scheduling parameters Linux is capable of or dis-
play information for given processes.
													
Long-running, non-interactive tasks may  benefit  from  SCHED_BATCH  as
timeslices are longer, less system-time is wasted by computing the next
runnable process and the caches stay stable.
													
Audio/video or other near-realtime applications may run with less skip-
ping  if  set  to SCHED_RR.  Use the static priority-switch -p to fine-
tune inter-process-hierarchies.
													
schedtool now supports setting the  CPU-affinity  introduced  in  linux
2.5.8.

%prep
%setup -q

%build
%make
# CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
install -m755 -d $RPM_BUILD_ROOT/%_bindir/
install -m755  %name $RPM_BUILD_ROOT/%_bindir/%name
install -m755 -d $RPM_BUILD_ROOT/%{_mandir}/man8/
install -m611  %name.8 $RPM_BUILD_ROOT/%{_mandir}/man8/%name.8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(755,root,root) %_bindir/*
%doc CHANGES INSTALL LICENSE PACKAGERS README SCHED_DESIGN TUNING
%attr(644,root,root) %{_mandir}/man8/%name.*




%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2011.0
+ Revision: 614810
- the mass rebuild of 2010.1 packages

* Thu Apr 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.0-1mdv2010.1
+ Revision: 533118
- update to 1.3.0
- fix license tag

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.2.10-5mdv2010.0
+ Revision: 433621
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.2.10-4mdv2009.0
+ Revision: 260601
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.2.10-3mdv2009.0
+ Revision: 252235
- rebuild

* Mon Mar 10 2008 Erwan Velu <erwan@mandriva.org> 1.2.10-1mdv2008.1
+ Revision: 183357
- 1.2.10

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2.9-1mdv2008.1
+ Revision: 140756
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jan 29 2007 Lenny Cartier <lenny@mandriva.com> 1.2.9-1mdv2007.0
+ Revision: 114845
- Update to 1.2.9
- Import schedtool

* Wed Feb 01 2006 Lenny Cartier <lenny@mandriva.com> 1.2.6-1mdk
- 1.2.6

* Thu Oct 20 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.2.5-2mdk
- fix man page (#13699)

* Tue Jul 05 2005 Lenny Cartier <lenny@mandriva.com> 1.2.5-1mdk
- 1.2.5

* Thu Mar 31 2005 Danny Tholen <obiwan@mailmij.org> 1.2.4-1mdk
- updated to latest version
- fix manpage

* Fri Aug 13 2004 Svetoslav Slavtchev <svetljo@gmx.de> 1.1.1-1mdk
- recompile for contrib

* Tue Jul 20 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 1.1.1-1thac
- Updated to latest version.

* Fri Jun 18 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 1.0-3thac
- Changed defattr to root,root
-

* Fri Jun 18 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 1.0-2thac
- Moved to bindir

* Sun Jun 13 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 1.0-1thac
- Built for Mandrake 10.0

