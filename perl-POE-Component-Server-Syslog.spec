#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Server-Syslog
Summary:	POE::Component::Server::Syslog - syslog services for POE
Summary(pl):	POE::Component::Server::Syslog - us³ugi sysloga dla POE
Name:		perl-POE-Component-Server-Syslog
Version:	1.00
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a68c8258a7ece01f2fb72f8575b02260
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Params-Validate
BuildRequires:	perl-POE >= 0.24
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Time-modules
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This component provides very simple UDP Syslog services for POE (named
pipe and other syslog interoperability features are expected in future
versions).

%description -l pl
Ten komponent udostêpnia bardzo proste us³ugi sysloga UDP dla POE
(obs³ugi nazwanych potoków i innych mo¿liwo¶ci wspó³pracy z syslogiem
mo¿na oczekiwaæ w kolejnych wersjach).

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
install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -r samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE 
%{perl_vendorlib}/POE/Component/Server/Syslog
%{perl_vendorlib}/POE/Component/Server/Syslog.pm
%{perl_vendorlib}/POE/Filter/Syslog.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
