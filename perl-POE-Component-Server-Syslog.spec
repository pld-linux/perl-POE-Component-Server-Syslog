#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-Server-Syslog
Summary:	POE::Component::Server::Syslog - syslog services for POE
Summary(pl):	POE::Component::Server::Syslog - us³ugi sysloga dla POE
Name:		perl-POE-Component-Server-Syslog
Version:	0.02
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9d13ce4eb4d3c1ce308478952b68e1e5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Time::ParseDate)
BuildRequires:	perl-POE >= 0.24
BuildRequires:	perl-Test-Simple
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
%{perl_vendorlib}/%{pdir}/*/*/*.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
