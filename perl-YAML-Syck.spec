%define	upstream_name    YAML-Syck
%define upstream_version 1.19

%define Werror_cflags %nil

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Fast, lightweight YAML loader and dumper
License:	MIT
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/YAML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:   perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{relase}
Provides:   perl-YAML-parser

%description
This module provides a Perl interface to the libsyck data
serialization library. It exports the Dump and Load functions for
converting Perl data structures to YAML strings, and the other way
around.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

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
%{perl_vendorarch}/YAML
%{perl_vendorarch}/auto/YAML
