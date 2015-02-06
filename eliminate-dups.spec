%define name eliminate-dups
%define version 1.2
%define release 13
%define qdir /var/qmail

Name:		%{name}
Summary:	Eliminates duplicate email messages for qmail users
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Mail
Source:		%{name}-%{version}.tar.bz2
Patch:		%{name}.patch.bz2
Requires:	perl
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Buildrequires:  perl-MD5

%description
eliminate-dups is a small perl program that will help in the elimination of
duplicate messages.


%prep

%setup -q
%patch -p1


%build
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
mkdir -p %{buildroot}
mv $RPM_BUILD_DIR/%{name}-%{version}/Makefile.dist $RPM_BUILD_DIR/%{name}-%{version}/Makefile
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/var/qmail/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/%{name} %{buildroot}%{qdir}/bin

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/%{name}-%{version}


%files 
%defattr(-,root,root)
%doc README INSTALL CHANGES
%{qdir}/bin/eliminate-dups



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2-12mdv2011.0
+ Revision: 618036
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.2-11mdv2010.0
+ Revision: 428554
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2-10mdv2009.0
+ Revision: 244696
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.2-8mdv2008.1
+ Revision: 136403
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import eliminate-dups


* Mon Aug 07 2006 Lenny Cartier <lenny@mandriva.com> 1.2-8mdv2007.0
- rebuild

* Fri Sep 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2-7mdk
- rebuild

* Mon Aug 18 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2-6mdk
- rebuild

* Thu Mar 07 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.2-5mdk
- rebuild

* Tue Jan 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2-4mdk
- rebuild 

* Sat Oct 28 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.2-3mdk
- Removed Packager
- macroization

* Fri Jul 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.2-2mdk
- BM

* Thu May 18 2000 Vincent Danen <vdanen@linux-mandrake.com> 1.2-1mdk
- wrote specfile
