Summary:	XCardII - graphical smartcard administration tool
Summary(pl.UTF-8):	XCardII - graficzne narzędzie do administrowania kartami procesorowymi
Name:		XCardII
Version:	0.9.9
Release:	1
License:	BSD
Group:		Applications
Source0:	https://alioth.debian.org/frs/download.php/394/%{name}-%{version}.tar.gz
# Source0-md5:	36a521169258a10ef388178284565e65
Patch0:		%{name}-pcsc.patch
URL:		http://muscleapps.alioth.debian.org/
BuildRequires:	libmusclecard-devel >= 1.1.0
BuildRequires:	pcsc-lite-devel >= 1.6.0
BuildRequires:	qt-devel >= 3.0
Requires:	libmusclecard >= 1.1.0
Obsoletes:	muscleframework-xcard
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCardII - graphical smartcard administration tool.

%description -l pl.UTF-8
XCardII - graficzne narzędzie do administrowania kartami
procesorowymi.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C src \
	CPP="%{__cxx} %{rpmcxxflags}" \
	INC="-I/usr/include/qt -I/usr/include/PCSC" \
	LIBS="%{rpmldflags} -lqt-mt -lmusclecard -lpcsclite -lpthread"

%install
rm -rf $RPM_BUILD_ROOT

install -D src/xcard $RPM_BUILD_ROOT%{_bindir}/xcard
install -D man/xcard.1 $RPM_BUILD_ROOT%{_mandir}/man1/xcard.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changelog README
%attr(755,root,root) %{_bindir}/xcard
%{_mandir}/man1/xcard.1*
