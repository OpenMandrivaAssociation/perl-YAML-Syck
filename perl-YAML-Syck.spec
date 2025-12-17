%define	upstream_name    YAML-Syck

%define Werror_cflags %{nil}

Name:       perl-%{upstream_name}
Version:    1.34
Release:    2
Summary:    Fast, lightweight YAML loader and dumper
License:    MIT
Group:      Development/Perl
Url:        https://metacpan.org/dist/%{upstream_name}
Source0:    https://cpan.metacpan.org/modules/by-module/YAML/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker) >= 6.590.0
BuildRequires: perl(Storable)
BuildRequires: perl(Test)
BuildRequires: perl-devel
BuildRequires:	perl(Test::More)
Provides:   perl-YAML-parser

Obsoletes: %{name} = 1.320.0-1

%description
This module provides a Perl interface to the libsyck data
serialization library. It exports the Dump and Load functions for
converting Perl data structures to YAML strings, and the other way
around.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build OPTIMIZE="%{optflags}"

%check
%make test

%install
%make_install

%files
%doc COMPATIBILITY COPYING Changes META.yml
%{_mandir}/*/*
%{perl_vendorarch}/JSON
%{perl_vendorarch}/YAML
%{perl_vendorarch}/auto/YAML
