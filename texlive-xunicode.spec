# revision 23897
# category Package
# catalog-ctan /macros/xetex/latex/xunicode
# catalog-date 2011-09-09 14:58:15 +0200
# catalog-license lppl1.3
# catalog-version 0.981
Name:		texlive-xunicode
Version:	0.981
Release:	1
Summary:	Generate Unicode characters from accented glyphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/xunicode
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xunicode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xunicode.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The package supports XeTeX's (and other putative future similar
engines') need for Unicode characters, in a similar way to what
the fontenc does for 8-bit (and the like) fonts: convert
accent-glyph sequence to a single Unicode character for output.
The package also covers glyphs specified by packages (such as
tipa) which define many commands for single text glyphs.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xunicode/xunicode.sty
%doc %{_texmfdistdir}/doc/xelatex/xunicode/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
