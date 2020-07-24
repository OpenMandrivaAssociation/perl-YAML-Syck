%define	upstream_name    YAML-Syck
%define upstream_version 1.32

%define Werror_cflags %{nil}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Fast, lightweight YAML loader and dumper

License:    MIT
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/YAML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker) >= 6.590.0
BuildRequires: perl(Storable)
BuildRequires: perl(Test)
BuildRequires: perl-devel
BuildRequires:	perl(Test::More)
Provides:   perl-YAML-parser

%description
This module provides a Perl interface to the libsyck data
serialization library. It exports the Dump and Load functions for
converting Perl data structures to YAML strings, and the other way
around.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc COMPATIBILITY COPYING Changes META.yml
%{_mandir}/*/*
%{perl_vendorarch}/JSON
%{perl_vendorarch}/YAML
%{perl_vendorarch}/auto/YAML
