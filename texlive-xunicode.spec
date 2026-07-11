%global tl_name xunicode
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.981
Release:	%{tl_revision}.1
Summary:	Generate Unicode characters from accented glyphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/xunicode
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xunicode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xunicode.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(tipa)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports XeTeX's (and other putative future similar
engines') need for Unicode characters, in a similar way to what the
fontenc does for 8-bit (and the like) fonts: convert accent-glyph
sequence to a single Unicode character for output. The package also
covers glyphs specified by packages (such as tipa) which define many
commands for single text glyphs.

