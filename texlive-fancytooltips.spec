# revision 27129
# category Package
# catalog-ctan /macros/latex/contrib/fancytooltips
# catalog-date 2012-06-03 20:06:11 +0200
# catalog-license lppl1.2
# catalog-version 1.8
Name:		texlive-fancytooltips
Version:	1.8
Release:	2
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
%doc %{_texmfdistdir}/doc/latex/fancytooltips/cite.png
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview-demo.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview-demo.sin.table
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview-demo.tex
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview-demo2.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancy-preview-demo2.tex
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancytooltips-example.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/fancytooltips-example.tex
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/pics/tecna2.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/pics/tooltipy.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/pics/tooltipy.tex
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/pics/tooltipy.tips
%doc %{_texmfdistdir}/doc/latex/fancytooltips/examples/readme
%doc %{_texmfdistdir}/doc/latex/fancytooltips/fancy-preview
%doc %{_texmfdistdir}/doc/latex/fancytooltips/fancytipmark1.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/fancytipmark2.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/fancytipmark3.pdf
%doc %{_texmfdistdir}/doc/latex/fancytooltips/fancytipmark4.pdf
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
