Name:           tenr-de-styles-pkg
Version:        1.1
Release:        %mkrel 1
Summary:        A collection of styles for fluxbox

Group:          Graphical desktop/Other
License:        Creative Commons Attribution-ShareAlike 2.5
URL:            http://tenr.de
Source0:        http://tenr.de/files/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch:      noarch
Requires:       fluxbox

%define  _styledir %{_datadir}/%{name}-%{version}

%description
A collection of styles/themes for use with Fluxbox. All styles/themes are
compatible with fluxStyle.

%prep
%setup -q
# I keep finding files and dirs with the wrong premissions on them in the tar
# balls from upstream
find styles/ \( -type d -exec chmod 755 '{}' \; -o -type f -exec chmod 644 '{}' \; \)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_styledir}/
cp -a styles $RPM_BUILD_ROOT%{_styledir}/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README NEWS License
%dir %{_styledir}
%{_styledir}/*
