         Date  Store Number         City Zip Code  County Number      County  \
0  11/04/2015          3717       SUMNER    50674            9.0      Bremer   
1  03/02/2016          2614    DAVENPORT    52807           82.0       Scott   
2  02/11/2016          2106  CEDAR FALLS    50613            7.0  Black Hawk   
3  02/03/2016          2501         AMES    50010           85.0       Story   
4  08/18/2015          3654      BELMOND    50421           99.0      Wright   

    Category              Category Name  Vendor Number  Item Number  \
0  1051100.0           APRICOT BRANDIES             55        54436   
1  1011100.0           BLENDED WHISKIES            395        27605   
2  1011200.0  STRAIGHT BOURBON WHISKIES             65        19067   
3  1071100.0         AMERICAN COCKTAILS            395        59154   
4  1031080.0             VODKA 80 PROOF            297        35918   

            Item Description  Bottle Volume (ml) State Bottle Cost  \
0  Mr. Boston Apricot Brandy                 750             $4.50   
1                    Tin Cup                 750            $13.75   
2                   Jim Beam                1000            $12.59   
3    1800 Ultimate Margarita                1750             $9.50   
4         Five O'clock Vodka                1750             $7.20   

  State Bottle Retail  Bottles Sold Sale (Dollars)  Volume Sold (Liters)  \
0               $6.75            12         $81.00                   9.0   
1              $20.63             2         $41.26                   1.5   
2              $18.89            24        $453.36                  24.0   
3              $14.25             6         $85.50                  10.5   
4              $10.80            12        $129.60                  21.0   

   Volume Sold (Gallons)  
0                   2.38  
1                   0.40  
2                   6.34  
3                   2.77  
4                   5.55  
Question #1:  The dataset has the shape: 
(270955, 18)
There are 270955 rows and 18 columns
Here are the types of each column: 
Date                      object
Store Number               int64
City                      object
Zip Code                  object
County Number            float64
County                    object
Category                 float64
Category Name             object
Vendor Number              int64
Item Number                int64
Item Description          object
Bottle Volume (ml)         int64
State Bottle Cost         object
State Bottle Retail       object
Bottles Sold               int64
Sale (Dollars)            object
Volume Sold (Liters)     float64
Volume Sold (Gallons)    float64
dtype: object
Question #2: 
Here is the count for each column with how many missing elements it has:
Date 0
Store Number 0
City 0
Zip Code 0
County Number 1077
County 1077
Category 68
Category Name 632
Vendor Number 0
Item Number 0
Item Description 0
Bottle Volume (ml) 0
State Bottle Cost 0
State Bottle Retail 0
Bottles Sold 0
Sale (Dollars) 0
Volume Sold (Liters) 0
Volume Sold (Gallons) 0
I think we should just leave these as null values, because to remove them, you would be losing other columns in that row which have meaningful data, and to select zero or the mean for these columns also wouldn't make sense, because the mean of a county number or a category number is meaningless.
To clean the data, I changed all of the columns with numeric values into floats if they were previously in strings.  Floats work for all columns, while ints would occasional lose data depending on the column - particularly dollar amounts where the cents can be important.  I also removed dollar signs and any other special characters that my show up.  For the date, I created 3 new float columns for the month, day, and year separately.
Question #3: 
There are a total of 1400 unique store numbere in the data set.  Of which, 28 had transactions only in 2016.  Since we are looking at sales from 2015 only, those rows will be excluded.
Question #4: 
What is the yearly liquor sales for each store in 2015?
  As explained on the data.iowa.gov website, the Alcoholic Beverages Division is buying and selling at a retail price to the stores.  I will assume all of the liquor that was purchased from the state was sold, so the yearly liquor sales for each store is equal to the sum of "Volume Sold (Liters)" column for all rows of each store.
Store Number
2106    9731.85
2113     659.85
2130    6891.37
2152     633.37
2178    1917.12
Name: Volume Sold (Liters), dtype: float64
What is the profit for each store in 2015?
 Since we don't know how much each store is selling the bottles they purchase for, I will interpret this question to be "What is the profit [to the Alcoholic Beverages Division] FROM each store?"  To find that we can subtract the State Bottle Cost from the State Bottle Retail (the net profit) and multiply that by the Bottles Sold to find the profit for each transaction, and then we can sum up all of the rows from each store to find the total profit from each store to the Alcoholic Beverages Division.
Store Number
2106    48838.08
2113     3109.04
2130    37325.20
2152     2587.53
2178     8165.70
Name: profit_per_transaction, dtype: float64
Question #5: 
Here are the nine broader categories I created, with the number of different bevarages that went under each category.
                Category Name
broad category               
brandy                      8
cocktail                    1
gin                         4
other                       4
rum                         6
shnapps                    32
tequila                     2
vodka                       8
whiskey                    13
Here is each broad category with the sum of bottles sold: 
broad category
brandy      152209
cocktail     53302
gin          85182
other        21934
rum         330452
shnapps     423277
tequila     113857
vodka       801660
whiskey     692801
Name: Bottles Sold, dtype: int64
The highest number of bottles sold is in the Vodka category with 801660 bottles sold.
Broad category with the highest profits: 
broad category
brandy      5.023882e+05
cocktail    1.922263e+05
gin         3.065027e+05
other       1.339834e+05
rum         1.526776e+06
shnapps     1.899944e+06
tequila     6.350565e+05
vodka       2.806093e+06
whiskey     3.674495e+06
Name: profit_per_transaction, dtype: float64
The highest profits is in the Whiskey category with 3674495.25 dollars of profits.
Question #6: 
                                                    Average  Minimum  Maximum  \
broad category Category Name                                                    
brandy         AMERICAN GRAPE BRANDIES             8.155071     1.50    28.13   
               APRICOT BRANDIES                    7.964788     2.94    16.94   
               BLACKBERRY BRANDIES                 9.206835     5.33    16.94   
               CHERRY BRANDIES                     8.023606     5.33     8.22   
               IMPORTED GRAPE BRANDIES            21.447436     1.34   449.99   
               MISCELLANEOUS  BRANDIES            17.384583     2.94    49.89   
               PEACH BRANDIES                      7.335354     2.94    10.68   
cocktail       AMERICAN COCKTAILS                 10.811873     2.25    18.74   
gin            AMERICAN DRY GINS                   8.861136     1.34    54.00   
               AMERICAN SLOE GINS                  7.525385     5.85     8.99   
               FLAVORED GINS                      10.826560     9.74    33.14   
               IMPORTED DRY GINS                  22.743702     5.88    60.15   
other          AMERICAN ALCOHOL                   13.291239     9.68    19.01   
               DECANTERS & SPECIALTY PACKAGES     21.420863     3.12   195.00   
               HIGH PROOF BEER - AMERICAN        142.760000   142.76   142.76   
rum            BARBADOS RUM                       15.344173    10.49    29.99   
               FLAVORED RUM                       12.724632     6.00    75.00   
               JAMAICA RUM                        16.493948    12.43    60.00   
               PUERTO RICO & VIRGIN ISLANDS RUM   11.621930     1.34    33.00   
               SPICED RUM                         14.477245     3.20    33.20   
shnapps        AMARETTO - IMPORTED                46.700000    46.70    46.70   
               AMERICAN AMARETTO                   6.796538     5.01    12.11   
               ANISETTE                            7.108000     6.75     7.88   
               APPLE SCHNAPPS                     10.171951     4.61    17.31   
               BUTTERSCOTCH SCHNAPPS               9.460435     6.51    11.81   
               CINNAMON SCHNAPPS                  11.404005     4.61    23.75   
               COFFEE LIQUEURS                    15.983292     7.46    37.49   
               CREAM LIQUEURS                     17.929295     6.75   148.50   
               CREME DE ALMOND                     6.847308     6.75    11.81   
               DARK CREME DE CACAO                 7.092803     5.85     7.13   
...                                                     ...      ...      ...   
               ROCK & RYE                         10.992442     7.40    15.75   
               ROOT BEER SCHNAPPS                  9.392778     8.25    13.91   
               SPEARMINT SCHNAPPS                  7.500000     7.50     7.50   
               STRAWBERRY SCHNAPPS                 8.274636     7.13     9.45   
               TRIPLE SEC                          4.331367     3.20    18.50   
               TROPICAL FRUIT SCHNAPPS             7.508213     5.51    11.81   
               WATERMELON SCHNAPPS                10.693173     9.45    11.81   
               WHISKEY LIQUEUR                    17.758294     1.34    44.58   
               WHITE CREME DE CACAO                7.029801     6.75     7.13   
               WHITE CREME DE MENTHE               7.130000     7.13     7.13   
tequila        TEQUILA                            20.592067     4.50    97.49   
vodka          100 PROOF VODKA                     8.763444     1.34    27.78   
               IMPORTED VODKA                     20.179493     3.81    63.99   
               IMPORTED VODKA - MISC              17.299717     4.50    44.61   
               LOW PROOF VODKA                    15.740000    15.74    15.74   
               OTHER PROOF VODKA                  11.842436    10.01    12.38   
               VODKA 80 PROOF                      9.450066     1.34   104.87   
               VODKA FLAVORED                     10.732392     3.36    43.95   
whiskey        BLENDED WHISKIES                   10.228969     1.58    65.25   
               BOTTLED IN BOND BOURBON            28.856579    12.71    40.64   
               CANADIAN WHISKIES                  14.256956     1.34    98.99   
               CORN WHISKIES                      36.926667    17.31    45.00   
               IRISH WHISKIES                     25.865306    10.11   252.00   
               JAPANESE WHISKY                    63.024348    26.24   286.86   
               SCOTCH WHISKIES                    25.292861     4.82   637.50   
               SINGLE BARREL BOURBON WHISKIES     29.589154    21.46    89.96   
               SINGLE MALT SCOTCH                 45.718392     9.27   420.00   
               STRAIGHT BOURBON WHISKIES          17.870253     1.58   187.50   
               STRAIGHT RYE WHISKIES              26.124330    12.36    91.50   
               TENNESSEE WHISKIES                 20.784560     2.48    52.11   

                                                     Total  
broad category Category Name                                
brandy         AMERICAN GRAPE BRANDIES            53733.76  
               APRICOT BRANDIES                    8832.95  
               BLACKBERRY BRANDIES                14546.80  
               CHERRY BRANDIES                     2647.79  
               IMPORTED GRAPE BRANDIES            98958.47  
               MISCELLANEOUS  BRANDIES             2503.38  
               PEACH BRANDIES                      4973.37  
cocktail       AMERICAN COCKTAILS                 74915.47  
gin            AMERICAN DRY GINS                  58120.19  
               AMERICAN SLOE GINS                  1271.79  
               FLAVORED GINS                       2706.64  
               IMPORTED DRY GINS                  66843.74  
other          AMERICAN ALCOHOL                    7615.88  
               DECANTERS & SPECIALTY PACKAGES     24826.78  
               HIGH PROOF BEER - AMERICAN           285.52  
rum            BARBADOS RUM                        6030.26  
               FLAVORED RUM                       92660.77  
               JAMAICA RUM                         6350.17  
               PUERTO RICO & VIRGIN ISLANDS RUM  116939.86  
               SPICED RUM                        211816.57  
shnapps        AMARETTO - IMPORTED                  140.10  
               AMERICAN AMARETTO                   9148.14  
               ANISETTE                             248.78  
               APPLE SCHNAPPS                      7873.09  
               BUTTERSCOTCH SCHNAPPS               8486.01  
               CINNAMON SCHNAPPS                   8313.52  
               COFFEE LIQUEURS                    30592.02  
               CREAM LIQUEURS                    112667.69  
               CREME DE ALMOND                      356.06  
               DARK CREME DE CACAO                 1113.57  
...                                                    ...  
               ROCK & RYE                           945.35  
               ROOT BEER SCHNAPPS                  3043.26  
               SPEARMINT SCHNAPPS                   742.50  
               STRAWBERRY SCHNAPPS                 2498.94  
               TRIPLE SEC                          5353.57  
               TROPICAL FRUIT SCHNAPPS             1764.43  
               WATERMELON SCHNAPPS                 5122.03  
               WHISKEY LIQUEUR                   193600.92  
               WHITE CREME DE CACAO                1412.99  
               WHITE CREME DE MENTHE                434.93  
tequila        TEQUILA                           249349.34  
vodka          100 PROOF VODKA                    28954.42  
               IMPORTED VODKA                    215274.83  
               IMPORTED VODKA - MISC             112551.96  
               LOW PROOF VODKA                      236.10  
               OTHER PROOF VODKA                    923.71  
               VODKA 80 PROOF                    334277.17  
               VODKA FLAVORED                    150264.22  
whiskey        BLENDED WHISKIES                  118113.91  
               BOTTLED IN BOND BOURBON             5482.75  
               CANADIAN WHISKIES                 386178.18  
               CORN WHISKIES                        443.12  
               IRISH WHISKIES                     72190.07  
               JAPANESE WHISKY                     1449.56  
               SCOTCH WHISKIES                   135949.13  
               SINGLE BARREL BOURBON WHISKIES      9438.94  
               SINGLE MALT SCOTCH                104603.68  
               STRAIGHT BOURBON WHISKIES         274165.42  
               STRAIGHT RYE WHISKIES              36260.57  
               TENNESSEE WHISKIES                147175.47  

[71 rows x 4 columns]
Question #7: 
Here is a list sorted by county and then by broad category, showing the total number of bottles sold for each category name.
   County broad category                     Category Name  Bottles Sold
0   Adair         brandy           AMERICAN GRAPE BRANDIES            37
1   Adair         brandy                  APRICOT BRANDIES            31
2   Adair         brandy               BLACKBERRY BRANDIES            99
3   Adair         brandy                   CHERRY BRANDIES            43
4   Adair         brandy           IMPORTED GRAPE BRANDIES            12
5   Adair       cocktail                AMERICAN COCKTAILS            81
6   Adair            gin                 AMERICAN DRY GINS            34
7   Adair            gin                 IMPORTED DRY GINS             7
8   Adair          other                  AMERICAN ALCOHOL            15
9   Adair          other    DECANTERS & SPECIALTY PACKAGES             6
10  Adair            rum                      BARBADOS RUM            12
11  Adair            rum                      FLAVORED RUM            30
12  Adair            rum  PUERTO RICO & VIRGIN ISLANDS RUM            94
13  Adair            rum                        SPICED RUM           305
14  Adair        shnapps                 AMERICAN AMARETTO            25
15  Adair        shnapps                    APPLE SCHNAPPS             6
16  Adair        shnapps             BUTTERSCOTCH SCHNAPPS             8
17  Adair        shnapps                 CINNAMON SCHNAPPS             7
18  Adair        shnapps                   COFFEE LIQUEURS             6
19  Adair        shnapps                    CREAM LIQUEURS            11
Here are the amounts of bottles sold for the largest amount of bottles sold in each catergory.  I couldn't figure out how to print out the category name, so this is just the bottles sold column.
                          Bottles Sold
County    broad category              
Adair     brandy                    99
          cocktail                  81
          gin                       34
          other                     15
          rum                      305
          shnapps                  338
          tequila                  325
          vodka                   1043
          whiskey                  885
Adams     brandy                    16
          cocktail                  55
          gin                        5
          other                      3
          rum                       31
          shnapps                  149
          tequila                   16
          vodka                     85
          whiskey                  251
Allamakee brandy                   224
          cocktail                  66
('Polk', 'vodka', 'VODKA 80 PROOF')
Question #8: 
Here is a list of all 99 counties in Iowa and their population sizes, sorted by population, obtained from http://www.iowa-demographics.com/counties_by_population.  Looking at the rows, there is a large jump in population size between county #10 (Dallas County with 80,000) to county #11(Warren County with 48,000).  Therefore, I will call the first 10 counties 'Large Counties', and the remaining counties 'Small Counties'.
    Rank                County Population
0      1           Polk County    467,711
1      2           Linn County    219,916
2      3          Scott County    172,126
3      4        Johnson County    144,251
4      5     Black Hawk County    133,455
5      6       Woodbury County    102,782
6      7        Dubuque County     97,125
7      8          Story County     96,021
8      9  Pottawattamie County     93,671
9     10         Dallas County     80,133
10    11         Warren County     48,626
11    12        Clinton County     47,768
12    13    Cerro Gordo County     43,017
13    14      Muscatine County     43,011
14    15       Marshall County     40,746
15    16     Des Moines County     40,055
16    17        Webster County     37,071
17    18         Jasper County     36,827
18    19        Wapello County     35,173
19    20            Lee County     35,089
It seems, as would be expected, that large counties have more total stores than small counties.  Looking at the desciptions below, large counties have an average 68 stores with a median of 53 stores, while small counties have an average and a median of only 7 stores.
count     10.000000
mean      68.600000
std       53.821103
min       17.000000
25%       38.500000
50%       53.000000
75%       71.250000
max      207.000000
Name: Store Number, dtype: float64
count    89.000000
mean      7.775281
std       4.740428
min       1.000000
25%       5.000000
50%       7.000000
75%      10.000000
max      21.000000
Name: Store Number, dtype: float64
However, when you look at the average number of stores based on the average population size per county in each subset, you see that they have almost identically 4 stores for every 10,000 people.
Number of stores per 10,000 people in a large county:  4.26831658465
Number of stores per 10,000 people in a small county:  4.56251302162
Averaging all of the orders in the 2 subsets, we see that large counties ordered an average of 11.2422927712 bottles per order, while small counties order an average of 8.04799002537 bottles per order.
It appears there are only minor diffences in tastes between the large counties and small counties.  The first list below is the sorted sum total of all bottles sold in large counties, and the second list is the sorted sum total of all bottles sold in small counties.  The noticeable difference is that in large counties significantly more vodka is sold than whiskey, while in small counties there actually is slightly more whiskey sold than vodka.  A possible reason for this could be that in large counties there are more cities where people enjoy mixed drinks that contain vodka, while in small counties there are more rural inhabitants that would opt for a straight whiskey drink more often than they would a mixed vodka drink. All other catergories are in equal standing across the two lists.
broad category
vodka       552795
whiskey     399476
shnapps     269588
rum         204690
brandy      114414
tequila      83596
gin          66018
cocktail     34805
other        13351
Name: Bottles Sold, dtype: int64
broad category
whiskey     293325
vodka       248865
shnapps     153689
rum         125762
brandy       37795
tequila      30261
gin          19164
cocktail     18497
other         8583
Name: Bottles Sold, dtype: int64
Question #9: 
In county_graph.png I have 2 scatter plots of the number of stores in a county based on the the number of inhabitants of the county, with a separate graph for large counties and small counties.  There doesn't seem to be much correlation between the two variables.  With the large counties, there are only 10 data points, so nothing signficant can be observed.  With the small counties you do see that there is some positive correlation, that as the population goes up, you can expect to have more stores, as would be expected.
Question #10: 
I found data online with unemployment rates for each county in Iowa.  My hypothesis was that if a county has a higher unemployment rate, it would have a higher number of bottles sold per person.  I calculated  the number of bottles sold per person in each county and put that on the y-axis as the dependant variable, and the unemployment rate for each county on the x-axis as the independant variable.  After drawing a scatter plot, in unemployment_graph.png, I didn't see any real correlation.  Then I thought that if unemployed people aren't pushing up the average number of bottles sold per person, maybe college students are.  There are 3 counties in Iowa that have public universities:  Iowa State University in Story County, University of Iowa in Johnson County, and University of Northern Iowa in Black Hawk County.  I wanted to see if they have a high average bottle per person purchase rate.  I created a bar graph in college_counties.png, and saw that although all 3 counties aren't pushing up the state average, Johnson county was equal to the state average, and since it is the 4th largest county in Iowa, it can definitely be setting a trend for the rest of the state average.  Something to explore further is to look at counties with private univesities which could have even higher drinking rates, and also to look at individual cities in each county where the univesities are, which could have a higher bottle purchase rate than the rest of the county.
                County  December\n2016
0         Adair County             2.8
1         Adams County             2.6
2     Allamakee County             6.1
3     Appanoose County             4.4
4       Audubon County             2.8
5        Benton County             3.6
6    Black Hawk County             4.5
7         Boone County             2.4
8        Bremer County             3.7
9      Buchanan County             3.8
10  Buena Vista County             3.1
11       Butler County             4.9
12      Calhoun County             3.4
13      Carroll County             2.3
14         Cass County             3.3
15        Cedar County             3.4
16  Cerro Gordo County             3.6
17     Cherokee County             3.2
18    Chickasaw County             4.4
19       Clarke County             3.2