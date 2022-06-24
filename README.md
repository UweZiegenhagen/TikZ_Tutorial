basis
```latex
\documentclass[tikz,border=0.5cm]{standalone}
\usetikzlibrary{backgrounds}
\tikzset{white background/.style={show background rectangle,tight background,
background rectangle/.style={fill=white}}}

\begin{document}
\begin{tikzpicture}[white background]
\draw[step=1cm,lightgray,very thin] (0,0) grid (15,10);
\draw (1,1) -- (2,2);
\end{tikzpicture}
\end{document}
```
![basis](Pictures/basis.png)
