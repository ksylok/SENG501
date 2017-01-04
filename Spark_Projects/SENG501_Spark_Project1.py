
# coding: utf-8

# # ![Spark Logo](http://spark-mooc.github.io/web-assets/images/ta_Spark-logo-small.png) + ![Python Logo](http://spark-mooc.github.io/web-assets/images/python-logo-master-v3-TM-flattened_small.png)
#  **Exploratory Analysis of Deerfoot Trail Commute Times**
# #### This lab will build on the techniques covered in the Spark tutorial to develop a simple application to compute some stats on commute times on Deerfoot Trail.  We will use the commute times and accidents data collected for Deerfoot Trail for the period September 2013 to April 2014.
# #### ** During this lab we will cover: **
# #### *Part 1:* Creating a base RDD and pair RDDs
# #### *Part 2:* Counting with pair RDDs
# #### *Part 3:* Finding mean values
# #### *Part 4:* Compute basic stats about the Deerfoot Trail data
# #### Note that, for reference, you can look up the details of the relevant methods in [Spark's Python API](https://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD)

# In[1]:

from pyspark import SparkContext
sc = SparkContext()


# ### ** Part 1: Creating a base RDD and pair RDDs **

# #### In this part of the lab, we will explore creating a base RDD with `parallelize` and using pair RDDs to count words.

# #### ** (1a) Create a base RDD **
# #### We'll start by generating a base RDD by using a Python list and the `sc.parallelize` method.  Then we'll print out the type of the base RDD.

# In[2]:

daysList = ['sunday', 'monday', 'tuesday', 'tuesday', 'friday']
daysRDD = sc.parallelize(daysList, 4)
# Print out the type of daysRDD
print(type(daysRDD))


# #### ** (1b) Pluralize and test **
# #### Let's use a `map()` transformation to add the letter 's' to each string in the base RDD we just created. We'll define a Python function that returns the word with an 's' at the end of the word.  Please replace `<FILL IN>` with your solution.  The print statement is a test of your function.
# #### This is the general form that exercises will take.  Exercises will include an explanation of what is expected, followed by code cells where one cell will have one or more `<FILL IN>` sections.  The cell that needs to be modified will have `# TODO: Replace <FILL IN> with appropriate code` on its first line.

# In[4]:

# TODO: Replace <FILL IN> with appropriate code
def makePlural(word):
    """Adds an 's' to `word`.

    Note:
        This is a simple function that only adds an 's'.  No attempt is made to follow proper
        pluralization rules.

    Args:
        word (str): A string.

    Returns:
        str: A string with 's' added to it.
    """
    #daysRDD.map(lambda word: word + 's')
    return word + 's'

print(makePlural('sunday'))


# #### ** (1c) Apply `makePlural` to the base RDD **
# #### Now pass each item in the base RDD into a [map()](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.map) transformation that applies the `makePlural()` function to each element. And then call the [collect()](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.collect) action to see the transformed RDD.

# In[6]:

# TODO: Replace <FILL IN> with appropriate code
pluralRDD = daysRDD.map(makePlural)
print(pluralRDD.collect())


# #### ** (1d) Pass a `lambda` function to `map` **
# #### Let's create the same RDD using a `lambda` function.

# In[7]:

# TODO: Replace <FILL IN> with appropriate code
pluralLambdaRDD = daysRDD.map(lambda x: x + 's')
print(pluralLambdaRDD.collect())


# #### ** (1e) Length of each word **
# #### Now use `map()` and a `lambda` function to return the first character in each word.  We'll `collect` this result directly into a variable.

# In[14]:

# TODO: Replace <FILL IN> with appropriate code
pluralFirstChars = (pluralRDD.map(lambda x: x[0]).collect())
print(pluralFirstChars)


# #### ** (1f) Pair RDDs **
# #### Often we would need to deal with pair RDDs.  A pair RDD is an RDD where each element is a pair tuple `(k, v)` where `k` is the key and `v` is the value. In this example, we will create a pair consisting of `('<day>', 1)` for each word element in the RDD.
# #### We can create the pair RDD using the `map()` transformation with a `lambda()` function to create a new RDD.

# In[43]:

# TODO: Replace <FILL IN> with appropriate code
dayPairs = daysRDD.map(lambda x: (x, 1))
print(dayPairs.collect())


# ### ** Part 2: Counting with pair RDDs **

# #### Now, let's count the number of times a particular day appears in the RDD. There are multiple ways to perform the counting, but some are much less efficient than others.
# #### A naive approach would be to `collect()` all of the elements and count them in the driver program. While this approach could work for small datasets, we want an approach that will work for any size dataset including terabyte- or petabyte-sized datasets. In addition, performing all of the work in the driver program is slower than performing it in parallel in the workers. For these reasons, we will use data parallel operations.

# #### ** (2a) `groupByKey()` approach **
# #### An approach you might first consider (we'll see shortly that there are better ways) is based on using the [groupByKey()](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.groupByKey) transformation. As the name implies, the `groupByKey()` transformation groups all the elements of the RDD with the same key into a single list in one of the partitions. There are two problems with using `groupByKey()`:
#   + #### The operation requires a lot of data movement to move all the values into the appropriate partitions.
#   + #### The lists can be very large. Consider a word count of English Wikipedia: the lists for common words (e.g., the, a, etc.) would be huge and could exhaust the available memory in a worker.
#  
# #### Use `groupByKey()` to generate a pair RDD of type `('day', iterator)`.

# In[256]:

# TODO: Replace <FILL IN> with appropriate code
# Note that groupByKey requires no parameters
daysGrouped = dayPairs.groupByKey()
for key, value in daysGrouped.collect():
    print('{0}: {1}'.format(key, list(value)))


# #### ** (2b) Use `groupByKey()` to obtain the counts **
# #### Using the `groupByKey()` transformation creates an RDD containing 3 elements, each of which is a pair of a day and a Python iterator.
# #### Now sum the iterator using a `map()` transformation.  The result should be a pair RDD consisting of (day, count) pairs.

# In[66]:

# TODO: Replace <FILL IN> with appropriate code
dayCountsGrouped = daysGrouped.map(lambda pair: (pair[0], sum(pair[1])))
print(dayCountsGrouped.collect())


# #### ** (2c) Counting using `reduceByKey` **
# #### A better approach is to start from the pair RDD and then use the [reduceByKey()](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.reduceByKey) transformation to create a new pair RDD. The `reduceByKey()` transformation gathers together pairs that have the same key and applies the function provided to two values at a time, iteratively reducing all of the values to a single value. `reduceByKey()` operates by applying the function first within each partition on a per-key basis and then across the partitions, allowing it to scale efficiently to large datasets.

# In[49]:

# TODO: Replace <FILL IN> with appropriate code
# Note that reduceByKey takes in a function that accepts two values and returns a single value
dayCounts = dayPairs.reduceByKey(lambda x, y: x + y)
print(dayCounts.collect())


# #### ** (2d) All together **
# #### The expert version of the code performs the `map()` to pair RDD, `reduceByKey()` transformation, and `collect` in one statement.

# In[56]:

# TODO: Replace <FILL IN> with appropriate code
dayCountsCollected = (daysRDD.
                       map(lambda x: (x, 1)).
                       reduceByKey(lambda x, y: x + y).
                       collect())
print(dayCountsCollected)


# ### ** Part 3: Finding unique days and a mean value **

# #### ** (3a) Unique words **
# #### Calculate the number of unique days in `daysRDD`.  You can use other RDDs that you have already created to make this easier.

# In[73]:

# TODO: Replace <FILL IN> with appropriate code
uniqueDays = daysRDD.distinct().count()
print(uniqueDays)


# #### ** (3b) Mean using `reduce` **
# #### Find the mean number of days per unique day in `dayCounts`.
# #### Use a `reduce()` action to sum the counts in `dayCounts` and then divide by the number of unique days.  First `map()` the pair RDD `dayCounts`, which consists of (key, value) pairs, to an RDD of values.

# In[76]:

# TODO: Replace <FILL IN> with appropriate code
from operator import add
totalCount = (dayCounts
              .map(lambda pair: pair[1])
              .reduce(add))
average = totalCount / float(uniqueDays)
print(totalCount)
print(round(average, 2))


# ### ** Part 4: Compute Deerfoot Trail stats **

# #### In this section we will apply some of the above concepts towards analyzing commute time and accidents data collected for Deerfoot Trail.

# #### ** (4a) Loading the data **
# #### We will first load the data.  The data was collected in the period September 2013 to April 2014.  It was obtained by querying Google Maps for commute times and Twitter for accident reports.  Although this data set is very small, because we are using parallel computation via Spark the functions we develop will scale for larger data sets.  To convert a text file into an RDD, we use the `SparkContext.textFile()` method. We will use `take(15)` to print 15 lines from this file.

# In[127]:

# Just run this code
import os.path
baseDir = os.path.join('data')
inputPath = os.path.join('SENG501', 'lab1', 'deerfoot.csv')
fileName = 'deerfoot.csv'

deerfootRDD = (sc.textFile(fileName, 8))
print('\n'.join(deerfootRDD.zipWithIndex().map(lambda l_num: '{0}: {1}'.format(l_num[1], l_num[0])).take(15)))


# #### ** (4b) Extracting fields relevant to the analysis **
# #### We will extract only those fields that will be useful for our further analysis in this lab.  Specifically, we are interested in field 2 (day), field 7 (commute time at 8 AM), and field 14 (commute time at 4 PM).  We consider only these 2 times since these best represent the morning and afternoon rush traffic.  Write a function `extractFields` that takes as input each record of `deerfootRDD` and produces a record for another RDD that only contains these 3 fields.

# In[138]:

# TODO: Replace <FILL IN> with appropriate code
def extractFields(deerfootRDDRecord):
    """Creates a record consisting of day, 8 AM commute time, and 4 PM commute time.

    Args:
        deerfootRDDRecord : a comma separated string consisting of all fields in the data set.

    Returns:
        extracted record: a comma separated record (day, 8 AM commute time, 4 PM commute time)
    """
    deerfootRDDRecord = deerfootRDDRecord.split(",")
    dataset = deerfootRDDRecord[1] + ',' + deerfootRDDRecord[6] + ',' + deerfootRDDRecord[13]
    return dataset
   
print(extractFields(deerfootRDD.take(1)[0]))


# #### ** (4c) Obtaining extracted RDD **
# #### Transform the `deerfootRDD` so that we get a resulting `deerfootPeakRDD` that only has peak hour commute times.

# In[214]:

# TODO: Replace <FILL IN> with appropriate code
deerfootPeakRDD = deerfootRDD.map(extractFields)

print(deerfootPeakRDD.take(5))


# #### ** (4d) Obtaining stats - counting number of occurrences of each day of the week **
# #### Start with the `deerfootPeakRDD`.  Create a pair RDD `deerfootDayPairRDD` that contains records where day is the key and 1 is the value. Apply another transformation on `deerfootDayPairRDD` to get a `deerfootDayCounts` RDD

# In[150]:

# TODO: Replace <FILL IN> with appropriate code
deerfootDayPairRDD = deerfootPeakRDD.map(lambda x: (x.split("," , 1)[0], 1))
#print(deerfootDayPairRDD.collect())
deerfootDayCounts = deerfootDayPairRDD.reduceByKey(lambda x, y: x + y)

deerfootDayCountsList = deerfootDayCounts.collect()
print(deerfootDayCountsList)
deerfootDayCountsDict = dict(deerfootDayCountsList)
print(deerfootDayCountsDict.get('Friday'))


# #### ** (4e) Filtering out Saturdays and Sundays **
# #### As we can see from the previous result, there is almost an equal number of days of each type in the data set, which suggests that there is no big gap in the data collection.  Let's say we are now only interested in commute time stats for Monday to Friday.  Write a function called `filterSatSun` that filters out records for Saturdays and Sundays in `deerfootPeakRDD`.  Apply this transformation on `deerfootPeakRDD` to obtain an RDD called `deerfootPeakMFRDD`. 

# In[194]:

# TODO: Replace <FILL IN> with appropriate code
def filterSatSun(deerfootPeakRDDRecord):
    """Ignores "Saturday" and "Sunday" records.

    Args:
        deerfootPeakRDDRecord: A comma separated string (day, 8 AM commute time, 4 PM commute time).

    Returns:
        false if day is "Saturday" or "Sunday". true if otherwise
    """
    compareRDDRecords = deerfootPeakRDDRecord.split(",")
    if compareRDDRecords[0] == 'Saturday' or compareRDDRecords[0] == 'Sunday':
        return False
    else:
        return True

deerfootPeakMFRDD = deerfootPeakRDD.filter(lambda x: filterSatSun(x))
print(deerfootPeakMFRDD.take(5))


# #### ** (4f) Computing average commute times for each day of the week **
# #### We will now compute the average of commute times for each day of the week for both 8 AM and 4 PM. To do this, first create a pair RDD called `deerfootPeakAMRDD` where each record has day as the key and 8 AM commute time as value.  Apply one or more appropriate transformations to compute average.  Repeat the process for the evening rush hour.  You can use the previously computed `deerfootDayCountsDict' in the average calculation. 

# In[257]:

# TODO: Replace <FILL IN> with appropriate code
from operator import add
deerfootPeakAMRDD = deerfootPeakMFRDD.map(lambda x: (x.split(",")[0], (x.split(",")[1])))
deerfootPeakAMreduceByDay = deerfootPeakAMRDD.reduceByKey(lambda x, y: int(x) + int(y)).collect()

amAverages = list()

for item in deerfootPeakAMreduceByDay:
    avg = item[1]/float(deerfootDayCountsDict.get(item[0]))
    amAverages.append((item[0],avg))

deerfootPeakPMRDD = deerfootPeakMFRDD.map(lambda x: (x.split(",")[0], (x.split(",")[2])))
deerfootPeakPMreduceByDay = deerfootPeakPMRDD.reduceByKey(lambda x, y: int(x) + int(y)).collect()

pmAverages = list()

for item in deerfootPeakPMreduceByDay:
    avg = item[1]/float(deerfootDayCountsDict.get(item[0]))
    pmAverages.append((item[0],avg))

print(amAverages)
print(pmAverages)


# #### ** (4g) Computing max morning hour rush commute times for each day of the week **
# #### For 8 AM, find the maximum commute time for each day of the week. 

# In[255]:

# TODO: Replace <FILL IN> with appropriate code
deerfootPeakAMMaxreduceByDay = deerfootPeakAMRDD.groupByKey().map(lambda x: (x[0], max(x[1]))).collect()
3print(deerfootPeakAMMaxreduceByDay)
for item in deerfootPeakAMMaxreduceByDay:
    print(item)


# In[ ]:



