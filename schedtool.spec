Name:		schedtool
Version:	1.3.0
Release:	7
Summary:	Tool for setting and querying scheduling parameters
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://freequaos.host.sk/schedtool/
Source0:	http://freequaos.host.sk/schedtool/%name-%version.tar.bz2

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
%autosetup -p1

%build
%set_build_flags
sed -i -e 's/^CFLAGS=.*/CFLAGS=%{optflags}/g' Makefile
sed -i -e 's#^CC=gcc#CC=%{__cc}#g' Makefile

%make_build

%install
%make_install RELEASE="%{name}" DESTPREFIX=%{_prefix}
chmod -x $RPM_BUILD_ROOT%{_mandir}/man8/schedtool.8.gz
gunzip $RPM_BUILD_ROOT%{_mandir}/man8/schedtool.8.gz

%files
%doc CHANGES INSTALL LICENSE PACKAGERS README SCHED_DESIGN TUNING
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man8/%{name}.*
