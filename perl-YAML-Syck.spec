%define	module	YAML-Syck
%define upstream_version 1.19

%define Werror_cflags %nil

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Fast, lightweight YAML loader and dumper
License:	MIT
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/YAML/%{module}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
Provides:	perl-YAML-parser

%description
This module provides a Perl interface to the libsyck data
serialization library. It exports the Dump and Load functions for
converting Perl data structures to YAML strings, and the other way
around.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%{__make} test

%install
%makeinstall_std

%files
%doc Changes COPYING README
%{_mandir}/*/*
%{perl_vendorarch}/JSON
%{perl_vendorarch}/YAML
%{perl_vendorarch}/auto/YAML
