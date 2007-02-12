#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Geo
%define	pnam	IP-PurePerl
Summary:	Geo::IP::PurePerl - Look up country by IP Address
Summary(pl.UTF-8):   Geo::IP::PurePerl - wyszukiwanie państw po adresach IP
Name:		perl-Geo-IP-PurePerl
Version:	1.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/T/TJ/TJMATHER/Geo-IP-PurePerl-%{version}.tar.gz
# Source0-md5:	42a6b9d4dd2563a20c8998556216e1de
URL:		http://search.cpan.org/dist/Geo-IP-PurePerl/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module uses a file based database. This database simply contains
IP blocks as keys, and countries as values. This database is more
complete and accurate than reverse DNS lookups.

This module can be used to automatically select the geographically
closest mirror, to analyze your web server logs to determine the
countries of your visiters, for credit card fraud detection, and for
software export controls.

%description -l pl.UTF-8
Ten moduł używa bazy danych opartej na pliku. Baza danych zawiera po
prostu bloki IP jako klucze i państwa jako wartości. Baz danych jest
bardziej kompletna i dokładna niż wyszukiwanie odwrotnych DNS.

Moduł ten może być używany do automatycznego wyboru najbliższego
geograficznie serwera lustrzanego, analizy logów serwera WWW w celu
określenia państw odwiedzających, wykrywania oszustw związanych z
kartami kredytowymi oraz kontroli eksportu oprogramowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%attr(755,root,root) %{_bindir}/geoip-lookup
%dir %{perl_vendorlib}/Geo
%dir %{perl_vendorlib}/Geo/IP
%{perl_vendorlib}/Geo/IP/*.pm
%{_mandir}/man1/geoip-lookup.1p*
%{_mandir}/man3/Geo::IP::PurePerl.3pm*
