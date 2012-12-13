%define _fontsdir               %{_datadir}/fonts
%define _ttfontsdir             %{_fontsdir}/truetype
%define _miscfontsdir           %{_fontsdir}/misc
%define _fontsconfdir           %{_sysconfdir}/fonts
%define _fontsconfddir          %{_fontsconfdir}/conf.d
%define _fontsconfavaildir      %{_datadir}/%{name}/conf.avail

Name:           google-droid-fonts
Version:        20121209
Release:        0
License:        Apache-2.0
Summary:        Fonts With Extensive Style and Language Support Developed for Android
Url:            http://www.ascendercorp.com/pr/2007-11-12/
Group:          System/Fonts
Source:         %{name}-%{version}.tar.xz
BuildArch:      noarch
Requires(post): %{_bindir}/fc-cache

%description
The Droid family of fonts consists of Droid Sans, Droid Sans Mono and
Droid Serif. Each contains extensive character set coverage including
Western Europe, Eastern/Central Europe, Baltic, Cyrillic, Greek and
Turkish support. The Droid Sans regular font also includes support for
Simplified and Traditional Chinese, Japanese and Korean support for the
GB2312, Big 5, JIS 0208 and KSC 5601 character sets respectively.

Droid was designed by Ascender's Steve Matteson to provide optimal quality
and comfort on a mobile handset when rendered in application menus, web
browsers and for other screen text. - Ascender Press Release,
http://www.ascendercorp.com/pr/2007-11-12/

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%post
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{_ttffontsdir} || :
fi

%postun
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{_ttffontsdir} || :
fi

%files
%defattr(-,root,root)
%license README.txt
%{_ttfontsdir}

