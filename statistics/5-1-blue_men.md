[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range?

>> 34.3% between 177.80 and 185.42 cm

Code

    cm_p_in = 2.540
    hicm = (6*12 + 1) * cm_p_in
    locm = (5*12 + 10) * cm_p_in
    phi = dist.cdf(hicm)
    plo = dist.cdf(locm)
    pct = (phi-plo)
    print("{0:.1%} between {1:.2f} and {2:.2f} cm".format(pct, locm, hicm))