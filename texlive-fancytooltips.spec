# revision 20781
# category Package
# catalog-ctan /macros/latex/contrib/fancytooltips
# catalog-date 2010-04-08 16:01:05 +0200
# catalog-license lppl1.2
# catalog-version 1.6
Name:		texlive-fancytooltips
Version:	1.6
Release:	1
Summary:	Include a wide range of material in PDF tooltips
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancytooltips
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytooltips.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytooltips.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytooltips.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package was inspired by the cooltooltips package. In
contrast to cooltooltips, fancytooltips allows inclusion of
tooltips which contain arbitrary TeX material or a series of
TeX materials (animated graphics) from an external PDF file. To
see the tooltips, you have to open the files in Adobe Reader.
The links and JavaScripts are inserted using eforms package
from the AcroTeX bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fancytooltips/fancytipmark.eps
%{_texmfdistdir}/tex/latex/fancytooltips/fancytipmark.pdf
%{_texmfdistdir}/tex/latex/fancytooltips/fancytipmark.svg
%{_texmfdistdir}/tex/latex/fancytooltips/fancytooltips.sty
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview/fancy-preview
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview/fancy-preview-demo.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview/fancy-preview-demo.sin.table
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview/fancy-preview-demo.tex
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview/fancypreview.bat
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview2/LDF.jpg
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview2/README
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview2/complie.sh
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview2/fancy-preview
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview2/marik.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview2/slides.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview2/slides.tex
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancytooltips-example-dvips.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancytooltips-example-dvips.tex
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancytooltips-example-min-dvips.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancytooltips-example-min-dvips.tex
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancytooltips-example-min.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancytooltips-example-min.tex
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancytooltips-example.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancytooltips-example.tex
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tecna2.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/images/ttp-1.jpg
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/logo.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/overlib.js
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/overlib_anchor.js
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/overlib_centerpopup.js
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/overlib_crossframe.js
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/overlib_cssstyle.js
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/overlib_debug.js
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/overlib_exclusive.js
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/overlib_followscroll.js
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/overlib_hideform.js
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/overlib_setonoff.js
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/overlib_shadow.js
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/tooltips2html-js.js
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/tooltips2html.css
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/tooltips2html.html
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/tooltips2html.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/tooltips2html.tex
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/tooltips2html.tips
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tex4ht/tooltips2html2.html
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tooltipy.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tooltipy.tex
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/tooltipy.tips
%doc %{_texmfdistdir}/doc/latex/fancytooltips/fancytooltips.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/readme
%doc %{_texmfdistdir}/doc/latex/fancytooltips/tip.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/tip.tex
#- source
%doc %{_texmfdistdir}/source/latex/fancytooltips/fancytooltips.dtx
%doc %{_texmfdistdir}/source/latex/fancytooltips/fancytooltips.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
