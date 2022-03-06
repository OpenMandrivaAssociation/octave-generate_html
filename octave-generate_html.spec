%global octpkg generate_html

Summary:	Generating HTML help pages for Octave packages
Name:		octave-%{octpkg}
Version:	0.3.2
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
This package provides functions for generating HTML pages that contain the
help texts for a set of functions. The package is designed to be as general
as possible, but also contains convenience functions for generating a set
of pages for entire packages.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

