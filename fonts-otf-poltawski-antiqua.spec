Summary:	OpenType's Poltawski-Antiqua fonts
Name:		fonts-otf-poltawski-antiqua
Version:	1.101
Release:	5
License:	GUST Font License
Group:		System/Fonts/True type
URL:		http://jmn.pl/antykwa-poltawskiego/
Source0:	http://jmn.pl/pliki/ap%{version}otf.zip
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	mkfontscale
BuildRequires:	mkfontdir

%description
This font was designed in the 'twenties and the 'thirties
of XX century by a Polish graphic artist and a typographer 
Adam PÃÅÅtawski.
It was widely used by Polish printing houses as long as metal
types were in use (until ca the 'sixties).

%prep
%setup -qc

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/OTF/antpolt

install -m 644 *.otf %{buildroot}%{_datadir}/fonts/OTF/antpolt

mkfontscale %{buildroot}%{_datadir}/fonts/OTF/antpolt
mkfontdir %{buildroot}%{_datadir}/fonts/OTF/antpolt

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/OTF/antpolt \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/otf-antpolt:pri=50

%files
%dir %{_datadir}/fonts/OTF/antpolt
%{_datadir}/fonts/OTF/antpolt/*.otf
%verify(not mtime) %{_datadir}/fonts/OTF/antpolt/fonts.dir
%{_datadir}/fonts/OTF/antpolt/fonts.scale
%{_sysconfdir}/X11/fontpath.d/otf-antpolt:pri=50

