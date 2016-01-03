[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Answer:

    Difference for totalwgt_lb
    Mean: Firsts 7.201094, Others 7.325856, Both 7.265671
    Variance: Firsts 2.018027, Others 1.943781, Both 1.979597
    Mean Difference: -0.124761
    Diff percent relative to both mean -1.717132
    Cohen d: -0.088673
    Difference: -1.996179 ozs
    
    Difference for prglngth
    Mean: Firsts 38.600952, Others 38.522914, Both 38.560560
    Variance: Firsts 7.794714, Others 6.842684, Both 7.301943
    Mean Difference: 0.078037
    Diff percent relative to both mean 0.202376
    Cohen d: 0.028879
    Difference: 0.546261 days
    Difference: 13.110261 hours

Code:
    
    from __future__ import print_function
    import sys
    import first
    import thinkstats2
    
    def showdiff(varname, series1, series2):
        """
        prints difference description of two series
        Args:
            varname:
            series1:
            series2:
    
        Returns:
            difference of mean between series
        """
        len1 = len(series1)
        len2 = len(series2)
    
        mean1 = series1.mean()
        mean2 = series2.mean()
        mean0 = (mean1 * len1 + mean2 * len2) / (len1 + len2)
    
        var1 = series1.var()
        var2 = series2.var()
        var0 = (var1 * len1 + var2 * len2) / (len1 + len2)
    
        diff = mean1 - mean2
        pctdmean = diff / mean0 * 100
        d = thinkstats2.CohenEffectSize(series1, series2)
    
        print("\nDifference for " + varname)
        print("Mean: Firsts {0:f}, Others {1:f}, Both {2:f}".format(mean1, mean2, mean0))
        print("Variance: Firsts {0:f}, Others {1:f}, Both {2:f}".format(var1, var2, var0))
        print("Mean Difference: {0:f}".format(diff))
        print("Diff percent relative to both mean {0:f}".format(pctdmean))
        print("Cohen d: {0:f}".format(d))
    
        return diff
    
    def main(script):
        lb_diff = showdiff("totalwgt_lb", firsts.totalwgt_lb, others.totalwgt_lb)
        print("Difference: {0:f} ozs".format(lb_diff * 16))
        
        weeks_diff = showdiff("prglngth", firsts.prglngth, others.prglngth)
        print("Difference: {0:f} days".format(weeks_diff * 7))
        print("Difference: {0:f} hours".format(weeks_diff * 7 * 24))
    
    if __name__ == '__main__':
        main(*sys.argv)

