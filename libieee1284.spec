Summary: A library for interfacing IEEE 1284-compatible devices
Name: libieee1284
Version: 0.2.11
Release: 9%{?dist}
License: GPLv2+
Group: System Environment/Libraries
URL: http://cyberelk.net/tim/libieee1284/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch1: libieee1284-strict-aliasing.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: xmlto, python-devel

%description
The libieee1284 library is for communicating with parallel port devices.

%package devel
Summary: Files for developing applications that use libieee1284
Requires: %{name} = %{version}-%{release}
Group: Development/Libraries

%description devel
The header files, static library, libtool library and man pages for
developing applications that use libieee1284.

%package python
Summary: Python extension module for libieee1284
Requires: %{name} = %{version}-%{release}
Group: System Environment/Libraries

%description python
Python extension module for libieee1284.  To use libieee1284 with Python,
use 'import ieee1284'.

%prep
%setup -q
%patch1 -p1 -b .strict-aliasing

%build
touch doc/interface.xml
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} INSTALL="install -p" install
rm -f %{buildroot}%{_libdir}/python*/*/*a
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING TODO AUTHORS NEWS
%{_libdir}/*.so.*
%{_bindir}/*

%files devel
%defattr(-,root,root)
%{_includedir}/ieee1284.h
%{_libdir}/*.so
%{_mandir}/*/*

%files python
%defattr(-,root,root)
%{_libdir}/python*/*/*.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Wed Jun 23 2010 Tim Waugh <twaugh@redhat.com> 0.2.11-9
- The python sub-package now requires the exactly-matching main
  package (bug #605169).
- Fixed strict aliasing warnings (bug #605170).

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.2.11-8.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 14 2009 Tim Waugh <twaugh@redhat.com> 0.2.11-7
- Package review fix: removed trailing dot in python package summary
  (bug #226031).

* Thu May 14 2009 Tim Waugh <twaugh@redhat.com> 0.2.11-6
- Package review fixes (bug #226031):
  - Drop prereq on ldconfig.
  - Removed trailing dot in devel package summary.
  - Fixed devel package requirement on main package.
  - Use SMP make flags.
  - Removed static libraries and la files.
  - Fixed source URL.
  - Make sure timestamps are preserved on install.
  - Ship AUTHORS and NEWS.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 0.2.11-4
- Rebuild for Python 2.6

* Wed Feb 13 2008 Tim Waugh <twaugh@redhat.com> 0.2.11-3
- Don't build PDF documentation as this creates multilib conflicts.

* Wed Jan  9 2008 Tim Waugh <twaugh@redhat.com> 0.2.11-2
- Rebuilt.

* Tue Sep 18 2007 Tim Waugh <twaugh@redhat.com> 0.2.11-1
- 0.2.11 (bug #246406).

* Wed Aug 29 2007 Tim Waugh <twaugh@redhat.com> 0.2.9-5
- Added dist tag.
- Fixed summary.
- Better buildroot tag.
- More specific license tag.

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.2.9-4
- rebuild against python 2.5

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.2.9-3.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.2.9-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.2.9-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Jul 19 2005 Tim Waugh <twaugh@redhat.com> 0.2.9-3
- Rebuild man pages.

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 0.2.9-2
- Rebuild for new GCC.

* Thu Jan 20 2005 Tim Waugh <twaugh@redhat.com> 0.2.9-1
- 0.2.9.
- Build requires python-devel.
- Ship Python extension module.

* Wed Sep 22 2004 Than Ngo <than@redhat.com> 0.2.8-4 
- add Prereq: /sbin/ldconfig

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun  9 2003 Tim Waugh <twaugh@redhat.com> 0.2.8-1
- Initial Red Hat Linux package.

* Wed Feb 26 2003 Tim Waugh <twaugh@redhat.com>
- Use the Makefile rule to build the PDF.

* Sat Aug 24 2002 Tim Waugh <twaugh@redhat.com>
- Ship test program.

* Sat Aug  3 2002 Tim Waugh <twaugh@redhat.com>
- The archive is now distributed in .tar.bz2 format.

* Fri Apr 26 2002 Tim Waugh <twaugh@redhat.com>
- No need to create man page symlinks any more.
- Build requires xmlto now, not docbook-utils.

* Wed Apr 24 2002 Tim Waugh <twaugh@redhat.com>
- The tarball builds its own man pages now; just adjust the symlinks.
- Run ldconfig.

* Mon Jan  7 2002 Tim Waugh <twaugh@redhat.com>
- Ship the PDF file with the devel package.

* Thu Nov 15 2001 Tim Waugh <twaugh@redhat.com>
- Initial specfile.
