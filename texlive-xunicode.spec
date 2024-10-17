Name:		texlive-xunicode
Version:	30466
Release:	2
Summary:	Generate Unicode characters from accented glyphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/xunicode
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xunicode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xunicode.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-tipa

%description
The package supports XeTeX's (and other putative future similar
engines') need for Unicode characters, in a similar way to what
the fontenc does for 8-bit (and the like) fonts: convert
accent-glyph sequence to a single Unicode character for output.
The package also covers glyphs specified by packages (such as
tipa) which define many commands for single text glyphs.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xunicode/xunicode.sty
%doc %{_texmfdistdir}/doc/xelatex/xunicode/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
