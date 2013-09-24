%define	modname	YAML-Syck
%define	modver	1.19

Summary:	Fast, lightweight YAML loader and dumper
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	5
License:	MIT
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/YAML/%{modname}-%{modver}.tar.gz
Patch0:		YAML-Syck-1.19-string-format-fix.patch
BuildRequires:	perl-devel
Provides:	perl-YAML-parser

%description
This module provides a Perl interface to the libsyck data
serialization library. It exports the Dump and Load functions for
converting Perl data structures to YAML strings, and the other way
around.

%prep
%setup -qn %{modname}-%{modver}
%apply_patches

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc Changes COPYING README
%{perl_vendorarch}/JSON
%{perl_vendorarch}/YAML
%{perl_vendorarch}/auto/YAML
%{_mandir}/man3/*

