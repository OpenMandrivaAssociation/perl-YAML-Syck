%define	module		YAML-Syck
%define	name		perl-%{module}
%define	modprefix	YAML
%define version		1.05
%define	release		%mkrel 3

Name: 		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Fast, lightweight YAML loader and dumper
License:	MIT
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel >= 5.3
Provides:   perl-YAML-parser
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
This module provides a Perl interface to the libsyck data
serialization library. It exports the Dump and Load functions for
converting Perl data structures to YAML strings, and the other way
around.


%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes COPYING README
%{_mandir}/*/*
%{perl_vendorarch}/JSON
%{perl_vendorarch}/%{modprefix}
%{perl_vendorarch}/auto/%{modprefix}
