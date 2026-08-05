<?xml version="1.0" encoding="UTF-8" ?>
<!-- **********************************************************************-->
<!-- Copyright 2022                                                        -->
<!-- David Austin                                                          -->
<!--                                                                       -->
<!-- This file is part of Understanding Linear Algebra                     -->
<!--                                                                       -->
<!-- Permission is granted to copy, distribute and/or modify this document -->
<!-- under the terms of the Creative Commons BY license.  The work         -->
<!-- may be used for free by any party so long as attribution is given to  -->
<!-- the author(s), the work and its derivatives are used in the spirit of -->
<!-- "share and share alike".  All trademarks are the registered marks of  -->
<!-- their respective owners.                                              -->
<!-- **********************************************************************-->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

<!-- Next paths assume current file has been copied to mathbook/user -->
<xsl:import href="./core/pretext-solution-manual-latex.xsl" />
<xsl:import href="common.xsl" />

<xsl:output method="text" />

<!-- Superfluous frontmatter for workbook -->
<!-- So we don't bother and kill first two pages   -->
<xsl:template match="*" mode="half-title" />
<xsl:template match="*" mode="ad-card" />

<!-- Chapters: default presentation, we have them all, so numbers OK     -->
<!-- Sections and Equivalents: kill them, except for specific ones below -->
<xsl:template match="conclusion|exercises|references|objectives|appendix|index|solutions|reading-questions" />

<!-- As a subset of full content, we can't         -->
<!-- point to much of the content with hyperlinks  -->
<!-- We do have the full context as we process, so -->
<!-- we can get numbers for cross-references and   -->
<!-- hard code them into the LaTeX                 -->
<!-- This override obliterates autonaming support  -->
<xsl:template match="*" mode="ref-id">
    <xsl:apply-templates select="." mode="number" />
</xsl:template>

<!-- We do the expedient thing and *hard-code* the number    -->
<!-- of each item cross-referenced from within the solutions -->
<!-- manual, so the cropss-refernce text matches with HTML   -->
<!-- output and LaTeX output for the entire book.            -->
<!-- Since the output LaTeX file is a subset of the content, -->
<!-- there will not be a \label for many \ref, and worse, if -->
<!-- there is a \label then a \ref to it will be wrong.      -->
<xsl:template match="*" mode="xref-number">
  <xsl:apply-templates select="." mode="number" />
</xsl:template>


<!-- If we do not include statements, then we kill -->
<!-- introductions and conclusions for exercise    -->
<!-- sections and exercise groups                  -->
<xsl:template match="exercises/introduction|exercises/conclusion|exercisegroup/introduction|exercisegroup/conclusion">
    <xsl:choose>
        <xsl:when test="$exercise.text.statement='yes'">
            <xsl:apply-imports />
        </xsl:when>
        <xsl:otherwise></xsl:otherwise>
    </xsl:choose>
</xsl:template>

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

<!-- We start a new page after each activity and PA -->
<xsl:template match="activity|exploration">
    <xsl:apply-imports />
    <xsl:text>\newpage&#xA;&#xA;</xsl:text>
</xsl:template>

<!-- We handle the colophon ourselves in chapter[1]; suppress PTX's generator -->
<xsl:template match="colophon-items"/>

<!-- Captions for Figures, Tables, Listings, Lists -->
<!-- xml:id is on parent, but LaTeX generates number with caption -->
<xsl:template match="figure|listing|table|list" mode="title-caption">
    <!-- construct appropriate command -->
    <xsl:choose>
        <xsl:when test="parent::sidebyside/parent::figure or parent::sidebyside/parent::sbsgroup/parent::figure">
            <xsl:text>\subcaption*{</xsl:text>
        </xsl:when>
        <xsl:when test="self::figure/parent::sidebyside">
            <xsl:text>\captionof*{figure}{</xsl:text>
        </xsl:when>
        <xsl:when test="self::table/parent::sidebyside">
            <xsl:text>\captionof*{table}{</xsl:text>
        </xsl:when>
        <xsl:when test="self::listing">
            <xsl:text>\captionof*{listingcap}{</xsl:text>
        </xsl:when>
        <xsl:when test="self::list">
            <xsl:text>\captionof*{namedlistcap}{</xsl:text>
        </xsl:when>
        <xsl:otherwise>
            <xsl:text>\caption*{</xsl:text>
        </xsl:otherwise>
    </xsl:choose>
    <!-- produce the actual content -->
    <xsl:text>\textbf{</xsl:text>
    <xsl:apply-templates select="." mode="type-name"/>
    <xsl:text> </xsl:text>
    <xsl:apply-templates select="." mode="number"/>
    <xsl:text>:} </xsl:text>
    <xsl:choose>
        <xsl:when test="self::figure or self::listing">
            <xsl:apply-templates select="." mode="caption-full"/>
        </xsl:when>
        <xsl:when test="self::table or self::list">
            <xsl:apply-templates select="." mode="title-full"/>
        </xsl:when>
        <!-- never used? -->
        <xsl:otherwise>
            <xsl:apply-templates select="caption"/>
        </xsl:otherwise>
    </xsl:choose>
    <xsl:text>}&#xa;</xsl:text>
</xsl:template>

<!-- Style titles -->
<xsl:template name="titlesec-section-style">
    <!-- Only the formatting of chapter titles was changed -->
    <xsl:text>\titleformat{\chapter}[display]&#xa;</xsl:text>
    <xsl:text>{\raggedleft\normalfont\color{chaptercolor}\Large}{</xsl:text>
    <xsl:text>\MakeUppercase{\divisionnameptx}\space</xsl:text>
    <!-- Don't draw the rule that makes the colored box since KDP barfs -->
    <!-- when we do that. -->
    <xsl:text>\rlap{\enskip\resizebox{!}{0.95cm}{\thechapter}</xsl:text>
    <xsl:text>}}{10pt}{\normalfont\Huge\itshape#1}&#xa;</xsl:text>
    <xsl:text>[{\Large\authorsptx}]&#xa;</xsl:text>
    <xsl:text>\titleformat{name=\chapter,numberless}[display]&#xa;</xsl:text>
    <xsl:text>{\raggedleft\normalfont\color{chaptercolor}\Huge\itshape}{}{0pt}{#1}&#xa;</xsl:text>
    <xsl:text>[{\Large\authorsptx}]&#xa;</xsl:text>
    <xsl:text>\titlespacing*{\chapter}{0pt}{30pt}{20pt}&#xa;</xsl:text>

    <!-- Everything in this template below here is stock PTX as of 2018-12-17 -->
    <xsl:text>\titleformat{\section}[block]&#xa;</xsl:text>
<xsl:text>{\normalfont\Large\bfseries}{\thesection\space\titleptx}{1em}{}&#xa;</xsl:text>
    <xsl:text>[{\large\authorsptx}]&#xa;</xsl:text>
    <xsl:text>\titleformat{name=\section,numberless}[block]&#xa;</xsl:text>
    <xsl:text>{\normalfont\Large\bfseries}{}{0pt}{#1}&#xa;</xsl:text>
    <xsl:text>[{\large\authorsptx}]&#xa;</xsl:text>
    <xsl:text>\titlespacing*{\section}{0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}&#xa;</xsl:text>
    <xsl:text>\titleformat{\subsection}[block]&#xa;</xsl:text>
    <xsl:text>{\normalfont\large\bfseries}{\thesubsection\space\titleptx}{1em}{}&#xa;</xsl:text>
    <xsl:text>[{\normalsize\authorsptx}]&#xa;</xsl:text>
    <xsl:text>\titleformat{name=\subsection,numberless}[block]&#xa;</xsl:text>
    <xsl:text>{\normalfont\large\bfseries}{}{0pt}{#1}&#xa;</xsl:text>
    <xsl:text>[{\normalsize\authorsptx}]&#xa;</xsl:text>
    <xsl:text>\titlespacing*{\subsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}&#xa;</xsl:text>
    <xsl:text>\titleformat{\subsubsection}[block]&#xa;</xsl:text>
    <xsl:text>{\normalfont\normalsize\bfseries}{\thesubsubsection\space\titleptx}{1em}{}&#xa;</xsl:text>
    <xsl:text>[{\small\authorsptx}]&#xa;</xsl:text>
    <xsl:text>\titleformat{name=\subsubsection,numberless}[block]&#xa;</xsl:text>
    <xsl:text>{\normalfont\normalsize\bfseries}{}{0pt}{#1}&#xa;</xsl:text>
    <xsl:text>[{\normalsize\authorsptx}]&#xa;</xsl:text>
    <xsl:text>\titlespacing*{\subsubsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}&#xa;</xsl:text>
</xsl:template>

<xsl:param name="latex.preamble.late">
    <xsl:text>\renewenvironment{activitysolution}[4]&#xa;</xsl:text>
    <xsl:text>  {\begin{tcolorbox}[activitysolutionstyle, title={\hyperref[#4]{#1~#2}\notblank{#3}{\space#3}{}}]}&#xa;</xsl:text>
    <xsl:text>  {\end{tcolorbox}\newpage}&#xa;</xsl:text>
    <xsl:text>\renewenvironment{explorationsolution}[4]&#xa;</xsl:text>
    <xsl:text>  {\begin{tcolorbox}[explorationsolutionstyle, title={\hyperref[#4]{#1~#2}\notblank{#3}{\space#3}{}}]}&#xa;</xsl:text>
    <xsl:text>  {\end{tcolorbox}\newpage}&#xa;</xsl:text>
    <xsl:value-of select="$latex.preamble.late.common" />
    <xsl:text>%% Override: no CC image footer on chapter-opening pages&#xa;</xsl:text>
    <xsl:text>\assignpagestyle{\chapter}{empty}&#xa;</xsl:text>
</xsl:param>

</xsl:stylesheet>
