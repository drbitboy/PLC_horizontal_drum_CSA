# PLC_horizontal_drum_CSA
Cross-sectional area of liquid in a cylindrical drum with its axis horizontal

Cf. https://www.plctalk.net/qanda/showthread.php?t=112685

Derivation
====

![](https://github.com/drbitboy/PLC_horizontal_drum_CSA/raw/main/derivation.jpg)

RSLogix 5000 V16 implementation in segment_csa.ACD
====


![](https://github.com/drbitboy/PLC_horizontal_drum_CSA/raw/main/segment_csa_acd.png)

Performance
====

Convergence is linear:  see plot below; abscissa is log 2**N (iteration), i.e linear with N

![](https://github.com/drbitboy/PLC_horizontal_drum_CSA/raw/main/segment_plot.png)
