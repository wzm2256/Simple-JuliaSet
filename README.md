# Simple code for plotting Julia Set.

The repository provides fast and preliminary python code for generating [Julia Set](http://en.wikipedia.org/wiki/Julia_set). Roughly speaking, the Julia Set is the set of complex numbers that do not diverge to infinity under some repeated iterations. This code use the following iteration:  
                    <center>Z = Z*Z + c,   </center>
                    
where Z and c are complex numbers. You can adjust c to get different types of Julia Set. For example, set c=-0.391-0.578i to get [Siegel disk fractal](https://mathworld.wolfram.com/SiegelDiskFractal.html). Some examples are shown in the root folder.