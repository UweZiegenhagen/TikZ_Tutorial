# 000 basis

The basis for our course is the following TikZ picture, that draws a blue grid from (0,0) in the left bottom corner to (15,10) the top right corner.

```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}

\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}
\draw (0,0) -- (1,1)--(2,0);
\draw[step=1cm,blue,thin] (0,0) grid (15,10);
\end{tikzpicture}
\end{document}
 
```
![000-basis](Pictures/000-basis.png)
# 001 simple_lines

Using the `\draw` command TikZ can draw a line from one coordinate to another. The width of the line can be specified explicitly, however TikZ provides a few default values as well.

```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}

\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}
\draw[step=1cm,blue,thin] (0,0) grid (15,10);
\draw[ultra thin] (1,1) -- (3,2);
\draw[very thin] (1,1.5) -- (3,2.5);
\draw[thin] (1,2) -- (3,3);
\draw[semithick] (1,2.5) -- (3,3.5);
\draw[thick] (1,3) -- (3,4);
\draw[very thick] (1,3.5) -- (3,4.5);
\draw[ultra thick] (1,4) -- (3,5);
\draw[line width=4pt] (1,4.5) -- (3,5.5);
\draw (1,5.5) -- (3,6.5);

\end{tikzpicture}
\end{document}
```
![001-simple_lines](Pictures/001-simple_lines.png)
# 002 simple_lines

One can also specify more than two coordinates for a line, as the following example shows.

```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}

\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}
\draw[step=1cm,blue,thin] (0,0) grid (15,10);

\draw (1,1) -- (2,2) -- (3,1) -- (7,6);

\end{tikzpicture}
\end{document}
```
![002-simple_lines](Pictures/002-simple_lines.png)
# 003 close path

A path can be closed automatically when instead of the first coordinate again the option `-- cycle` is set.

```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}

\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}
\draw[step=1cm,blue,thin] (0,0) grid (15,10);

\draw (1,1) -- (3,7) -- (8,3) -- cycle;

\end{tikzpicture}
\end{document}
```
![003-close-path](Pictures/003-close-path.png)
# 004 line styles

Besides solid lines TikZ supports also `dashed` and `dotted` lines. Each of them is also available in a `loosely` and `densely` version.

It is also possible to define more sophisticated `patterns`.

```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}

\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}
\draw[step=1cm,blue,very thin] (0,0) grid (15,10);

\draw [dashed] (1,1) -- (6,3);
\draw [loosely dashed] (1,1.5) -- (6,3.5);
\draw [densely dashed] (1,2) -- (6,4);

\draw [dotted] (1,3) -- (6,5);
\draw [loosely dotted] (1,3.5) -- (6,5.5);
\draw [densely dotted] (1,4) -- (6,6);

\end{tikzpicture}
\end{document}
```
![004-line-styles](Pictures/004-line-styles.png)
# 005 relative coordinates

You can also use relative coordinates by adding one or two plus signs before the coordinate.

The version with two plus signs updates the coordinate from which the relative steps are taken, so based on some point we say "move x units horizontally and y units vertically", the next relative coordinate uses the newly created coordinate to determine the next step.

```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}

\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}
\draw[step=1cm,blue,thin] (0,0) grid (15,10);

\draw (1,1) -- ++(5,1) -- ++(-1,1) -- ++(3,3);
\end{tikzpicture}
\end{document}
 
```
![005-relative-coordinates](Pictures/005-relative-coordinates.png)
# 006 relative coordinates no updates

The version with just one plus sign might be a little bit confusing at first.

Let us compare it with the two-plus-version. The two-plus version in the following picture starts with the point (5.5,5.5), from there we move one unit to the right and one unit up and from _this new point_ one unit to the left and one unit up.

The one-plus-version uses the point (8.5,5.5) as _reference base_ for *all* following one-plus-coordinates. We start from (8.5,5.5) one unit to the right and one unit up, the next coordinate is one unit to the left and one unit up from the original point (8.5,5.5).

```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}

\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}
\draw[step=1cm,blue,thin] (0,0) grid (15,10);
\draw (5.5,5.5) -- ++(1,1) -- ++(-1,1);

\draw (8.5,5.5) -- +(1,1) -- +(-1,1);

\end{tikzpicture}
\end{document}
 
```
![006-relative-coordinates-no-updates](Pictures/006-relative-coordinates-no-updates.png)
# 007 polar coordinates
```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}

\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}
\draw[step=1cm,blue,thin] (0,0) grid (15,10);
\draw[red,thick] (5,5) -- ++(90:1) -- ++(45:1) -- ++(0:3) ;

\end{tikzpicture}
\end{document}
 
```
![007-polar-coordinates](Pictures/007-polar-coordinates.png)
# 008 Nodes_Coordinates
```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}

\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}
\draw[step=1cm,lightgray,thin] (0,0) grid (15,10);
\node (a) at (1,1){A};
\coordinate (b) at (3,3);
\draw[->] (a) -- (b);
\end{tikzpicture}
\end{document}
 
```
![008-Nodes_Coordinates](Pictures/008-Nodes_Coordinates.png)
# 009 Nodes_Shapes
```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}
\usetikzlibrary{shapes}
\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}
\draw[step=1cm,lightgray,thin] (0,0) grid (15,10);
\node[rectangle,draw=red] (a) at (1,1){A};
\node[circle,draw=red] (b) at (1,2){B};
\node[coordinate,draw=red] (c) at (1,3){C};

\node[ellipse,draw=red] (d) at (1,4){D};
\node[circle split,draw=red] (e) at (1,5.5){E \nodepart{lower}EE};

\node[diamond,draw=red] (f) at (1,7){F};

\node[draw=red,regular polygon,regular polygon sides=5] at (1,8.5) {$n=5$};
\node[draw=red,regular polygon,regular polygon sides=7] at (4,1) {$n=7$};
\node[draw=red,regular polygon,regular polygon sides=9] at (4,3) {$n=9$};
\node[draw=red,regular polygon,regular polygon sides=17] at (4,5) {$n=17$};

 \node[draw=red,star,star points=5] at (4,8.5) {$p=5$};
\end{tikzpicture}
\end{document}
 
 
% rectangle, circle, and coordinate are always defined
% rest via shapes library
```
![009-Nodes_Shapes](Pictures/009-Nodes_Shapes.png)
# 010 Node_Formatting
```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}
\usetikzlibrary{shadows} 
\usetikzlibrary{spy} 

\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}
[
mybox/.style={rectangle,draw=black, rounded corners,xshift=1cm,yshift=1cm,minimum width=25mm, thick, minimum height=10mm},
redbox/.style={mybox, fill=red},
spy using outlines={circle, magnification=4, size=3cm, connect spies}
]
\draw[step=1cm,lightgray,thin] (0,0) grid (15,10);

\node[rectangle,draw=red] (a) at (2,1){111};

\node[rectangle,rounded corners,  draw=red] (b) at (2,2){222};

\node[rectangle,rounded corners,  minimum width=30mm, minimum height=15mm, draw=red, fill = yellow] (c) at (2,3.5){333};

\node[rectangle,rounded corners,  minimum width=30mm, minimum height=15mm, draw=red, fill = yellow, font=\ttfamily\bfseries] (d) at (2,5.5){444};

\node[rectangle,rounded corners,  minimum width=30mm, minimum height=15mm, draw=red, very thick, fill = yellow, font=\ttfamily\bfseries] (e) at (2,7.5){555};

\node[mybox, fill = white] (f) at (6,2){666};

\node[mybox, fill = white, drop shadow] (g) at (6,4){777};

\node[redbox] (g) at (6,6){777};

\node[mybox, fill = white, drop shadow={opacity=0.25}] (g) at (10,4){777};

\spy [blue, size=2cm] on (12.25,4.5) in node [right] at (12.75,4);

\end{tikzpicture}
\end{document}
 
 
% rectangle, circle, and coordinate are always defined
% rest via shapes library
```
![010-Node_Formatting](Pictures/010-Node_Formatting.png)
# 011 Node Anchors
```latex
%!TEX TS-program = LuaLaTeX

%https://tex.stackexchange.com/questions/482057/extending-anchors-in-tikz
\documentclass[tikz,border=0.5cm]{standalone}
\usetikzlibrary{positioning,calc}

\tikzset{punkt/.style = {
    shape=circle, fill = blue, minimum size = 0.25cm
}}

\tikzset{rechteck/.style = {
        shape  = rectangle, draw   = black,minimum height = 10cm,
        minimum width  = 14cm
}}

\begin{document}
\begin{tikzpicture}[node distance=3cm]
  \node (r) at (0,0) [rechteck] {};
  \node[label=r.center] at (r.center) [punkt] {};
  \node[label=r.north] at (r.north) [punkt] {};
  \node[label=r.south] at (r.south) [punkt] {};
  \node[label=r.east] at (r.east) [punkt] {};
  \node[label=r.west] at (r.west) [punkt] {};
  \node[label=r.north east] at (r.north east) [punkt] {};
  \node[label=r.north west] at (r.north west) [punkt] {};
  \node[label=r.south east] at (r.south east) [punkt] {};
  \node[label=r.south west] at (r.south west) [punkt] {};

\path (r.south west) -- (r.north) coordinate[pos=0.25] (r-sw-n-viertel);  
\node[label=r-sw-n-viertel] at (r-sw-n-viertel) [punkt] {}; 
  
\path (r.south west) -- (r.north) coordinate[pos=0.5] (r-sw-n-mitte);  
\node[label=r-sw-n-mitte] at (r-sw-n-mitte) [punkt] {}; 

\path (r.south west) -- (r.north) coordinate[pos=0.75] (r-sw-n-dreiviertel);  
\node[label=r-sw-n-dreiviertel] at (r-sw-n-dreiviertel) [punkt] {}; 

\node[label=r-n-se-viertel] at ($(r.south east)!.25!(r.north)$) [punkt] {};
 
  
\end{tikzpicture}
\end{document} 
```
![011-Node-Anchors](Pictures/011-Node-Anchors.png)
# 098 Example
```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}
\usetikzlibrary{positioning,calc}

\usepackage[usefilenames,RMstyle=Light,SSstyle=Light,TTstyle=Light,DefaultFeatures={Ligatures=Common}]{plex-otf} 
\renewcommand*\familydefault{\sfdefault}

\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}[box/.style={rectangle,thick,draw=black,
minimum width=20mm, minimum height=10mm,
align=center,node distance=0.5cm},scale=0.9, transform shape]

\node at (0,0) [box] (noise) {Noise};
\node [box, below = of noise] (vco2) {VCO2};
\node [box, below = of vco2] (vco1) {VCO1};
\node [box, right = 1cm of vco2] (vcf) {VCF};
\draw [thick,->] (vco2) -- (vcf);

\coordinate (coordoffset) at ($(vco2.west)!0.5!(vco2.north west)$);

\node [left = of coordoffset](offset) {offset};
\draw [thick,->] (offset) -- (coordoffset);

\node [right = 1cm of noise] (temp1) {};

\coordinate (vcf1) at ($(vcf.west)!0.5!(vcf.north west)$);
\coordinate (vcf2) at ($(vcf.west)!0.5!(vcf.south west)$);
\coordinate (vco21) at ($(vco2.north east)!0.5!(vco2.east)$);
\coordinate (vco22) at ($(vco2.south east)!0.5!(vco2.east)$);

\node [box, right = of vcf] (vca) {VCA};
\node [box, below = of vcf] (adsr1) {ADSR};
\node [box, below = of vca] (adsr2) {ADSR};

\node [right = 0.5cm of vca] (output) {output};
\node [box, below left = 0.5cm of vco1] (keyboard) {Keyboard};

\node [left = 1.5cm of vco1,align=center](cv) {control \\ voltage };

\coordinate (noisetemp1) at ($(noise.east)!0.5!(temp1.west)$);
\coordinate (vco1adsr1) at ($(vco1.east)!0.5!(adsr1.west)$);

\coordinate (vco2vcf1) at ($(vco21)!0.5!(vcf1)$);
\coordinate (vco2vcf2) at ($(vco22)!0.5!(vcf2)$);

\draw[->,thick] (vco1.east) -- (vco1adsr1) --  (vco2vcf2) -- (vcf2);
\draw[->,thick] (noise.east) -- (noisetemp1) --  (vco2vcf1) -- (vcf1);

\draw[->,thick] (adsr1) -- (vcf);
\draw[->,thick] (adsr2) -- (vca);
\draw[->,thick] (vcf) -- (vca);
\draw[->,thick] (vca) -- (output);

\draw [thick,->] (keyboard) -| (adsr1);
\draw [thick,->] (keyboard) -| (adsr2);
\draw [thick,->] (keyboard) |- (vco1);
\draw [thick,->] (keyboard) |- (vco2.base west);
\end{tikzpicture}
\end{document}
 
```
![098-Example](Pictures/098-Example.png)
# 099 Coordinates

Coordinates are like nodes with an empty label.

```latex
%!TEX TS-program = LuaLaTeX
\documentclass[tikz,border=0.5cm]{standalone}

\pdfvariable suppressoptionalinfo \numexpr32+64+512\relax

\begin{document}
\begin{tikzpicture}
\draw[step=1cm,blue,thin] (0,0) grid (15,10);

\coordinate (a) at (0,0);
\coordinate (b) at (5,4);
\coordinate (c) at (6,2);

\draw (a) -- (b)--(c);

\end{tikzpicture}
\end{document}
 
```
![099-Coordinates](Pictures/099-Coordinates.png)
