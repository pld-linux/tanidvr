Summary:	A tool for DVRs based on the DVR-IP protocol
Name:		tanidvr
Version:	1.4.0
Release:	1
License:	BSD
Group:		Applications/Graphics
URL:		http://tanidvr.sourceforge.net
Source0:	http://downloads.sourceforge.net/tanidvr/%{name}-%{version}.tar.bz2
# Source0-md5:	fd952dd786e934879c60987cd2184d98
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TaniDVR is a CLI tool for accessing DVRs used for CCTV surveillance
systems based on the proprietary DVR-IP protocol (port 37777/TCP).
Those are inexpensive Linux-based OEM DVRs sold under several distinct
brands around the world.All those DVRs, regardless their branding, are
produced by this company: Zhejiang Dahua Technology Co.,
Ltd.Unfortunately those DVRs do not come with Un*x-compatible (Linux,
- *BSD..) clients, and its web interface only works with a certain web
browser for a certain proprietary OS.So now you can finally access
(watch, record) the videos from such DVRs from a proper OS.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/dhav2mkv
