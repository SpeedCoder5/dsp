[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range?

>> 63.309470 percent

Code

    import scipy.stats
    mu = 178
    sigma = 7.7
    dist = scipy.stats.norm(loc=mu, scale=sigma)
    type(dist)
    hicm = (6*12 + 1) * 2.540 
    locm = (5*12 + 10) * 2.450
    phi = dist.cdf(hicm)
    plo = dist.cdf(locm)
    pct = (phi-plo) * 100
    print("{0:f} percent".format(pct))