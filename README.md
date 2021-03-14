# PLC_horizontal_drum_CSA
Cross-sectional area of liquid in a cylindrical drum with its axis horizontal

Cf. https://www.plctalk.net/qanda/showthread.php?t=112685

Derivation
====

![](https://github.com/drbitboy/PLC_horizontal_drum_CSA/raw/main/derivation.jpg)

RSLogix 5000 V16 implementation in segment_csa.ACD
====

Parameters:

    R - Radius of drum, arbitrary length units

Inputs:

    L0 - Level of liquid in drum, distance below half-full/-empty; -R is full; +R is empty

Outputs:

    Area - Calculated volume below L0 at end of scan
         - Initialized to 0 at the start of the scan
         - Incremented on each iteration of Rung 1 loop

Intermediate tags:

    L - Iteration parameter
      - Initialized to L0 at the start of the scan
      - Modified on each iteration of Rung 1 loop

    tttN - Proxy for iteration counter
         - 2**N i.e. "two-to-the-N" power
         - Initialized to 1 at the start of the scan
         - Doubled at the end of each scan
         - Loop exits when 2**N = 1,048,576 = 2**20, so algorithm is limited to 20 iterations

![](https://github.com/drbitboy/PLC_horizontal_drum_CSA/raw/main/segment_csa_acd.png)

Performance
====

Convergence is linear:  see plot below; abscissa is log 2**N (iteration), i.e linear with N

![](https://github.com/drbitboy/PLC_horizontal_drum_CSA/raw/main/segment_plot.png)
