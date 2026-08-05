<?xml version="1.0" encoding="UTF-8" ?>
<!-- **********************************************************************-->
<!-- Copyright 2017-2026                                                   -->
<!-- David Austin                                                          -->
<!--                                                                       -->
<!-- This file is part of Understanding Linear Algebra.                    -->
<!--                                                                       -->
<!-- Permission is granted to copy, distribute and/or modify this document -->
<!-- under the terms of the Creative Commons BY-SA license.  The work      -->
<!-- may be used for free by any party so long as attribution is given to  -->
<!-- the author(s), the work and its derivatives are used in the spirit of -->
<!-- "share and share alike".  All trademarks are the registered marks of  -->
<!-- their respective owners.                                              -->
<!-- **********************************************************************-->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

<xsl:import href="./core/pretext-solution-manual-latex.xsl" />
<xsl:import href="ancillary-common.xsl" />
<xsl:variable name="title-separator" select="'\\[0.25\baselineskip]'"/>

<xsl:output method="text" />

<!-- Superfluous frontmatter for a solution manual -->
<!-- So we don't bother and kill first two pages   -->
<xsl:template match="*" mode="half-title" />
<xsl:template match="*" mode="ad-card" />

<xsl:template match="exercise[@exercise-interactive='webwork-reps']" mode="solutions"> </xsl:template>

<!-- Suppress preface in its default position (book/preface fires before chapter[1]) -->
<xsl:template match="preface"/>

<!-- Emit title page, colophon, preface, TOC, then solutions -->
<xsl:template match="chapter[1]|article/section[1]">
    <!-- 1. Title page -->
    <xsl:text>\begin{titlepage}&#xa;</xsl:text>
    <xsl:text>{\centering&#xa;</xsl:text>
    <xsl:text>\vspace*{1.5in}&#xa;</xsl:text>
    <xsl:text>{\Huge\bfseries\itshape </xsl:text>
    <xsl:for-each select="$document-root/title/line">
        <xsl:if test="position() > 1"><xsl:text>\\[0.15in]</xsl:text></xsl:if>
        <xsl:apply-templates />
    </xsl:for-each>
    <xsl:text>}\\[1in]&#xa;</xsl:text>
    <xsl:text>{\large </xsl:text>
    <xsl:value-of select="normalize-space($document-root/bibinfo/author/personname)"/>
    <xsl:text>}\\[0.25in]&#xa;</xsl:text>
    <xsl:text>{\large </xsl:text>
    <xsl:value-of select="normalize-space($document-root/bibinfo/author/institution)"/>
    <xsl:text>}\\[0.5in]&#xa;</xsl:text>
    <xsl:text>{\large\today}\par}&#xa;</xsl:text>
    <xsl:text>\end{titlepage}&#xa;</xsl:text>
    <!-- 2. Colophon (copyright page, verso of title) -->
    <xsl:text>\thispagestyle{empty}&#xa;</xsl:text>
    <xsl:text>\vspace*{\stretch{2}}&#xa;</xsl:text>
    <xsl:if test="$document-root/bibinfo/edition">
        <xsl:text>\noindent{\bfseries Edition}: </xsl:text>
        <xsl:apply-templates select="$document-root/bibinfo/edition"/>
        <xsl:text>\par\medskip&#xa;</xsl:text>
    </xsl:if>
    <xsl:if test="$document-root/bibinfo/website">
        <xsl:text>\noindent{\bfseries Website}: </xsl:text>
        <xsl:apply-templates select="$document-root/bibinfo/website/url[1]"/>
        <xsl:text>\par\medskip&#xa;</xsl:text>
    </xsl:if>
    <xsl:for-each select="$document-root/bibinfo/copyright">
        <xsl:text>\noindent\textcopyright{} </xsl:text>
        <xsl:apply-templates select="year"/>
        <xsl:text>\quad{}</xsl:text>
        <xsl:apply-templates select="holder"/>
        <xsl:if test="shortlicense">
            <xsl:text>\\[0.5\baselineskip]&#xa;</xsl:text>
            <xsl:apply-templates select="shortlicense"/>
        </xsl:if>
        <xsl:text>\par\medskip&#xa;</xsl:text>
    </xsl:for-each>
    <xsl:text>\vspace*{\stretch{1}}&#xa;</xsl:text>
    <xsl:text>\null\clearpage&#xa;</xsl:text>
    <!-- 3. Preface -->
    <xsl:for-each select="$document-root/preface">
        <xsl:text>\chapter*{</xsl:text>
        <xsl:choose>
            <xsl:when test="title"><xsl:apply-templates select="title/node()"/></xsl:when>
            <xsl:otherwise>Preface</xsl:otherwise>
        </xsl:choose>
        <xsl:text>}&#xa;</xsl:text>
        <xsl:apply-templates select="*[not(self::title)]"/>
        <xsl:text>\clearpage&#xa;</xsl:text>
    </xsl:for-each>
    <!-- 4. Table of contents -->
    <xsl:text>\tableofcontents\clearpage&#xa;</xsl:text>
    <!-- 5. All solutions -->
    <xsl:apply-imports />
</xsl:template>

<!-- We handle the colophon ourselves in chapter[1]; suppress PTX's generator -->
<xsl:template match="colophon-items"/>

<xsl:param name="latex.preamble.late">
  <xsl:text>% These override what PreTeXt supplies by default. The only addition&#xa;</xsl:text>
  <xsl:text>% is the after clause. If things start looking odd, look earlier in&#xa;</xsl:text>
  <xsl:text>% the LaTeX file to see how PreTeXt has redefined these three styles&#xa;</xsl:text>
  <xsl:text>% and update latex.preamble.late&#xa;</xsl:text>
  <xsl:text>\tcbset{ divisionsolutionstyle/.style={bwminimalstyle,&#xa;</xsl:text>
  <xsl:text>runintitlestyle, exercisespacingstyle, after title={\space},&#xa;</xsl:text>
  <xsl:text>breakable, parbox=false, after={\clearpage} } }&#xa;</xsl:text>
  <xsl:text>\tcbset{ explorationsolutionstyle/.style={bwminimalstyle,&#xa;</xsl:text>
  <xsl:text>runintitlestyle, exercisespacingstyle, after
  title={\space},&#xa;</xsl:text>
  <xsl:text>breakable, parbox=false ,after={\clearpage}} }&#xa;</xsl:text>
  <xsl:text>\tcbset{ activitysolutionstyle/.style={bwminimalstyle,&#xa;</xsl:text>
  <xsl:text>runintitlestyle, exercisespacingstyle, after title={\space},&#xa;</xsl:text>
  <xsl:text>breakable, parbox=false, after={\clearpage}} }&#xa;</xsl:text>

  <xsl:value-of select="$latex.preamble.late.common" />
  <xsl:text>%% Override: no CC image footer on chapter-opening pages&#xa;</xsl:text>
  <xsl:text>\assignpagestyle{\chapter}{empty}&#xa;</xsl:text>
</xsl:param>

</xsl:stylesheet>
