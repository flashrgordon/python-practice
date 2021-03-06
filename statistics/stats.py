
import math

### SAMPLE STATISTICS FORMULAS ###

# expects a list of values and returns the sample standard deviation
def getSampleSD(values):
    # formula for sample SD is:
    #   sqrt((sum from 1->n(xi - mean)^2)/(n-1))
    n = len(values)
    sum = sum(values)
    mean = sum/n
    num = 0 # numerator
    for x in values:
        num = num + ((x-mean)**2)
    den = n-1 # denominator

    return math.sqrt(num/den)

# expects a list of values and returns the sample variance
def getSampleVariance(values):
    # formula for sample Variance is:
    #   (sum from 1->n(xi - mean)^2)/(n-1)
    n = len(values)
    sum = sum(values)
    mean = sum/n
    num = 0 # numerator
    for x in values:
        num = num + ((x-mean)**2)
    den = n-1 # denominator

    return num/den

# expects a list of values and returns the sample mean
def getSampleMean(values):
    # formula for sample mean is:
    #   (sum of all values)/(# of values)
    return sum(values)/len(values)

# expects a list of values and returns the sample geometric mean
def getGeometricMean(values):
    product = 1
    for x in values:
        product = product * x
    return product ** (len(values))

# expects a list of values and returns the median value
def getMedian(values):
    values.sort()
    length=float(len(values))
    if (length % 2 == 1):   # odd number of elements
        index = (length+1)/2
        return values[index]
    else:
        n1 = values[(length-1)/2]
        n2 = values[(length+1)/2]
        return (n1+n2)/2

# expects a list of values and a cutoff index then returns
# the interpolated value at values[cutoff]
# used for percentiles
def interpolate(values, cutoff):
    floor = float(math.floor(cutoff))
    ceil = float(math.ceiling(cutoff))

    #calculate weighted average
    return (floor * (cutoff - floor) + (ceil * (ceil - cutoff))) / 2

# expects a list of values and percentile value and returns
# the cutoff value for that percentile
def getPercentileCutoff(values, p):
    values.sort()
    cutoff = float(p*len(values)/100) # number of values in pth percentile
    return interpolate(values, cutoff)

# expects a list of values and a cutoff value then returns
# the percentile that cutoff value is
def getPercentile(values, cutoff):
    values.sort()
    num_values = 0.0
    for x in values:
        if (x < cutoff):
            num_values = num_values + 1.0
        else:
            return (num_values/len(values))*100


### POPULATION INFERENCE FORMULAS ###

# expects a list of sample data values and the alpha error value then returns the
# margin of error as a string of an inclusive range in interval notation
def getMeanConfidenceInterval(values, alpha)
    sample_mean = getSampleMean(values)
    sample_SD = getSampleSD(values)
    z_score = 0

    # These values are constants from a standard normal distribution table
    if (alpha == .99):
        z_score = 2.57583
    elif (alpha == .95):
        z_score = 1.95996
    elif (alpha == .90):
        z_score = 1.64485

    margin_of_error = ((z_score * sample_SD) / math.sqrt(len(values))
    min = sample_mean - margin_of_error
    max = sample_mean + margin_of_error

    return ("(" + min + ", " + max + ")")
