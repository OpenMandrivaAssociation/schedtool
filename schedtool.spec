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


