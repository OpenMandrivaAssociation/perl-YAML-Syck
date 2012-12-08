%define	module	YAML-Syck
%define upstream_version 1.19

%define Werror_cflags %nil

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Fast, lightweight YAML loader and dumper
License:	MIT
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/YAML/%{module}-%{upstream_version}.tar.gz
Patch0:		YAML-Syck-1.19-string-format-fix.patch

BuildRequires:	perl-devel
Provides:	perl-YAML-parser

%description
This module provides a Perl interface to the libsyck data
serialization library. It exports the Dump and Load functions for
converting Perl data structures to YAML strings, and the other way
around.

%prep
%setup -q -n %{module}-%{upstream_version}
%patch0 -p1 -b .str_fmt~

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%__make test

%install
%makeinstall_std

%files
%doc Changes COPYING README
%{_mandir}/*/*
%{perl_vendorarch}/JSON
%{perl_vendorarch}/YAML
%{perl_vendorarch}/auto/YAML


%changelog
* Thu Jan 26 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 1.190.0-2
+ Revision: 769198
- string format fix
- cleanups
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - 1.19
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.170.0-2
+ Revision: 667466
- mass rebuild

* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.170.0-1mdv2011.0
+ Revision: 602398
- update to new version 1.17

* Fri Nov 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.150.0-1mdv2011.0
+ Revision: 596612
- update to 1.15

* Sat Aug 28 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.140.0-1mdv2011.0
+ Revision: 573794
- update to 1.14

* Sun Aug 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 569937
- update to 1.12

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.100.0-3mdv2011.0
+ Revision: 564363
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.100.0-2mdv2011.0
+ Revision: 555299
- rebuild

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 552376
- update to 1.10

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.1
+ Revision: 406388
- rebuild using %%perl_convert_version

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2010.0
+ Revision: 371655
- new version
- disable format errors

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-3mdv2009.1
+ Revision: 324623
- provides virtual package perl-YAML-parser

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.05-2mdv2009.0
+ Revision: 268884
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2009.0
+ Revision: 217442
- update to new version 1.05

* Sun Feb 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2008.1
+ Revision: 169972
- update to new version 1.04

* Mon Jan 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2008.1
+ Revision: 155677
- update to new version 1.01

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.00-2mdv2008.1
+ Revision: 151357
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdv2008.1
+ Revision: 116899
- update to new version 1.00
- update to new version 1.00

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.99-2mdv2008.1
+ Revision: 109332
- rebuild

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.99-1mdv2008.1
+ Revision: 104607
- update to new version 0.99
- rollback
- update to new version 0.98

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.97-1mdv2008.0
+ Revision: 78723
- update to new version 0.97

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.96-1mdv2008.0
+ Revision: 63981
- update to new version 0.96

* Mon Aug 06 2007 Funda Wang <fwang@mandriva.org> 0.95-1mdv2008.0
+ Revision: 59424
- New version 0.95

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.94-1mdv2008.0
+ Revision: 52532
- update to new version 0.94

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.91-1mdv2008.0
+ Revision: 46721
- update to new version 0.91

* Mon Apr 30 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 0.85-1mdv2008.0
+ Revision: 19376
-New version


* Sun Jan 28 2007 Scott Karns <scottk@mandriva.org> 0.82-1mdv2007.0
+ Revision: 114605
- Updated to CPAN version 0.82
- Changed license

* Fri Dec 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.72-1mdv2007.1
+ Revision: 97357
- new version

  + Scott Karns <scottk@mandriva.org>
    - import perl-YAML-Syck-0.67-1mdv2007.0

* Mon Jul 31 2006 Scott Karns <scottk@mandriva.org> 0.67-1mdv2007.0
- Updated to 0.67

* Sun Jul 02 2006 Scott Karns <scottk@mandriva.org> 0.61-1mdv2007.0
- Updated to 0.61

* Sun Jul 02 2006 Scott Karns <scottk@mandriva.org> 0.60-1mdv2007.0
- Updated to 0.60

* Sun May 28 2006 Scott Karns <scottk@mandriva.org> 0.45-1mdv2007.0
- Updated to 0.45

* Sat May 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.44-3mdk
- Fix BuildRequires, perl-devel is needed for the build

* Fri May 05 2006 Scott Karns <scottk@mandriva.org> 0.44-2mdk
- Put release conditional around BuildRequires: perl-devel

* Thu May 04 2006 Scott Karns <scottk@mandriva.org> 0.44-1mdk
- Updated to 0.44

* Sun Apr 30 2006 Scott Karns <scottk@mandriva.org> 0.43-1mdk
- Updated to 0.43

* Thu Apr 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.42-2mdk
- Add BuildRequires: Perl-devel
- Fix Source URL

* Wed Apr 26 2006 Scott Karns <scottk@mandriva.org> 0.42-1mdk
- Updated to 0.42

* Wed Apr 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.41-1mdk
- contributed by  Scott Karns <scott@karnstech.com>

