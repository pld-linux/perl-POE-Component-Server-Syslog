#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Server-Syslog
Summary:	POE::Component::Server::Syslog - syslog services for POE
Summary(pl.UTF-8):	POE::Component::Server::Syslog - usługi sysloga dla POE
Name:		perl-POE-Component-Server-Syslog
Version:	1.18
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6f2738b00dc954cf0e1575f315398593
URL:		http://search.cpan.org/dist/POE-Component-Server-Syslog/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.24
BuildRequires:	perl-Params-Validate
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Time-modules
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This component provides very simple UDP Syslog services for POE (named
pipe and other syslog interoperability features are expected in future
versions).

%description -l pl.UTF-8
Ten komponent udostępnia bardzo proste usługi sysloga UDP dla POE
(obsługi nazwanych potoków i innych możliwości współpracy z syslogiem
można oczekiwać w kolejnych wersjach).

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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
