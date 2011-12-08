%define name eliminate-dups
%define version 1.2
%define release %mkrel 12
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
mv %{_builddir}/%{name}-%{version}/Makefile.dist %{_builddir}/%{name}-%{version}/Makefile
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/var/qmail/bin
install -m 755 %{_builddir}/%{name}-%{version}/%{name} %{buildroot}%{qdir}/bin

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}


%files 
%defattr(-,root,root)
%doc README INSTALL CHANGES
%{qdir}/bin/eliminate-dups

