%global octpkg generate_html

Summary:	Generating HTML help pages for Octave packages
Name:		octave-generate_html
Version:	0.3.3
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/generate_html/
Source0:	https://downloads.sourceforge.net/octave/generate_html-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
This package provides functions for generating HTML pages that contain the
help texts for a set of functions. The package is designed to be as general
as possible, but also contains convenience functions for generating a set
of pages for entire packages.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

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

