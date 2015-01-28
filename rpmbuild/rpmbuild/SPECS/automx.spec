Name: automx
Version: 1.0.2
Release: 3
Summary: Mendix Auto Utility (auto-mx)	

License: GPL-3.0+
URL: https://mendix.com		
Source0: automx-1.0.2.tar.gz	
#BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch

Requires(pre): jre >= 1.7, m2ee-tools

%description
  Utility which aims to automatically install and
  setup Mendix runtime, and rest of utility's
  which are needed to run Mendix applications.

%pre
  echo -e "\n-----------------------------------------\n"
  echo -e "Installation complete!\n"
  echo -e "Please run \"auto-mx\" to start the install"
  echo -e "\n-----------------------------------------\n"

%prep
%setup -q


#%build
#exit 0
%install
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot}
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}%{_bindir}/auto-mx %{buildroot}%{_bindir} 
echo hallo



%files
%defattr(-,root,root,-)
#%doc
/usr/bin/auto-mx


%changelog
* Tue Jan 28 2015 Adnan Hodzic <adnan.hodzic@mendix.com> 1.0.2
- Debugged el7 installation error
- Added latest auto-mx source
- Updated postinst dialog with -e paramater
* Wed Jan 15 2015 Marck Oemar <marck.oemar@mendix.com> 1.0-2
- removed postgresql dep
* Wed Jan 7 2015 Marck Oemar <marck.oemar@mendix.com> 1.0-1
- initial version

