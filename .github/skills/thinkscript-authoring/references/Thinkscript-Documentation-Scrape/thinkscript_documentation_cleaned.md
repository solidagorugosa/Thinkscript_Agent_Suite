
================================================================================PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Annotations
Date
The following annotation types are available:
Date
Date
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Annotations/Date
Date
Date
Syntax

@Date

Description

Annotates an integer input as a date:

The date must be specified using the YYYYMMDD format.
Only integer inputs can be annotated as a date.
To annotate multiple inputs, specify annotations for each.

Change annotated date inputs by:

Using the built-in date picker in the study properties.

Right-clicking the chart area on a specific date.

Example 1
@Date
input date = 20240101;
AddVerticalLine(GetYYYYMMDD() >= date and GetYYYYMMDD()[1] < date);

This script draws a vertical line at the specified date.

Example 2
@Date
input beginDate = 20231106;
@Date
input endDate = 20231226;

plot Line = if GetYYYYMMDD() >= beginDate and GetYYYYMMDD()[1] < beginDate or  GetYYYYMMDD() >= endDate and GetYYYYMMDD()[1] < endDate then close else Double.NaN;
Line.EnableApproximation();

This script draws a line between closing prices for beginDate and endDate.


PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants
Choose your constant from the list:
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod
Aggregation period constants define a specific aggregation period for your studies and strategies. The period length varies from one minute to option expiration.
Choose an aggregation period from the list:
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-DAY
Syntax

AggregationPeriod.DAY

Description

Defines aggregation period equal to one day (86,400,000 milliseconds).

Example
def agg = AggregationPeriod.DAY; 
plot data = close(period = agg);

This example script draws the daily Close price plot. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

FOUR_HOURS
TWO_DAYS

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-FIFTEEN-MIN
Syntax

AggregationPeriod.FIFTEEN_MIN

Description

Defines aggregation period equal to fifteen minutes (900,000 milliseconds).

Example
def agg = AggregationPeriod.FIFTEEN_MIN; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to fifteen minutes. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

TEN_MIN
TWENTY_MIN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-FIVE-MIN
Syntax

AggregationPeriod.FIVE_MIN

Description

Defines aggregation period equal to five minutes (300,000 milliseconds).

Example
def agg = AggregationPeriod.FIVE_MIN; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to five minutes. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

FOUR_MIN
TEN_MIN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-FOUR-DAYS
Syntax

AggregationPeriod.FOUR_DAYS

Description

Defines aggregation period equal to four days (345,600,000 milliseconds).

Example
def agg = AggregationPeriod.FOUR_DAYS; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to four days. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

THREE_DAYS
WEEK

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-FOUR-HOURS
Syntax

AggregationPeriod.FOUR_HOURS

Description

Defines aggregation period equal to four hours (14,400,000 milliseconds).

Example
def agg = AggregationPeriod.FOUR_HOURS; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to four hours. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

TWO_HOURS
DAY

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-FOUR-MIN
Syntax

AggregationPeriod.FOUR_MIN

Description

Defines aggregation period equal to four minutes (240,000 milliseconds).

Example
def agg = AggregationPeriod.FOUR_MIN; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to four minutes. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

THREE_MIN
FIVE_MIN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-HOUR
Syntax

AggregationPeriod.HOUR

Description

Defines aggregation period equal to one hour (3,600,000 milliseconds).

Example
def agg = AggregationPeriod.HOUR; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to one hour. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

THIRTY_MIN
TWO_HOURS

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-MIN
Syntax

AggregationPeriod.MIN

Description

Defines aggregation period equal to one minute (60,000 milliseconds).

Example
def agg = AggregationPeriod.MIN; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to one minute. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

AggregationPeriod
TWO_MIN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-MONTH
Syntax

AggregationPeriod.MONTH

Description

Defines aggregation period equal to one month (2,592,000,000 milliseconds).

Example
def agg = AggregationPeriod.MONTH; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to one month. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

WEEK
OPT_EXP

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-OPT-EXP
Syntax

AggregationPeriod.OPT_EXP

Description

Defines aggregation period equal to option expiration (2,678,400,000 milliseconds).

Example
def agg = AggregationPeriod.OPT_EXP; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to option expiration. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

MONTH
QUARTER

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-QUARTER
Syntax

AggregationPeriod.QUARTER

Description

The AggregationPeriod.QUARTER constant can be used with some functions to make the data aggregation period equal to one calendar quarter (7,776,000,000 milliseconds). 

Example
def agg = AggregationPeriod.QUARTER; 

plot data = close(period = agg);

The above script plots the close price aggregated on a quarterly basis. Note that this script only works on charts with an aggregation period less than or equal to one quarter.

See also: GetAggregationPeriod function in the Others section.

OPT_EXP
YEAR

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-TEN-MIN
Syntax

AggregationPeriod.TEN_MIN

Description

Defines aggregation period equal to ten minutes (600,000 milliseconds).

Example
def agg = AggregationPeriod.TEN_MIN; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to ten minutes. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

FIVE_MIN
FIFTEEN_MIN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-THIRTY-MIN
Syntax

AggregationPeriod.THIRTY_MIN

Description

Defines aggregation period equal to thirty minutes (1,800,000 milliseconds).

Example
def agg = AggregationPeriod.THIRTY_MIN; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to thirty minutes. Note that aggregation period used in this example cannot be less than chart aggregation period.

See the GetAggregationPeriod function in the Others section.

TWENTY_MIN
HOUR

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-THREE-DAYS
Syntax

AggregationPeriod.THREE_DAYS

Description

Defines aggregation period equal to three days (259,200,000 milliseconds)

Example
def agg = AggregationPeriod.THREE_DAYS; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to three days. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

TWO_DAYS
FOUR_DAYS

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-THREE-MIN
Syntax

AggregationPeriod.THREE_MIN

Description

Defines aggregation period equal to three minutes (180,000 milliseconds).

Example
def agg = AggregationPeriod.THREE_MIN; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to three minutes. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

TWO_MIN
FOUR_MIN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-TWENTY-MIN
Syntax

AggregationPeriod.TWENTY_MIN

Description

Defines aggregation period equal to twenty minutes (1,200,000 milliseconds).

Example
def agg = AggregationPeriod.TWENTY_MIN; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to twenty minutes. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

FIFTEEN_MIN
THIRTY_MIN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-TWO-DAYS
Syntax

AggregationPeriod.TWO_DAYS

Description

Defines aggregation period equal to two days (172,800,000 milliseconds).

Example
def agg = AggregationPeriod.TWO_DAYS; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to two days. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

DAY
THREE_DAYS

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-TWO-HOURS
Syntax

AggregationPeriod.TWO_HOURS

Description

Defines aggregation period equal to two hours (7,200,000 milliseconds).

Example
def agg = AggregationPeriod.TWO_HOURS; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to two hours. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

HOUR
FOUR_HOURS

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-TWO-MIN
Syntax

AggregationPeriod.TWO_MIN

Description

Defines aggregation period equal to two minutes (120,000 milliseconds).

Example
def agg = AggregationPeriod.TWO_MIN; 
plot data = close(period = agg);

This example script draws the Close price plot with aggregation period equal to two minutes. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

MIN
THREE_MIN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-WEEK
Syntax

AggregationPeriod.WEEK

Description

Defines aggregation period equal to one week (604,800,000 milliseconds)

Example
def agg = AggregationPeriod.WEEK; 
plot data = close(period = agg);

This example script draws the weekly Close price plot. Note that aggregation period used in this example cannot be less than chart aggregation period.

See also GetAggregationPeriod function in the Others section.

FOUR_DAYS
MONTH

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AggregationPeriod/AggregationPeriod-YEAR
Syntax

AggregationPeriod.YEAR

Description

The AggregationPeriod.YEAR constant can be used with some functions to make the data aggregation period equal to one calendar year (31,536,000,000 milliseconds). 

Example
def agg = AggregationPeriod.YEAR; 

plot data = close(period = agg);

The above script plots the close price aggregated on a yearly basis.

See also: GetAggregationPeriod function in the Others section.

QUARTER
Alert

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Alert
BAR
ONCE
TICK
Alert constants represent different types of alerts for the Alert function.
Choose an alert constant from the list:
BAR
ONCE
TICK
BAR
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Alert/Alert-BAR
BAR
ONCE
TICK
BAR
Syntax

Alert.BAR

Description

Defines the alert that can be triggered only once per bar.

Example

See the Alert function in the Others section.

Alert
ONCE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Alert/Alert-ONCE
BAR
ONCE
TICK
ONCE
Syntax

Alert.ONCE

Description

Defines the alert that can be triggered only once after adding a study.

Example

See the Alert function in the Others section.

BAR
TICK

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Alert/Alert-TICK
BAR
ONCE
TICK
TICK
Syntax

Alert.TICK

Description

Defines the alert that can be triggered after each tick.

Example

See the Alert function in the Others section.

ONCE
AverageType

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AverageType
EXPONENTIAL
HULL
SIMPLE
WEIGHTED
WILDERS
In this section you will find information on the constants used with MovingAverage function.
EXPONENTIAL
HULL
SIMPLE
WEIGHTED
WILDERS
EXPONENTIAL
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AverageType/AverageType-EXPONENTIAL
EXPONENTIAL
HULL
SIMPLE
WEIGHTED
WILDERS
EXPONENTIAL
Syntax

AverageType.EXPONENTIAL

Description

Used with MovingAverage function to define the Exponential Moving Average.

Example

AverageType
HULL

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AverageType/AverageType-HULL
EXPONENTIAL
HULL
SIMPLE
WEIGHTED
WILDERS
HULL
Syntax

AverageType.HULL

Description

Used with MovingAverage function to define the Hull Moving Average.

Example

EXPONENTIAL
SIMPLE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AverageType/AverageType-SIMPLE
EXPONENTIAL
HULL
SIMPLE
WEIGHTED
WILDERS
SIMPLE
Syntax

AverageType.SIMPLE

Description

Used with MovingAverage function to define the Simple Moving Average.

Example

HULL
WEIGHTED

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AverageType/AverageType-WEIGHTED
EXPONENTIAL
HULL
SIMPLE
WEIGHTED
WILDERS
WEIGHTED
Syntax

AverageType.WEIGHTED

Description

Used with MovingAverage function to define the Weighted Moving Average.

Example

SIMPLE
WILDERS

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/AverageType/AverageType-WILDERS
EXPONENTIAL
HULL
SIMPLE
WEIGHTED
WILDERS
WILDERS
Syntax

AverageType.WILDERS

Description

Used with MovingAverage function to define the Wilder's Moving Average.

Example

WEIGHTED
ChartType

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/ChartType
BAR
CANDLE
CANDLE_TREND
HEIKIN_ASHI
EQUIVOLUME
LINE
AREA
In this section you will find information on the constants used in SetChartType function.
BAR
CANDLE
CANDLE_TREND
HEIKIN_ASHI
EQUIVOLUME
LINE
AREA
BAR
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/ChartType/ChartType-AREA
BAR
CANDLE
CANDLE_TREND
HEIKIN_ASHI
EQUIVOLUME
LINE
AREA
AREA
Syntax

ChartType.AREA

Description

Used in SetChartType function to set the Area chart type.

Example

See the SetChartType article in the Look and Feel functions section.

LINE
Color

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/ChartType/ChartType-BAR
BAR
CANDLE
CANDLE_TREND
HEIKIN_ASHI
EQUIVOLUME
LINE
AREA
BAR
Syntax

ChartType.BAR

Description

Used in SetChartType function to set the Bar chart type.

Example

See the SetChartType article in the Look and Feel functions section.

ChartType
CANDLE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/ChartType/ChartType-CANDLE
BAR
CANDLE
CANDLE_TREND
HEIKIN_ASHI
EQUIVOLUME
LINE
AREA
CANDLE
Syntax

ChartType.CANDLE

Description

Used in SetChartType function to set the Candle chart type.

Example

See the SetChartType article in the Look and Feel functions section.

BAR
CANDLE_TREND

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/ChartType/ChartType-CANDLE-TREND
BAR
CANDLE
CANDLE_TREND
HEIKIN_ASHI
EQUIVOLUME
LINE
AREA
CANDLE_TREND
Syntax

ChartType.CANDLE_TREND

Description

Used in SetChartType function to set the Candle Trend chart type.

Example

See the SetChartType article in the Look and Feel functions section.

CANDLE
HEIKIN_ASHI

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/ChartType/ChartType-EQUIVOLUME
BAR
CANDLE
CANDLE_TREND
HEIKIN_ASHI
EQUIVOLUME
LINE
AREA
EQUIVOLUME
Syntax

ChartType.EQUIVOLUME

Description

Used in SetChartType function to set the Equivolume chart type.

Example

See the SetChartType article in the Look and Feel functions section.

HEIKIN_ASHI
LINE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/ChartType/ChartType-HEIKIN-ASHI
BAR
CANDLE
CANDLE_TREND
HEIKIN_ASHI
EQUIVOLUME
LINE
AREA
HEIKIN_ASHI
Syntax

ChartType.HEIKIN_ASHI

Description

Used in SetChartType function to set the Heikin Ashi chart type.

Example

See the SetChartType article in the Look and Feel functions section.

CANDLE_TREND
EQUIVOLUME

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/ChartType/ChartType-LINE
BAR
CANDLE
CANDLE_TREND
HEIKIN_ASHI
EQUIVOLUME
LINE
AREA
LINE
Syntax

ChartType.LINE

Description

Used in SetChartType function to set the Line chart type.

Example

See the SetChartType article in the Look and Feel functions section.

EQUIVOLUME
AREA

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
Here is the full list of the colors:
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
BLACK
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-BLACK
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
BLACK
Syntax

Color.BLACK

Description

Defines the black color. Its RGB representation is (0, 0, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

Color
BLUE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-BLUE
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
BLUE
Syntax

Color.BLUE

Description

Defines the blue color. Its RGB representation is (0, 0, 255).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

BLACK
CURRENT

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-CURRENT
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
CURRENT
Syntax

Color.CURRENT

Description

Refers to the default plot color (or redefined color in case it was changed on the UI). When using the AssignPriceColor function the constant is responsible for price bars color. In combintaion with the AssignBackgroundColor function the constant defines the corresponding background color.

Example

See the SetDefaultColor function in the Look and Feel functions section.

BLUE
CYAN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-CYAN
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
CYAN
Syntax

Color.CYAN

Description

Defines the cyan color. Its RGB representation is (0, 255, 255).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

CURRENT
DARK_GRAY

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-DARK-GRAY
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
DARK_GRAY
Syntax

Color.DARK_GRAY

Description

Defines the dark gray color. Its RGB representation is (64, 64, 64).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

CYAN
DARK_GREEN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-DARK-GREEN
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
DARK_GREEN
Syntax

Color.DARK_GREEN

Description

Defines the dark green color. Its RGB representation is (0, 100, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

DARK_GRAY
DARK_ORANGE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-DARK-ORANGE
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
DARK_ORANGE
Syntax

Color.DARK_ORANGE

Description

Defines the dark orange color. Its RGB representation is (255, 127, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

DARK_GREEN
DARK_RED

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-DARK-RED
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
DARK_RED
Syntax

Color.DARK_RED

Description

Defines the dark red color. Its RGB representation is (128, 0, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

DARK_ORANGE
DOWNTICK

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-DOWNTICK
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
DOWNTICK
Syntax

Color.DOWNTICK

Description

Defines the downtick color. Its RGB representation is (204, 0, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel section.

DARK_RED
GRAY

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-GRAY
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
GRAY
Syntax

Color.GRAY

Description

Defines the gray color. Its RGB representation is (128, 128, 128).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

DOWNTICK
GREEN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-GREEN
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
GREEN
Syntax

Color.GREEN

Description

Defines the green color. Its RGB representation is (0, 255, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

GRAY
LIGHT_GRAY

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-LIGHT-GRAY
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
LIGHT_GRAY
Syntax

Color.LIGHT_GRAY

Description

Defines the light gray color. Its RGB representation is (192, 192, 192).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

GREEN
LIGHT_GREEN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-LIGHT-GREEN
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
LIGHT_GREEN
Syntax

Color.LIGHT_GREEN

Description

Defines the light green color. Its RGB representation is (144, 238, 114).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

LIGHT_GRAY
LIGHT_ORANGE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-LIGHT-ORANGE
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
LIGHT_ORANGE
Syntax

Color.LIGHT_ORANGE

Description

Defines the light orange color. Its RGB representation is (255, 165, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

LIGHT_GREEN
LIGHT_RED

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-LIGHT-RED
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
LIGHT_RED
Syntax

Color.LIGHT_RED

Description

Defines the light red color. Its RGB representation is (255, 63, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

LIGHT_ORANGE
LIME

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-LIME
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
LIME
Syntax

Color.LIME

Description

Defines the lime color. Its RGB representation is (191, 255, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

LIGHT_RED
MAGENTA

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-MAGENTA
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
MAGENTA
Syntax

Color.MAGENTA

Description

Defines the magenta color. Its RGB representation is (255, 0, 255).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

LIME
ORANGE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-ORANGE
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
ORANGE
Syntax

Color.ORANGE

Description

Defines the orange color. Its RGB representation is (255, 200, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

MAGENTA
PINK

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-PINK
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
PINK
Syntax

Color.PINK

Description

Defines the pink color. Its RGB representation is (255, 175, 175).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

ORANGE
PLUM

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-PLUM
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
PLUM
Syntax

Color.PLUM;

Description

Defines the plum color. Its RGB representation is (128, 0, 128).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

PINK
RED

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-RED
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
RED
Syntax

Color.RED

Description

Defines the red color. Its RGB representation is (255, 0, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

PLUM
UPTICK

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-UPTICK
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
UPTICK
Syntax

Color.UPTICK

Description

Defines the uptick color. Its RGB representation is (3, 128, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

RED
VIOLET

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-VIOLET
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
VIOLET
Syntax

Color.VIOLET

Description

Defines the violet color. Its RGB representation is (153, 153, 255).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

UPTICK
WHITE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-WHITE
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
WHITE
Syntax

Color.WHITE

Description

Defines the white color. Its RGB representation is (255, 255, 255).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

VIOLET
YELLOW

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Color/Color-YELLOW
BLACK
BLUE
CURRENT
CYAN
DARK_GRAY
DARK_GREEN
DARK_ORANGE
DARK_RED
DOWNTICK
GRAY
GREEN
LIGHT_GRAY
LIGHT_GREEN
LIGHT_ORANGE
LIGHT_RED
LIME
MAGENTA
ORANGE
PINK
PLUM
RED
UPTICK
VIOLET
WHITE
YELLOW
YELLOW
Syntax

Color.YELLOW

Description

Defines the yellow color. Its RGB representation is (255, 255, 0).

Sample

Example

See the SetDefaultColor function in the Look and Feel functions section.

WHITE
CrossingDirection

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/CrossingDirection
ABOVE
BELOW
ANY
Crossing direction constants define a specific switch of the relationship between arguments of the Crosses function.
Choose a crossing direction constant from the list:
ABOVE
BELOW
ANY
ABOVE
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/CrossingDirection/CrossingDirection-ABOVE
ABOVE
BELOW
ANY
ABOVE
Syntax

CrossingDirection.ABOVE

Description

This constant is used with the Crosses function to find when the first value becomes greater than the second.

Note that this constant can be replaced with reserved word yes.

Example
plot avg = Average(close, 10);
plot crossing = Crosses(close, avg, CrossingDirection.ABOVE);
crossing.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_UP);

This code marks the bars at which the Close price gets higher than its 10 period average.

CrossingDirection
BELOW

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/CrossingDirection/CrossingDirection-ANY
ABOVE
BELOW
ANY
ANY
Syntax

CrossingDirection.ANY

Description

Defines the change of relation of two values in the Crosses function irrespective of its direction.

Example
plot avg = Average(close, 10);
plot crossing = Crosses(close, avg, CrossingDirection.ANY);
crossing.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_UP);

This code marks the bars at which the Close price becomes greater or less than its 10 period average.

BELOW
Curve

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/CrossingDirection/CrossingDirection-BELOW
ABOVE
BELOW
ANY
BELOW
Syntax

CrossingDirection.BELOW

Description

This constant is used with the Crosses function to find when the first value becomes less than the second.

Note that this constant can be replaced with reserved word no.

Example
plot avg = Average(close, 10);
plot crossing = Crosses(close, avg, CrossingDirection.BELOW);
crossing.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_DOWN);

This code marks the bars at which the Close price becomes less than its 10 period average.

ABOVE
ANY

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Curve
FIRM
LONG_DASH
MEDIUM_DASH
SHORT_DASH
POINTS
In this section you will find information on the constants used with SetStyle function to define the style of curve to be plotted.
Choose your constant from the list:
FIRM
LONG_DASH
MEDIUM_DASH
SHORT_DASH
POINTS
FIRM
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Curve/Curve-FIRM
FIRM
LONG_DASH
MEDIUM_DASH
SHORT_DASH
POINTS
FIRM
Syntax

Curve.FIRM

Description

Defines the firm style curve constant.

Sample

Example

See the SetStyle function in the Look and Feel functions section.

Curve
LONG_DASH

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Curve/Curve-LONG-DASH
FIRM
LONG_DASH
MEDIUM_DASH
SHORT_DASH
POINTS
LONG_DASH
Syntax

Curve.LONG_DASH

Description

Defines the style of curve with long dashes.

Sample

Example

See the SetStyle function in the Look and Feel functions section.

FIRM
MEDIUM_DASH

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Curve/Curve-MEDIUM-DASH
FIRM
LONG_DASH
MEDIUM_DASH
SHORT_DASH
POINTS
MEDIUM_DASH
Syntax

Curve.MEDIUM_DASH

Description

Defines the style of curve with medium-size dashes.

Sample

Example

See the SetStyle function in the Look and Feel functions section.

LONG_DASH
SHORT_DASH

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Curve/Curve-POINTS
FIRM
LONG_DASH
MEDIUM_DASH
SHORT_DASH
POINTS
POINTS
Syntax

Curve.POINTS

Description

Defines the points style curve constant.

Sample

Example

See the SetStyle function in the Look and Feel functions section.

SHORT_DASH
Double

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Curve/Curve-SHORT-DASH
FIRM
LONG_DASH
MEDIUM_DASH
SHORT_DASH
POINTS
SHORT_DASH
Syntax

Curve.SHORT_DASH

Description

Defines the style of curve with short dashes.

Sample

Example

See the SetStyle function in the Look and Feel functions section.

MEDIUM_DASH
POINTS

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Double
E
NaN
NEGATIVE_INFINITY
Pi
POSITIVE_INFINITY
This section describes mathematical constants such as exponent or pi.
Choose a constant from the list:
E
NaN
NEGATIVE_INFINITY
Pi
POSITIVE_INFINITY
E
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Double/Double-E
E
NaN
NEGATIVE_INFINITY
Pi
POSITIVE_INFINITY
E
Syntax

Double.E

Description

Returns the value of the exponent constant.

Example (Price Oscillator)

See the Exp function in the Mathematical and Trigonometrical functions section.

Double
NaN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Double/Double-NEGATIVE-INFINITY
E
NaN
NEGATIVE_INFINITY
Pi
POSITIVE_INFINITY
NEGATIVE_INFINITY
Syntax

Double.NEGATIVE_INFINITY

Description

Defines the negative value of infinitely large magnitude.

Example
input price = close;
def length = if close > close[1] then 20 else 30;
plot VariableMax = fold i = 0 to length with m = Double.NEGATIVE_INFINITY do Max(m, getValue(price, i, 30));

This script finds the greatest of several recent values of price, with a non-constant number of values being processed.

NaN
Pi

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Double/Double-NaN
E
NaN
NEGATIVE_INFINITY
Pi
POSITIVE_INFINITY
NaN
Syntax

Double.NaN

Description

Returns the value that indicates that the result of an operation is not a number.

Example (Price Oscillator)

See the IsNaN function in the Mathematical and Trigonometrical section.

E
NEGATIVE_INFINITY

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Double/Double-POSITIVE-INFINITY
E
NaN
NEGATIVE_INFINITY
Pi
POSITIVE_INFINITY
POSITIVE_INFINITY
Syntax

Double.POSITIVE_INFINITY

Description

Defines the positive value of infinitely large magnitude.

Example
declare lower;
def range = high - low;
plot SmallestRange = LowestAll(if range == 0 then Double.POSITIVE_INFINITY else range);

This script finds the smallest non-zero candle range on chart.

Pi
EarningTime

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Double/Double-Pi
E
NaN
NEGATIVE_INFINITY
Pi
POSITIVE_INFINITY
Pi
Syntax

Double.Pi

Description

Returns the value of the pi constant.

Example (Price Oscillator)

See the ASin, ACos, Sin, and Cos functions in the Mathematical and Trigonometrical functions section.

NEGATIVE_INFINITY
POSITIVE_INFINITY

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/EarningTime
ANY
BEFORE_MARKET
AFTER_MARKET
In this section you will find information on the constants used with HasEarnings function.
ANY
BEFORE_MARKET
AFTER_MARKET
ANY
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/EarningTime/EarningTime-AFTER-MARKET
ANY
BEFORE_MARKET
AFTER_MARKET
AFTER_MARKET
Syntax

EarningTime.AFTER_MARKET

Description

Used with HasEarnings function to query whether the earnings announcement takes place after market close.

Example

See the HasEarnings article in the Corporate Actions functions section.

BEFORE_MARKET
Events

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/EarningTime/EarningTime-ANY
ANY
BEFORE_MARKET
AFTER_MARKET
ANY
Syntax

EarningTime.ANY

Description

Used with HasEarnings function to query whether there are announced earnings. The announcement can take place before market open, or after market close, or during market hours, or at unspecified time.

Example

See the HasEarnings article in the Corporate Actions functions section.

EarningTime
BEFORE_MARKET

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/EarningTime/EarningTime-BEFORE-MARKET
ANY
BEFORE_MARKET
AFTER_MARKET
BEFORE_MARKET
Syntax

EarningTime.BEFORE_MARKET

Description

Used with HasEarnings function to query whether the earnings announcement takes place before market open.

Example

See the HasEarnings article in the Corporate Actions functions section.

ANY
AFTER_MARKET

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Events
CONFERENCE_CALL
DIVIDEND
EARNINGS
SPLIT
In this section you will find information on the constants used with GetEventOffset function.
CONFERENCE_CALL
DIVIDEND
EARNINGS
SPLIT
CONFERENCE_CALL
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Events/Events-CONFERENCE-CALL
CONFERENCE_CALL
DIVIDEND
EARNINGS
SPLIT
CONFERENCE_CALL
Syntax

Events.CONFERENCE_CALL

Description

Used with GetEventOffset function to return offset for conference calls.

Example

See the GetEventOffset article in the Corporate Actions section.

Events
DIVIDEND

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Events/Events-DIVIDEND
CONFERENCE_CALL
DIVIDEND
EARNINGS
SPLIT
DIVIDEND
Syntax

Events.DIVIDEND

Description

Used with GetEventOffset function to return offset for dividend events.

Example

See the GetEventOffset article in the Corporate Actions section.

CONFERENCE_CALL
EARNINGS

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Events/Events-EARNINGS
CONFERENCE_CALL
DIVIDEND
EARNINGS
SPLIT
EARNINGS
Syntax

Events.EARNINGS

Description

Used with GetEventOffset function to return offset for earnings announcements.

Example

See the GetEventOffset article in the Corporate Actions section.

DIVIDEND
SPLIT

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Events/Events-SPLIT
CONFERENCE_CALL
DIVIDEND
EARNINGS
SPLIT
SPLIT
Syntax

Events.SPLIT

Description

Used with GetEventOffset function to return offset for split events.

Example

See the GetEventOffset article in the Corporate Actions section.

EARNINGS
FiscalPeriod

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FiscalPeriod
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FiscalPeriod/FiscalPeriod-QUARTER
Syntax

FiscalPeriod.QUARTER

Description

The FiscalPeriod.QUARTER constant can be set as a value of the fiscalPeriod input parameter of some of the Stock Fundamentals functions, in which case the value is returned based on the quarterly fiscal data.

Below is the list of functions compatible with this constant:

CurrentRatio
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
GrossProfitMargin
NetProfitMargin
OperatingProfitMargin
ReturnOnAssets
ReturnOnEquity
TaxRate
TotalAssetTurnover
FiscalPeriod
YEAR

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FiscalPeriod/FiscalPeriod-YEAR
Syntax

FiscalPeriod.YEAR

Description

The FiscalPeriod.YEAR constant can be used as a value of the fiscalPeriod input parameter of a Stock Fundamentals function so that the value returned is based on the yearly fiscal data. This is the default value of the fiscalPeriod parameter of all Stock Fundamentals functions.

QUARTER
FontSize

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FontSize
SMALL
MEDIUM
LARGE
LARGER
VERY_LARGE
X_LARGE
The Font Size constants are used with the AddLabel() function to define the font size of the label text. The following location constants are available:
SMALL
MEDIUM
LARGE
LARGER
VERY_LARGE
X_LARGE
SMALL
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FontSize/FontSize-LARGE
SMALL
MEDIUM
LARGE
LARGER
VERY_LARGE
X_LARGE
LARGE
Syntax

FontSize.LARGE

Description

Used with the AddLabel() function to increase the default font size by 200%.

Example
AddLabel(yes, "Current symbol: " + GetSymbol(), size = FontSize.LARGE);

Displays a label with the name of the current symbol using the large font size.

MEDIUM
LARGER

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FontSize/FontSize-LARGER
SMALL
MEDIUM
LARGE
LARGER
VERY_LARGE
X_LARGE
LARGER
Syntax

FontSize.LARGER

Description

Used with the AddLabel() function to increase the default font size by 250%.

Example
AddLabel(yes, "Current symbol: " + GetSymbol(), size = FontSize.LARGER);

Displays a label with the name of the current symbol using the larger font size.

LARGE
VERY_LARGE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FontSize/FontSize-MEDIUM
SMALL
MEDIUM
LARGE
LARGER
VERY_LARGE
X_LARGE
MEDIUM
Syntax

FontSize.MEDIUM

Description

Used with the AddLabel() function to increase the default font size by 150%.

Example
AddLabel(yes, "Current symbol: " + GetSymbol(), size = FontSize.MEDIUM);

Displays a label with the name of the current symbol using the medium font size.

SMALL
LARGE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FontSize/FontSize-SMALL
SMALL
MEDIUM
LARGE
LARGER
VERY_LARGE
X_LARGE
SMALL
Syntax

FontSize.SMALL

Description

Default value; used with the AddLabel() function to specify text font size.

Example
AddLabel(yes, "Current symbol: " + GetSymbol(), size = FontSize.SMALL);

Displays a label with the name of the current symbol using the small font size.

FontSize
MEDIUM

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FontSize/FontSize-VERY_LARGE
SMALL
MEDIUM
LARGE
LARGER
VERY_LARGE
X_LARGE
VERY_LARGE
Syntax

FontSize.VERY_LARGE

Description

Used with the AddLabel() function to increase the default font size by 300%.

Example
AddLabel(yes, "Current symbol: " + GetSymbol(), size = FontSize.VERY_LARGE);

Displays a label with the name of the current symbol using the very large font size.

LARGER
X_LARGE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FontSize/FontSize-X_LARGE
SMALL
MEDIUM
LARGE
LARGER
VERY_LARGE
X_LARGE
X_LARGE
Syntax

FontSize.X_LARGE

Description

Used with the AddLabel() function to increase the default font size by 350%.

Example
AddLabel(yes, "Current symbol: " + GetSymbol(), size = FontSize.X_LARGE);

Displays a label with the name of the current symbol using the extra large font size.

VERY_LARGE
FundamentalType

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
In this section you will find information on the constants used in Fundamental function.
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
HIGH
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType/FundamentalType-CLOSE
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
CLOSE
Syntax

FundamentalType.CLOSE

Description

Used with Fundamental function to return the Close price.

Example

See the Fundamental function article in the Others section.

LOW
OPEN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType/FundamentalType-HIGH
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
HIGH
Syntax

FundamentalType.HIGH

Description

Used with Fundamental function to return the High price.

Example

See the Fundamental function article in the Others section.

FundamentalType
LOW

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType/FundamentalType-HL2
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
HL2
Syntax

FundamentalType.HL2

Description

Used with Fundamental function to return the arithmetical mean of High and Low prices.

Example

See the Fundamental function article in the Others section.

OPEN
HLC3

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType/FundamentalType-HLC3
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
HLC3
Syntax

FundamentalType.HLC3

Description

Used with Fundamental function to return the arithmetical mean of High, Low, and Close prices.

Example

See the Fundamental function article in the Others section.

HL2
OHLC4

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType/FundamentalType-IMP-VOLATILITY
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
IMP_VOLATILITY
Syntax

FundamentalType.IMP_VOLATILITY

Description

Used with Fundamental function to return the implied volatility value.

Example

See the Fundamental function article in the Others section.

OPEN_INTEREST
TICK_COUNT

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType/FundamentalType-LOW
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
LOW
Syntax

FundamentalType.LOW

Description

Used with Fundamental function to return the Low price.

Example

See the Fundamental function article in the Others functions section.

HIGH
CLOSE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType/FundamentalType-OHLC4
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
OHLC4
Syntax

FundamentalType.OHLC4

Description

Used with Fundamental function to return the arithmetical mean of High, Low, Open, and Close prices.

Example

See the Fundamental function article in the Others section.

HLC3
VWAP

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType/FundamentalType-OPEN
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
OPEN
Syntax

FundamentalType.OPEN

Description

Used with Fundamental function to return the Open price.

Example

See the Fundamental function article in the Others section.

CLOSE
HL2

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType/FundamentalType-OPEN-INTEREST
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
OPEN_INTEREST
Syntax

FundamentalType.OPEN_INTEREST

Description

Used with Fundamental function to return the open interest value.

Example

See the Fundamental function article in the Others section.

VOLUME
IMP_VOLATILITY

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType/FundamentalType-TICK-COUNT
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
TICK_COUNT
Syntax

FundamentalType.TICK_COUNT

Description

Used with the Fundamental function to return the number of trades corresponding to an intraday bar.

Example
declare lower;

declare zerobase;

plot Trades = Fundamental(FundamentalType.TICK_COUNT); 

Trades.SetPaintingStrategy(PaintingStrategy.HISTOGRAM);

On an intraday chart, this script plots a histogram that represents the number of trades for each bar.

IMP_VOLATILITY
Location

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType/FundamentalType-VOLUME
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
VOLUME
Syntax

FundamentalType.VOLUME

Description

Used with Fundamental function to return the volume value.

Example

See the Fundamental function article in the Others section.

VWAP
OPEN_INTEREST

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/FundamentalType/FundamentalType-VWAP
HIGH
LOW
CLOSE
OPEN
HL2
HLC3
OHLC4
VWAP
VOLUME
OPEN_INTEREST
IMP_VOLATILITY
TICK_COUNT
VWAP
Syntax

FundamentalType.VWAP

Description

Used with Fundamental function to return the volume weighted average price value.

Example

See the Fundamental function article in the Others section.

OHLC4
VOLUME

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Location
TOP_LEFT
TOP_RIGHT
BOTTOM_LEFT
BOTTOM_RIGHT
Location constants are used with the AddLabel() function to specify the position of a label on the chart.
The following is a list of available location constants:
TOP_LEFT
TOP_RIGHT
BOTTOM_LEFT
BOTTOM_RIGHT
TOP_LEFT
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Location/Location-BOTTOM-LEFT
TOP_LEFT
TOP_RIGHT
BOTTOM_LEFT
BOTTOM_RIGHT
BOTTOM_LEFT
Syntax

Location.BOTTOM_LEFT

Description

Used with the AddLabel() function to place a label in the bottom-left corner of the chart.

Example
AddLabel(yes, "Current symbol: " + GetSymbol(), location = Location.BOTTOM_LEFT);

Displays a label in the bottom-left corner of the chart with the name of the current symbol.

TOP_RIGHT
BOTTOM_RIGHT

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Location/Location-BOTTOM-RIGHT
TOP_LEFT
TOP_RIGHT
BOTTOM_LEFT
BOTTOM_RIGHT
BOTTOM_RIGHT
Syntax

Location.BOTTOM_RIGHT

Description

Used with the AddLabel() function to place a label in the bottom-right corner of the chart.

Example
AddLabel(yes, "Current symbol: " + GetSymbol(), location = Location.BOTTOM_RIGHT); 

Displays a label in the bottom-right corner of the chart with the name of the current symbol.

BOTTOM_LEFT
MonkeyVolumeShowStyle

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Location/Location-TOP-LEFT
TOP_LEFT
TOP_RIGHT
BOTTOM_LEFT
BOTTOM_RIGHT
TOP_LEFT
Syntax

Location.TOP_LEFT

Description

Used with the AddLabel() function to place a label in the top-left corner of the chart.

Example
AddLabel(yes, "Current symbol: " + GetSymbol(), location = Location.TOP_LEFT);

Displays a label in the top-left corner of the chart with the name of the current symbol.

Location
TOP_RIGHT

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Location/Location-TOP-RIGHT
TOP_LEFT
TOP_RIGHT
BOTTOM_LEFT
BOTTOM_RIGHT
TOP_RIGHT
Syntax

Location.TOP_RIGHT

Description

Used with the AddLabel() function to place a label in the top-right corner of the chart.

Example
AddLabel(yes, "Current symbol: " + GetSymbol(), location = Location.TOP_RIGHT);

Displays a label in the top-right corner of the chart with the name of the current symbol.

TOP_LEFT
BOTTOM_LEFT

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/MonkeyVolumeShowStyle
ALL
LAST
NONE
In this section you will find information on the constants used in MonkeyBars function. These constants control display properties of Volume Profile histograms with monkeyBars function.
ALL
LAST
NONE
ALL
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/MonkeyVolumeShowStyle/MonkeyVolumeShowStyle-ALL
ALL
LAST
NONE
ALL
Syntax

MonkeyVolumeShowStyle.ALL

Description

Used with MonkeyBars function to supplement each section of Monkey Bars with Volume Profile histogram.

MonkeyVolumeShowStyle
LAST

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/MonkeyVolumeShowStyle/MonkeyVolumeShowStyle-LAST
ALL
LAST
NONE
LAST
Syntax

MonkeyVolumeShowStyle.LAST

Description

Used with MonkeyBars function to supplement the last section of Monkey Bars with Volume Profile histogram.

ALL
NONE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/MonkeyVolumeShowStyle/MonkeyVolumeShowStyle-NONE
ALL
LAST
NONE
NONE
Syntax

MonkeyVolumeShowStyle.NONE

Description

Used with MonkeyBars function to define that Volume Profile histograms will not be displayed.

LAST
NumberFormat

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/NumberFormat
DOLLAR
THREE_DECIMAL_PLACES
TWO_DECIMAL_PLACES
In this section you will find information on the constants used with AsText function to define format of numbers in which the string should be displayed.
DOLLAR
THREE_DECIMAL_PLACES
TWO_DECIMAL_PLACES
DOLLAR
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/NumberFormat/NumberFormat-DOLLAR
DOLLAR
THREE_DECIMAL_PLACES
TWO_DECIMAL_PLACES
DOLLAR
Syntax

NumberFormat.DOLLAR

Description

Used with AsText function to return a string expressing a number as a dollar amount:

Symbol "$" is prepended;

Two digits after the decimal point are always used;

Thousand separators are used.

Example

See the AsText article in the Others section.

NumberFormat
THREE_DECIMAL_PLACES

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/NumberFormat/NumberFormat-THREE-DECIMAL-PLACES
DOLLAR
THREE_DECIMAL_PLACES
TWO_DECIMAL_PLACES
THREE_DECIMAL_PLACES
Syntax

NumberFormat.THREE_DECIMAL_PLACES

Description

Used with AsText function to return a string expressing a number rounded down to three digits after the decimal point.

Example

See the AsText article in the Others section.

DOLLAR
TWO_DECIMAL_PLACES

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/NumberFormat/NumberFormat-TWO-DECIMAL-PLACES
DOLLAR
THREE_DECIMAL_PLACES
TWO_DECIMAL_PLACES
TWO_DECIMAL_PLACES
Syntax

NumberFormat.TWO_DECIMAL_PLACES

Description

Used with AsText function to return a string expressing a number rounded down to two digits after the decimal point.

Example

See the AsText article in the Others section.

THREE_DECIMAL_PLACES
OptionClass

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/OptionClass
CALL
PUT
Option Class constants define the type of option to be used as an argument with the GetATMOption function.
Two constants are available:
CALL
PUT
CALL
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/OptionClass/OptionClass-CALL
CALL
PUT
CALL
Syntax

OptionClass.CALL

Description

Used with GetATMOption function to define the Call option.

Example

See the GetATMOption article in the Option Related section.

OptionClass
PUT

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/OptionClass/OptionClass-PUT
CALL
PUT
PUT
Syntax

OptionClass.PUT

Description

Used with GetATMOption function to define the Put option.

Example

See the GetATMOption article in the Option Related section.

CALL
OrderType

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/OrderType
BUY_AUTO
BUY_TO_CLOSE
BUY_TO_OPEN
SELL_AUTO
SELL_TO_CLOSE
SELL_TO_OPEN
In this section you will find information on the constants used in AddOrder function.
BUY_AUTO
BUY_TO_CLOSE
BUY_TO_OPEN
SELL_AUTO
SELL_TO_CLOSE
SELL_TO_OPEN
BUY_AUTO
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/OrderType/OrderType-BUY-AUTO
BUY_AUTO
BUY_TO_CLOSE
BUY_TO_OPEN
SELL_AUTO
SELL_TO_CLOSE
SELL_TO_OPEN
BUY_AUTO
Syntax

OrderType.BUY_AUTO

Description

Used in AddOrder function to add a buying order for entering a new long position or closing a short position. Note that you can switch order to Strategy Properties article for details.

Example

See the AddOrder article in the Others section.

OrderType
BUY_TO_CLOSE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/OrderType/OrderType-BUY-TO-CLOSE
BUY_AUTO
BUY_TO_CLOSE
BUY_TO_OPEN
SELL_AUTO
SELL_TO_CLOSE
SELL_TO_OPEN
BUY_TO_CLOSE
Syntax

OrderType.BUY_TO_CLOSE

Description

Used in addOrder function to add a buying order for closing a short position. Note that you can switch order to Strategy Properties article for details.

Example

See the AddOrder article in the Others section.

BUY_AUTO
BUY_TO_OPEN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/OrderType/OrderType-BUY-TO-OPEN
BUY_AUTO
BUY_TO_CLOSE
BUY_TO_OPEN
SELL_AUTO
SELL_TO_CLOSE
SELL_TO_OPEN
BUY_TO_OPEN
Syntax

OrderType.BUY_TO_OPEN

Description

Used in AddOrder function to add a buying order for entering a new long position. Note that you can switch order to Strategy Properties article for details.

Example

See the AddOrder article in the Others section.

BUY_TO_CLOSE
SELL_AUTO

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/OrderType/OrderType-SELL-AUTO
BUY_AUTO
BUY_TO_CLOSE
BUY_TO_OPEN
SELL_AUTO
SELL_TO_CLOSE
SELL_TO_OPEN
SELL_AUTO
Syntax

OrderType.SELL_AUTO

Description

Used in AddOrder function to add a selling order for entering a new short position or closing a long position. Note that you can switch order to Strategy Properties article for details.

Example

See the AddOrder article in the Others section.

BUY_TO_OPEN
SELL_TO_CLOSE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/OrderType/OrderType-SELL-TO-CLOSE
BUY_AUTO
BUY_TO_CLOSE
BUY_TO_OPEN
SELL_AUTO
SELL_TO_CLOSE
SELL_TO_OPEN
SELL_TO_CLOSE
Syntax

OrderType.SELL_TO_CLOSE

Description

Used in AddOrder function to add a selling order for closing a long position. Note that you can switch order to Strategy Properties article for details.

Example

See the AddOrder article in the Others section.

SELL_AUTO
SELL_TO_OPEN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/OrderType/OrderType-SELL-TO-OPEN
BUY_AUTO
BUY_TO_CLOSE
BUY_TO_OPEN
SELL_AUTO
SELL_TO_CLOSE
SELL_TO_OPEN
SELL_TO_OPEN
Syntax

OrderType.SELL_TO_OPEN

Description

Used in AddOrder function to add a selling order for entering a new short position. Note that you can switch order to Strategy Properties article for details.

Example

See the AddOrder article in the Others section.

SELL_TO_CLOSE
PaintingStrategy

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
The constants in this section define painting strategy styles.
Here is the list of the constants:
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
ARROW_DOWN
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-ARROW-DOWN
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
ARROW_DOWN
Syntax

PaintingStrategy.ARROW_DOWN

Description

Defines the arrow down painting strategy.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

PaintingStrategy
ARROW_UP

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-ARROW-UP
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
ARROW_UP
Syntax

PaintingStrategy.ARROW_UP

Description

Defines the arrow up painting strategy.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

ARROW_DOWN
BOOLEAN_ARROW_DOWN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-BOOLEAN-ARROW-DOWN
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
BOOLEAN_ARROW_DOWN
Syntax

PaintingStrategy.BOOLEAN_ARROW_DOWN

Description

Defines the boolean arrow down painting strategy. Boolean plots only have two values: true and false; the painting strategy is used to mark true values with down arrows above high prices of corresponding bars.  

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

ARROW_UP
BOOLEAN_ARROW_UP

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-BOOLEAN-ARROW-UP
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
BOOLEAN_ARROW_UP
Syntax

PaintingStrategy.BOOLEAN_ARROW_UP

Description

Defines the boolean arrow down painting strategy. Boolean plots only have two values: true and false; the painting strategy is used to mark true values with up arrows below low prices of corresponding bars.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

BOOLEAN_ARROW_DOWN
BOOLEAN_POINTS

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-BOOLEAN-POINTS
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
BOOLEAN_POINTS
Syntax

PaintingStrategy.BOOLEAN_POINTS

Description

Defines the boolean points painting strategy. It supposes that a plot computes logical values and only true values are displayed as points at the current closing price.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

BOOLEAN_ARROW_UP
BOOLEAN_WEDGE_DOWN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-BOOLEAN-WEDGE-DOWN
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
BOOLEAN_WEDGE_DOWN
Syntax

PaintingStrategy.BOOLEAN_WEDGE_DOWN

Description

Defines the boolean wedge down painting strategy. Boolean plots only have two values: true and false; the painting strategy is used to mark true values with down wedges below low prices of corresponding bars.

Sample
Example

See the SetPaintingStrategy function in the Look and Feel section.

BOOLEAN_POINTS
BOOLEAN_WEDGE_UP

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-BOOLEAN-WEDGE-UP
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
BOOLEAN_WEDGE_UP
Syntax

PaintingStrategy.BOOLEAN_WEDGE_UP

Description

Defines the boolean wedge up painting strategy. Boolean plots only have two values: true and false; the painting strategy is used to mark true values with up wedges above high prices of corresponding bars.

Sample
Example

See the SetPaintingStrategy function in the Look and Feel section.

BOOLEAN_WEDGE_DOWN
DASHES

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-DASHES
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
DASHES
Syntax

PaintingStrategy.DASHES

Description

Defines the dashes painting strategy.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

BOOLEAN_WEDGE_UP
HISTOGRAM

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-HISTOGRAM
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
HISTOGRAM
Syntax

PaintingStrategy.HISTOGRAM

Description

Defines the histogram painting strategy.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

DASHES
HORIZONTAL

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-HORIZONTAL
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
HORIZONTAL
Syntax

PaintingStrategy.HORIZONTAL

Description

Defines the painting strategy with long segments forming a continuous line when the study has the same value for adjacent bars.

Sample

Example

This painting strategy is used to draw Point of Control, Value Area High, Value Area Low, Profile High, and Profile Low plots by profile studies (TPOProfile, VolumeProfile, MonkeyBars).

HISTOGRAM
LINE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-LINE
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
LINE
Syntax

PaintingStrategy.LINE

Description

Defines the line painting strategy.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

HORIZONTAL
LINE_VS_POINTS

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-LINE-VS-POINTS
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
LINE_VS_POINTS
Syntax

PaintingStrategy.LINE_VS_POINTS

Description

Defines the line and points painting strategy.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

LINE
LINE_VS_SQUARES

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-LINE-VS-SQUARES
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
LINE_VS_SQUARES
Syntax

PaintingStrategy.LINE_VS_SQUARES

Description

Defines the line and squares painting strategy.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

LINE_VS_POINTS
LINE_VS_TRIANGLES

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-LINE-VS-TRIANGLES
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
LINE_VS_TRIANGLES
Syntax

PaintingStrategy.LINE_VS_TRIANGLES

Description

Defines the line and triangles painting strategy.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

LINE_VS_SQUARES
POINTS

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-POINTS
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
POINTS
Syntax

PaintingStrategy.POINTS

Description

Defines the points painting strategy.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

LINE_VS_TRIANGLES
SQUARED_HISTOGRAM

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-SQUARED-HISTOGRAM
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
SQUARED_HISTOGRAM
Syntax

PaintingStrategy.SQUARED_HISTOGRAM

Description

Defines the painting strategy where study values are represented as a histogram with wide columns. Unlike the basic HISTOGRAM painting strategy, its adjacent columns are not divided.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

POINTS
SQUARES

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-SQUARES
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
SQUARES
Syntax

PaintingStrategy.SQUARES

Description

Defines the painting strategy with squares marking study values.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

SQUARED_HISTOGRAM
TRIANGLES

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-TRIANGLES
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
TRIANGLES
Syntax

PaintingStrategy.TRIANGLES

Description

Defines the painting strategy with triangles marking study values.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

SQUARES
VALUES_ABOVE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-VALUES-ABOVE
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
VALUES_ABOVE
Syntax

PaintingStrategy.VALUES_ABOVE

Description

Defines a painting strategy which draws numeric plot values above the current high price. For more information about the constant, see the SequenceCounter study definition.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

TRIANGLES
VALUES_BELOW

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PaintingStrategy/PaintingStrategy-VALUES-BELOW
ARROW_DOWN
ARROW_UP
BOOLEAN_ARROW_DOWN
BOOLEAN_ARROW_UP
BOOLEAN_POINTS
BOOLEAN_WEDGE_DOWN
BOOLEAN_WEDGE_UP
DASHES
HISTOGRAM
HORIZONTAL
LINE
LINE_VS_POINTS
LINE_VS_SQUARES
LINE_VS_TRIANGLES
POINTS
SQUARED_HISTOGRAM
SQUARES
TRIANGLES
VALUES_ABOVE
VALUES_BELOW
VALUES_BELOW
Syntax

PaintingStrategy.VALUES_BELOW

Description

Defines a painting strategy which draws numeric plot values below the current low price. For more information about the constant, see the Sequence Counter study definition.

Sample

Example

See the SetPaintingStrategy function in the Look and Feel section.

VALUES_ABOVE
PricePerRow

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PricePerRow
AUTOMATIC
TICKSIZE
The constants described in this section are used in combination with the profile functions to define a price range.
Choose a constant from the list:
AUTOMATIC
TICKSIZE
AUTOMATIC
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PricePerRow/PricePerRow-AUTOMATIC
AUTOMATIC
TICKSIZE
AUTOMATIC
Syntax

PricePerRow.AUTOMATIC

Description

Defines the "height" (price range) of each row of the profile. When this constant is specified, the height of a row is computed to have a total number of rows equal to 50 for Monkey Bars and 85 for others.

Note that this constant can only be used in conjunction with the Profile functions.

PricePerRow
TICKSIZE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PricePerRow/PricePerRow-TICKSIZE
AUTOMATIC
TICKSIZE
TICKSIZE
Syntax

PricePerRow.TICKSIZE

Description

Defines the "height" (price range) of each row of the profile. When this constant is specified, the height of a row is equal to the minimal price change for the current symbol.

Note that this constant can only be used in conjunction with the Profile functions.

AUTOMATIC
PriceType

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PriceType
ASK
BID
LAST
MARK
Used with Fundamental functions, the PriceType constants define which type of price for a fundamental value needs to be returned:
ASK
BID
LAST
MARK
ASK
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PriceType/PriceType-ASK
ASK
BID
LAST
MARK
ASK
Syntax

PriceType.ASK

Description

Use it with Fundamental functions to state that an ask price needs to be returned. Note that for non-Forex symbols, this price type is only supported on intraday charts with time interval not greater than 15 days.

Example
input priceType = PriceType.ASK;

plot AskPrice = open(priceType = priceType);

By default, this script returns the open of ask price for the currently selected symbol, with the price type customizable via input parameters.

PriceType
BID

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PriceType/PriceType-BID
ASK
BID
LAST
MARK
BID
Syntax

PriceType.BID

Description

Use it with Fundamental functions to state that a bid price needs to be returned. Note that for non-Forex symbols, this price type is only supported on intraday charts with time interval not greater than 15 days.

Example
input priceType = PriceType.BID;

plot BidPrice = close(priceType = priceType);

By default, this script returns the close of bid price for the currently selected symbol, with the price type customizable via input parameters.

ASK
LAST

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PriceType/PriceType-LAST
ASK
BID
LAST
MARK
LAST
Syntax

PriceType.LAST

Description

Use it with Fundamental functions to state that a last price needs to be returned.

Example
input priceType = PriceType.LAST;

plot LastPrice = close(priceType = priceType);

By default, this script returns the close of last price of the currently selected symbol, with the price type customizable via input parameters.

BID
MARK

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/PriceType/PriceType-MARK
ASK
BID
LAST
MARK
MARK
Syntax

PriceType.MARK

Description

Use it with Fundamental functions to state that a mark price needs to be returned. Note that for non-Forex symbols, this price type is only supported on intraday charts with time interval not greater than 15 days.

Example
input priceType = PriceType.MARK;

plot MarkPrice = close(priceType = priceType);

By default, this script returns the close of mark price of the currently selected symbol, with the price type customizable via input parameters.

LAST
ProfitLossMode

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/ProfitLossMode
COST_BASIS
EXECUTION_PRICE
COST_BASIS
EXECUTION_PRICE
COST_BASIS
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/ProfitLossMode/ProfitLossMode-COST-BASIS
COST_BASIS
EXECUTION_PRICE
COST_BASIS
Syntax

ProfitLossMode.COST_BASIS

Description

The ProfitLossMode.COST_BASIS constant can be set as a value of the profitLossMode input parameter of the GetOpenPL function, in which case the Open Profit/Loss value is calculated as the difference between a position’s net liquidation value and cost basis times the position size. The value is calculated for positions on the specified symbol, for the currently selected account. Cost basis values are provided by Schwab and include the effects of commissions and tax elections.

ProfitLossMode
EXECUTION_PRICE

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/ProfitLossMode/ProfitLossMode-EXECUTION-PRICE
COST_BASIS
EXECUTION_PRICE
EXECUTION_PRICE
Syntax

ProfitLossMode.EXECUTION_PRICE

Description

The ProfitLossMode.EXECUTION_PRICE constant can be set as a value of the profitLossMode input parameter of the GetOpenPL function, in which case the Open Profit/Loss value is calculated as the difference between a position’s net liquidation value and execution price times the position size. The value is calculated for positions on the specified symbol, for the currently selected account.

COST_BASIS
Sound

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Sound
NoSound
Bell
Ding
Ring
Chimes
thinkscript® provides you with a set of constants for sounds. These can be used in combination with Alert constants to create alerts.
Choose a sound from the list:
NoSound
Bell
Ding
Ring
Chimes
NoSound
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Sound/Sound-Bell
NoSound
Bell
Ding
Ring
Chimes
Bell
Syntax

Sound.Bell

Description

Defines the bell sound constant.

Example

See the Alert function in the Others section.

NoSound
Ding

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Sound/Sound-Chimes
NoSound
Bell
Ding
Ring
Chimes
Chimes
Syntax

Sound.Chimes

Description

Defines the chimes sound constant.

Example

See the Alert function in the Others section.

Ring

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Sound/Sound-Ding
NoSound
Bell
Ding
Ring
Chimes
Ding
Syntax

Sound.Ding

Description

Defines the ding sound constant.

Example

See the Alert function in the Others section.

Bell
Ring

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Sound/Sound-NoSound
NoSound
Bell
Ding
Ring
Chimes
NoSound
Syntax

Sound.NoSound

Description

Defines the no sound constant.

Example

See the Alert function in the Others section.

Sound
Bell

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Constants/Sound/Sound-Ring
NoSound
Bell
Ding
Ring
Chimes
Ring
Syntax

Sound.Ring

Description

Defines the ring sound constant.

Example

See the Alert function in the Others section.

Ding
Chimes

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Data-Types
Any
boolean
CustomColor
double
IDataHolder
int
String
Symbol
Data Conversion
The data type for variables is automatically defined after assignment while functions accept arguments of specific data types as parameters, reducing runtime errors and ensuring consistent data usage.
Here is the full list of available data types:
Any
boolean
CustomColor
double
IDataHolder
int
String
Symbol
Any
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Data-Types/Any
Any
boolean
CustomColor
double
IDataHolder
int
String
Symbol
Data Conversion
Any
Description

Value of any data type from this section, except for CustomColor.

boolean

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Data-Types/CustomColor
Any
boolean
CustomColor
double
IDataHolder
int
String
Symbol
Data Conversion
CustomColor
Description

Color value, for example, Color.RED.

boolean
double

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Data-Types/Data-Conversion
Any
boolean
CustomColor
double
IDataHolder
int
String
Symbol
Data Conversion
Data Conversion
Argument	Data Accepted	Conversion Rule
Any	boolean, double, IDataHolder, int, String	-
boolean	double, IDataHolder, int	0 (0.0) and Double.NaN are converted to no (false), other numbers to yes (true).
CustomColor	-	-
double	boolean, IDataHolder, int	yes is converted to 1.0, no to 0.0.
IDataHolder	boolean, double, int	A number is converted to an array whose elements are all equal to that number. Logical values are preliminary converted to numerical.
int	boolean, double, IDataHolder	yes is converted to 1, no to 0. Non-integer numbers are rounded towards zero.
String	Symbol	
-
Symbol
	String	
-
Symbol
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Data-Types/IDataHolder
Any
boolean
CustomColor
double
IDataHolder
int
String
Symbol
Data Conversion
IDataHolder
Description

An array of data, consisting of floating point values, for example, close or volume.

double
int

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Data-Types/String
Any
boolean
CustomColor
double
IDataHolder
int
String
Symbol
Data Conversion
String
Description

A string of text, for example, "TEXT". Double quotes are used to mark text constants.

int
Symbol

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Data-Types/Symbol
Any
boolean
CustomColor
double
IDataHolder
int
String
Symbol
Data Conversion
Symbol
Description

Note: symbols need to be specified using double quotes.

String
Data Conversion

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Data-Types/boolean
Any
boolean
CustomColor
double
IDataHolder
int
String
Symbol
Data Conversion
boolean
Description

Logical value - true (yes) or false (no).

Any
CustomColor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Data-Types/double
Any
boolean
CustomColor
double
IDataHolder
int
String
Symbol
Data Conversion
double
Description

A floating point number, for example 1.5.

Note that you can drop the zero integer part and start the notation from the radix point. For example, 0.02 can also be written as .02.

CustomColor
IDataHolder

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Data-Types/int
Any
boolean
CustomColor
double
IDataHolder
int
String
Symbol
Data Conversion
int
Description

An integer number, for example 5.

IDataHolder
String

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Declarations
hide_on_daily
hide_on_intraday
lower
on_volume
once_per_bar
real_size
upper
weak_volume_dependency
zerobase
The section contains the following declarations:
hide_on_daily
hide_on_intraday
lower
on_volume
once_per_bar
real_size
upper
weak_volume_dependency
zerobase
hide_on_daily
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Declarations/hide-on-daily
hide_on_daily
hide_on_intraday
lower
on_volume
once_per_bar
real_size
upper
weak_volume_dependency
zerobase
hide_on_daily
Syntax

declare hide_on_daily;

Description

Hides a study on charts with aggregation periods equal to or greater than 1 day.

Example
declare hide_on_daily;

plot SMA = average(close);
SMA.AssignValueColor(GetColor(secondsFromTime(0) / 3600));

This study plots SMA of Close price and assigns a different color to the plot each hour. Due to declaration, this study will be hidden on daily charts.

hide_on_intraday

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Declarations/hide-on-intraday
hide_on_daily
hide_on_intraday
lower
on_volume
once_per_bar
real_size
upper
weak_volume_dependency
zerobase
hide_on_intraday
Syntax

declare hide_on_intraday;

Description

Hides a study on intraday charts (time charts with aggregation period less than 1 day and tick charts).

Example
declare hide_on_intraday;

declare lower;

plot OpenInterest = open_interest();

As open interest is only available for aggregations greater than or equal to 1 day, you can use the declaration so studies that use it are automatically hidden on intraday charts.

hide_on_daily
lower

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Declarations/lower
hide_on_daily
hide_on_intraday
lower
on_volume
once_per_bar
real_size
upper
weak_volume_dependency
zerobase
lower
Syntax

declare lower;

Description

Places a study on the lower subgraph. This declaration is used when your study uses values that are considerably lower or higher than price history or volume values.

Example (Price Oscillator)
declare lower;

input price = close;
input fastLength = 9;
input slowLength = 18;

plot PriceOsc = Average(price, fastLength) - Average(price, slowLength);

The example plots the difference between the two average values calculated on 9 and 18-bar intervals. The result value is lower compared to the price value. Therefore, it is reasonable to put the plot on the lower subgraph to avoid scaling the main chart.

hide_on_intraday
on_volume

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Declarations/on-volume
hide_on_daily
hide_on_intraday
lower
on_volume
once_per_bar
real_size
upper
weak_volume_dependency
zerobase
on_volume
Syntax

declare on_volume;

Description

Places a plot on the volume subgraph.

General Information

By default, the application automatically defines where to place a study. If the study contains volume values and values not related to the base subgraph, then this study is displayed on the volume subgraph, otherwise it is displayed on the base subgraph.

However, it may be required to forcibly place the study on the volume subgraph regardless of the values you are using.

Example (Volume Accumulation on the Volume Subgraph)
declare on_volume;
plot VolumeAccumulation = (close - (high + low) / 2) * volume;

The code in the example contains both volume and base subgraph related values. In order to place the study on the volume subgraph, the code uses the on_volume declaration. To study an example that uses only non-volume values, see the real_size function article.

lower
once_per_bar

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Declarations/once-per-bar
hide_on_daily
hide_on_intraday
lower
on_volume
once_per_bar
real_size
upper
weak_volume_dependency
zerobase
once_per_bar
Syntax

declare once_per_bar;

Description

Changes the recalculation mode of a study. By default, last study values are recalculated after each tick. If this declaration is applied, the study is forced to recalculate the last values only once per bar. This declaration can be used to reduce CPU usage for studies which do not need to be recalculated per each tick.

Example
declare once_per_bar;
input time = 0930;
AddVerticalLine(secondsFromTime(time)[1] < 0 && secondsFromTime(time) >= 0, time);

This study plots a vertical line between the bars created before and after the specified time in the EST time zone. Since the creation time for bars is fixed, there is no need to recalculate the study after each tick.

on_volume
real_size

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Declarations/real-size
hide_on_daily
hide_on_intraday
lower
on_volume
once_per_bar
real_size
upper
weak_volume_dependency
zerobase
real_size
Syntax

declare real_size;

Description

The real_size declaration is used in scripts of lower studies so that, when superimposed, they all employ a single scale marked off in absolute units. This can be useful if percentage view isn't desired for some reason. Note that real_size needs to be declared for all studies you are going to superimpose, otherwise the percentage view will be used.

Example
declare lower;

declare real_size;

input length = 14;

input averageType = AverageType.WILDERS;

plot ADX = DMI(length, averageType).ADX;

A customized version of the ADX technical indicator that uses the real_size declaration.

once_per_bar
upper

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Declarations/upper
hide_on_daily
hide_on_intraday
lower
on_volume
once_per_bar
real_size
upper
weak_volume_dependency
zerobase
upper
Syntax

declare upper;

Description

Enables you to place a study either on the base subgraph or on the volume subgraph. Note that a study is placed on the volume subgraph in case only volume values are used in the study. This declaration is applied by default to all studies not containing the lower and on_volume declarations.

Example (Price Oscillator)
declare upper;

input price = close;
input length = 9;

plot AvgWtd = wma(price, length);

In this example, the upper declaration places the weighted moving average plot on the main chart.

real_size
weak_volume_dependency

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Declarations/weak-volume-dependency
hide_on_daily
hide_on_intraday
lower
on_volume
once_per_bar
real_size
upper
weak_volume_dependency
zerobase
weak_volume_dependency
Syntax

declare weak_volume_dependency;

Description

Places a study on the volume subgraph when at least one volume value is used.

Example (Keltner Channels)
declare weak_volume_dependency;

input factor = 1.5;
input length = 20;
input price = close;

def shift = factor * AvgTrueRange(high, close, low, length);
def average = Average(price, length);

plot Avg = average;
plot Upper_Band = average + shift;
plot Lower_Band = average - shift;

Consider you are analyzing data that contains both volume and base subgraph related values using the code provided above. You want to display the plot on the base subgraph except for cases when you use at least one volume value. For the latter case, you would like to use the volume subgraph. In order to implement the logics, you use the weak_volume_declaration. If you use the close price input in the code, the study will be displayed on the base subgraph. If you use the volume price input, then there is a weak volume dependency and the study will be displayed on the volume subgraph.

upper
zerobase

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Declarations/zerobase
hide_on_daily
hide_on_intraday
lower
on_volume
once_per_bar
real_size
upper
weak_volume_dependency
zerobase
zerobase
Syntax

declare zerobase;

Description

Sets the minimal value on a study axis to zero if there are no negative values in the study.

Example (Price Oscillator)
declare zerobase;
declare lower;
plot Vol = Volume;

In this example, the Vol plot contains no negative values. It is reasonable to set the minimum value on the study axis to zero using the zerobase declaration.

weak_volume_dependency

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
All the functions are spread among the following sections:
Fundamentals
Look and Feel — updated
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio — updated
Profiles
Stock Fundamentals
Others
Fundamentals
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Corporate-Actions
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
GetActualEarnings
GetDividend
GetEstimatedEarnings
GetEventOffset
GetSplitDenominator
GetSplitNumerator
HasConferenceCall
HasEarnings
Portfolio
Profiles
Stock Fundamentals
Others
Corporate Actions
This section contains functions related to corporate actions.
Here is the full list:
GetActualEarnings
GetDividend
GetEstimatedEarnings
GetEventOffset
GetSplitDenominator
GetSplitNumerator
HasConferenceCall
HasEarnings
Date and Time
GetActualEarnings
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Corporate-Actions/GetActualEarnings
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
GetActualEarnings
GetDividend
GetEstimatedEarnings
GetEventOffset
GetSplitDenominator
GetSplitNumerator
HasConferenceCall
HasEarnings
Portfolio
Profiles
Stock Fundamentals
Others
GetActualEarnings
GetActualEarnings ();    
Description

Returns actual earnings for the current symbol.

Example 1
declare lower;
def AECont = if IsNaN(GetActualEarnings()) then AECont [1] else GetActualEarnings();
plot DilutedEarnings = if AECont <> 0 then AECont else Double.NaN;

The example draws values of diluted earnings for the current symbol. Values between earnings are saved using the AECont variable.

Example 2
declare lower;
def AE = if IsNaN(GetActualEarnings()) then 0 else GetActualEarnings();
plot EPS_TTM = Sum(AE, 252);
def pe = close / EPS_TTM;
AddLabel(yes, "P/E Ratio: " + pe);

The code draws values of diluted earnings for approximately twelve months. Also it shows the current Price-Earnings Ratio in the chart label. Note that this example works only for daily charts because it uses an assumption that there are 252 daily bars in a year.

Corporate Actions
GetDividend

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Corporate-Actions/GetDividend
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
GetActualEarnings
GetDividend
GetEstimatedEarnings
GetEventOffset
GetSplitDenominator
GetSplitNumerator
HasConferenceCall
HasEarnings
Portfolio
Profiles
Stock Fundamentals
Others
GetDividend
GetDividend ();    
Description

Returns a dividend amount for the current symbol.

Example 1
declare lower;
def DCont = if IsNaN(GetDividend()) then DCont[1] else GetDividend();
plot Dividend = if DCont <> 0 then DCont else Double.NaN;

The example plots dividends for the current symbol on a separate subgraph. Values between different Ex-Dividend dates are saved using the DCont variable.

Example 2
declare lower;
def DCont = if IsNaN(GetDividend()) then DCont[1] else GetDividend();
plot DivA = if DCont <> 0 then DCont * 4 else Double.NaN;
def yield = DivA / close * 100;
AddLabel(yes, yield + "% Yield", DivA.TakeValueColor());

The example draws the annual dividend plot (considering that dividends are quarterly and they remain on the same level through the year). Also the code in this example defines a chart label that indicates the calculated dividend yield value in percentage and draws it using the same color as the main plot.

GetActualEarnings
GetEstimatedEarnings

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Corporate-Actions/GetEstimatedEarnings
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
GetActualEarnings
GetDividend
GetEstimatedEarnings
GetEventOffset
GetSplitDenominator
GetSplitNumerator
HasConferenceCall
HasEarnings
Portfolio
Profiles
Stock Fundamentals
Others
GetEstimatedEarnings
GetEstimatedEarnings ();    
Description

Returns estimate earnings for the current symbol.

Example
declare lower;
plot EstEarning = GetEstimatedEarnings();
EstEarning.SetPaintingStrategy(PaintingStrategy.POINTS);

The example draws estimated earnings for the current symbol as points on a separate subgraph.

GetDividend
GetEventOffset

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Corporate-Actions/GetEventOffset
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
GetActualEarnings
GetDividend
GetEstimatedEarnings
GetEventOffset
GetSplitDenominator
GetSplitNumerator
HasConferenceCall
HasEarnings
Portfolio
Profiles
Stock Fundamentals
Others
GetEventOffset
GetEventOffset ( int eventType , int numberOfEventsToSkip );    
Default values:
eventType: Events.DIVIDEND
numberOfEventsToSkip: 0
Description

Returns number of bars before an upcoming or after a past event. The eventType parameter uses an Events constant to specify the type of the event: conference call, dividend, split, or earnings announcement. The numberOfEventsToSkip parameter defines which event of the specified type should be used: negative values define the number of the event in retrospective order, other values define upcoming events with zero corresponding to the closest one. Note that the sign of the value returned by this function is opposite to that of the numberOfEventsToSkip parameter: positive values for negative numberOfEventsToSkip, negative for zero or positive numberOfEventsToSkip.

Input parameters
Parameter	Default value	Description
eventType	Events.DIVIVDEND	Defines the type of event since/until which bars are counted.
numberofEventsToSkip	0	If negative, defines number of a past event, otherwise, number of the upcoming one. Zero value corresponds to the closest upcoming event.
Example
AddChartBubble(
 HasConferenceCall(),
 high,
 "The last conference call was " + 
  GetEventOffset(Events.CONFERENCE_CALL, -1) + 
  " bars ago");

This example script displays a chart bubble indicating the number of bars since the most recent conference call.

GetEstimatedEarnings
GetSplitDenominator

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Corporate-Actions/GetSplitDenominator
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
GetActualEarnings
GetDividend
GetEstimatedEarnings
GetEventOffset
GetSplitDenominator
GetSplitNumerator
HasConferenceCall
HasEarnings
Portfolio
Profiles
Stock Fundamentals
Others
GetSplitDenominator
GetSplitDenominator ();    
Description

Returns the split denominator for the current symbol.

Example
AddVerticalLine(!IsNaN(GetSplitDenominator()), if GetSplitNumerator() > GetSplitDenominator()
    then "Split!"
    else "Reverse Split!", Color.GRAY);

The code draws a gray vertical line with the "Split!" or "Reverse Split!" label for days when a corresponding split took place. For more information, see the AddVerticalLine function.

GetEventOffset
GetSplitNumerator

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Corporate-Actions/GetSplitNumerator
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
GetActualEarnings
GetDividend
GetEstimatedEarnings
GetEventOffset
GetSplitDenominator
GetSplitNumerator
HasConferenceCall
HasEarnings
Portfolio
Profiles
Stock Fundamentals
Others
GetSplitNumerator
GetSplitNumerator ();    
Description

Returns a split numerator for the current symbol.

Example
declare lower;
input initialPosition = 100;
def position = CompoundValue(1, if !IsNaN(GetSplitDenominator())
       then position[1] * GetSplitNumerator() / GetSplitDenominator()
       else position[1], initialPosition);
plot CurrentPosition = position;

This example shows trader position changes taking into account the splits presented on the chart.

GetSplitDenominator
HasConferenceCall

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Corporate-Actions/HasConferenceCall
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
GetActualEarnings
GetDividend
GetEstimatedEarnings
GetEventOffset
GetSplitDenominator
GetSplitNumerator
HasConferenceCall
HasEarnings
Portfolio
Profiles
Stock Fundamentals
Others
HasConferenceCall
HasConferenceCall ();    
Description

Returns true if there is an earnings conference call, false - otherwise.

Example
plot ConfCall = HasConferenceCall();
ConfCall.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

The code draws a dot based on the close price when the current symbol has a conference call. For more information, see the PaintingStrategy.BOOLEAN_POINTS constant.

GetSplitNumerator
HasEarnings

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Corporate-Actions/HasEarnings
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
GetActualEarnings
GetDividend
GetEstimatedEarnings
GetEventOffset
GetSplitDenominator
GetSplitNumerator
HasConferenceCall
HasEarnings
Portfolio
Profiles
Stock Fundamentals
Others
HasEarnings
HasEarnings ( int type );    
Default values:
type: EarningTime.ANY
Description

Returns true if there are announced earnings, and false otherwise. Use an EarningTime constant to specify the time of announcement.

Input parameters
Parameter	Default value	Description
type	EarningTime.ANY	Defines the time of the earnings announcement: after market close, befor market open, or either.
Example
plot isBefore = HasEarnings(EarningTime.BEFORE_MARKET);
plot isAfter = HasEarnings(EarningTime.AFTER_MARKET);
plot isDuringOrUnspecified = HasEarnings() and !isBefore and !isAfter;
isBefore.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_UP);
isAfter.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_DOWN);
isDuringOrUnspecified.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

This example script marks announced earnings with an up arrow if they are expected before market open, down arrow if they are expected after market close, and a dot if they are expected during market trading hours or the time is not specified.

HasConferenceCall
Portfolio

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Date and Time
During analysis you often work with quote historical data. For this reason you will find useful the date and time functions featured in this section. For example, with the help of the functions you can draw the close plot for the last three years or draw the open plot for the first half of each year.
Here is the full list of the functions:
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Statistical
CountTradingDays
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/CountTradingDays
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
CountTradingDays
CountTradingDays ( int fromDate , int toDate );    
Description

Returns the number of trading days in the specified time period (including both starting and ending dates) for the current symbol. Note that fromDate and toDate parameters should be specified in the YYYYMMDD format.

Input parameters
Parameter	Default value	Description
fromDate	-	Defines the beginning date of the period, in the YYYYMMDD format.
toDate	-	Defines the end date of the period, in the YYYYMMDD format.
Example
def yearstart = GetYear() * 10000 + 101;
AddLabel(yes, CountTradingDays(yearstart, GetYYYYMMDD()) + " trading days since year start");

This script displays a chart label indicating the number of trading days from the first day of the year to the current day for the chosen symbol.

Date and Time
DaysFromDate

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/DaysFromDate
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
DaysFromDate
DaysFromDate ( IDataHolder fromDate );    
Description

Returns the number of days from the specified date. Note that the fromDate argument is specified in the EST timezone and has the YYYYMMDD format.

Input parameters
Parameter	Default value	Description
fromDate	-	Defines the date from which days are counted, in the YYYYMMDD format.
Example
input BeginDate = 20090101;

plot Price = if DaysFromDate(BeginDate) >= 0 and DaysFromDate(BeginDate) <= 50 then close else double.NaN;

This example script draws the close plot for bars in the 50 days interval starting from BeginDate.

CountTradingDays
DaysTillDate

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/DaysTillDate
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
DaysTillDate
DaysTillDate ( IDataHolder tillDate );    
Description

Returns the number of days till the specified date. Note that the tillDate argument is specified in the EST timezone and has the YYYYMMDD format.

Input parameters
Parameter	Default value	Description
tillDate	-	Defines the date until which days are counted, in the YYYYMMDD format.
Example
input EndDate = 20090101;

plot price = if DaysTillDate(EndDate) >= 0 and DaysTillDate(EndDate) <= 50 then close else double.NaN;

The example draws the close plot for bars in the 50 days interval ending on EndDate.

DaysFromDate
GetDay

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/GetDay
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetDay
GetDay ();    
Description

Returns the number of the current bar day in the CST timezone. The output is returned in the range from 1 through 365 (366 for leap years).

Example
plot Price = if GetDay() <= 100 then close else Double.NaN;

The code draws the close plot for the first 100 days of each year.

DaysTillDate
GetDayOfMonth

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/GetDayOfMonth
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetDayOfMonth
GetDayOfMonth ( int yyyyMmDd );    
Description

Returns number of day in the month based on the given YYYYMMDD parameter.

Input parameters
Parameter	Default value	Description
yyyyMmDd	-	Defines the day whose number is returned.
Example
input first_day = 10;
input last_day = 20;
plot Data = if GetDayofMonth(GetYyyyMmDd()) between first_day and last_day then close else double.NaN;

Displays the close price only for days of month falling into a specified interval.

GetDay
GetDayOfWeek

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/GetDayOfWeek
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetDayOfWeek
GetDayOfWeek ( int yyyyMmDd );    
Description

Returns the day of week based on the given YYYYMMDD parameter. The return value ranges from from 1 (Monday) to 7 (Sunday).

Input parameters
Parameter	Default value	Description
yyyyMmDd	-	Defines the day whose number is returned.
Example
declare hide_on_intraday;
input day_of_week = {default Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday};
AddChartBubble(GetDayofWeek(GetYYYYMMDD()) == day_of_week + 1, high, "Here it is");

Displays bubbles with text for a certain day of week.

GetDayOfMonth
GetLastDay

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/GetLastDay
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetLastDay
GetLastDay ();    
Description

Returns the number of the last bar day in the CST timezone. The output is returned in the range from 1 through 365 (366 for leap years).

Example
plot Price = if GetLastDay() == GetDay() and GetLastYear() == GetYear() then close else Double.NaN;

This example draws the close plot for the last bar day of the current year.

GetDayOfWeek
GetLastMonth

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/GetLastMonth
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetLastMonth
GetLastMonth ();    
Description

Returns the number of the last bar month in the CST timezone. The output is returned in the range from 1 through 12.

Example 1
plot Price = if GetLastMonth() == GetMonth() and GetLastYear() == GetYear()  then close else Double.NaN;

The example draws the close plot for the last month of the current year.

Example 2
plot Price = if GetLastMonth() == GetMonth() then open else Double.NaN;

This code draws the open plot for the last month of each year.

GetLastDay
GetLastWeek

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/GetLastWeek
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetLastWeek
GetLastWeek ();    
Description

Returns the number of the last bar week in the CST timezone. The output is returned in the range from 1 through 53.

Example
plot Price = if GetLastWeek() == GetWeek() and GetLastYear() == GetYear() then high else Double.NaN;

This example draws the high plot for the last week of the current year.

GetLastMonth
GetLastYear

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/GetLastYear
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetLastYear
GetLastYear ();    
Description

Returns the number of the last bar year in the CST timezone.

Example
plot Price = if GetLastYear() == GetYear() then close else Double.NaN;

The code draws the close plot for the current year.

GetLastWeek
GetMonth

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/GetMonth
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetMonth
GetMonth ();    
Description

Returns the number of the current bar month in the CST timezone. The output is returned in the range from 1 through 12.

Example
plot Price = if GetMonth() <= 6 then close else Double.NaN;

The example draws the close plot for the first half of each year.

GetLastYear
GetTime

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/GetTime
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetTime
GetTime ();    
Description

Returns the number of milliseconds since the epoch (January 1, 1970, 00:00:00 GMT).

Example
def isRollover = GetYYYYMMDD() != GetYYYYMMDD()[1];

def beforeStart = GetTime() < RegularTradingStart(GetYYYYMMDD());

def vol = if isRollover and beforeStart then volume else if beforeStart then vol[1] + volume else Double.NaN;

plot PreMarketVolume = vol;

On an intraday chart, this script will plot the cumulative pre-market volume for the charted symbol. 

GetMonth
GetWeek

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/GetWeek
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetWeek
GetWeek ();    
Description

Returns the number of the current bar week in the CST timezone. The output is returned in the range from 1 through 53.

Example
plot Price = if GetWeek() % 2 == 1 then close else Double.NaN;

The example draws the close plot for odd weeks of each year.

GetTime
GetYear

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/GetYYYYMMDD
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetYYYYMMDD
GetYYYYMMDD ();    
Description

Returns the date of the current bar in the YYYYMMDD format. This date corresponds to the day whose trading session contains the current bar. Note that on intraday charts, this date and the actual date might not be the same for Forex and Futures symbols.

Example
declare lower;
input endDate = 20100101;
def cond = GetYYYYMMDD() < endDate;
plot Price = if cond then close else Double.NaN;

This example plots closing price only when the date of the current bar is less than the one specified in the endDate input.

GetYear
RegularTradingEnd

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/GetYear
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetYear
GetYear ();    
Description

Returns the number of the current bar year in the CST timezone.

Example
plot Price = if GetYear() > GetLastYear() - 3 then open else Double.NaN;

The example draws the close plot for the last three years.

GetWeek
GetYYYYMMDD

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/RegularTradingEnd
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
RegularTradingEnd
RegularTradingEnd ( int yyyyMmDd );    
Description

Returns the number of milliseconds elapsed since the epoch (January 1, 1970, 00:00:00 GMT) till the end of the regular trading hours on a given day for the current symbol. The trading day is to be specified using the YYYYMMDD format. 

Input parameters
Parameter	Default value	Description
yyyyMmDd	-	Defines the trading day in the YYYYMMDD format.
Example

See the RegularTradingStart function example.

GetYYYYMMDD
RegularTradingStart

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/RegularTradingStart
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
RegularTradingStart
RegularTradingStart ( int yyyyMmDd );    
Description

Returns the number of milliseconds elapsed since the epoch (January 1, 1970, 00:00:00 GMT) till the start of the regular trading hours on a given day for the current symbol. The trading day is to be specified using the YYYYMMDD format.

Input parameters
Parameter	Default value	Description
yyyyMmDd	-	Defines the trading day in the YYYYMMDD format.
Example
def rth = (RegularTradingEnd(GetYYYYMMDD()) - RegularTradingStart(GetYYYYMMDD())) / AggregationPeriod.HOUR;
AddLabel(yes, "RTH duration (hrs): " + rth);

This example script displays a chart label with duration of a regular trading session in hours.

RegularTradingEnd
SecondsFromTime

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/SecondsFromTime
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
SecondsFromTime
SecondsFromTime ( int fromTime );    
Description

Returns the number of seconds from the specified time (24-hour clock notation) in the EST timezone. Note that this function always returns zero when chart's aggregation period is greater than or equal to 1 day.

Input parameters
Parameter	Default value	Description
fromTime	-	Defines time from which seconds are counted, in the HHMM format, 24-hour clock notation.
Example
input OpenTime = 0930;
input DurationHours = 1;

def durationSec = DurationHours * 60 * 60;
def secondsPassed = SecondsFromTime(OpenTime);

plot Price = if secondsPassed >= 0 and secondsPassed <= durationSec then close else  double.NaN;

The plot displays the close value based on the specified duration and the beginning in the EST timezone format.

RegularTradingStart
SecondsTillTime

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Date---Time/SecondsTillTime
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
CountTradingDays
DaysFromDate
DaysTillDate
GetDay
GetDayOfMonth
GetDayOfWeek
GetLastDay
GetLastMonth
GetLastWeek
GetLastYear
GetMonth
GetTime
GetWeek
GetYear
GetYYYYMMDD
RegularTradingEnd
RegularTradingStart
SecondsFromTime
SecondsTillTime
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
SecondsTillTime
SecondsTillTime ( int tillTime );    
Description

Returns the number of seconds till the specified time (24-hour clock notation) in the EST timezone. Note that this function always returns zero when chart's aggregation period is greater than or equal to 1 day.

Input parameters
Parameter	Default value	Description
tillTime	-	Defines time until which seconds are counted, in the HHMM format, 24-hour clock notation.
Example
input CloseTime = 1600;
input DurationHours = 1;

def durationSec = DurationHours * 60 * 60;
def secondsRemained = SecondsTillTime(closeTime);

plot Price = if secondsRemained >= 0 and secondsRemained <= durationSec then close else double.NaN;

This example draws the close plot based on the defined duration and through the specified time in EST.

SecondsFromTime
Corporate Actions

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Fundamentals
Here is the full list:
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
ask
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/ask
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
ask
Syntax

ask

Description

Example
plot spread = ask - bid;
AssignBackgroundColor(if spread < 0.05 then Color.GREEN else if spread < 0.25 then Color.YELLOW else Color.RED);

This example script is used as a custom quote. It calculates a bid-ask spread and assigns different colors according to its value.

Note that you cannot reference historical data using this function, e.g. ask[1] is an invalid expression.

Fundamentals
bid

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/bid
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
bid
Syntax

bid

Description

Example
plot "Diff, %" = round(100 * ((bid + ask) / 2 - close) / close, 2);
AssignBackgroundColor(if "Diff, %" > 0 then Color.UPTICK else if "Diff, %" < 0 then Color.DOWNTICK else Color.GRAY);

This example script is used as a custom quote. It calculates percentage difference between mark and last prices and assigns colors according to its sign.

Note that you cannot reference historical data using this function, e.g. bid[1] is an invalid expression.

ask
close

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/close
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
close
close ( Symbol symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

Returns the Close price for the specific symbol, aggregation period and price type. You can use both Aggregation Period constants and pre-defined string values (e.g. Day, 2 Days, Week, Month, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article.

Valid parameters for the price type are: LAST, ASK, BID, and MARK. Alternatively, you can use the PriceType constants.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the Close price is returned.
period	current aggregation	Defines aggregation period for which the Close price is returned.
priceType	current price type	Defines the type of price to be returned: Last, Ask, Bid, or Mark.
Example
declare lower;
		
input symbol = {default "IBM", "GOOG/3", "(2*IBM - GOOG/6 + GE)/2"} ;
plot PriceClose = close(symbol);

Draws the close plot of either IBM, GOOG divided by three, or a composite price consisting of IBM, GOOG, and GE. Each of the symbols can be selected in the Edit Studies dialog.

bid
high

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/high
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
high
high ( String symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

Returns the High price for the specific symbol, aggregation period and price type. You can use both Aggregation Period constants and pre-defined string values (e.g. Day, 2 Days, Week, Month, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article.

Valid parameters for the price type are: LAST, ASK, BID, and MARK. Alternatively, you can use the PriceType constants.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the High price is returned.
period	current aggregation	Defines aggregation period for which the High price is returned.
priceType	current price type	Defines the type of price to be returned: Last, Ask, Bid, or Mark.
Example
declare lower;
		
input symbol = "IBM";
plot PriceHigh = high(symbol);

This example script plots High price for IBM.

close
hl2

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/hl2
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
hl2
hl2 ( String symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

Returns (High + Low)/2. You can use both Aggregation Period constants and pre-defined string values (e.g. Day, 2 Days, Week, Month, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article.

Valid parameters for the price type are: LAST, ASK, BID, and MARK. Alternatively, you can use the PriceType constants.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the price is returned.
period	current aggregation	Defines aggregation period for which the price is returned.
priceType	current price type	Defines the type of price to be returned: Last, Ask, Bid, or Mark.
Example
declare lower;

input symbol = "IBM";        
input period = AggregationPeriod.WEEK;

plot MedianPrice = hl2(symbol, period);

This example script plots weekly median price for IBM.

high
hlc3

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/hlc3
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
hlc3
hlc3 ( String symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

Returns the typical price (arithmetical mean of High, Low, and Close price values) for the specific symbol, aggregation period and price type. You can use both Aggregation Period constants and pre-defined string values (e.g. Day, 2 Days, Week, Month, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article.

Valid parameters for the price type are: LAST, ASK, BID, and MARK. Alternatively, you can use the PriceType constants.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the typical price is returned.
period	current aggregation	Defines aggregation period for which the typical price is returned.
priceType	current price type	Defines the type of price to be returned: Last, Ask, Bid, or Mark.
Example
plot TypicalPrice = hlc3;

This example script draws the typical price plot.

hl2
imp_volatility

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/imp-volatility
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
imp_volatility
imp_volatility ( String symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

Returns the implied volatility for the specific symbol, aggregation period and price type. You can use both Aggregation Period constants and pre-defined string values (e.g. Day, 2 Days, Week, Month, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article.

Valid parameters for the price type are: LAST, ASK, BID, and MARK. Alternatively, you can use the PriceType constants.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the implied volatility is returned.
period	current aggregation	Defines aggregation period for which the implied volatility is returned.
priceType	current price type	Defines the type of price for which the implied volatility is returned: Last, Ask, Bid, or Mark.
Example
declare lower;
		
plot ImpliedVolatility = imp_volatility();

Draws the implied volatility plot for the current symbol.

hlc3
low

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/low
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
low
low ( String symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

Returns the Low price for the specific symbol, aggregation period and price type. You can use both Aggregation Period constants and pre-defined string values (e.g. Day, 2 Days, Week, Month, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article.

Valid parameters for the price type are: LAST, ASK, BID, and MARK. Alternatively, you can use the PriceType constants.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the Low price is returned.
period	current aggregation	Defines aggregation period for which the Low price is returned.
priceType	current price type	Defines the type of price to be returned: Last, Ask, Bid, or Mark.
Example
plot LowDaily = low(period = AggregationPeriod.DAY);
plot LowWeekly = low(period = AggregationPeriod.WEEK);
plot LowMonthly = low(period = AggregationPeriod.MONTH);

This example script draws daily, weekly, and monthly Low price plots for the current symbol.

imp_volatility
ohlc4

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/ohlc4
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
ohlc4
ohlc4 ( String symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

Returns the (Open + High + Low + Close)/4 value for the specific symbol, aggregation period and price type. You can use both Aggregation Period constants and pre-defined string values (e.g. Day, 2 Days, Week, Month, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article.

Valid parameters for the price type are: LAST, ASK, BID, and MARK. Alternatively, you can use the PriceType constants.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the price is returned.
period	current aggregation	Defines aggregation period for which the price is returned.
priceType	current price type	Defines the type of price to be returned: Last, Ask, Bid, or Mark.
Example
plot OHLCMean = ohlc4;

This example script plots the arithmetical mean of Open, High, Low and Close.

low
open

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/open
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
open
open ( String symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

Returns the Open price for the specific symbol, aggregation period and price type. You can use both Aggregation Period constants and pre-defined string values (e.g. Day, 2 Days, Week, Month, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article.

Valid parameters for the price type are: LAST, ASK, BID, and MARK. Alternatively, you can use the PriceType constants.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the Open price is returned.
period	current aggregation	Defines aggregation period for which the Open price is returned.
priceType	current price type	Defines the type of price to be returned: Last, Ask, Bid, or Mark.
Example
input symbol = "EUR/USD";
input period = AggregationPeriod.MONTH;
input price_type = {default "LAST", "BID", "ASK", "MARK"};
plot Data = open(symbol, period, price_type);

This example script plots daily Open price plot for EUR/USD with LAST price type.

ohlc4
open_interest

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/open-interest
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
open_interest
open_interest ( String symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

Returns the open interest value for the specific symbol, aggregation period and price type. You can use both Aggregation Period constants and pre-defined string values (e.g. Day, 2 Days, Week, Month, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article.

Valid parameters for the price type are: LAST, ASK, BID, and MARK. Alternatively, you can use the PriceType constants.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the open interest is returned.
period	current aggregation	Defines aggregation period for which the open interest is returned.
priceType	current price type	Defines the type of price for which the open interest is returned: Last, Ask, Bid, or Mark.
Example
declare lower;
		
plot OpenInterest = open_interest();

This example script draws the open interest plot for the current symbol.

open
tick_count

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/tick-count
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
tick_count
tick_count ( String symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

Returns the number of trades corresponding to an intraday bar. You can use both Aggregation Period constants and pre-defined string values (e.g., 1 min, 2 hours, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article. Note that this function is only supported on intraday charts, thus you cannot use aggregations greater than or equal to 1 Day.

Valid parameters for the price type are: LAST, ASK, BID, and MARK. Alternatively, you can use the PriceType constants.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input Parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the number of trades is returned.
period	current aggregation	Defines aggregation period for which the number of trades is returned. Only intraday aggregations are allowed.
priceType	current price type	The type of price to be taken into account. Choosing LAST will have the function return the number of trades, while choosing MARK, BID, or ASK will have it count changes in quotes of the corresponding price type.
Example
declare lower;

declare zerobase;

plot TradeCount = tick_count;

plot AvgTradeCount = Average(TradeCount, 50);

TradeCount.SetPaintingStrategy(PaintingStrategy.HISTOGRAM);

TradeCount.AssignValueColor(if TradeCount >= AvgTradeCount then Color.UPTICK else Color.DOWNTICK);

On an intraday chart, this script plots a histogram that represents the number of trades for each bar along with its simple moving average over 50 bars. If the number of trades is greater than its average, the histogram is displayed in uptick color; otherwise, the downtick color is used. 

open_interest
volume

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/volume
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
volume
volume ( String symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

Returns the volume value for the specific symbol, aggregation period and price type. You can use both Aggregation Period constants and pre-defined string values (e.g. Day, 2 Days, Week, Month, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article.

Valid parameters for the price type are: LAST, ASK, BID, and MARK. Alternatively, you can use the PriceType constants.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the volume is returned.
period	current aggregation	Defines aggregation period for which the volume is returned.
priceType	current price type	Defines the type of price for which the volume is returned: Last, Ask, Bid, or Mark.
Example
declare lower;
		
input divider = 1000000;
plot VolumeDivided = volume / divider;
VolumeDivided.SetPaintingStrategy(PaintingStrategy.HISTOGRAM);

This example script plots the histogram of volume value divided by a specified number. By default, the divider is equal to 1000000.

tick_count
vwap

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Fundamentals/vwap
Fundamentals
ask
bid
close
high
hl2
hlc3
imp_volatility
low
ohlc4
open
open_interest
tick_count
volume
vwap
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
vwap
vwap ( String symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

Returns the volume weighted average price value for the specific symbol, aggregation period and price type. You can use both Aggregation Period constants and pre-defined string values (e.g. Day, 2 Days, Week, Month, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article.

Valid parameters for the price type are: LAST, ASK, BID, and MARK. Alternatively, you can use the PriceType constants.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the VWAP is returned.
period	current aggregation	Defines aggregation period for which the VWAP is returned.
priceType	current price type	Defines the type of price for which the VWAP is returned: Last, Ask, Bid, or Mark.
Example
plot DailyVWAP = vwap(period = AggregationPeriod.DAY);
plot WeeklyVWAP = vwap(period = AggregationPeriod.WEEK);
plot MonthlyVWAP = vwap(period = AggregationPeriod.MONTH);

This example script plots daily, weekly, and monthly VolumeWeightedAveragePrice values for the current symbol.

volume
Look and Feel

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Look and Feel
The full set of the functions is provided in the following list:
AddChartBubble
AddCloud
AddLabel — updated
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Fundamentals
AddChartBubble
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/AddChartBubble
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddChartBubble
AddChartBubble ( boolean time condition , double price location , Any text , CustomColor color , boolean up );    
Default values:
color: Color.RED
up: Yes
Description

Adds a bubble with a text to the specified location when the specified condition is true.

Note that you can break down the text into several lines; this can be done using \n escape sequence (see Example 2 for details).

Input parameters
Parameter	Default value	Description
time condition	-	Defines condition upon which the bubble is displayed
price location	-	Defines price at which the tip of the bubble is displayed
text	-	Defines text to be displayed in the bubble
color	Color.RED	Defines color of the bubble
up	Yes	Defines whether the bubble should be displayed above the price location (otherwise it will be displayed below)
Example
input timeFrame = {default DAY, "2 DAYS", "3 DAYS", "4 DAYS", WEEK, MONTH, "OPT EXP"};
AddChartBubble(high == high(period = timeFrame), high, "High of " + timeFrame + ": " + high, Color.green, yes);
AddChartBubble(low == low(period = timeFrame), low, "Low of " + timeFrame + ": " + low, Color.green, no);

This example shows bubbles with values and a description on the selected time frame extremums.

Example 2 (Multiline Display)
AddChartBubble(GetYYYYMMDD() != GetYYYYMMDD()[1], high, "O: " + open(period = "DAY") + "\nChg: " + ( open(period = "DAY") - open(period = "DAY")[1] ), Color.PLUM, yes);

This example adds chart bubbles after rollover lines, which display daily Open price and its change since previous day's Open.

Look and Feel
AddCloud

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/AddCloud
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddCloud
AddCloud ( IDataHolder data1 , IDataHolder data2 , CustomColor color1 , CustomColor color2 );    
Default values:
color1: Color.YELLOW
color2: Color.RED
Description

Plots a translucent cloud bounded above and below by values data1 and data2. Areas where data1 is greater than data2 are assigned color1, others are filled with color2. By default, the cloud border is invisble: to make it visible, set the showBorder parameter value to yes. Note that AddCloud accepts both defined variables and plots as input parameters.

Input parameters
Parameter	Default value	Description
data1	-	Defines the first value for comparison.
data2	-	Defines the second value for comparison.
color1	Color.YELLOW	Defines color of sections where data1 is greater than data2.
color1	Color.RED	Defines color of sections where data1 is less than or equal to data2.

showBorder

	

no

	

Controls visibility of the cloud border.

Example 1
def OpenPrice = open;

def ClosePrice = close;

AddCloud(OpenPrice, ClosePrice, color.RED, color.GREEN, yes);

In this example, the AddCloud function draws a translucent cloud that highlights the difference between the values of OpenPrice and ClosePrice. Green cloud areas correspond to bull candles, while red areas correspond to bear candles. Even though the script contains no plots, the values of OpenPrice and ClosePrice are displayed as the cloud border.

Example 2
plot CurrentPrice = close;
plot PastPrice = close[10];
AddCloud(CurrentPrice, PastPrice, Color.VIOLET, Color.PINK);

In this example, the AddCloud draws the translucent "cloud" and paints it according to the following rule:

if CurrentPrice > PastPrice then the cloud is violet;
if CurrentPrice < PastPrice then the cloud is pink.

Note that the order in which the arguments appear in the AddCloud function affects the logics. For example, if you swap over the PastPrice and the CurrentPrice:

plot CurrentPrice = close;
plot PastPrice = close[10];
AddCloud(PastPrice, CurrentPrice, Color.VIOLET, Color.PINK);

the rule will be:

if PastPrice > CurrentPrice, then the cloud is violet;
if PastPrice < CurrentPrice, then the cloud is pink.
Example 3

Although AddCloud requires that both upper and lower boundaries be specified as plots or variables, it is possible to set those as infinity bounds so that certain chart areas are highlighted. Consider the following example:

def hiLevel = if close >= Average(close) then Double.POSITIVE_INFINITY else Double.NEGATIVE_INFINITY;

AddCloud(hiLevel, -hiLevel, Color.LIGHT_GREEN, Color.LIGHT_RED);

This script will display infinite vertical stripes on chart: green stripes where the close price is greater than or equal to its average, and red ones where it is less. 

AddChartBubble
AddLabel

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/AddLabel
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddLabel
AddLabel ( boolean visible , Any text , CustomColor color , int location , int size , boolean rowOwnership );    
Default values:
color: Color.RED
location: Location.TOP_LEFT
size: FontSize.SMALL
rowOwnership: no
Description

Adds a text label to the specified location on the chart. Note that you can also use this function to display some text in custom quotes (see example below).

You can use the optional rowOwnership parameter to make a label claim exclusive use of the row it is placed on. This is helpful when displaying important messages or banners that shouldn’t be crowded by other labels. When a label has rowOwnership = yes, no other label can appear in the same row, even if it shares the same location or font size. Other labels will be pushed to adjacent rows.

Note: When AddLabel() calls another function, e.g., AddLabel(yes, "GetDividend: " + GetDividend()); -- it only uses the value of that function at the last real bar. So in this example, if the last real bar does not contain any dividend announcement, the value will be N/A.

Tip: To avoid label overlap with chart elements like bubbles or bars, you can enable the Fit study markers option. Go to Chart settings, then Price axis, and check Fit study markers.

Input parameters
Parameter	Default value	Description
visible	-	Defines the condition upon which the label is displayed.
text	-	Defines the text to be displayed in the label.
color	Color.RED	Defines the color of the label. You can use a Color constant for this parameter.
location	Location.TOP_LEFT	Defines the location of the label. You can use a Location constant for this parameter.
size	FontSize.SMALL	Defines the font size of the label. You can use a FontSize constant for this parameter.

rowOwnership

	

no

	

If set to yes, this label claims ownership of the entire chart row. Other labels will be drawn on rows above or below. 

Example
def avgPrice = GetAveragePrice();
def trendUp = close > Average(close);

AddLabel(yes, "My Avg Price: " + avgPrice, if trendUp then Color.GREEN else Color.RED, location = Location.TOP_LEFT, size = FontSize.SMALL, rowOwnership = yes);

AddLabel(yes, if close > Average(close, 20) then "Uptrend" else "Downtrend", location = Location.TOP_RIGHT, size = FontSize.X_LARGE);

The first label shows My Avg Price: [value] in green or red depending on whether the current price is above or below the average close. This label uses the rowOwnership = yes parameter, which causes it to claim the entire row for itself. No other label can appear on the same row.

The second label displays "Uptrend" or "Downtrend" based on a 20-bar moving average. Because the first label owns its row, this label is automatically pushed to the next row below, even though both are set to the same location.  If used in Custom Quotes, the words "Uptrend" or "Downtrend" will appear in the quote cell based on the same condition.

AddCloud
AddVerticalLine

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/AddVerticalLine
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddVerticalLine
AddVerticalLine ( boolean visible , Any text , CustomColor color , int stroke );    
Default values:
text: ""
color: Color.RED
stroke: Curve.SHORT_DASH
Description

Adds a vertical line with specified text.

Input parameters
Parameter	Default value	Description
visible	-	Defines condition upon which the line is displayed.
text	" "	Defines text to be displayed next to the line.
color	Color.RED	Defines color of the line.
stroke	Curve.SHORT_DASH	Defines style of the line. Any of the Curve constants can be used for this parameter.
Example
input period = {WEEK, default MONTH};
AddVerticalLine((period == period.WEEK and GetWeek() <> GetWeek()[1]) or (period == period.MONTH and GetMonth() <> GetMonth()[1]), "", Color.ORANGE, curve.SHORT_DASH);

The code draws orange short-dashed vertical lines with a defined frequency.

AddLabel
AssignBackgroundColor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/AssignBackgroundColor
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AssignBackgroundColor
AssignBackgroundColor ( CustomColor color );    
Description

Sets a background color. Note that when used in script for a custom quote, this function sets the background color of the quote cell.

Input parameters
Parameter	Default value	Description
color	-	Defines color to be assigned to background.
Example
plot ADX = ADX();
AssignBackgroundColor(if ADX > 20 then Color.DARK_ORANGE else Color.BLACK);

When used in custom quotes, this script will paint the cell background dark orange when a possible trend is detected (ADX>20), and black otherwise. Note that the ADX value is calculated for the last real bar only, so that change will only be visible if the condition is met at the last real bar.

AddVerticalLine
AssignNormGradientColor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/AssignNormGradientColor
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AssignNormGradientColor
AssignNormGradientColor ( int length , CustomColor lowestColor , CustomColor highestColor );    
Description

Fills a plot with a gradient using the current, the lowest, and the highest values of the last length bars to define a specific color. If the current plot value is positive and the highest, then it is painted with the highestColor. If the current plot value is negative and the lowest, then it is painted with the lowestColor. The center color of the gradient is always situated on the zero level which means that the positive part of the plot uses the higher colors of the gradient, and the negative part uses the lower colors.

Note that Past Offset is not affected by length parameter as the function assigns length = 1 to the first bar and then gradually increases it to the specified value.

Input parameters
Parameter	Default value	Description
length	-	Defines the period upon which the highest and lowest values are found. This parameter can be expressed as a dynamic value.
lowestColor	-	Defines color corresponding to the lowest value.
highestColor	-	Defines color corresponding to the highest value.
Example
declare lower;
input colorNormLength = 14;
input fastLength = 9;
input slowLength = 18;
plot PriceOsc = Average(close, fastLength) - Average(close, slowLength);
PriceOsc.AssignNormGradientColor(colorNormLength, Color.LIGHT_RED, Color.YELLOW);

The example shows the Price Oscillator study which is a momentum study calculated as the difference between two moving averages. The biggest positive difference for the last colorNormLength is painted yellow, the smallest is painted light red. The rest of the values are painted using intermediate colors depending on how far they are located from the two extreme points.

AssignBackgroundColor
AssignPriceColor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/AssignPriceColor
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AssignPriceColor
AssignPriceColor ( CustomColor color );    
Input parameters
Parameter	Default value	Description
color	-	Defines color to be assigned to the price bar.
Description

Sets a color of the price bar.

Example
declare lower;

plot MFI = MoneyFlowIndex();
plot OverBought = 80;
plot OverSold = 20;

MFI.DefineColor("OverBought", Color.ORANGE);
MFI.DefineColor("OverSold", Color.BLUE);

OverBought.SetDefaultColor(Color.GRAY);
OverSold.SetDefaultColor(Color.GRAY);

AssignPriceColor(if MFI >= OverBought then MFI.color("OverBought") else if MFI <= OverSold then MFI.color("OverSold") else Color.CURRENT);

In this example price bars are colored depending on the MFI plot which refers to the MoneyFlowIndex study. If the MFI is greater or equals 80 then the price plot is colored orange, if the MFI is lower or equals 20 then it is colored blue. In the rest of cases the color will not change and will remain grey which is defined by the Color.CURRENT constant. In order to be able to change colors for the AssignPriceColor function without actually changing the code, the example refers to colors of the MFI plot.

Note that you cannot paint the same price bar using multiple studies simultaneously.

 

AssignNormGradientColor
AssignValueColor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/AssignValueColor
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AssignValueColor
AssignValueColor ( CustomColor color );    
Description

Paints intervals of a plot with desired colors depending on a condition. The specified colors override the default color set for the plot. Note that when used in script for a custom quote, this function sets the color of the quote value.

Input parameters
Parameter	Default value	Description
color	-	Defines color to be applied to the plot.
Example
plot Diff = close - close[1];
Diff.AssignValueColor(if Diff >= 0 then Color.UPTICK else Color.DOWNTICK);

In this example, if the difference between the current closing value and the closing value for the previous bar is positive, the Diff plot is painted green, otherwise it is painted red.

Colors can be specified in the following ways:

Note that you can change colors of a plot in the Edit Studies dialog only if you use the Color function to define these colors. In the rest of cases you can change the colors only by editing the source code of a study.

AssignPriceColor
Color

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/Color
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Color ( String name );    
Description

Gets a plot color using the title of the color. Note that the color should be defined using the DefineColor function.

Input parameters
Parameter	Default value	Description
name	-	Defines the name of the color.
Example
declare lower;
plot Price = close;
Price.DefineColor("Up", Color.UPTICK);
Price.DefineColor("Down", Color.DOWNTICK);
Price.AssignValueColor(if Price >= Price[1] then Price.Color("Up") else Price.Color("Down"));

The code paints the closing plot with "Up" and "Down" colors depending on the price change as compared to the previous bar.

AssignValueColor
CreateColor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/CreateColor
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
CreateColor
CreateColor ( double red , double green , double blue );    
Description

Generates a color based on its rgb code.

Input parameters
Parameter	Default value	Description
red	-	Defines color value on red scale.
green	-	Defines color value on green scale.
blue	-	Defines color value on blue scale.
Example
plot Price = close;
Price.SetDefaultColor(CreateColor(255, 220, 210));

This example paints the Price chart in color that has the 255, 220, 210 rgb code.

Color
DefineColor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/DefineColor
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
DefineColor
DefineColor ( String name , CustomColor color );    
Description

Defines a named color for a plot with the default color value. This color can be changed in the Edit Studies dialog.

Input parameters
Parameter	Default value	Description
name	-	Defines the name of the color.
color	-	Defines color to be used with specified name.
Example
declare lower;
input length = 12;
plot Momentum = close - close[length];
Momentum.DefineColor("Positive", Color.UPTICK);
Momentum.DefineColor("Negative", Color.DOWNTICK);
Momentum.AssignValueColor(if Momentum >= 0 then Momentum.Color("Positive") else Momentum.Color("Negative"));

This example paints the Momentum plot in different colors according to its trend. The DefineColor function defines Positive and Negative color names as aliases for Color.UPTICK and Color.DOWNTICK constants. You can change the colors in the Edit Studies dialog and their order is the same as in the source code. If the trend of the plot is positive then it is painted in Positive (Uptick) color. If the trend is negative, the plot is painted in Negative (Downtick) color.

Note that in order to refer to a specific color the code uses the Color function.

 

CreateColor
DefineGlobalColor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/DefineGlobalColor
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
DefineGlobalColor
DefineGlobalColor ( String name , CustomColor color );    
Description

Defines a named color for a plot with a default color value. This color can be changed in the menu.

Input parameters
Parameter	Default value	Description
name	-	Defines the name of the color.
color	-	Defines color to be used with specified name.
Example
DefineGlobalColor("Global1", CreateColor(128, 0, 128));
plot signal = high > Highest(high[1]);
plot NinetyPercent = 0.9*close;
signal.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_DOWN);
signal.SetDefaultColor(GlobalColor("Global1"));
NinetyPercent.SetDefaultColor(GlobalColor("Global1"));

This example defines and uses a global color. This color can be changed in the Globals sub-tab of the Study Properties.

DefineColor
EnableApproximation

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/EnableApproximation
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
EnableApproximation
EnableApproximation ();    
Description

Connects adjacent non-NaN values.

Example
plot ZZ = ZigZagSign();
ZZ.EnableApproximation();

The first line of the code defines the ZZ plot as a reference to the ZigZagSign plot. The second line enables the approximation for the plot in order to connect separate reversal points with lines.

DefineGlobalColor
GetColor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/GetColor
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetColor
GetColor ( int index );    
Default values:
index: 0
Description

Returns a color from the color palette. Note that colors in color palettes vary based on the Look and Feel you are using. Regardless of the current Look and Feel, the selection of colors in the palettes ensures optimal data visualization.

The following table lists the available colors for different look and feel settings.

Index

	

	

0	

 

 

 

	

1	

	

2	

	

3	

	

4	

	

5	

	

6	

	

 

7	

	

8	

	

9	

	

Calling GetColor with any index outside of this range is equal to calling GetColor(AbsValue(index) % 10), that is, the same 10 colors are repeated in a cycle.

Input parameters
Parameter	Default value	Description
index	-	Defines the number of the color from the predefined palette.
Example
input length = 12;
plot SMA = SimpleMovingAvg(close, length);
plot EMA = MovAvgExponential(close, length);

SMA.SetDefaultColor(GetColor(1));
EMA.SetDefaultColor(GetColor(5));

This script plots two lines: the 12 period simple moving average and the exponential moving average of the Close price using colors 1 and 5 from the predefined palette, respectively.

EnableApproximation
GlobalColor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/GlobalColor
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GlobalColor
GlobalColor ( String name );    
Description

Gets a plot color by name. The color should be defined by the plot.DefineColor(name, color) statement.

Input parameters
Parameter	Default value	Description
name	-	Defines the name of the color.
Example

See the DefineGlobalColor function example.

GetColor
Hide

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/Hide
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Hide
Hide ();    
Description

Makes a plot hidden by default. This function may be required to hide plot data that is not used in the analysis at the moment.

Example
plot PriceClose = close;
plot PriceOpen = open;
PriceOpen.Hide();

This example makes the PriceOpen plot invisible by default.

GlobalColor
HideBubble

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/HideBubble
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
HideBubble
HideBubble ();    
Description

Makes the last value bubble of a plot invisible.

Example
plot Data = volume;
Data.HideBubble();

The example hides the last value bubble of the Data plot.

Hide
HidePricePlot

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/HidePricePlot
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
HidePricePlot
HidePricePlot ( double hide price );    
Default values:
hide price: Yes
Description

Hides the price plot for the current symbol if the Boolean condition value is yes.

Input parameters
Parameter	Default value	Description
hide price	yes	Defines condition upon which the price plot is hidden.
Example
plot closeOnly = close;
HidePricePlot(yes);

The example code solely displays the Close price plot.

HideBubble
HideTitle

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/HideTitle
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
HideTitle
HideTitle ();    
Description

Removes the plot value from the graph title.

Example
declare lower;

plot PriceOsc = Average(close, 9) - Average(close, 18);
plot PriceOscLine = PriceOsc;
plot ZeroLine = 0;

PriceOsc.SetDefaultColor(Color.VIOLET);
PriceOsc.SetPaintingStrategy(PaintingStrategy.HISTOGRAM);
PriceOscLine.SetDefaultColor(Color.LIGHT_GRAY);
PriceOscLine.HideTitle(); 
ZeroLine.SetDefaultColor(Color.PINK);
ZeroLine.HideTitle();

The example draws the Price Oscillator study consisting of two plots - a histogram and line. The HideTitle function is used to deallocate equal values of PriceOsc and PriceOscLine plots and a permanent zero value for the ZeroLine plot from the status string.

HidePricePlot
SetChartType

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/SetChartType
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
SetChartType
SetChartType ( double chart type );    
Description

Sets a desirable non-Monkey chart type directly from the script. Note that you can also set the chart type along with its color settings within the Chart Settings window, for more information on that, see the Appearance Settings article.

Input parameters
Parameter	Default value	Description
chart type	-	Defines chart type to be set: Area, Bar, Candle, Candle Trend, Heikin Ashi, or Line. This parameter accepts ChartType constants as value.
Example
plot price = close;
SetChartType(ChartType.AREA);

This code sets the Area chart type and outlines it with the Close price plot.

HideTitle
SetDefaultColor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/SetDefaultColor
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
SetDefaultColor
SetDefaultColor ( CustomColor color );    
Description

Sets the default color of a plot. This setting affects the color of the plot when the study is first initialized or added to the chart.

Input parameters
Parameter	Default value	Description
color	-	Defines the default plot color.
Example
plot Data = close;
Data.SetDefaultColor(Color.RED);

The example sets the default color of the Data plot to red.

SetChartType
SetHiding

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/SetHiding
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
SetHiding
SetHiding ( double condition );    
Description

Controls visibility of a plot depending on a condition. If this condition is true, the plot is hidden; otherwise the plot is visible.

Input parameters
Parameter	Default value	Description
condition	-	Defines condition upon which the plot is hidden.
Example
plot DailyClose = close(period = AggregationPeriod.DAY);
plot WeeklyClose = close(period = AggregationPeriod.WEEK);
plot MonthlyClose = close(period = AggregationPeriod.MONTH);

DailyClose.SetHiding(GetAggregationPeriod() >= AggregationPeriod.DAY);
WeeklyClose.SetHiding(GetAggregationPeriod() >= AggregationPeriod.WEEK);
MonthlyClose.SetHiding(GetAggregationPeriod() >= AggregationPeriod.MONTH);

Note that if a Boolean function is used as a condition, only its value at the last real bar is taken into account.

SetDefaultColor
SetLineWeight

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/SetLineWeight
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
SetLineWeight
SetLineWeight ( int lineWeight );    
Description

Sets a weight of a line.

Input parameters
Parameter	Default value	Description
lineWeight	-	Defines the line weight in pixels.
Example
plot Price = close;
Price.SetLineWeight(5);

This code sets the weight of a line to 5. The value is measured in pixels and ranges from 1 to 5 inclusively.

SetHiding
SetPaintingStrategy

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/SetPaintingStrategy
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
SetPaintingStrategy
SetPaintingStrategy ( int paintingStrategy );    
Description

Input parameters
Parameter	Default value	Description
paintingStrategy	-	Defines painting style of the line with PaintingStrategy constants.
Example
plot Data = open;
Data.SetPaintingStrategy(PaintingStrategy.HISTOGRAM);

In this example, the painting style of the Data plot is a histogram.

SetLineWeight
SetStyle

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/SetStyle
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
SetStyle
SetStyle ( int curve );    
Description

Controls a style of a curve.

Input parameters
Parameter	Default value	Description
curve	Curve.SHORT_DASH	Defines style of the line. Any of the Curve constants can be used for this parameter.
Example
plot Data = low;
Data.SetStyle(Curve.SHORT_DASH);

This example script draws the Low price plot using a short-dashed curve.

SetPaintingStrategy
TakeValueColor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Look---Feel/TakeValueColor
Fundamentals
Look and Feel
AddChartBubble
AddCloud
AddLabel
AddVerticalLine
AssignBackgroundColor
AssignNormGradientColor
AssignPriceColor
AssignValueColor
CreateColor
DefineColor
DefineGlobalColor
EnableApproximation
GetColor
GlobalColor
Hide
HideBubble
HidePricePlot
HideTitle
SetChartType
SetDefaultColor
SetHiding
SetLineWeight
SetPaintingStrategy
SetStyle
TakeValueColor
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
TakeValueColor
TakeValueColor ();    
Description

Returns the color of the current bar.

Example
input price = close;
input length = 12;
plot Avg = Average(price, length);
AddChartBubble(Avg == HighestAll(Avg), Avg, "Max. Average", Avg.TakeValueColor());

In this example, the TakeValueColor is called to ensure that the bubble is the same color as the SMA plot.

SetStyle
Option Related

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Mathematical and Trigonometric
As appears from the section title, this section collects mathematical and trigonometric functions. Besides traditional functions such as sine, cosine, or logarithm, the section also contains some more specific ones. For example, it has the isNaN function that defines if a parameter is a number, or the Round function that rounds a value to a certain number of digits.
Find all the functions in the following list:
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
AbsValue
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/ACos
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
ACos
ACos ( double value );    
Description

Returns the arc cosine of a value in the range from 0 through pi.

Input parameters
Parameter	Default value	Description
value	-	Defines argument whose arc cosine is returned. Values for this argument must be in the [-1;1] range.
Example
declare lower;
plot Data = Acos(0.5) == Double.Pi / 3;

The expression in the second line of code compares two values and draws a plot. If the two values are equal, it draws the unit (true) plot . Otherwise, it draws the zero (false) plot. The arc cosine of 0.5 equals pi/3. So the example draws the unit plot.

AbsValue
ASin

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/ASin
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
ASin
ASin ( double value );    
Description

Returns the arc sine of a value in the range from -pi/2 through pi/2.

Input parameters
Parameter	Default value	Description
value	-	Defines argument whose arc sine is returned. Values for this argument must be in the [-1;1] range.
Example 1
declare lower;
plot Data = Asin(0.5) == Double.Pi / 3;

Similar to the ACos example, the code above compares two values and draws the unit (true) plot if they are equal. If the values are not equal, the zero (false) plot is drawn. As the arc sine of 0.5 is not equal pi/3, the example script draws the zero plot.

Example 2
declare lower;
input length = 3;
def height = close - close[length];
def hypotenuse = Sqrt( Sqr(length) + Sqr(height) );
plot "Angle, deg" = ASin(height/hypotenuse) * 180 / Double.Pi;

The code draws a line that connects the current close value with the close value on the desired bar in the past. The Asin function is used to calculate the angle of slope of the line.

ACos
ATan

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/ATan
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
ATan
ATan ( double value );    
Description

Returns the arc tangent of an angle in the range of -pi/2 through pi/2.

Input parameters
Parameter	Default value	Description
value	-	Defines argument whose arc tangent is returned.
Example
declare lower;
input length = 3;
def avg = Average(close, length);
def height = avg - avg[length];
plot "Angle, deg" = ATan(height/length) * 180 / Double.Pi;

The code calculates the angle of slope of the simple moving average with the given length. The angle itself is calculated using the ATan function.

ASin
Ceil

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/AbsValue
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AbsValue
AbsValue ( double value );    
Description

Returns the absolute value of an argument. If the argument is positive, the argument is returned. If the argument is negative, the negation of the argument is returned.

Input parameters
Parameter	Default value	Description
value	-	Defines argument whose absolute value is returned.
Example
declare lower;
plot Absolute = AbsValue(open - close);

The example plots the absolute value of difference between the open and close price which can be either positive, or negative.

Mathematical and Trigonometric
ACos

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Ceil
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Ceil
Ceil ( double value );    
Description

Rounds a value up to the nearest integer (which is not less than the value).

Input parameters
Parameter	Default value	Description
value	-	Defines value to round up.
Example
plot data = Ceil(close);

The example returns the integer that is equal to or next higher than the close price.

ATan
Cos

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Cos
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Cos
Cos ( double angle );    
Description

Returns the trigonometric cosine of an angle.

Input parameters
Parameter	Default value	Description
angle	-	Defines angle (in radians) whose cosine is calculated.
Example
declare lower;
input a = 0;
input b = 10;
input periodBars = 20;
def w = 2 * Double.Pi / periodBars;
def x = CompoundValue(1, x[1] + 1, 0);
plot F = a + b * Cos(w * x);

The code draws the cosine function depending on a variable which starts from one and increments by one on each bar. The cyclic frequency(w) is calculated based on the periodBars input.

Ceil
Crosses

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Crosses
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Crosses
Crosses ( IDataHolder data1 , IDataHolder data2 , double direction );    
Default values:
direction: CrossingDirection.ANY
Description

The Crosses function tests if data1 gets higher or lower than data2. It returns true when data1 becomes greater than data2 if the direction parameter is CrossingDirection.ABOVE. Conversely, the function returns true when data1 becomes less than data2 if the direction parameter is CrossingDirection.BELOW. The function can also indicate a crossover irrespective of its direction if the direction parameter is CrossingDirection.ANY.

Input parameters
Parameter	Default value	Description
data1	-	Defines the first value for comparison.
data2	-	Defines the second value for comparison.
direction	-	Defines whether to find crossovers of first value above or below the second value. This parameter accepts Crossing Direction constants as value.
Example 1
plot avg = Average(close, 10);
plot crossing1 = close > avg and close[1] <= avg[1];
plot crossing2 = Crosses(close, avg, CrossingDirection.ABOVE);
crossing1.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_UP);
crossing2.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_DOWN);

The crossing1 and crossing2 variables are equal definitions of a condition when the Close price crosses the simple moving average with the length equal to 10. In other words, the Crosses function serves as a more compact and flexible way of defining intersections.

Example 2
input crossingType = {default above, below};
def avg = Average(close, 10);
plot Crossing = Crosses(close, avg, crossingType == CrossingType.above);
Crossing.SetPaintingStrategy(if crossingType == CrossingType.above
    then PaintingStrategy.BOOLEAN_ARROW_UP
    else PaintingStrategy.BOOLEAN_ARROW_DOWN);

The example first determines the crossing type of the Close price and the simple moving average for the last 10 bars. Depending on whether the crossing is up or down, the code draws either the arrow up or arrow down mark below and above the corresponding bars. Note that above and below here are enumeration constants.

Cos
Exp

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Exp
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Exp
Exp ( double number );    
Description

Returns the exponential value of a number.

Input parameters
Parameter	Default value	Description
number	-	Defines number whose exponential value is returned.
Example 1
declare lower;
input x = 3;
plot Calculate1 = Exp(x);
plot Calculate2 = Power(Double.E, x);

The example calculates the value of the exponent raised to the power of x using two different approaches. The results of the calculations are equal.

Example 2
declare lower;
def temp = 0.1 * (RSIWilder() - 50);
def x = WMA(temp, 9);
plot IFT_RSI = (Exp(2 * x) - 1) / (Exp(2 * x) + 1);

The code plots the Inversed Fisher Transform indicator based on the smoothed RSI value. Initially, the code subtracts the standart RSIWilder by 50 and multiplies the result by 0.1 to get values starting from -5 and through 5. Then it smoothes the values using the WMA function. Finally, it calculates the IFT for the values.

Crosses
Floor

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Floor
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Floor
Floor ( double value );    
Description

Rounds a value down to the nearest integer (which is not greater than the value).

Input parameters
Parameter	Default value	Description
value	-	Defines value to round down.
Example
plot Lower = Floor(low);
plot Upper = Ceil(high);

This example draws a channel at integer levels which fits high and low prices.

Exp
IsInfinite

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/IsInfinite
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
IsInfinite
IsInfinite ( double value );    
Description

Returns true if the specified number is infinitely large in magnitude.

Input parameters
Parameter	Default value	Description
value	-	Defines value to test.
Example 1
declare lower;

input dividend = 10;
input divisor = 0;

def tempResult = dividend / divisor;
plot Result = if IsInfinite(tempResult) then 0 else tempResult;

The example draws the result of division the dividend by the divisor on a separate subgraph. If the divisor is equal to zero then the division produces the infine number. The IsInfinite function returns true as a result of verifying the infinite number and the result is assigned 0.

Example 2
declare lower;

input dividend = 10;
input divisor = 0;

plot Result = if divisor == 0 then 0 else dividend / divisor;

This example is similar to the previous one. But here the validation is performed before the division which makes the code simplier.

Floor
IsNaN

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/IsNaN
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
IsNaN
IsNaN ( double value );    
Description

The IsNaN function returns true if the specified parameter is not a number and false otherwise.

Input parameters
Parameter	Default value	Description
value	-	Defines value to test.
Example 1
def onExpansion = if IsNaN(close) then yes else no;
plot HighestClose = if onExpansion then HighestAll(close) else double.NaN;
plot LowestClose = if onExpansion then LowestAll(close) else double.NaN;

This example code draws the highest and the lowest close  price on the right expansion of the subgraph (see the image below). For more information about the chart expansion, please refer to the Time Axis article.

Example 2
declare lower;

input symbol = "IBM";

def closeSymbol = close(symbol);

def closeSymbolWithoutNaN = CompoundValue(1, if IsNaN(closeSymbol) then closeSymbolWithOutNaN[1] else closeSymbol, closeSymbol);

plot Data = closeSymbolWithOutNaN;

This code plots the close price of an input symbol across the current chart. Any gap in the input symbol price data (NaN value) is replaced with the last-known close price value before the gap. 

IsInfinite
Lg

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Lg
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Lg
Lg ( double number );    
Description

Returns the base-10 logarithm of an argument.

Input parameters
Parameter	Default value	Description
number	-	Defines number whose logarithm is calculated.
Example
declare lower;
plot data = Lg(close);

The example draws the base-10 logarithm plot of the close values.

IsNaN
Log

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Log
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Log
Log ( double number );    
Description

Returns the natural logarithm of an argument.

Input parameters
Parameter	Default value	Description
number	-	Defines number whose logarithm is calculated.
Example
declare lower;
plot data = Log(close);

The code draws the plot of the logarithm of the closing price of a stock.

Lg
Max

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Max
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Max
Max ( double value1 , double value2 );    
Description

Returns the greater of two values.

Input parameters
Parameter	Default value	Description
value1	-	Defines the first value for comparison.
value2	-	Defines the second value for comparison.
Example
def SMA = SimpleMovingAvg();
plot data = Max(close, SMA);

This example displays the higher value of either the closing price or the simple moving average.

Log
Min

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Min
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Min
Min ( double value1 , double value2 );    
Description

Returns the smaller of two values.

Input parameters
Parameter	Default value	Description
value1	-	Defines the first value for comparison.
value2	-	Defines the second value for comparison.
Example
plot data = Min(close, open);

The code draws the smaller value of the close and open values.

Max
Power

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Power
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Power
Power ( double number , double power );    
Description

Returns the value of the first argument raised to the power of the second argument.

Input parameters
Parameter	Default value	Description
number	-	Defines the number to raise to the power.
power	-	Defines the power to which the number is raised.
Example
declare lower;
plot Close1_5 = Power(close, 1.5);

The example draws the plot of the close value raised to the power of 1.5.

Min
Random

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Random
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Random
Random ();    
Description

Returns a value with a positive sign, greater than or equal to 0.0 and less than 1.0

Example
declare lower;
input limit = 10;
plot Noise = Random() * limit;

The code draws a plot of random values ranging from 0. to 10.

Power
Round

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Round
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Round
Round ( double number , int numberOfDigits );    
Default values:
numberOfDigits: 2
Description

Rounds a number to a certain number of digits.

Input parameters
Parameter	Default value	Description
number	-	Defines the number to round.
numberOfDigits	2	Defines the number of digits to which the number is rounded.
Example
plot SMA = Round(Average(close, 12) / TickSize(), 0) * TickSize();

This example script plots 12 period SMA rounded to the nearest tick size value.

Random
RoundDown

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/RoundDown
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
RoundDown
RoundDown ( double number , int numberOfDigits );    
Default values:
numberOfDigits: 2
Description

Rounds a number towards zero to a certain number of digits.

Input parameters
Parameter	Default value	Description
number	-	Defines the number to round down.
numberOfDigits	2	Defines the number of digits to which the number is rounded down.
Example

See the RoundUp function example.

Round
RoundUp

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/RoundUp
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
RoundUp
RoundUp ( double number , int numberOfDigits );    
Default values:
numberOfDigits: 2
Description

Rounds a number up to a certain number of digits.

Input parameters
Parameter	Default value	Description
number	-	Defines the number to round up.
numberOfDigits	2	Defines the number of digits to which the number is rounded up.
Example
input price = close;
input digits = 0;
plot ceiling = RoundUp(price, digits);
plot floor = RoundDown(price, digits);

This example plots bands representing a price of the instrument rounded up and down to a certain number of digits.

RoundDown
Sign

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Sign
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Sign
Sign ( double number );    
Description

Returns the algebraic sign of a number: 1 if the number is positive, 0 if zero and -1 if negative.

Input parameters
Parameter	Default value	Description
number	-	Defines the number whose sign is found.
Example 1
declare lower;
plot Trend = Sign( ExpAverage(close, 15) - ExpAverage(close, 30) );

The example draws a plot showing the current trend as 1(bullish), 0(neutral), or -1(bearish) values depending on the difference between two EMAs.

Example 2
declare lower;
plot Data = Average(Sign(close - close[1]) * (high - low), 15);

The example draws the average range for 15 bars considering the closing price change as compared to the previous bar.

RoundUp
Sin

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Sin
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Sin
Sin ( double angle );    
Description

Returns the trigonometric sine of an angle.

Input parameters
Parameter	Default value	Description
angle	-	Defines angle (in radians) whose sine is calculated.
Example
declare lower;
input a = 0;
input b = 10;
input periodBars = 20;
def w = 2 * Double.Pi / periodBars;
def x = CompoundValue(1, x[1] + 1, 0);
plot F = a + b * Sin(w * x);

The code draws the sine function depending on the variable which starts from one and increments by one on each bar. The cyclic frequency(w) is calculated based on the periodBars constant.

Sign
Sqr

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Sqr
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Sqr
Sqr ( double value );    
Description

Calculates the square of an argument.

Input parameters
Parameter	Default value	Description
value	-	Defines number whose square is calculated.
Example
declare lower;
plot Data = Sqr(StDev(close, 10));

The example draws the variance of close for the last 10 bars. Variance by definition is a square of the standard deviation.

Sin
Sqrt

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Sqrt
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Sqrt
Sqrt ( double value );    
Description

Calculates the square root of an argument.

Input parameters
Parameter	Default value	Description
value	-	Defines number whose square root is calculated.
Example
declare lower;
plot data = Sqrt(close);

The draws the plot of the square root of the closing price of a stock.

Sqr
Sum

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Sum
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Sum
Sum ( IDataHolder data , int length );    
Default values:
length: 12
Description

Returns the sum of values for the specified number of bars. The default value of length is 12.

Input parameters
Parameter	Default value	Description
data	-	Defines values to be summed.
length	12	Defines number of bars for which the values are summed.
Example 1
declare lower;
plot data = Sum(close, 20);

The example displays a line that is the sum of the last 20 days' closing prices.

Example 2
plot data = Sum(close, 20)/20;

This example returns the sum of the last 20 days' closing prices divided by 20. This value is called 20 day moving average.

Sqrt
Tan

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/Tan
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Tan
Tan ( double angle );    
Description

Returns the trigonometric tangent of an angle.

Input parameters
Parameter	Default value	Description
angle	-	Defines angle (in radians) whose tangent is calculated.
Example
declare lower;
input length = 5;
input min = 30;
input max = 90;
plot CheckingTangentHit = Between((close - close[length]) / length, Tan(min * double.Pi / 180), Tan(max * double.Pi / 180));

The code checks if the tangle of the closing price angle of slope is within the defined limits.

Sum
TotalSum

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Math---Trig/TotalSum
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
AbsValue
ACos
ASin
ATan
Ceil
Cos
Crosses
Exp
Floor
IsInfinite
IsNaN
Lg
Log
Max
Min
Power
Random
Round
RoundDown
RoundUp
Sign
Sin
Sqr
Sqrt
Sum
Tan
TotalSum
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
TotalSum
TotalSum ( IDataHolder data );    
Description

Returns the sum of all values from the first bar to the current.

Input parameters
Parameter	Default value	Description
data	-	Defines values to be summed.
Example
declare lower;
plot data = TotalSum(volume);

The example returns the total accumulated volume for the time frame of the current chart.

Tan
Statistical

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Option Related
This section contains functions to work with options.
Here is the full list:
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Look and Feel
Delta
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/Delta
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Delta
Delta ( IDataHolder Underlying Price , IDataHolder Volatility );    
Default values:
Underlying Price: close(getUnderlyingSymbol())
Volatility: imp_volatility(getUnderlyingSymbol())
Description

Calculates the delta option greek.

Input parameters
Parameter	Default value	Description
Underlying Price	close(getUnderlyingSymbol())	Defines price to be used in calculation of delta.
Volatility	imp_volatility(getUnderlyingSymbol())	Defines volatility to be used in calculation of delta.
Example
declare lower;
def epsilon = 0.01 * close(GetUnderlyingSymbol());
plot approxDelta = (OptionPrice(underlyingPrice = close(GetUnderlyingSymbol()) + epsilon) - OptionPrice()) / epsilon;
plot Delta = Delta();

This example illustrates the approximate calculation of delta by dividing a change in the theoretical option price by a change in the underlying symbol price.

Option Related
Gamma

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/Gamma
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Gamma
Gamma ( IDataHolder Underlying Price , IDataHolder Volatility );    
Default values:
Underlying Price: close(getUnderlyingSymbol())
Volatility: imp_volatility(getUnderlyingSymbol())
Description

Calculates the gamma option greek.

Input parameters
Parameter	Default value	Description
Underlying Price	close(getUnderlyingSymbol())	Defines price to be used in calculation of gamma.
Volatility	imp_volatility(getUnderlyingSymbol())	Defines volatility to be used in calculation of gamma.
Example
def shift = 0.1*close(GetUnderlyingSymbol());
plot theoreticalprice = OptionPrice(underlyingPrice = close(GetUnderlyingSymbol()) + shift);
plot firstorder = OptionPrice() + shift * Delta();
plot secondorder = firstorder + shift*shift/2 * Gamma();

This example illustrates the use of the Gamma function to calculate changes in the theoretical option price when the underlying symbol price changes significantly. While the expression using delta is only a rough estimate of the resulting price, taking gamma into account results in much better approximation.

Delta
GetATMOption

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/GetATMOption
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetATMOption
GetATMOption ( String underlyingSymbol , int yyyyMmDd , String optionType );    
Default values:
underlyingSymbol: Underlying symbol
optionType: OptionClass.CALL
Description

Returns the code of the option of the specified series, which has the strike price closest to the current market price. You can specify the series by defining underlying symbol, expiration date, and option type (Put or Call).

Input parameters
Parameter	Default value	Description
underlyingSymbol	current symbol	Defines symbol of the option.
yyyyMmDd	-	Defines expiration date of the option in the YYYYMMDD format.
optionType	OptionClass.CALL	Defines whether the option is Put or Call. This parameter accepts Option Class constants as value.
Example 1
input expirationDate = 20120421;
AddLabel(IsOptionable(), "ATM Call option is " + GetATMOption(GetUnderlyingSymbol(), expirationDate, OptionClass.CALL));

This script adds a chart label showing the code of the at-the-money Call option of currently chosen symbol with expiration date April 21, 2012.

Example 2
declare lower;
plot AprilATMPutPrice = close(GetATMOption(GetUnderlyingSymbol(), 20120421, OptionClass.PUT));

This script plots the Close price of the at-the-money Put option of currently chosen symbol with expiration date April 21, 2012.

Gamma
GetDaysToExpiration

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/GetDaysToExpiration
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetDaysToExpiration
GetDaysToExpiration ();    
Description

Returns the number of days till the expiration of the current option.

Example
declare hide_on_intraday;
input weeks = 4;
AddChartBubble(
  GetDaysToExpiration() == 7 * weeks + 1,
  high,
  "Weeks till expiration: " + weeks,
  Color.YELLOW,
  yes
);
AddChartBubble(
  GetDaysToExpiration() == 1,
  high,
  "Expiration Friday",
  Color.RED,
  yes
);

This script shows two bubbles on the option chart: the red one indicating the Expiration Friday and the yellow one indicating a bar four weeks prior to the Expiration Friday.

GetATMOption
GetNextExpirationOption

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/GetNextExpirationOption
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetNextExpirationOption
GetNextExpirationOption ( String optionCode );    
Default values:
optionCode: Option code
Description

Returns the code of the option with the same strike price as the input one, but belonging to the next series.

Input parameters
Parameter	Default value	Description
underlyingSymbol	-	Defines the input option.
Example
plot NextOption = close(GetNextExpirationOption());

On the option chart, this script plots the Close price of the option in the next series, with the same underlying, strike price, and side.

GetDaysToExpiration
GetNextITMOption

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/GetNextITMOption
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetNextITMOption
GetNextITMOption ( String optionCode );    
Default values:
optionCode: Option code
Input parameters
Parameter	Default value	Description
optionCode	-	Defines the input option.
Description

Returns the code of the next option in the same series as the input one. For a Put option, the code of the next option with higher strike will be returned; for a Call option, this function will return the code of the next option with lower strike.

Note that, despite the function name, the code of the next option in in-the-money direction is returned, which is not necessarily an in-the-money option.

Example
AddLabel(yes, "Next ITM option is" + GetNextITMOption(".GOOG120317C580"));

This script adds a chart label showing the code of the next Call option for Google in the series with expiration date March 17, 2012, whose strike price is lower than that of the specified one ($580).

GetNextExpirationOption
GetNextOTMOption

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/GetNextOTMOption
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetNextOTMOption
GetNextOTMOption ( String optionCode );    
Default values:
optionCode: Option code
Input parameters
Parameter	Default value	Description
optionCode	-	Defines the input option.
Description

Returns the code of the next option in the same series as the input one. For a Put option, the code of the next option with lower strike will be returned; for a Call option, this function will return the code of the next option with higher strike.

Note that, despite the function name, the code of the next option in out-of-the-money direction is returned, which is not necessarily an out-of-the-money option.

Example
AddLabel(yes, "Next OTM option is" + GetNextOTMOption(".GOOG120317C580"));

This script adds a chart label showing the code of the next Call option for Google in the series with expiration date March 17, 2012, whose strike price is higher than that of the specified one ($580).

GetNextITMOption
GetStrike

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/GetStrike
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetStrike
GetStrike ();    
Description

Returns the strike price for the current option.

Example
input strike_price_interval = 5;
input steps = 1;
plot OtherPrice = OptionPrice(GetStrike() + steps * strike_price_interval);

This example plots the theoretical price of an option with a different strike.

GetNextOTMOption
GetUnderlyingSymbol

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/GetUnderlyingSymbol
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetUnderlyingSymbol
GetUnderlyingSymbol ();    
Description

Returns the underlying symbol for the current option.

Example
AddLabel(yes, GetSymbolPart() + " is an option for " + GetUnderlyingSymbol());

This script adds a chart label showing the underlying symbol for the current option.

GetStrike
IsEuropean

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/IsEuropean
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
IsEuropean
IsEuropean ();    
Description

Returns true if the current option is European, false if American.

Example
AddLabel(yes, "This is " + if IsEuropean() then "a European" else "an American" + " style option.");

For option symbols, this example displays a label informing whether it is an American or a European style option.

GetUnderlyingSymbol
IsOptionable

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/IsOptionable
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
IsOptionable
IsOptionable ();    
Description

Returns true if the current symbol is optionable, false - otherwise.

Example
AddLabel(IsOptionable(), "IV: " + imp_volatility() * 100 +  "%");

Displays a label for optionable symbols showing the implied volatility in percentage.

IsEuropean
IsPut

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/IsPut
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
IsPut
IsPut ();    
Description

Returns true if the current option is PUT, false if CALL.

Example
plot Opposite = OptionPrice(IsPut = !IsPut());

This example plots theoretical price of an option with the same underlying, strike price, and expiration but the opposite right.

IsOptionable
OptionPrice

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/OptionPrice
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
OptionPrice
OptionPrice ( IDataHolder strike , IDataHolder isPut , IDataHolder daysToExpiration , IDataHolder underlyingPrice , IDataHolder Volatility , double isEuropean , double yield , double interestRate );    
Default values:
strike: getStrike()
isPut: isPut()
daysToExpiration: getDaysToExpiration()
underlyingPrice: close(getUnderlyingSymbol())
Volatility: imp_volatility(getUnderlyingSymbol())
isEuropean: isEuropean()
yield: getYield()
interestRate: getInterestRate()
Description

Calculates the theoretical option price. By default, this function uses implied volatility averaged over different options for the underlying, so the returned result is approximate.

Input parameters
Parameter	Default value	Description
strike	-	Defines the strike price for the option.
isPut	-	Defines whether or not the current is Put.
daysToExpiration	-	Defines the number of days till the expiration of the option.
underlyingPrice	close(getUnderlyingSymbol())	Defines the price of underlying symbol.
Volatility	imp_volatility(getUnderlyingSymbol())	Defines the volatility with which the theoretical price is calculated.
isEuropean	-	Defines whether or not the oprion is European.
yield	-	Defines the yield of the underlying symbol for the option.
interestRate	-	Defines the global interest rate.
Example
input underlying = "GOOG";
input strike = 700.0;
input expiration_date = 20140118;
input is_put = no;
input interest_rate = 0.06;
input yield = 0.0;
input is_european = no;

def iv;
if GetAggregationPeriod() < AggregationPeriod.DAY {
    iv = imp_volatility(underlying, AggregationPeriod.DAY);
} else {
    iv = imp_volatility(underlying);
}

plot TheoOptPrice = OptionPrice(strike, is_put, DaysTillDate(expiration_date), close(underlying), iv, is_european, yield, interest_rate);

This script plots the theoretical price of Google January 2014 call option with $700 strike and interest rate of 6%.

IsPut
Rho

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/Rho
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Rho
Rho ( IDataHolder Underlying Price , IDataHolder Volatility );    
Default values:
Underlying Price: close(getUnderlyingSymbol())
Volatility: imp_volatility(getUnderlyingSymbol())
Description

Calculates the rho option greek.

Input parameters
Parameter	Default value	Description
Underlying Price	close(getUnderlyingSymbol())	Defines price to be used in calculation of rho.
Volatility	imp_volatility(getUnderlyingSymbol())	Defines volatility to be used in calculation of rho.
Example
declare lower;
def epsilon = 0.0001;
plot approxRho = (OptionPrice(interestRate = GetInterestRate() + epsilon) - OptionPrice()) / epsilon / 100;
plot Rho = Rho();

This example illustrates the approximate calculation of rho by dividing a change in the theoretical option price by a change in the risk-free interest rate.

OptionPrice
Theta

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/Theta
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Theta
Theta ( IDataHolder Underlying Price , IDataHolder Volatility );    
Default values:
Underlying Price: close(getUnderlyingSymbol())
Volatility: imp_volatility(getUnderlyingSymbol())
Description

Calculates the theta option greek.

Input parameters
Parameter	Default value	Description
Underlying Price	close(getUnderlyingSymbol())	Defines price to be used in calculation of theta.
Volatility	imp_volatility(getUnderlyingSymbol())	Defines volatility to be used in calculation of theta.
Example
declare lower;
plot approxTheta = (OptionPrice() - OptionPrice(DaysToExpiration = GetDaysToExpiration() + 1));
plot Theta = Theta();

This example illustrates the approximate calculation of theta by finding a change in the theoretical option price produced by increasing the time to expiration by one day.

Rho
Vega

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Option-Related/Vega
Fundamentals
Look and Feel
Option Related
Delta
Gamma
GetATMOption
GetDaysToExpiration
GetNextExpirationOption
GetNextITMOption
GetNextOTMOption
GetStrike
GetUnderlyingSymbol
IsEuropean
IsOptionable
IsPut
OptionPrice
Rho
Theta
Vega
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Vega
Vega ( IDataHolder Underlying Price , IDataHolder Volatility );    
Default values:
Underlying Price: close(getUnderlyingSymbol())
Volatility: imp_volatility(getUnderlyingSymbol())
Description

Calculates the vega option greek.

Input parameters
Parameter	Default value	Description
Underlying Price	close(getUnderlyingSymbol())	Defines price to be used in calculation of vega.
Volatility	imp_volatility(getUnderlyingSymbol())	Defines volatility to be used in calculation of vega.
Example
declare lower;
def epsilon = 0.01 * imp_volatility(GetUnderlyingSymbol());
plot approxVega = (OptionPrice(Volatility = imp_volatility(GetUnderlyingSymbol()) + epsilon) - OptionPrice()) / epsilon / 100;
plot Vega = vega();

This example illustrates the approximate calculation of vega by dividing a change in the theoretical option price by a change in implied volatility of the underlying.

Theta

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
Others
This section contains functions not fitting the rest of the sections. Each of the functions is used as a supplement for technical analysis.
Here is the full list:
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
Stock Fundamentals
AddOrder
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/AddOrder
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
AddOrder
AddOrder ( int type , IDataHolder condition , IDataHolder price , IDataHolder tradeSize , CustomColor tickColor , CustomColor arrowColor , String name );    
Default values:
type: OrderType.BUY_AUTO
price: open[-1]
tradeSize: specified by strategy settings
tickColor: Color.MAGENTA
arrowColor: Color.MAGENTA
name: "<strategy name>"
Description

Adds an order of specified side and position effect for the next bar when the condition is true.

Input parameters
Parameter	Default value	Description
type	OrderType.BUY_AUTO	Defines order side and position effect using the OrderType constants.
condition	-	Defines condition upon which the order is added.
price	open[-1]	Defines price at which the order is added.
tradeSize	-	

Defines the number of contracts traded. Note that this value overrides the trade size specified in Strategy Global Settings.

tickColor	Color.MAGENTA	Defines the color of tick marking the trade price.
arrowColor	Color.MAGENTA	Defines the color of signal arrow.
name	strategy name	Defines the order name which will be displayed on "Orders" tabs in strategy settings, in strategy report, and as captions to the Buy/Sell signal arrows on chart. By default, all orders use the same name as the strategy itself.
Example
AddOrder(OrderType.BUY_AUTO, close > close[1], open[-1], 50, Color.ORANGE, Color.ORANGE, "Sample buy @ " + open[-1]);

If the current Close price is higher than the previous, the code opens the long position or closes the short one at the Open price of the next bar. The trade size will be equal to 50, signals will be colored orange, and each signal will display the buying price.

Others
Alert

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/Alert
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
Alert ( IDataHolder condition , String text , int alert type , String sound );    
Default values:
alert type: Alert.ONCE
sound: Sound.NoSound
Description

Shows an alert message with the text and plays the sound when the condition is true. Note that you can create studies containing only alert function call without defining any plots.

Note: When Alert() calls another function, e.g., Alert (HasEarnings()); -- it only uses the value of that function at the last real bar. So, if the last real bar does not contain any earnings announcement, alert will not be triggered.

Input parameters
Parameter	Default value	Description
condition	-	Defines condition upon which the alert is displayed.
text	-	Defines text of the alert message.
alert type	Alert.ONCE	Defines periodicity with which the alert is shown. This parameter accepts Alert constants as value.
sound	Sound.NoSound	Defines the alert sound. This parameter accepts Sound constants as value.
Example 1
Alert(Crosses(close, Average(close, 15), CrossingDirection.ABOVE), "Closing price crosses over SMA!");

This alert is triggered on the first cross of the Close price over the SMA with the length equal to 15. It can be triggered only once and does not play any sound, because it uses default values Alert.ONCE and Sound.NoSound for the alert type and sound.

Example 2
def condition = Crosses(Average(close, 15), Average(close, 30), CrossingDirection.ABOVE);
Alert(condition, "Bullish!", Alert.BAR);

This alert is triggered when the fast average crosses the slow average and shows the corresponding text message. It can be triggered once per bar and does not play any sound, because it uses Alert.BAR value for the alert type and default Sound.NoSound value for the sound.

Example 3
Alert(close >= 100 and close < 200, "100 <= Tick < 200!", Alert.TICK, Sound.Ding);
Alert(close >= 200, "Tick > 200!", Alert.TICK, Sound.Chimes);

First alert is triggered for each tick greater than 100, but less than 200 and the second alert - for each tick greater than 200. Both alerts also display a text and play sound other than default.

AddOrder
AsDollars
You may also like
Alerts
The Alerts section is only displayed for studies that have scripted alerts, i.e., use the ...
Study Alerts
Study Alerts are signals generated when a study-based condition is fulfilled. You can use both ...

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/AsDollars
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
AsDollars
AsDollars ( double value );    
Description

Converts a number into a string expressing a dollar amount:

Symbol "$" is added before the number;
Two digits after the decimal point are always used;
Thousand separators (comma) are used.
Input parameters
Parameter	Default value	Description
value	-	Defines number to be converted into a string.
Example
AddLabel(yes, "Current True Range is " + AsDollars(TrueRange(high, close, low)));

This script adds a chart label showing current True Range as amount in dollars.

Alert
AsPercent

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/AsPercent
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
AsPercent
AsPercent ( double value );    
Description

Converts a number into a string expressing percentage:

Symbol "%" is added after the number;
Up to two digits after the decimal point are used (precision is 0.01%);
Thousand separators (comma) are used.
Input parameters
Parameter	Default value	Description
value	-	Defines number to be converted into a string.
Example
input length = 9;
AddLabel(yes, AsPercent((close - close[length]) / close[length]));

This script adds a chart label showing percent Rate of Change in Close price.

AsDollars
AsPrice

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/AsPrice
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
AsPrice
AsPrice ( double value );    
Description

Converts a number into string according to price notation used by the instrument. This function only applies the notation characteristic of the instrument and does not round values down to the tick size.

Input parameters
Parameter	Default value	Description
value	-	Defines value to be converted.
Example
AddLabel(yes, AsPrice(Average(close, 10)));

If applied to /ZF chart, this script adds a chart label showing a 10 period SMA of Close price using 1/32nds price notation (XXX'YYZ).

AsPercent
Assert

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/AsText
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
AsText
AsText ( double value , String format );    
Default values:
format: NumberFormat.TWO_DECIMAL_PLACES
Description

Converts a number into string with specified properties. The properties are adjusted using the format parameter which can be expressed as a NumberFormat constant.

Input parameters
Parameter	Default value	Description
value	-	Defines number to be converted into a string.
format	NumberFormat.TWO_DECIMAL_PLACES	Defines text format with a NumberFormat constant.
Example
input length = 9;
AddLabel(yes, AsText((close - close[length]) / close[length], NumberFormat.TWO_DECIMAL_PLACES));

This script adds a chart label showing Rate of Change in Close price rounded down to two digits after the decimal point.

Assert
BarNumber

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/Assert
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
Assert
Assert ( boolean condition , Any message );    
Default values:
message: "assert failed"
Description

Throws a runtime error message in case the specified condition is false. The error message can be viewed by clicking Exclamation indicator in the top left corner of the chart.

Input parameters
Parameter	Default value	Description
condition	-	Defines condition upon which the error message is displayed.
message	"assert failed"	Defines the text of error message.
Example
input percent = 5.0;
Assert(percent > 0.0, "percent must be positive");
plot UpperBand = (1 + percent / 100 ) * close ;
plot LowerBand = (1 - percent / 100 ) * close ;

If "percent" input parameter is not a positive value, study plots are not displayed and Exclamation indicator appears.

AsPrice
AsText

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/BarNumber
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
BarNumber
BarNumber ();    
Description

Returns the current bar number.

Example 1
declare lower;
input length = 14;
plot RSquared = Sqr(Correlation(BarNumber(), close, length));

The output value of BarNumber increments by one on each new bar and represents a linear dependency. For this reason it can be used to calculate values for the RSquared plot that approximates the price with the linear regression trendline.

Example 2
declare lower;
plot Data = if BarNumber() <= 5 then 100 else if BarNumber() == 6 or BarNumber() == 7 then 150 else 200;

The examples draws the Data plot depending on the bar number. If the number is less or equal to 5 then its value is 100, if the number is 5 or 6 then 150, in the rest of the cases its value is 200.

AsText
Between

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/Between
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
Between
Between ( double parameter , double value1 , double value2 );    
Description

Tests if the specified parameter is within the range of value1 and value2 inclusively. The function returns 1 (true) if the data is between the two parameter values, and 0 (false) if the data is outside of the two parameter values.

Input parameters
Parameter	Default value	Description
parameter	-	Defines parameter to test.
value1	-	Defines the first endpoint of the range.
value2	-	Defines the second endpoint of the range.
Example
declare lower;
input lowLimit = 140.0;
input highLimit = 160.0;
plot Between1 = Between(close, lowLimit, highLimit);
plot Between2 = close >= lowLimit and close <= highLimit;

The code will return 1 if the closing price is between lowLimit and highLimit, and 0 if the closing price is below lowLimit or above highLimit. The example also shows the alternative solution to the between function implemented using the double inequality.

BarNumber
CompoundValue

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/CompoundValue
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
CompoundValue
CompoundValue ( int length , IDataHolder visible data , IDataHolder historical data );    
Default values:
length: 1
Description

Calculates a compound value according to following rule: if a bar number is greater than length then the visible data value is returned, otherwise the historical data value is returned. This function is used to initialize studies with recursion.

Input parameters
Parameter	Default value	Description
length	1	Defines length with which the bar number is compared.
visible data	-	Defines data to be returned if bar number exceeds the specified length.
historical data	-	Defines data to be returned if bar number is less than or equal to the specified length.
Example
declare lower;
def x = CompoundValue(2, x[1] + x[2], 1);
plot FibonacciNumbers = x;

The example calculates the Fibonacci sequence. Starting from the third bar each following number is calculated as the sum of the previous two numbers while the numbers for the first two bars are equal to one. As a result you will get a plot containing values 1, 1, 2, 3, 5, etc.

Between
Concat

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/Concat
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
Concat
Concat ( Any value1 , Any value2 );    
Description

Concatenates two string values. If the values' type is not string it is first converted to a string (for doubles it saves four decimal places)

Input parameters
Parameter	Default value	Description
value1	-	Defines the first value to concatenate.
value2	-	Defines the second value to concatenate.
Example
input symbol = "IBM";
AddLabel(yes, Concat("SMA (", Concat(symbol, Concat(", 10): ", Round(Average(close(symbol), 10), 1)))));

This example displays a constantly visible chart label with the SMA of the given symbol with the length equal to 10 rounded to one decimal place.

input symbol = "IBM";
AddLabel (yes, "SMA ("+ symbol + ", 10): " + Round(Average(close(symbol), 10), 1));
CompoundValue
EntryPrice

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/EntryPrice
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
EntryPrice
EntryPrice ();    
Description

Returns the price of the entry order. For several entry orders in the same direction as the currently held position the function returns the average price for all of them.

Example
AddOrder(OrderType.SELL_TO_CLOSE, close > EntryPrice() + 3 or close < EntryPrice() - 9);

Adds a Sell order for closing a long position when the Close price is either greater than the entry price by 3 (for taking profits) or less by 9 (for safety).

Concat
First
You may also like
Watchlist
Watchlists are one of the key thinkorswim® features. A watchlist is a collection of symbols with ...

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/FPL
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
FPL
FPL ();    
Description

Returns floating Profit/Loss value based on strategy signals. For each bar, this value is equal to the possible Profit/Loss if the position were exited at the Close price.

Example
declare lower;

plot FPL = FPL();
plot ZeroLine = 0;

FPL.SetPaintingStrategy(PaintingStrategy.SQUARED_HISTOGRAM);
FPL.DefineColor("Positive", Color.UPTICK);
FPL.DefineColor("Negative", Color.DOWNTICK);
FPL.AssignValueColor(if FPL >= 0 then FPL.Color("Positive") else FPL.Color("Negative"));
ZeroLine.SetDefaultColor(Color.GRAY);

This script plots the floating Profit/Loss and colors the plot based on whether the hypothetical exit would result in profit or loss.

First
Fundamental

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/First
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
First
First ( IDataHolder data );    
Description

Returns the value of the parameter expression in the first bar.

Input parameters
Parameter	Default value	Description
data	-	Defines expression whose value is returned.
Example
declare lower;
def close1 = First(close);
plot Data = (close - close1) / close1 * 100;

The code calculates the close price percentage move on the analogy of the Percentage View mode for charts. In this example the parameter expression for the first function is close. This means that the close1 variable always holds close for the first bar.

EntryPrice
FPL

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/Fundamental
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
Fundamental
Fundamental ( int fundamentalType , String symbol , Any period , String priceType );    
Default values:
symbol: getSymbol()
period: "<current period>"
priceType: "<current type>"
Description

This function is generalization of fundamental functions, i.e. it returns the specified price for the chosen symbol, aggregation period, and price type.

This function should be used with one of the Fundamental Type constants to perform as the corresponding fundamental function. For more information about these constants, see the Fundamental Type constants section.

You can use both Aggregation Period constants and pre-defined string values (e.g. Day, 2 Days, Week, Month, etc.) as valid parameters for the aggregation period. The full list of the pre-defined string values can be found in the Referencing Secondary Aggregation article.

Valid parameters for the price type are: LAST, ASK, BID, and MARK.

Note that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.

Input parameters
Parameter	Default value	Description
fundamentalType	-	Defines fundamental value to be returned. This parameter accepts Fundamental Type constants.
symbol	current symbol	Defines symbol for which the fundamental value is returned.
period	current aggregation	Defines aggregation period for which the fundamental value is returned.
priceType	current price type	Defines the type of value to be returned: Last, Ask, Bid, or Mark.
Example
declare lower;

input price = FundamentalType.CLOSE;
input relationWithSecurity = "SPX";

def price1 = Fundamental(price);
def price2 = Fundamental(price, relationWithSecurity);

plot Relation = if price2 == 0 then Double.NaN else price1 / price2;
Relation.SetDefaultColor(GetColor(1));

This script exemplifies usage of the Fundamental function in the Symbol Relation study.

FPL
GetAggregationPeriod
You may also like
Phase Scores
Phase Scores is a thinkorswim gadget that provides you with an outline of fundamental and ...
MedianAverage
The Median Average plots the median value for specified fundamental data.
SectorRotationModel
The Sector Rotation Model is an attempt to integrate fundamental approach into a technical ...

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/GetAggregationPeriod
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
GetAggregationPeriod
GetAggregationPeriod ();    
Description

The GetAggregationPeriod function returns the current aggregation period in milliseconds for time charts, in ticks for tick charts, and in dollars for range charts. The aggregation period returned is:

For time charts: the amount of milliseconds required to complete one candle
For tick charts: the amount of ticks required to complete one candle
For range charts: the price range required to complete a range bar

Note: For GetAggregationPeriod, aggregations 1 Day and 24 hours are the same, even though they may produce different results on the charts. For example, an equality check for daily aggregation GetAggregationPeriod() >= AggregationPeriod.DAY  will return true when applied to a 24-hour aggregation chart.

Example
input lengthIntraday = 20;
input lengthDaily = 10;
plot data;
if GetAggregationPeriod() < AggregationPeriod.DAY {
    data = Average(close, lengthIntraday);
} else {
    data = Average(close, lengthDaily);
}

This example script plots a simple moving average with a length that depends on the current aggregation period. If the current aggregation period is shorter than one day, then the script plots the average with the length equal to the lengthIntraday. For aggregation periods of one day and greater, it plots the average with the length equal to lengthDaily.

Fundamental
GetInterestRate
You may also like
Time Charts
Time charts are probably the most popular chart type in terms of aggregation as the algorithm of ...
Percentage View
Percentage view is a TOS feature that enables you to view price changes as percentage values. ...
CumulativeOvernightVolume
The Cumulative Overnight Volume is a technical indicator that detects unusually high volume ...

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/GetInterestRate
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
GetInterestRate
GetInterestRate ();    
Description

Returns the global interest rate. This function cannot be used in Study Filters.

Example
declare lower;
input loan = 1000;
plot Charge = loan * GetInterestRate();
AddLabel(yes, "Interest Rate: " + GetInterestRate() * 100);

This example draws a charge for the loan at the current interest rate displayed in the chart label.

GetAggregationPeriod
GetPriceType
You may also like
OptionRho
Option Rho is a hedge parameter, one of the so-called Greeks. It measures sensitivity of option ...

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/GetPriceType
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
GetPriceType
GetPriceType ();    
Description

Returns the price type selected for the current symbol: "Last", "Bid", "Ask", or "Mark". Note that the last three are supported by non-Forex symbols only on intraday charts with time interval not greater than 15 days; on all other charts this function will always return "Last" for non-Forex symbols.

Example
AddLabel(yes, "The " + GetPricetype() + " price type is selected");

This script adds a chart label showing which price type is currently selected.

GetInterestRate
GetSymbol
You may also like
MomentumPercentDiff
The Momentum Percent Diff is a momentum-based technical indicator. Unlike the regular Momentum ...
Tick Charts
Tick charts represent the count of intraday trades: a new bar (or candlestick, line section, ...
WilliamsAD
The Williams Accumulation/Distribution study is used to determine either the marketplace is ...

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/GetSymbol
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
GetSymbol
GetSymbol ();    
Description

Returns the currently selected symbol.

When used on a futures chart, GetSymbol() returns the corresponding futures symbol with a namespace appended. Namespace is a market identifier code*.

Consider an /ES chart. To find this symbol’s namespace use AddLabel():

AddLabel(yes, GetSymbol()); 

The function displays /ES:XCME, where XCME is a namespace reserved for the Chicago Mercantile Exchange.

To avoid unexpected results, use namespaces in string comparisons:

AddLabel(GetSymbol() == "/ES:XCME", "Chart for /ES!");
Example
declare lower;
plot Diff = close(GetSymbol()) - close("IBM");

This example script plots the difference between Close prices of currently selected symbol and IBM.

*A namespace, or market identifier code (MIC), is a four-letter code assigned by the International Organization for Standardization (ISO) that uniquely identifies trading exchanges and markets, facilitating automated trade processing.

GetPriceType
GetSymbolPart

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/GetSymbolPart
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
GetSymbolPart
GetSymbolPart ( int position );    
Default values:
position: 1
Input parameters
Parameter	Default value	Description
position	-	Defines number of symbol part to be returned.
Description

Returns a part of the composite symbol.

When used on a futures chart, GetSymbolPart() returns the part of the corresponding composite futures symbol with a namespace appended. Namespace is a market identifier code*.

Consider a composite /ES+/YM chart. To find these symbols’ namespace use AddLabel():

AddLabel(yes, GetSymbolPart(1) + " + " + GetSymbolPart(2));

The function displays /ES:XCME + /YM:XCBT, where:

XCME is a namespace reserved for the Chicago Mercantile Exchange.
XCBT is a namespace reserved for the Chicago Board of Trade.

To avoid unexpected results, use namespaces in string comparisons. For example, to check if a two-part composite symbol has "/ES":

AddLabel(GetSymbolPart(1) == "/ES:XCME" or GetSymbolPart(2) == "/ES:XCME", "Composite symbol contains /ES!");

Note that all parts of a composite symbol are read in alphabetical order. For example, if you choose "KO+GE", it will be read as "GE+KO" by the system.

Example
declare lower;

plot Spreads = close(GetSymbolPart(1)) - close(GetSymbolPart(2));

The code calculates the spread between the first and second parts of the composite symbol.

*A namespace, or market identifier code (MIC), is a four-letter code assigned by the International Organization for Standardization (ISO) that uniquely identifies trading exchanges and markets, facilitating automated trade processing.

GetSymbol
GetValue

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/GetValue
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
GetValue
GetValue ( IDataHolder data , IDataHolder dynamic offset , int max offset );    
Default values:
max offset: 0
Description

Returns the value of data with the specified dynamic offset.

Note: For positive offset values, dynamic offset should be less than or equal to max offset. For negative offset values, dynamic offset should be less than or equal to max offset.

Input parameters
Parameter	Default value	Description
data	-	Defines data to be returned.
dynamic offset	-	

Defines expression with which the dynamic offset is calculated.

max offset	0	

Defines the maximum value of the dynamic offset by adjusting the past or future offset value. This value is positive for the past dynamic offset and negative for the dynamic future offset. When set to zero, the offset is not adjusted.

Example
plot ClosingPriceForHighestHigh = GetValue(close, GetMaxValueOffset(high, 12), 12);

The example script plots the close price of a bar that contains the highest high price among the last twelve bars.

GetSymbolPart
GetYield

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/GetYield
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
GetYield
GetYield ();    
Description

Returns the yield of the current stock or the underlying symbol for the current option.

Example
declare lower;
plot CurrentYield = GetYield() * 100;
def AD = GetYield() * close;
AddLabel(yes, "Annual Dividends: " + AD);

This script plots the current yield line and places a chart label indicating annual dividends.

GetValue
HasContractChangeEvent
You may also like
Message Center
Message Center is a thinkorswim gadget that helps you stay informed on a variety of events. ...
Account Statement
The Account Statement interface provides you with a line-item description of how funds have ...

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/HasContractChangeEvent
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
HasContractChangeEvent
HasContractChangeEvent ( String rootSymbol );    
Default values:
rootSymbol: getSymbol()
Description

Returns true if active futures contract has changed; false, otherwise.

Input parameters
Parameter	Default value	Description
rootSymbol	current symbol	Defines the root symbol.
Example
def change = open - close[1];
AddVerticalLine(HasContractChangeevent(), "Change is " + change);

This example script draws a vertical line at the point where active contract change has occurred. It also displays the difference between the first Open after active contract change and last Close price of previously active contract. Note that this example only makes sense when automatic contract change adjustments for futures is disabled (see the Futures Settings article for details).

GetYield
If

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/If
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
If
If ( double condition , double true value , double false value );    
Description

Returns true value if condition is true and false value otherwise. There are two ways to use the function. First, you can use it as the right side of an equation with 3 parameters: a condition, a true value and a false value. Secondly, you can use it in a conjunction with else to create more complex conditions.

Note that input arguments can only be numerical of type double. If other values are needed (e.g. Color constants), use the if-expression. E.g. for CustomColor arguments, the following code is valid:

AssignPriceColor(if close > open then Color.UPTICK else Color.DOWNTICK);

The following script will result in compilation error as type CustomColor is not compatible with type double:

AssignPriceColor(if(close > open, Color.UPTICK, Color.DOWNTICK));
Input parameters
Parameter	Default value	Description
condition	-	Defines condition to be tested.
true value	-	Defines value to be returned if condition is true.
false value	-	Defines value to be returned if condition is false.
Example
plot Maximum1 = If(close > open, close, open);
plot Maximum2 = if close > open then close else open;
plot Maximum3;
if close > open {
    Maximum3 = close;
} else {
    Maximum3 = open;
}

The code draws either close or open value depending on the condition in the if-statement. If close is higher than open, then close is drawn, otherwise open is drawn. Maximum2 and Maximum3 plots use alternative solutions such as if-expression and if-statement correspondingly.

HasContractChangeEvent
TickSize

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/TickSize
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
TickSize
TickSize ( String symbol );    
Default values:
symbol: getSymbol()
Description

Returns the minimum possible tick size for the specified symbol.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the tick size is returned.
Example
input numberOfTicks = 3;
plot OverBought = Highest(high)[1] + numberOfTicks * TickSize();
plot OverSold = Lowest(low)[1] - numberOfTicks * TickSize();
plot BreakOut = if Close >= OverBought then Close else if Close <= OverSold then Close else Double.NaN;
Breakout.SetPaintingStrategy(PaintingStrategy.POINTS);
Breakout.SetLineWeight(3);
Breakout.HideBubble();

Initially the example draws the OverBought and OverSold plots. The OverBought plot is calculated by adding the given number of ticks to the highest price for the last 12 bars starting from previous bar. The OverSold plot is calculated the same way but by subtracting the ticks from the lowest price. If the close price is out of the area of the first two plots the code displays the BreakOut plot.

If
TickValue

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Others/TickValue
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AddOrder
AsDollars
AsPercent
AsPrice
Assert
AsText
BarNumber
Between
CompoundValue
Concat
EntryPrice
First
FPL
Fundamental
GetAggregationPeriod
GetInterestRate
GetPriceType
GetSymbol
GetSymbolPart
GetValue
GetYield
HasContractChangeEvent
If
TickSize
TickValue
TickValue
TickValue ( String symbol );    
Default values:
symbol: getSymbol()
Description

Returns the dollar value of a symbol tick.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the tick value is returned.
Example
AddLabel(yes, "Contract size is " + TickValue()/TickSize());

In this example the contract size is calculated using the tick size and value.

TickSize

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Portfolio
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
GetAggregatedPL
GetAveragePrice
GetNetLiq
GetOpenPL
GetPortfolioAggregatedPL
GetPortfolioSharePrice
GetQuantity
GetTotalCash
Profiles
Stock Fundamentals
Others
Portfolio
Portfolio functions enable you to utilize figures specific to your own account in calculations. If applied to a symbol, the functions will not include its derivatives in the calculation.
The following limitations apply when using the GetAveragePrice, GetOpenPL, and GetQuantity functions:
They cannot be used on charts with a price type other than LAST (i.e., they won't work with MARK, ASK, or BID price types).
If applied to a futures product chart, they subscribe to the active contract data.
Note also that Portfolio functions can only be used with the following aggregation periods: 1 min, 2 min, 3 min, 4 min, 5 min, 10 min, 15 min, 20 min, 30 min, 1h, or 1 day. Time period for the aggregation of 1 day is limited to 1 year. 
Currently, the following Portfolio functions are available:
GetAggregatedPL — new
GetAveragePrice
GetNetLiq
GetOpenPL
GetPortfolioAggregatedPL — new
GetPortfolioSharePrice — new
GetQuantity
GetTotalCash
Corporate Actions
GetAggregatedPL
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Portfolio/GetAggregatedPL
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
GetAggregatedPL
GetAveragePrice
GetNetLiq
GetOpenPL
GetPortfolioAggregatedPL
GetPortfolioSharePrice
GetQuantity
GetTotalCash
Profiles
Stock Fundamentals
Others
GetAggregatedPL
GetAggregatedPL ( Symbol symbol );    
Default values:
symbol: current symbol
Description

Returns the aggregated Profit/Loss (P/L) for a specified symbol, for the currently selected account and over a defined period. The Aggregated P/L is calculated as the difference between the current value of a position (based on the most recent MARK price) and the trade price of the position at the chart’s start point. It is adjusted for all trades that occurred during that period. 

Unlike GetOpenPL, which calculates real-time P/L on the open position, GetAggregatedPL provides historical P/L from a defined start point. 
 

Input Parameters

Parameter

	

Default value

	

Description

symbol

	

current symbol

	

Defines the instrument for which the aggregated profit/loss will be returned.

Example
declare lower;

def aggPL = GetAggregatedPL ();
plot AggregatedPL = aggPL;
AggregatedPL.AssignValueColor (if AggregatedPL >= 0 then Color.GREEN else Color.RED);

This script plots the aggregated profit/loss value of the current symbol using the selected aggregation period. The plot is colored green for positive values and red for negative ones. 

Portfolio
GetAveragePrice

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Portfolio/GetAveragePrice
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
GetAggregatedPL
GetAveragePrice
GetNetLiq
GetOpenPL
GetPortfolioAggregatedPL
GetPortfolioSharePrice
GetQuantity
GetTotalCash
Profiles
Stock Fundamentals
Others
GetAveragePrice
GetAveragePrice ( Symbol symbol );    
Default values:
symbol: current symbol
Description

Returns the average trade price for a specified instrument, for the currently selected account. 

Note: there are certain limitations of usage of Portfolio functions; for more information on that, refer to the Portfolio functions index page.

Input Parameters
Parameter	Default value	Description
symbol	current symbol	Defines the instrument for which the average price will be returned.
Example
declare lower;

def qty = GetQuantity();
def openCost = qty * GetAveragePrice();
def netLiq = qty * close;

plot ManualOpenPL = netLiq - openCost;
plot AutoOpenPL = GetOpenPL();

This example script uses the GetAveragePrice function along with GetQuantity to manually calculate the Open Profit/Loss value. The resulting plot is shown with its automatic version calculated using the GetOpenPL function. The calculation is based on the execution price. Note that manual calculation of Open Profit/Loss used in this script is only valid for symbols with a dollar value equal to 1. For instruments that have a different dollar value, NetLiq and OpenCost formulas are to be multiplied by it.

GetAggregatedPL
GetNetLiq

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Portfolio/GetNetLiq
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
GetAggregatedPL
GetAveragePrice
GetNetLiq
GetOpenPL
GetPortfolioAggregatedPL
GetPortfolioSharePrice
GetQuantity
GetTotalCash
Profiles
Stock Fundamentals
Others
GetNetLiq
GetNetLiq ();    
Description

The GetNetLiq function returns the net liquidation value for the currently selected account. It is the current account value if all the positions on that account were to be closed at the current market price.

Note: Studies that use this function return N/A if chart property Show Extended-Hours Trading session is de-activated. To make sure this property is activated, navigate to Style -> Settings and then choose the tab that corresponds to the type of security you are currently analyzing: Equities, Options, or Futures. The Show Extended-Hours Trading session checkbox is located in the Axis area in the lower half of each of these tabs.

Example

The example script below plots the net liquidation value of the currently selected account on a lower subgraph. The value will be plotted as a histogram, which will change its color based on whether the value is positive or negative.

declare lower;

plot AccountNetLiq = GetNetLiq();
plot ZeroLine = 0;

AccountNetLiq.SetDefaultColor(GetColor(1));
AccountNetLiq.SetPaintingStrategy(PaintingStrategy.SQUARED_HISTOGRAM);
AccountNetLiq.DefineColor("Positive", Color.UPTICK);
AccountNetLiq.DefineColor("Negative", Color.DOWNTICK);
AccountNetLiq.AssignValueColor(if AccountNetLiq >= 0
then AccountNetLiq.Color("Positive")
else AccountNetLiq.Color("Negative"));
GetAveragePrice
GetOpenPL

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Portfolio/GetOpenPL
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
GetAggregatedPL
GetAveragePrice
GetNetLiq
GetOpenPL
GetPortfolioAggregatedPL
GetPortfolioSharePrice
GetQuantity
GetTotalCash
Profiles
Stock Fundamentals
Others
GetOpenPL
GetOpenPL ( Symbol symbol , int profitLossMode );    
Default values:
symbol: current symbol
profitLossMode: ProfitLossMode.EXECUTION_PRICE
Description

Returns the Open Profit/Loss value for a specified symbol, for the currently selected account. This value is the difference between a position’s net liquidation value and either execution price or cost basis times the position size, based on the profitLossMode parameter value. Cost basis values are provided by Schwab and include the effects of commissions and tax elections. By default, the value is returned based on the execution price; however, you can use ProfitLossMode constants to switch between the modes.

Note: there are certain limitations of usage of Portfolio functions; for more information on that, refer to the Portfolio functions index page.

Input Parameters
Parameter	Default value	Description
symbol	current symbol	Defines the instrument for which the Open Profit/Loss will be returned.
profitLossMode	ProfitLossMode.EXECUTION_PRICE	Defines whether the Open Profit/Loss value is to be calculated based on the execution price or cost basis.
Example
declare lower;

def openCost = GetQuantity() * GetAveragePrice();

plot PercentPL = GetOpenPL() / AbsValue(openCost) * 100;
PercentPL.AssignValueColor(if PercentPL >= 0 then Color.UPTICK else Color.DOWNTICK);

This example script calculates and plots the P/L% value using three of the Portfolio functions: GetOpenPL, GetQuantity, and GetAveragePrice. The calculation is based on the execution price. Positive parts of the plot are colored green and the negative ones red. Note that manual calculation of Open Profit/Loss used in this script is only valid for symbols with a dollar value equal to 1. For instruments that have a different dollar value, the OpenCost formula is to be multiplied by it.

GetNetLiq
GetPortfolioAggregatedPL

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Portfolio/GetPortfolioAggregatedPL
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
GetAggregatedPL
GetAveragePrice
GetNetLiq
GetOpenPL
GetPortfolioAggregatedPL
GetPortfolioSharePrice
GetQuantity
GetTotalCash
Profiles
Stock Fundamentals
Others
GetPortfolioAggregatedPL
GetPortfolioAggregatedPL ();    
Description

Returns the aggregated Profit/Loss (P/L) value for all positions in the account within the currently selected chart timeframe. This value represents the cumulative difference between the current market value and the initial trade price of all positions opened during the chart’s time interval. 

The calculation considers all instruments in the portfolio and reflects realized and unrealized profit/loss values.

Example
declare upper;

plot TotalPL = GetPortfolioAggregatedPL();
TotaPL.AssignValueColor(if Total PL >= 0 then Color.UPTICK else Color.DOWNTICK);

This script displays the aggregated P/L of the portfolio over the selected chart timeframe. Gains are plotted in green, losses in red. 

GetOpenPL
GetPortfolioSharePrice

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Portfolio/GetPortfolioSharePrice
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
GetAggregatedPL
GetAveragePrice
GetNetLiq
GetOpenPL
GetPortfolioAggregatedPL
GetPortfolioSharePrice
GetQuantity
GetTotalCash
Profiles
Stock Fundamentals
Others
GetPortfolioSharePrice
GetPortfolioSharePrice ();    
Description

Returns the Portfolio Share Price (PSP) value for the current chart symbol. PSP is a performance metric that tracks profitability of the currently selected account over time, isolating market-based gains or losses from cash movements like deposits, withdrawals, or dividends. 

Example
declare lower;

plot PSP = GetPortfolioSharePrice();
PSP.SetDefaultColor(Color.CYAN);

This example plots the current Portfolio Share Price on the chart. 

GetPortfolioAggregatedPL
GetQuantity

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Portfolio/GetQuantity
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
GetAggregatedPL
GetAveragePrice
GetNetLiq
GetOpenPL
GetPortfolioAggregatedPL
GetPortfolioSharePrice
GetQuantity
GetTotalCash
Profiles
Stock Fundamentals
Others
GetQuantity
GetQuantity ( Symbol symbol );    
Default values:
symbol: current symbol
Description

Returns the number of shares or contracts of a specified instrument held on the currently selected account.

Note: there are certain limitations of usage of Portfolio functions; for more information on that, refer to the Portfolio functions index page.

Input Parameters
Parameter	Default value	Description
symbol	current symbol	Defines the instrument for which the shares/contracts quantity will be returned.
Example
declare lower;

def qty = GetQuantity();
def openCost = qty * GetAveragePrice();
def netLiq = qty * close;

plot ManualOpenPL = netLiq - openCost;
plot AutoOpenPL = GetOpenPL();

This example script uses the GetQuantity function along with GetAveragePrice to manually calculate the Open Profit/Loss value. The resulting plot is shown with its automatic version calculated using the GetOpenPL function. The calculation is based on the execution price. Note that manual calculation of Open Profit/Loss used in this script is only valid for symbols with a dollar value equal to 1. For instruments that have a different dollar value, NetLiq and OpenCost formulas are to be multiplied by it.

GetPortfolioSharePrice
GetTotalCash

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Portfolio/GetTotalCash
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
GetAggregatedPL
GetAveragePrice
GetNetLiq
GetOpenPL
GetPortfolioAggregatedPL
GetPortfolioSharePrice
GetQuantity
GetTotalCash
Profiles
Stock Fundamentals
Others
GetTotalCash
GetTotalCash ();    
Description

The GetTotalCash function returns the total amount of cash available on the currently selected account.

Note: Studies that use this function return N/A if chart property Show Extended-Hours Trading session is de-activated. To make sure this property is activated, navigate to Style -> Settings and then choose the tab that corresponds to the type of security you are currently analyzing: Equities, Options, or Futures. The Show Extended-Hours Trading session checkbox is located in the Axis area in the lower half of each of these tabs.

GetQuantity
Profiles

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Profiles
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
DataProfile
GetHighest
GetHighestValueArea
GetLowest
GetLowestValueArea
GetPointOfControl
MonkeyBars
Show
TimeProfile
VolumeProfile
Stock Fundamentals
Others
Profiles
The list of functions:
DataProfile
GetHighest
GetHighestValueArea
GetLowest
GetLowestValueArea
GetPointOfControl
MonkeyBars
Show
TimeProfile
VolumeProfile
Portfolio
DataProfile
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Profiles/DataProfile
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
DataProfile
GetHighest
GetHighestValueArea
GetLowest
GetLowestValueArea
GetPointOfControl
MonkeyBars
Show
TimeProfile
VolumeProfile
Stock Fundamentals
Others
DataProfile
DataProfile ( iDataHolder data , double pricePerRow , iDataHolder startNewProfile , int onExpansion , int numberOfProfiles , double value area percent );    
Default values:
pricePerRow: PricePerRow.Automatic
onExpansion: Yes
numberOfProfiles: "all"
value area percent: 70.0
Description

The DataProfile function plots an activity profile for any given input variable such as study or function. The activity profile is essentially a horizontal diagram that gives insight into which values are most often reached by the input variable.

The histogram is calculated based on the following algorithm:

The system finds the value range of the variable.
This value range is broken into intervals. This process can be automatic (the range is broken into 85 equal parts), ticksize-based (each interval's length is equal to the minimum value movement), and manual (interval length is specified by user). The interval length defines the height of each histogram row.
The system calculates the number of times the variable value has reached each of the intervals.
Each histogram row then has a length proportional to the corresponding number calculated in Step 3. 

Here is how you can read the DataProfile histogram:

The longest row represents the value most often reached by the input variable. It is also called Point Of Control.
The range surrounding the Point Of Control where 70% of the value movements took place is called Value Area and represents frequent values. The mentioned percentage is the default and can be modified using input parameters.
Input Parameters

Parameter

	

Default value

	

Description

data	-	The variable to calculate the Data Profile for.
pricePerRow	PricePerRow.AUTOMATIC	The row height. This value can be calculated automatically (use the PricePerRow.AUTOMATIC constant to break the entire range into 85 equal parts), ticksize-based (use the PricePerRow.TICKSIZE constant to break the range into intervals, each having a length equal to minimum value movement), or manually (specify the desirable interval length).
startNewProfile	-	Defines a condition, which, when satisfied, gives the function a signal to calculate a new profile.
onExpansion	Yes	Defines whether or not to show the profile on the expansion area of the chart.
numberOfProfiles	"all"	Defines the number of profiles to be displayed if onExpansion is set to no. If onExpansion is set to yes, then this parameter is ignored and only one profile is shown.
value area percent	70.0	Defines the percentage of frequent value movements to be included in the Value Area.
Example
declare lower;

def rsi = reference RSI();

def condition = GetYear() != GetYear()[1];

profile CustomProfile = DataProfile(data = rsi, onExpansion = no, startNewProfile = condition);

CustomProfile.Show();

plot POC = CustomProfile.GetPointOfControl();

The above code displays yearly data profiles of RSI and their Points Of Control as a plot.

Profiles
GetHighest

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Profiles/GetHighest
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
DataProfile
GetHighest
GetHighestValueArea
GetLowest
GetLowestValueArea
GetPointOfControl
MonkeyBars
Show
TimeProfile
VolumeProfile
Stock Fundamentals
Others
GetHighest
GetHighest ();    
Description

Returns the highest price value reached by the instrument within the time period for which the profile is accumulated.

Example
def yyyymmdd = GetYYYYMMDD();
def day_number = DaysFromDate(First(yyyymmdd)) + GetDayOfWeek(First(yyyymmdd));
def period = Floor(day_number / 7);
def cond = 0 < period - period[1];
profile vol = VolumeProfile("startNewProfile" = cond, "onExpansion" = no);
vol.Show();
plot b = vol.GetHighest();

This script plots the High price for each weekly Volume profile.

DataProfile
GetHighestValueArea

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Profiles/GetHighestValueArea
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
DataProfile
GetHighest
GetHighestValueArea
GetLowest
GetLowestValueArea
GetPointOfControl
MonkeyBars
Show
TimeProfile
VolumeProfile
Stock Fundamentals
Others
GetHighestValueArea
GetHighestValueArea ();    
Description

Returns the highest price of the profile's Value Area.

Example
def yyyymmdd = GetYYYYMMDD();
def day_number = DaysFromDate(First(yyyymmdd)) + GetDayOfWeek(First(yyyymmdd));
def period = Floor(day_number / 7);
def cond = 0 < period - period[1];
profile vol = VolumeProfile("startNewProfile" = cond, "onExpansion" = no);
vol.Show("va color" = Color.YELLOW);
plot b = vol.GetHighestValueArea();

This script plots the highest price of each weekly Volume profile's Value Area.

GetHighest
GetLowest

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Profiles/GetLowest
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
DataProfile
GetHighest
GetHighestValueArea
GetLowest
GetLowestValueArea
GetPointOfControl
MonkeyBars
Show
TimeProfile
VolumeProfile
Stock Fundamentals
Others
GetLowest
GetLowest ();    
Description

Returns the lowest price value reached by the instrument within the time period for which the profile is accumulated.

Example
def yyyymmdd = GetYYYYMMDD();
def day_number = DaysFromDate(First(yyyymmdd)) + GetDayOfWeek(First(yyyymmdd));
def period = Floor(day_number / 7);
def cond = 0 < period - period[1];
profile vol = VolumeProfile("startNewProfile" = cond, "onExpansion" = no);
vol.Show();
plot b = vol.GetLowest();

This script plots the Low price for each weekly Volume profile.

GetHighestValueArea
GetLowestValueArea

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Profiles/GetLowestValueArea
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
DataProfile
GetHighest
GetHighestValueArea
GetLowest
GetLowestValueArea
GetPointOfControl
MonkeyBars
Show
TimeProfile
VolumeProfile
Stock Fundamentals
Others
GetLowestValueArea
GetLowestValueArea ();    
Description

Returns the lowest price of the profile's Value Area.

Example
def yyyymmdd = GetYYYYMMDD();
def day_number = DaysFromDate(First(yyyymmdd)) + GetDayOfWeek(First(yyyymmdd));
def period = Floor(day_number / 7);
def cond = 0 < period - period[1];
profile vol = VolumeProfile("startNewProfile" = cond, "onExpansion" = no);
vol.Show("va color" = Color.YELLOW);
plot b = vol.GetLowestValueArea();

This script plots the lowest price of each weekly Volume profile's Value Area.

GetLowest
GetPointOfControl

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Profiles/GetPointOfControl
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
DataProfile
GetHighest
GetHighestValueArea
GetLowest
GetLowestValueArea
GetPointOfControl
MonkeyBars
Show
TimeProfile
VolumeProfile
Stock Fundamentals
Others
GetPointOfControl
GetPointOfControl ();    
Description

Returns the price value of the Point of Control level closest to the middle of profile's price range.

Example
def yyyymmdd = GetYYYYMMDD();
def day_number = DaysFromDate(First(yyyymmdd)) + GetDayOfWeek(First(yyyymmdd));
def period = Floor(day_number / 7);
def cond = 0 < period - period[1];
profile tpo = TimeProfile("startNewProfile" = cond, "onExpansion" = no);
tpo.Show();
plot b = tpo.GetPointOfControl();

This script displays the Point of Control plot for weekly TPO profiles.

GetLowestValueArea
MonkeyBars

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Profiles/MonkeyBars
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
DataProfile
GetHighest
GetHighestValueArea
GetLowest
GetLowestValueArea
GetPointOfControl
MonkeyBars
Show
TimeProfile
VolumeProfile
Stock Fundamentals
Others
MonkeyBars
MonkeyBars ( IDataHolder timeInterval , String symbol , double pricePerRow , IDataHolder startNewProfile , int onExpansion , int numberOfProfiles , double the playground percent , boolean emphasize first digit , String volumeProfileShowStyle , double volumePercentVA , boolean show initial balance , int initial balance range );    
Default values:
symbol: getSymbol()
pricePerRow: PricePerRow.AUTOMATIC
onExpansion: Yes
numberOfProfiles: "all"
the playground percent: 70.0
emphasize first digit: No
volumeProfileShowStyle: MonkeyVolumeShowStyle.NONE
volumePercentVA: 70.0
show initial balance: Yes
initial balance range: 3
Description

Calculates the Monkey Bars profile with user-defined parameters.

Input parameters
Parameter	Default value	Description
timeInterval	-	Defines an ordinal number of aggregation period. The first decade is displayed as digits 1-2..-9-0 in the first palette color, the second decade is displayed as digits 1-2..-9-0 in the second palette color, and so on.
symbol	current symbol	Defines symbol to calculate Monkey Bars for.
pricePerRow	PricePerRow.AUTOMATIC	Defines the "height" (price range) of each row of Monkey Bars. This value can be defined by an actual price range or a PricePerRow constant.
startNewProfile	-	Defines condition: when it is true, the monkeyBars function is given a trigger signal to calculate the new profile.
onExpansion	Yes	Defines whether or not to show Monkey Bars on the expansion area of the chart.
numberOfProfiles	"all"	Defines the number of profiles to be displayed if onExpansion is set to no. If onExpansion is set to yes then this parameter is ignored and only one profile is shown.
the playground percent	70.0	Defines the percentage of the trading activity for which The Playground is determined.
emphasize first digit	No	Defines whether or not to highlight the opening digit of each period in bold.
volumeProfileShowStyle	MonkeyVolumeShowStyle.NONE	Defines Monkey Bars sections that will be complemented with Volume Profile histogram. Use a MonkeyVolumeShowStyle constant for this purpose. ALL will add the histogram to each section; LAST, to the last one, and NONE will not display the histograms.
volumePercentVA	70.0	Defines the percentage of the trading activity for which the Value Area is determined for Volume profile. If NONE is chosen for volumeProfileShowStyle, this input parameter will be ignored.
showInitialBalance	Yes	Defines whether or not to mark Initial Balance with a bracket. Initial Balance is a High-Low range of first several bars.
initialBalanceRange	3	Defines the number of bars for which the Initial Balance is marked if show initial balance is set to yes. If show initial balance is set to no, this parameter is ignored.
Example
def yyyymmdd = GetYYYYMMDD();
def timeInterval = GetDayOfMonth(yyyymmdd);
def allchart = 0;
profile monkey = MonkeyBars(timeInterval, "startNewprofile"=allchart);
monkey.Show();

This script displays Monkey Bars with 1 day aggregation period for the whole chart.

GetPointOfControl
Show

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Profiles/Show
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
DataProfile
GetHighest
GetHighestValueArea
GetLowest
GetLowestValueArea
GetPointOfControl
MonkeyBars
Show
TimeProfile
VolumeProfile
Stock Fundamentals
Others
Show
Show ( CustomColor color , CustomColor poc color , CustomColor va color , double opacity , CustomColor open color , CustomColor close color , CustomColor ib color , CustomColor volume color , CustomColor volume va color , CustomColor volume poc color );    
Default values:
color: Color.PLUM
poc color: Color.CURRENT
va color: Color.CURRENT
opacity: 50.0
open color: Color.CURRENT
close color: Color.CURRENT
ib color: Color.CURRENT
volume color: Color.PLUM
volume va color: Color.CURRENT
volume poc color: Color.CURRENT
Description

This function controls visibility and color scheme of Time, Volume, and Monkey Bars profiles. Note that profiles calculated by the corresponding functions will only be visible if the Show function is applied to them.

The color parameter defines the main color of Time and Volume profile bars.

The poc color parameter defines the color of the Point of Control.

The va color parameter defines the color of the Value Area.

The opacity parameter sets the degree of histogram opacity, in percent.

The open color parameter defines the color of the square marking the Monkey Bars' Open price.

The close color parameter defines the color of the arrow marking the Monkey Bars' Close price.

The ib color parameter only affects MonkeyBars function. It defines the color of Initial Balance bracket.

The volume color parameter only affects MonkeyBars function. It defines the color of Volume Profile if you chose to complement Monkey Bars with it.

The volume va color parameter only affects volume poc color parameter. Color.CURRENT is used for any of the elements (profile itself, point of control, value area), that element is not displayed.

 

Input parameters
Parameter	Default value	Description
color	Color.PLUM	Defines the main color of Time and Volume profile bars.
poc color	Color.CURRENT	Defines the color of Point of Control.
va color	Color.CURRENT	Defines the color of Value Area.
opacity	50.0	Defines the degree of histogram opacity, in percent.
open color	Color.CURRENT	Defines the color of the square marking the Monkey Bars' Open price.
close color	Color.CURRENT	Defines the color of the square marking the Monkey Bars' Close price.
ib color	Color.CURRENT	Only affects MonkeyBars function. It defines the color of Initial Balance bracket.
volume color	Color.PLUM	Only affects MonkeyBars function. It defines the color of Volume Profile if you chose to complement Monkey Bars with it.
volume va color	Color.CURRENT	Only affects MonkeyBars function. It defines the color of the Value Area of Volume Profile if you chose to complement Monkey Bars with it.
volume poc color	Color.CURRENT	Only affects MonkeyBars function. It defines the color of the Point of Control of Volume Profile if you chose to complement Monkey Bars with it.
Example
def bn = BarNumber();
def start = 0;
profile mb = MonkeyBars(timeInterval = bn, startNewProfile = start, volumeProfileShowStyle = MonkeyVolumeShowStyle.ALL);
mb.Show("volume color" = Color.RED, "volume va color" = Color.WHITE, "volume poc color" = Color.GREEN);

This script displays Monkey Bars with flipped Volume Profile. Volume Profile is displayed in red color with white Value Area and green Point of Control.

MonkeyBars
TimeProfile

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Profiles/TimeProfile
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
DataProfile
GetHighest
GetHighestValueArea
GetLowest
GetLowestValueArea
GetPointOfControl
MonkeyBars
Show
TimeProfile
VolumeProfile
Stock Fundamentals
Others
TimeProfile
TimeProfile ( String symbol , double pricePerRow , IDataHolder startNewProfile , int onExpansion , int numberOfProfiles , double value area percent );    
Default values:
symbol: getSymbol()
pricePerRow: PricePerRow.AUTOMATIC
onExpansion: Yes
numberOfProfiles: "all"
value area percent: 70.0
Description

Displays the time price opportunity (TPO) profile with user-defined calculation parameters.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol to calculate the TPO profile for.
pricePerRow	PricePerRow.AUTOMATIC	Defines the "height" (price range) of each row of the profile. This value can be defined by an actual price range or a PricePerRow constant.
startNewProfile	-	

Defines condition: when it is true, the function is given a signal to calculate a new profile.

onExpansion	Yes	Defines whether or not to show the profile on expansion area of the chart.
numberOfProfiles	"all"	Defines the number of profiles to be displayed if onExpansion is set to no. If onExpansion is set to yes then this parameter is ignored and only one profile is shown.
value area percent	70.0	Defines the percentage of the trading activity for which the Value Area is determined.
Example
def allchart = 0;
profile tpo = TimeProfile("startnewprofile"=allchart);
tpo.Show("color"=Color.BLUE);

This script plots TPO profile study (colored blue) that aggregates all chart data on the right expansion.

Show
VolumeProfile

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Profiles/VolumeProfile
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
DataProfile
GetHighest
GetHighestValueArea
GetLowest
GetLowestValueArea
GetPointOfControl
MonkeyBars
Show
TimeProfile
VolumeProfile
Stock Fundamentals
Others
VolumeProfile
VolumeProfile ( String symbol , double pricePerRow , IDataHolder startNewProfile , int onExpansion , int numberOfProfiles , double value area percent );    
Default values:
symbol: getSymbol()
pricePerRow: PricePerRow.AUTOMATIC
onExpansion: Yes
numberOfProfiles: "all"
value area percent: 70.0
Description

Displays the volume profile with user-defined calculation parameters.

The symbol parameter defines a symbol to calculate the volume profile for.

The pricePerRow parameter defines the "height" (price range) of each row of the profile. This value can be defined by an actual price range or a PricePerRow constant.

The startNewProfile parameter defines a condition; when it is true, the function is given a trigger signal to calculate the new volume profile.

The onExpansion parameter defines whether or not the profile is shown on the expansion area of the chart.

The numberOfProfiles parameter defines the number of profiles to be displayed if onExpansion is set to no. If onExpansion is set to yes then this parameter is ignored and only one profile is shown.

The value area percent parameter sets the percentage of the trading activity for which the Value Area is determined.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol to calculate the volume profile for.
pricePerRow	PricePerRow.AUTOMATIC	Defines the "height" (price range) of each row of the profile. This value can be defined by an actual price range or a PricePerRow constant.
startNewProfile	-	Defines condition: when it is true, the function is given a trigger signal to calculate the new profile.
onExpansion	Yes	Defines whether or not to show the profile on expansion area of the chart.
numberOfProfiles	"all"	Defines the number of profiles to be displayed if onExpansion is set to no. If onExpansion is set to yes then this parameter is ignored and only one profile is shown.
value area percent	70.0	Defines the percentage of the trading activity for which the Value Area is determined.
Example
def allchart = 0;
profile vol = VolumeProfile("startnewprofile"=allchart);
vol.Show("color"=Color.YELLOW);

This script plots Volume profile study (colored yellow) that aggregates all chart data on the right expansion.

TimeProfile
Stock Fundamentals

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Statistical
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Correlation
Covariance
Inertia
InertiaAll
LinDev
StDev
StDevAll
StErr
StErrAll
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Statistical
Here is the full list of the statistical functions:
Correlation
Covariance
Inertia
InertiaAll
LinDev
StDev
StDevAll
StErr
StErrAll
Mathematical and Trigonometric
Correlation
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Statistical/Correlation
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Correlation
Covariance
Inertia
InertiaAll
LinDev
StDev
StDevAll
StErr
StErrAll
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Correlation
Correlation ( IDataHolder data1 , IDataHolder data2 , int length );    
Default values:
length: 10
Description

Returns the correlation coefficient between the data1 and data2 variables for the last length bars.

General Information

Correlation defines the relation between two variables. See the following example to learn how the coefficient is calculated.

Input parameters
Parameter	Default value	Description
data1	-	Defines the first of the two variables for which the correlation is calculated.
data2	-	Defines the second of the two variables for which the correlation is calculated.
length	10	Defines the period on which the correlation is calculated.
Example
script correlationTS {
    input data1 = close;
    input data2 = close;
    input length = 12;
    plot CorrelationTS = Covariance(data1, data2, length) / ( StDev(data1, length) * StDev(data2, length) );
}

declare lower;
input length = 10;
input secondSymbol = "SPX";
plot Correlation1 = Correlation(close, close(secondSymbol), length);
plot Correlation2 = CorrelationTS(close, close(secondSymbol), length);

Statistical
Covariance

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Statistical/Covariance
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Correlation
Covariance
Inertia
InertiaAll
LinDev
StDev
StDevAll
StErr
StErrAll
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Covariance
Covariance ( IDataHolder data1 , IDataHolder data2 , int length );    
Default values:
length: 10
Description

Returns the covariance coefficient between the data1 and data2 variables for the last length bars.

General Information

Covariance defines whether two variables have the same trend or not. If the covariance is positive, then the two values move in the same direction, if negative the two values move inversely. The covariance formula is provided in the following example.

Input parameters
Parameter	Default value	Description
data1	-	Defines the first of the two variables for which the covariance is calculated.
data2	-	Defines the second of the two variables for which the covariance is calculated.
length	10	Defines the period on which the covariance is calculated.
Example
script covarianceTS {
    input data1 = close;
    input data2 = close;
    input length = 12;
    plot CovarianceTS = Average(data1 * data2, length) - Average(data1, length) * Average(data2, length);
}

declare lower;
input length = 10;
input secondSymbol = "SPX";
plot Covariance1 = Covariance(close, close(secondSymbol), length);
plot Covariance2 = CovarianceTS(close, close(secondSymbol), length);

Correlation
Inertia

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Statistical/Inertia
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Correlation
Covariance
Inertia
InertiaAll
LinDev
StDev
StDevAll
StErr
StErrAll
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Inertia
Inertia ( IDataHolder data , int length );    
Description

Draws the linear regression curve using the least-squares method to approximate data for each set of bars defined by the length parameter. The resulting interpolation function for each set of bars is defined by equation: y = a * current_bar + b . See the following example for details.

Input parameters
Parameter	Default value	Description
data	-	Defines the variable for which the linear regression curve is calculated.
length	-	Defines the period on which the approximation method is applied.
Example
script inertiaTS {
    input y = close;
    input n = 20;
    def x = x[1] + 1;
    def a = (n * Sum(x * y, n) - Sum(x, n) * Sum(y, n) ) / ( n * Sum(Sqr(x), n) - Sqr(Sum(x, n)));
    def b = (Sum(Sqr(x), n) * Sum(y, n) - Sum(x, n) * Sum(x * y, n) ) / ( n * Sum(Sqr(x), n) - Sqr(Sum(x, n)));
    plot InertiaTS = a * x + b;
}

input length = 20;
plot LinReg1 = Inertia(close, length);
plot LinReg2 = InertiaTS(close, length);

Draws the linear regression plot for the close value for the defined set of bars.

Covariance
InertiaAll

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Statistical/InertiaAll
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Correlation
Covariance
Inertia
InertiaAll
LinDev
StDev
StDevAll
StErr
StErrAll
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
InertiaAll
InertiaAll ( IDataHolder data , int length , int startDate , int startTime , double extendToLeft , double extendToRight );    
Default values:
length: all chart
startDate: 0
startTime: 0
extendToLeft: No
extendToRight: No
Description

Draws the linear regression function either for the entire plot or for the interval defined by the length parameter. If you specify length, the approximation is applied only for the last length bars of the plot, otherwise the approximation is applied for the entire plot and it is calculated based on all bars from the plot. See the Inertia function for more information.

The startDate (specified in the YYYYMMDD format) and startTime (specified in the HHMM format) define the date and time for the starting point of linear regression. These parameters override any value of the length if the startDate is non-zero.

By default, the function will return Double.NaN at any moment in time outside the interval used for calculation of linear regression. This behavior can be changed by using non-zero values of extendToLeft and extendToRight parameters.

Input parameters
Parameter	Default value	Description
data	-	Defines the variable for which the linear regression is calculated.
length	all chart	If specified, defines number of the last bars for which the curve is plotted, otherwise, the curve is plotted for the whole chart.
startDate	0	If specified, defines the date of starting point for calculation of linear regression, in the YYYYMMDD format.
startTime	0	If specified, defines the time of starting point for calculation of linear regression, in the YYYYMMDD format.
extendToLeft	No	Defines whether or not to extend the linear regression to the left of the end point.
extendToRight	-	Defines whether or not to extend the linear regression to the right of the end point.
Example
input length = 20;
plot MiddleLR = InertiaAll(close, length);

The example draws the linear regression for the close value for the defined number of last bars.

Inertia
LinDev

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Statistical/LinDev
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Correlation
Covariance
Inertia
InertiaAll
LinDev
StDev
StDevAll
StErr
StErrAll
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
LinDev
LinDev ( IDataHolder data , int length );    
Default values:
length: 12
Input parameters
Parameter	Default value	Description
data	-	Defines the variable for which the standard deviation is calculated.
length	12	Defines the period on which the standard deviation is calculated.
Description

Returns the linear deviation of data for the last length bars.

General Information

Linear deviation measures the average absolute difference between the mean and the current value.

Example
declare lower;
input length = 10;
plot LinearDev = LinDev(close, length);

The code draws the linear deviation plot for the current symbol for the defined number of bars.

Example 2
script LinDevTS {
    input data = close;
    input length = 12;
    def avgData = Average(data, length);
    plot LinDevTS = ( fold i = 0 to length with LD do LD + AbsValue(avgData - GetValue(data, i)) ) / length;
}

declare lower;

input length = 12;

plot LinDev1 = LinDev(close, length);
plot LinDev2 = LinDevTS(close, length);

InertiaAll
StDev

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Statistical/StDev
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Correlation
Covariance
Inertia
InertiaAll
LinDev
StDev
StDevAll
StErr
StErrAll
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
StDev
StDev ( IDataHolder data , int length );    
Default values:
length: 12
Description

Returns the standard deviation of data for the last length bars.

General Information

Standard deviation measures how widely values range from the average value. Standard deviation is calculated as a square root of variance, which is the average of the squared deviations from the mean.

Input parameters
Parameter	Default value	Description
data	-	Defines the variable for which the standard deviation is calculated.
length	12	Defines the period on which the standard deviation is calculated.
Example
script StDevTS {
    input data = close;
    input length = 12;
    def avgData = Average(data, length);
    plot StDevTS1 = Sqrt( (fold i = 0 to length with SD do SD + Sqr(GetValue(data, i) - avgData) ) / length);
    plot StDevTS2 = Sqrt(Average(Sqr(data), length) - Sqr(Average(data, length)));
}
declare lower;
input length = 10;
plot StDev1 = StDev(close, length);
plot StDev2 = StDevTS(close, length).StDevTS1;
plot StDev3 = StDevTS(close, length).StDevTS2;

LinDev
StDevAll

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Statistical/StDevAll
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Correlation
Covariance
Inertia
InertiaAll
LinDev
StDev
StDevAll
StErr
StErrAll
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
StDevAll
StDevAll ( IDataHolder data , int length , int startDate , int startTime , double extendToLeft , double extendToRight );    
Default values:
length: all chart
startDate: 0
startTime: 0
extendToLeft: No
extendToRight: No
Description

Returns the standard deviation of data for the entire plot or for the interval of the last bars defined by the length parameter. The difference of this function from StDev is that the output result for the last bar is used for the whole interval calculated.

If the length parameter is not specified, the function is calculated for the entire plot.

The startDate (specified in the YYYYMMDD format) and startTime (specified in the HHMM format) define the date and time for the starting point of linear regression. These parameters override any value of the length if startDate is non-zero.

By default, the function will return Double.NaN at any moment in time outside the interval used for calculation of linear regression. This behavior can be changed by using non-zero values of extendToLeft and extendToRight parameters.

Input parameters
Parameter	Default value	Description
data	-	Defines the variable for which the standard deviation is calculated.
length	all chart	If specified, defines number of the last bars for which the curve is plotted, otherwise, the curve is plotted for the whole chart.
startDate	0	If specified, defines the date of starting point for calculation of standard deviation, in the YYYYMMDD format.
startTime	0	If specified, defines the time of starting point for calculation of standard deviation, in the YYYYMMDD format.
extendToLeft	No	Defines whether or not to extend the standard deviation curve to the left of the end point.
extendToRight	No	Defines whether or not to extend the standard deviation curve to the right of the end point.
Example
input price = close;

def regression = InertiaAll(price, 30);
def stdDeviation = StDevAll(price, 30);

plot UpperLine = regression + stdDeviation;
plot LowerLine = regression - stdDeviation;

The example draws the Standard Deviation Channel, which is the linear regression channel spaced by standard deviation. The deviation channel is based on price data for the last 30 bars.

StDev
StErr

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Statistical/StErr
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Correlation
Covariance
Inertia
InertiaAll
LinDev
StDev
StDevAll
StErr
StErrAll
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
StErr
StErr ( IDataHolder data , int length );    
Default values:
length: 12
Description

Returns the standard error calculated for the last length bars from current bar. Returns the standard deviation between data and linear regression of data.

Input parameters
Parameter	Default value	Description
data	-	Defines the variable for which the standard error is calculated.
length	12	Defines the period on which the standard error is calculated.
Example
declare lower;
input length = 10;
plot StdError = StErr(close, length);

The example calculates the standard error of close values for the defined number of bars.

StDevAll
StErrAll

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Statistical/StErrAll
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Correlation
Covariance
Inertia
InertiaAll
LinDev
StDev
StDevAll
StErr
StErrAll
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
StErrAll
StErrAll ( IDataHolder data , int length , int startDate , int startTime , double extendToLeft , double extendToRight );    
Default values:
length: all chart
startDate: 0
startTime: 0
extendToLeft: No
extendToRight: No
Description

Returns the standard error of data around the regression line for the entire plot or for the interval of last bars defined by the length parameter. The difference of thIS function from StErr is that the output result for the last bar is used for the whole interval calculated.

If the length parameter is not specified, the function is calculated for the entire plot.

The startDate (specified in the YYYYMMDD format) and startTime (specified in the HHMM format) define the date and time for the starting point of linear regression. These parameters override any value of the length if the startDate is non-zero.

By default, the function will return Double.NaN at any moment in time outside the interval used for calculation of linear regression. This behavior can be changed by using non-zero values of extendToLeft and extendToRight parameters.

Input parameters
Parameter	Default value	Description
data	-	Defines the variable for which the standard error is calculated.
length	all chart	If specified, defines number of the last bars for which the curve is plotted, otherwise, the curve is plotted for the whole chart.
startDate	0	If specified, defines the date of starting point for calculation of standard error, in the YYYYMMDD format.
startTime	0	If specified, defines the time of starting point for calculation of standard error, in the YYYYMMDD format.
extendToLeft	No	Defines whether or not to extend the standard error curve to the left of the end point.
extendToRight	No	Defines whether or not to extend the standard error curve to the right of the end point.
Example
input price = close;

def regression = InertiaAll(price);
def stdError = StErrAll(price);

plot UpperLine = regression + stdError;
plot LowerLine = regression - stdError;

The example draws the Standard Error Channel which is the linear regression channel spaced by a standard error. The error channel is based on the price data for the last 30 bars.

StErr
Date and Time

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
Stock Fundamentals
The Stock Fundamentals group functions return values of financial statement metrics of publicly quoted companies. By default, the values are returned for the currently selected symbol and are based on the annual reporting data. Some of the functions can return the values based on quarterly reporting data (see the article on the FiscalPeriod.QUARTER constant).
The following functions are currently available in the Stock Fundamentals group:
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Profiles
BookValuePerShare
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/BookValuePerShare
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
BookValuePerShare
BookValuePerShare ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The BookValuePerShare function returns the current book value of a company divided by the number of its outstanding shares. In the event of company liquidation, this is the amount of money to be allocated to a holder for each common share held. The value is calculated based on the annual fiscal data and is by default returned for the currently selected symbol. To specify a different symbol for this function, modify the value of the symbol input parameter. The FiscalPeriod.QUARTER constant is not compatible with the fiscalPeriod input parameter of this function.

Stock Fundamentals
CurrentRatio

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/CurrentRatio
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
CurrentRatio
CurrentRatio ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The CurrentRatio function returns the ratio of a company's total assets to its total current liabilities. By default, the value is returned for the currently selected symbol and based on the annual reporting data. To specify a different symbol for this function, modify the value of the symbol input parameter. To use quarterly data instead of annual, assign the FiscalPeriod.QUARTER constant to the fiscalPeriod input parameter.

BookValuePerShare
DividendPayout

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/DividendPayout
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
DividendPayout
DividendPayout ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The DividendPayout function returns the ratio of a company's common dividends to that same company's net income less bottom line and preferred dividend requirement, expressed in percent. The value is calculated based on the annual fiscal data and is by default returned for the currently selected symbol. To specify a different symbol for this function, modify the value of the symbol input parameter. The FiscalPeriod.QUARTER constant is not compatible with the fiscalPeriod input parameter of this function.

CurrentRatio
DividendsPerShareTTM

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/DividendsPerShareTTM
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
DividendsPerShareTTM
DividendsPerShareTTM ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The DividendsPerShareTTM function returns the value of trailing 12-month dividends per share for the specified symbol. The trailing 12-month dividends per share is calculated as the ratio of total dividends paid out by a company to the number of its outstanding shares of common stock over the last 12 months. By default, the value is returned for the currently selected symbol and based on the annual reporting data. To specify a different symbol for this function, modify the value of the symbol input parameter. To use quarterly data instead of annual, assign the FiscalPeriod.QUARTER constant to the fiscalPeriod input parameter.

DividendPayout
EarningsPerShareTTM

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/EarningsPerShareTTM
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
EarningsPerShareTTM
EarningsPerShareTTM ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The EarningsPerShareTTM function returns the value of trailing 12-month earnings per share for the specified symbol. The trailing 12-month earnings per share is calculated as the ratio of company's profit to the number of its outstanding shares of common stock over the last 12 months. By default, the value is returned for the currently selected symbol and based on the annual reporting data. To specify a different symbol for this function, modify the value of the symbol input parameter. To use quarterly data instead of annual, assign the fiscalPeriod.QUARTER constant to the fiscalPeriod input parameter.

DividendsPerShareTTM
FinancialLeverage

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/FinancialLeverage
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
FinancialLeverage
FinancialLeverage ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The FinancialLeverage functions returns the ratio of a company's total assets to its common equity. By default, the value is returned for the currently selected symbol and based on the annual reporting data. To specify a different symbol for this function, modify the value of the symbol input parameter. To use quarterly data instead of annual, assign the FiscalPeriod.QUARTERLY constant to the fiscalPeriod input parameter.

EarningsPerShareTTM
FixedChargeCoverageRatio

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/FixedChargeCoverageRatio
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
FixedChargeCoverageRatio
FixedChargeCoverageRatio ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The FixedChargeCoverageRatio function returns the ratio of a company's earnings before interest and taxes (EBIT) to that same company's fixed charges (interest expense on debt and preferred dividends including tax). By default, the value is returned for the current symbol and based on the annual reporting data. To specify a different symbol for this function, modify the value of the symbol input parameter. To use quarterly data instead of annual, assign the FiscalPeriod.QUARTERLY constant to the fiscalPeriod input parameter.

FinancialLeverage
FreeCashFlowPerShare

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/FreeCashFlowPerShare
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
FreeCashFlowPerShare
FreeCashFlowPerShare ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The FreeCashFlowPerShare function returns the ratio of free cash flow to the number of outstanding shares for the specified symbol. The free cash flow is calculated as cash flow from operating activities less capital expenditures and total dividends paid. The value is calculated based on the annual fiscal data and is by default returned for the currently selected symbol. To specify a different symbol for this function, modify the value of the symbol input parameter. The FiscalPeriod.QUARTER constant is not compatible with the fiscalPeriod input parameter of this function.

FixedChargeCoverageRatio
GrossProfitMargin

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/GrossProfitMargin
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
GrossProfitMargin
GrossProfitMargin ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The GrossProfitMargin function returns the ratio of a company's gross income to its net sales or revenues. By default, the value is returned for the currently selected symbol and based on the annual reporting data. To specify a different symbol for this function, modify the value of the symbol input parameter. To use quarterly data instead of annual, assign the FiscalPeriod.QUARTER constant to the fiscalPeriod input parameter.

FreeCashFlowPerShare
InterestRate

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/InterestRate
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
InterestRate
TaxRate ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The InterestRate function returns the ratio of a company's interest expense on debt to the debt amount, expressed in percent. The debt amount is calculated as the sum of the short-term debt, the current portion of the long-term debt, and the long-term debt. The value is calculated based on the annual fiscal data and is by default returned for the currently selected symbol. To specify a different symbol for this function, modify the value of the symbol input parameter. The FiscalPeriod.QUARTER constant is not compatible with the fiscalPeriod input parameter of this function.

GrossProfitMargin
InventoryTurnover

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/InventoryTurnover
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
InventoryTurnover
InventoryTurnover ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The InventoryTurnover function returns the ratio of cost of goods sold by a company to the average of last year's and current year's inventories. By default, this value is calculated for the currently selected symbol. To specify a different symbol for this function, modify the value of the symbol input parameter. The function only uses yearly fiscal data so the FiscalPeriod.QUARTER constant is not compatible with its input parameter fiscalPeriod.

InterestRate
LongTermDebtToCapital

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/LongTermDebtToCapital
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
LongTermDebtToCapital
LongTermDebtToCapital ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The LongTermDebtToCapital function returns the ratio of a company's long-term debt to its total capital, expressed in percent. By default, the value is returned for the currently selected symbol. To specify a different symbol for this function, modify the value of the symbol input parameter. The function can only be calculated using yearly fiscal data so the FiscalPeriod.QUARTER constant is not compatible with its input parameter fiscalPeriod.

InventoryTurnover
NetProfitMargin

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/NetProfitMargin
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
NetProfitMargin
NetProfitMargin ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The NetProfitMargin function returns the ratio of a company's net income (income less the bottom line) to that same company's total sales or revenues, expressed in percent. By default, the value is returned for the currently selected symbol and based on the annual reporting data. To specify a different symbol for this function, modify the value of the symbol input parameter. To use quarterly data instead of annual, assign the FiscalPeriod.QUARTER constant to the fiscalPeriod input parameter.

LongTermDebtToCapital
OperatingProfitMargin

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/OperatingProfitMargin
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
OperatingProfitMargin
OperatingProfitMargin ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The OperatingProfitMargin function returns the ratio of a company's operating income to its net sales or revenues, expressed in percent. The operating income is calculated as total sales or revenues less total operating expenses. By default, the value is returned for the currently selected symbol and based on the annual reporting data. To specify a different symbol for this function, modify the value of the symbol input parameter. To use quarterly data instead of annual, assign the FiscalPeriod.QUARTER constant to the fiscalPeriod input parameter.

NetProfitMargin
QuickRatio

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/QuickRatio
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
QuickRatio
QuickRatio ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The QuickRatio function returns the ratio of a company's cash, short-term investments, and net receivables to its total current liabilities. The value is calculated based on the annual fiscal data and is by default returned for the currently selected symbol. To specify a different symbol for this function, modify the value of the symbol input parameter. The FiscalPeriod.QUARTER constant is not compatible with the fiscalPeriod input parameter of this function.

OperatingProfitMargin
ReturnOnAssets

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/ReturnOnAssets
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
ReturnOnAssets
ReturnOnAssets ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The ReturnOnAssets function calculates the ratio of a company's net income to its total assets. By default, the value is returned for the currently selected symbol and based on the annual reporting data. To specify a different symbol for this function, modify the value of the symbol input parameter. To use quarterly data instead of annual, assign the FiscalPeriod.QUARTER constant to the fiscalPeriod input parameter.

QuickRatio
ReturnOnEquity

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/ReturnOnEquity
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
ReturnOnEquity
ReturnOnEquity ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The ReturnOnEquity function returns the net income of a company expressed as a percentage of shareholders' equity (average of last year's and current year's common equity). The net income is equal to total profit less the bottom line and preferred dividend requirement. By default, the value is returned for the currently selected symbol and based on the annual reporting data. To specify a different symbol for this function, modify the value of the symbol input parameter. To use quarterly data instead of annual, assign the FiscalPeriod.QUARTER constant to the fiscalPeriod input parameter.

ReturnOnAssets
SalesPerShare

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/SalesPerShare
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
SalesPerShare
SalesPerShare ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The SalesPerShare function returns the ratio of a company's sales or revenues to the number of outstanding shares. The value is calculated based on the annual fiscal data and is by default returned for the currently selected symbol. To specify a different symbol for this function, modify the value of the symbol input parameter. The FiscalPeriod.QUARTER constant is not compatible with the fiscalPeriod input parameter of this function.

ReturnOnEquity
TaxRate

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/TaxRate
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
TaxRate
TaxRate ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The TaxRate function returns the ratio of income tax imposed on a company to the income before tax of that same company, expressed in percent. By default, the value is returned for the current symbol and based on the annual reporting data. To specify a different symbol for this function, modify the value of the symbol input parameter. To use quarterly data instead of annual, assign the FiscalPeriod.QUARTER constant to the fiscalPeriod input parameter.

SalesPerShare
TotalAssetTurnover

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Stock-Fundamentals/TotalAssetTurnover
Fundamentals
Look and Feel
Option Related
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
BookValuePerShare
CurrentRatio
DividendPayout
DividendsPerShareTTM
EarningsPerShareTTM
FinancialLeverage
FixedChargeCoverageRatio
FreeCashFlowPerShare
GrossProfitMargin
InterestRate
InventoryTurnover
LongTermDebtToCapital
NetProfitMargin
OperatingProfitMargin
QuickRatio
ReturnOnAssets
ReturnOnEquity
SalesPerShare
TaxRate
TotalAssetTurnover
Others
TotalAssetTurnover
TotalAssetTurnover ( Symbol symbol , int fiscalPeriod );    
Default values:
symbol: current symbol
fiscalPeriod: FiscalPeriod.YEAR
Description

The TotalAssetTurnover function returns the ratio of a company's net sales or revenues to its total assets. By default, the value is returned for the currently selected symbol and based on the annual reporting data. To specify a different symbol for this function, modify the value of the symbol input parameter. To use quarterly data instead of annual, assign the FiscalPeriod.QUARTER constant to the fiscalPeriod input parameter.

TaxRate
Others

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Here is the full list of the functions:
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Option Related
AccumDist
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/AccumDist
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
AccumDist
AccumDist ( IDataHolder high , IDataHolder close , IDataHolder low , IDataHolder open , IDataHolder volume );    
Description

Returns the Accumulation/Distribution value.

General Information

Some studies, for example the AccDist, use the simplified formula to calculate the Accumulation/Distribution. The formula does not contain open prices.

Input parameters
Parameter	Default value	Description
high	-	Defines the High price to be used in calculation.
close	-	Defines the Close price to be used in calculation.
low	-	Defines the Low price to be used in calculation.
open	-	Defines the Open price to be used in calculation.
volume	-	Defines the volume to be used in calculation.
Example
script AccumDistTS {
    input high = high;
    input close = close;
    input low = low;
    input open = open;
    input volume = volume;
    plot AccumDistTS = TotalSum(if high - low > 0 then (close - open) / (high - low) * volume else 0);
}

declare lower;
plot AccumDist1 = AccumDist(high, close, low, open, volume);
plot AccumDist2 = AccumDistTS(high, close, low, open, volume);

Average

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/Average
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Average
Average ( IDataHolder data , int length );    
Default values:
length: 12
Description

Returns the average value of a set of data for the last length bars. If the length of the data set is not specified, the default value is used. See the following example to learn how the average is calculated.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the average is found.
length	12	Defines period on which the average value is found.
Example 1
script AverageTS {
    input data = close;
    input length = 12;
    plot AverageTS = Sum(data, length) / length;
}

input price = close;
input length = 12;
plot SMA1 = Average(price, length);
plot SMA2 = AverageTS(price, length);

Example 2
plot SMA = Average(close, 20);

The example displays the moving average for the last 20 closing prices.

AccumDist
BodyHeight

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/BodyHeight
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
BodyHeight
BodyHeight ();    
Description

Returns the height of the candlestick body. It is equal to the absolute value of the difference between the open and close values.

Sample

Example
declare lower;
input length = 12;
plot AverageBodyHeight = Average(BodyHeight(), length);

This script plots the 12 period average body height on the lower subgraph.

Average
EMA2

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/EMA2
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
EMA2
EMA2 ( IDataHolder data , int prefetch , double smoothing factor , int First Bar );    
Default values:
prefetch: 0
First Bar: 0
Description

Returns the exponential moving average (EMA) of data with a smoothing factor. The prefetch parameter controls the number of historical data points used to initialize the EMA for the first bar. The First Bar parameter is deprecated and should not be used.

The calculation formula of the EMA2 is the same as in ExpAverage, with the only difference that you need to explicitly specify the smoothing factor instead of length.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the average is found.
prefetch	0	Defines the number of historical data points used to initialize EMA for the first bar.
smoothing factor	-	Defines smoothing factor for calculation of the average, see the formula.
First Bar	0	Deprecated parameter.
Example
input additionalBars = 0;
plot ExpAvg = EMA2(close, additionalBars, 0.2);

The code plots the exponential moving average of the close price with a smoothing factor of 0.2. Note that all studies using EMA2 fetch a necessary number of additional bars for correct initialization, thus adding more initialization data by increasing additionalBars input has little impact on the study.

BodyHeight
ExpAverage

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/ExpAverage
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
ExpAverage
ExpAverage ( IDataHolder data , int length );    
Default values:
length: 12
Description

Returns the exponential moving average (EMA) of data with length.

The formula for the calculation of the exponential moving average is recursively defined as follows:

EMA1 = price1;

EMA2 = α*price2 + (1 - α)*EMA1;

EMA3 = α*price3 + (1 - α)*EMA2;

EMAN = α*priceN + (1 - α)*EMAN-1;

where α is a smoothing coefficient equal to 2/(length + 1).

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the average is found.
length	12	Defines period on which the average is found.
Example
input price = close;
input length = 12;
plot ExpAvg = ExpAverage(price, length);

The example plots an exponential moving average of a security's Close price.

EMA2
FastKCustom

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/FastKCustom
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
FastKCustom
FastKCustom ( IDataHolder data , int length );    
Default values:
length: 14
Description

Returns values from 0 through 100 depending on a price. If the price is the lowest for the last length bars then 0 is returned. If the price is the highest for the last length bars then 100 is returned.

The function is calculated according to the following algorithm:

FastKCustom =  if Highest(close, 12) - Lowest(close, 12) > 0 then (close - Lowest(close, 12)) / (Highest(close, 12) - Lowest(close, 12))*100 else 0

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the FastK is found.
length	14	Defines the period on which the prices are translated into 0..100 range.
Example
declare lower;
input colorNormLength = 14;
plot Price = close;
def abs = AbsValue(Price);
def normVal = FastKCustom(abs, colorNormLength);
Price.AssignValueColor( CreateColor(255, 2.55 * normVal, 0) );

The FastKCustom function is used to assign a normVal value to each bar depending on its price. Zero value is assigned if the current closing price is the lowest on the last 14 bars, 100 is assigned if the current closing price is the highest on the last 14 bars. The normVal is used in the AssignValueColor function to paint a plot with colors ranging from red (255, 0,0) to yellow (255, 255, 0). The green component of the color varies depending on the current value of normVal.

 

ExpAverage
GetMarketMakerMove

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/GetMarketMakerMove
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetMarketMakerMove
GetMarketMakerMove ( String symbol );    
Default values:
symbol: getSymbol()
Description

Returns the value of Market Maker Move (MMM) indicator which calculates the expected magnitude of price movement based on market volatility. This calculation is performed using stock price, volatility differential, and time to expiration.

Input parameters
Parameter	Default value	Description
symbol	current symbol	Defines symbol for which the Market Maker Move is calculated.
Example
AddLabel(yes, "Market Maker Move:" + GetMarketMakerMove());

This script adds a chart label showing Market Maker Move value calculated for the currently selected symbol.

FastKCustom
GetMaxValueOffset

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/GetMaxValueOffset
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetMaxValueOffset
GetMaxValueOffset ( IDataHolder data , int length );    
Default values:
length: 25
Description

Returns the offset of the highest value of data for the last length bars.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the highest value is found.
length	25	Defines period on which the highest value is found.
Example
declare lower;

input length = 25;

def upIndex = GetMaxValueOffset(high, length);
def downIndex = GetMinValueOffset(low, length);

plot AroonUp = (length - upIndex) * 100.0 / length;
plot AroonDown = (length - downIndex) * 100.0 / length;

The example calculates the Aroon Indicator. The GetMaxValueOffset is used to calculate the upIndex variable that defines the number of bars appeared starting from the maximum value for the last length bars. When drawing the AroonUp, the upIndex is recorded as a percentage from the overall number of length bars.

GetMarketMakerMove
GetMinValueOffset

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/GetMinValueOffset
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
GetMinValueOffset
GetMinValueOffset ( IDataHolder data , int length );    
Default values:
length: 25
Description

Returns the offset of the lowest value of data for the last length bars.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the lowest value is found.
length	25	Defines period on which the lowest value is found.
Example
declare lower;

input length = 25;

def upIndex = GetMaxValueOffset(high, length);
def downIndex = GetMinValueOffset(low, length);

plot AroonOsc = (downIndex - upIndex) * 100.0 / length;

The example calculates the Aroon Oscillator. The GetMinValueOffset is used to calculate the downIndex variable that defines the number of bars appeared starting from the minimum value for the last length bars. Then the downIndex value and the upIndex values are used to draw the resulting AroonOsc plot.

GetMaxValueOffset
Highest

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/Highest
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Highest
Highest ( IDataHolder data , int length );    
Default values:
length: 12
Description

Returns the highest value of data for the last length bars.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the highest value is found.
length	12	Defines period on which the highest value is found.
Example
input length = 20;

plot LowerBand = Lowest(low[1], length);
plot UpperBand = Highest(high[1], length);
plot MiddleBand = (LowerBand + UpperBand) / 2;

The plots in the example illustrate the Donchian Channels system where the Lower Band and the Upper Band are calculated as the minimum low and maximum high for the previous length bars. Note that the low and high for the current bar are left out of account. In order to implement this approach the [1] index is applied to the corresponding parameters.

GetMinValueOffset
HighestAll

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/HighestAll
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
HighestAll
HighestAll ( IDataHolder data );    
Description

Returns the highest value of data for all bars in the chart.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the highest value is found.
Example
input price = close;

plot MiddleLR = InertiaAll(price);
def dist = HighestAll(AbsValue(MiddleLR - price));
plot UpperLR = MiddleLR + dist;
plot LowerLR = MiddleLR - dist;

The code draws a regression channel where the highest and the lowest borders are defined with the help of the maximum deviation between the price and regression line. The deviation is calculated for all bars using the HighestAll function.

Highest
HighestWeighted

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/HighestWeighted
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
HighestWeighted
HighestWeighted ( IDataHolder data , int length , IDataHolder coefficient );    
Default values:
length: 14
Description

Returns the highest value of data weighted with the coefficient for the last length bars.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the highest value is found.
length	14	Defines period on which the weighting is applied.
coefficient	-	Defines the weighting coefficient for data.
Example
declare lower;
input price1 = close;
input price2 = open;
def delta = price2 - price1;

plot HWBuiltin = HighestWeighted(price1, 3, delta);
plot HW = Max(Max(price1, price1[1] + delta), price1[2] + 2 * delta);

This example shows how the HighestWeighted is constructed by taking maximum of several values. The two plots coincide.

HighestAll
IsAscending

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/IsAscending
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
IsAscending
IsAscending ( IDataHolder value , int length );    
Default values:
length: 3
Description

Tests if the trend is ascending by calculating the average slope coefficient of trendlines whose start points are MidBodyVal for a specified number of bars and end points are value for current bar. If the slope is positive then the trend is considered ascending.

Input parameters
Parameter	Default value	Description
value	-	Defines data to test for uptrend conditions.
length	3	Defines period to test for uptrend conditions.
Example
AssignPriceColor(if IsAscending(close, 10) then Color.GREEN else Color.RED);

This example paints price bars in green color if the closing price in comparison to the MidBodyVal for the last 10 bars is considered ascending and in red color otherwise.

HighestWeighted
IsDescending

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/IsDescending
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
IsDescending
IsDescending ( IDataHolder value , int length );    
Default values:
length: 3
Description

Tests if the trend is descending by calculating the average slope coefficient of trendlines whose start points are MidBodyVal for a specified number of bars and end points are value for current bar. If the slope is negative then the trend is considered descending.

Input parameters
Parameter	Default value	Description
value	-	Defines data to test for downtrend conditions.
length	3	Defines period to test for downtrend conditions.
Example
plot DescBar = IsDescending(close, 10);
DescBar.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

This example draws points at the closing prices for all bars considered as descending in comparison to the MidBodyValfor the last 10 bars.

IsAscending
IsDoji

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/IsDoji
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
IsDoji
IsDoji ( int length , double bodyFactor );    
Default values:
length: 20
bodyFactor: 0.05
Description

Returns true if the current candle is Doji (i.e. its Close price and Open price are equal or almost the same) and false otherwise. Note that a candle is considered Doji if its body height does not exceed average body height multiplied by the specified factor. The average body height is calculated for a specified number of preceding candles.

Input parameters
Parameter	Default value	Description
length	20	Defines period on which average body height is calculated.
factor	0.05	Defines factor by which the average body height is multiplied.
Example
input length = 25;

def IsDoji = IsDoji(length);
plot ThreeDoji = IsDoji[2] and
                 IsDoji[1] and
                 IsDoji;

ThreeDoji.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

    

This example marks the last of three consecutive Doji candles. In this case, a candle will be considered Doji if its body height does not exceed 5% (default value) of the average body height calculated for last 25 candles.

IsDescending
IsLongBlack

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/IsLongBlack
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
IsLongBlack
IsLongBlack ( int length );    
Default values:
length: 20
Description

Returns true for the current candle if:

its close price is lower than its open price;
its body is longer than either of the shadows;
its body is longer than the average body size calculated for the specified number of preceding candles.
Input parameters
Parameter	Default value	Description
length	20	Defines period on which average body height is calculated.
Example
input length = 20;

def IsLongBlack = IsLongBlack(length);
plot TwoLongBlack = IsLongBlack[1] and
                    IsLongBlack;

TwoLongBlack.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_DOWN);
    

This example draws an arrow marking the last of two consecutive long bearish candles.

IsDoji
IsLongWhite

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/IsLongWhite
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
IsLongWhite
IsLongWhite ( int length );    
Default values:
length: 20
Description

Returns true for the current candle if:

Its Close price is higher than the Open price;
Its body is longer than each shadow;
Its body is longer than the average body size calculated for the specified number of preceding candles.
Input parameters
Parameter	Default value	Description
length	20	Defines period on which average body height is calculated.
Example
input length = 20;

def IsLongWhite = IsLongWhite(length);
plot TwoLongWhite = IsLongWhite[1] and
                    IsLongWhite;

TwoLongWhite.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_UP);
    

This example draws an arrow marking the last of two consecutive long bullish candles.

IsLongBlack
Lowest

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/Lowest
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Lowest
Lowest ( IDataHolder data , int length );    
Default values:
length: 12
Description

Returns the lowest value of data for the last length bars.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the lowest value is found.
length	12	Defines period on which the lowest value is found.
Example
declare lower;

input length = 10;

def HH = Highest(high, length);
def LL = Lowest(low, length);

plot "Williams %R" = if HH == LL then -100 else (HH - close) / (HH - LL) * (-100);

The example shows the Williams %R calculation. In particular, it is required to define the minimum low for the last length bars including the current bar. Therefore, to define the minimum, the example uses the Lowest function.

IsLongWhite
LowestAll

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/LowestAll
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
LowestAll
LowestAll ( IDataHolder data );    
Description

Returns the lowest value of data for all bars in the chart.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the lowest value is found.
Example

def HH = HighestAll(high);
def LL = LowestAll(low);

plot G1 = HH / 2;
plot G2 = (HH + LL) / 2;
plot G3 = HH / 4;
plot G4 = (HH - LL) / 4 + LL;

The example shows the Major Gann Levels which uses all chart bars to calculate the maximum high and minimum low values.

Lowest
LowestWeighted

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/LowestWeighted
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
LowestWeighted
LowestWeighted ( IDataHolder data , int length , IDataHolder coefficient );    
Default values:
length: 14
Description

Returns the lowest value of data weighted with the coefficient for the last length bars.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the lowest value is found.
length	14	Defines period on which the weighting is applied.
coefficient	-	Defines the weighting coefficient for data.
Example
declare lower;
input price1 = close;
input price2 = open;
def delta = price2 - price1;

plot LWBuiltin = LowestWeighted(price1, 3, delta);
plot LW = Min(Min(price1, price1[1] + delta), price1[2] + 2 * delta);

This example shows how the LowestWeighted is constructed by taking minimum of several values. The two plots coincide.

LowestAll
Median

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/Median
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Median
Median ( IDataHolder data , int length );    
Default values:
length: 12
Description

Returns the median value of data for the last length bars. Median value is equal to the middle element of ascendingly sorted data set if the number of elements is odd; if the number of elements is even, median value is equal to the average between the two middle elements of ascendingly sorted data set.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the median value is found.
length	12	Defines period on which the median value is found.
Example
input length = 15;
plot med = Median(high, length);

This example script plots a median High price among the last 15 bars.

LowestWeighted
MidBodyVal

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/MidBodyVal
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
MidBodyVal
MidBodyVal ();    
Description

Returns the price corresponding to the middle of the candelstick body. This price can be calculated as (open + close)/2.

Sample

Example
plot CandleBodyTop = MidBodyVal() + 0.5 * BodyHeight();
plot CandleBodyBottom = MidBodyVal() - 0.5 * BodyHeight();

This script plots two lines: the first one connecting all the candle body tops and the second one connecting all the candle body bottoms.

Median
MoneyFlow

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/MoneyFlow
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
MoneyFlow
MoneyFlow ( IDataHolder high , IDataHolder close , IDataHolder low , IDataHolder volume , int length );    
Default values:
length: 12
Description

Returns the money flow value.

Input parameters
Parameter	Default value	Description
high	-	Defines the High price to be used in calculation.
close	-	Defines the Close price to be used in calculation.
low	-	Defines the Low price to be used in calculation.
volume	-	Defines the volume to be used in calculation.
length	12	Defines the period on which the money flow value is calculated.
Example
script moneyflowTS {
    input high = high;
    input close = close;
    input low = low;
    input volume = volume;
    input length = 14;
    def price = high + close + low;
    def moneyFlow = price * volume;
    def positiveMoneyFlow = Sum(if price >price[1] then MoneyFlow else 0, length);
    def totalMoneyFlow = Sum(MoneyFlow, length);
    plot moneyflowTS = if totalMoneyFlow != 0 then 100 * positiveMoneyFlow / totalMoneyFlow else 0;
}

declare lower;
input length = 14;
plot moneyflow1 = MoneyFlow(high, close, low, volume, length);
plot moneyflow2 = MoneyFlowTS(high, close, low, volume, length);

In this example the money flow is calculated and plotted based on two different implementations that have equal results. The first implementation is based on the moneflowTS function, the second one is based on the built-in MoneyFlow function.

MidBodyVal
MovingAverage

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/MovingAverage
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
MovingAverage
MovingAverage ( int averageType , IDataHolder data , int length );    
Default values:
averageType: AverageType.Simple
length: 12
Description

Returns the average value of specified type and length for a data set. Available average types are: Simple, Exponential, Weighted, Wilder's, and Hull. Each type can be defined using AverageType constants.

Input parameters
Parameter	Default value	Description
averageType	AverageType.Simple	Defines type of average to be applied. This parameter accepts AverageType constants as value.
data	-	Defines data for which the average is found.
length	12	Defines period on which the average value is found.
Example
input price = FundamentalType.CLOSE;
input aggregationPeriod = AggregationPeriod.DAY;
input length = 12;
input averageType = AverageType.SIMPLE;

plot MovAvg = MovingAverage(averageType, Fundamental(price, period = aggregationPeriod), length); 

This example script plots a moving average of specified type and length for specified fundamental data.

MoneyFlow
TrueRange

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/TrueRange
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
TrueRange
TrueRange ( IDataHolder high , IDataHolder close , IDataHolder low );    
Description

Returns the true range (TR).

TR is the greatest of the following:

the difference between the current high and the current low
the difference between the current high and the previous close
the difference between the previous close and the current low
Input parameters
Parameter	Default value	Description
high	-	Defines the High price to be used in calculation.
close	-	Defines the Close price to be used in calculation.
low	-	Defines the Low price to be used in calculation.
Example
script TrueRangeTS {
    input high = high;
    input close = close;
    input low = low;
    plot TrueRangeTS = Max(close[1], high) - Min(close[1], low);
}

plot TrueRange1 = TrueRange(high, close, low);
plot TrueRange2 = TrueRangeTS(high, close, low);

MovingAverage
Ulcer

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/Ulcer
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
Ulcer
Ulcer ( IDataHolder data , int length );    
Default values:
length: 14
Description

Returns the Ulcer Index of data for the last length bars. The Ulcer Index is equal to root mean square of price percentage retracement which is calculated using the formula:

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the Ulcer Index is found.
length	14	Defines period on which the Ulcer Index is found.
Example
declare lower;
input length = 100;
input risk_free_rate = 0.01;

def somedate = 20000101;
def growth = close - close[length];
def days = DaysFromDate(somedate) - DaysFromDate(somedate)[length];
def annualreturn = growth / close[length] * 365 / days;

plot MartinRatio = (annualreturn - risk_free_rate) * 100 / Ulcer(close, length);

This example calculates the Martin Ratio for an instrument.

TrueRange
WildersAverage

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/WMA
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
WMA
WMA ( IDataHolder data , int length );    
Default values:
length: 9
Description

Returns Weighted Moving Average value. The Weighted Moving Average is calculated by multiplying each of the previous days' data by a weight factor. That factor is equal to the number of days past the first day. The total is then divided by the sum of the factors.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the average is found.
length	9	Defines period on which the average value is found.
Example
plot WMA = WMA(close, 20);

The example displays the weighted moving average for the last 20 closing prices.

WildersAverage
Mathematical and Trigonometric

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Functions/Tech-Analysis/WildersAverage
Fundamentals
Look and Feel
Option Related
AccumDist
Average
BodyHeight
EMA2
ExpAverage
FastKCustom
GetMarketMakerMove
GetMaxValueOffset
GetMinValueOffset
Highest
HighestAll
HighestWeighted
IsAscending
IsDescending
IsDoji
IsLongBlack
IsLongWhite
Lowest
LowestAll
LowestWeighted
Median
MidBodyVal
MoneyFlow
MovingAverage
TrueRange
Ulcer
WildersAverage
WMA
Mathematical and Trigonometric
Statistical
Date and Time
Corporate Actions
Portfolio
Profiles
Stock Fundamentals
Others
WildersAverage
WildersAverage ( IDataHolder data , int length );    
Default values:
length: 12
Description

Returns the Wilder's Moving Average of data with a smoothing coefficient that equals 1/length. The first value is calculated as the simple moving average and then all values are calculated as the exponential moving average.

The formula for the calculation of the average can be recursively defined as:

MAWilders1 = SMA(length);

MAWilders2 = α*price2 + (1 - α)*MAWilders1;

MAWilders3 = α*price3 + (1 - α)*MAWilders2;

MAWildersN = α*priceN + (1 - α)*MAWildersN-1;

where α is the smoothing coefficient equal to 1/length.

Input parameters
Parameter	Default value	Description
data	-	Defines data for which the average is found.
length	12	Defines period on which the average value is found.
Example
input length = 10;
plot WildersAvg = WildersAverage(close, length);
plot ExpAvg = EMA2(close, 0, 1 / length);

This code draws two plots: the first is a Wilder's average of the Close price, and the second is the exponential moving average with the corresponding smoothing factor. The two plots differ to a certain extent due to variance in initialization.

Ulcer
WMA

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Operators
Arithmetic
Comparison
Conditional
Indexing
Logical
Operator Precedence
Here is the full list of available operators:
Arithmetic
Comparison
Conditional
Indexing
Logical
Arithmetic
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Operators/Arithmetic
Arithmetic
Comparison
Conditional
Indexing
Logical
Operator Precedence
Arithmetic
Description

The following arithmetic opeators are available in thinkscript®:

Operator	Description
+	addition, string concatenation
-	subtraction
*	multiplication
/	division
%	remainder

All arithmetic operators are binary. Note that "+" operator is used for string concatenation, see Example 2 for details.

Example 1
declare hide_on_intraday;
AddChartBubble(getDay() % 20 == 5, high, concat("Day ", getDay()));

Draws a cloud near the 5th, 25th, 45th, etc., day of the year.

Example 2
addchartBubble(yes, 0, "hello" + "world");

This example string will add a chart bubble with specified text composed of two strings concatenated.

Comparison

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Operators/Comparison
Arithmetic
Comparison
Conditional
Indexing
Logical
Operator Precedence
Comparison
Description

Operator	Description
==	is equal to
equals	is equal to
is equal to	is equal to
!=	is not equal to
<>	is not equal to
is not equal to	is not equal to
<	is less than
is less than	is less than
>	is greater than
is greater than	is greater than
<=	is less than or equal to
is less than or equal to	is less than or equal to
>=	is greater than or equal to
is greater than or equal to	is greater than or equal to
between	between
crosses	crosses
crosses above	crosses above
crosses below	crosses below

The x between y and z statement is equal to the y <= x and x <= z  statement.

For information on using crosses, crosses above, and crosses below operators, refer to the crosses reserved word article.

For information on using the human-readable operators containing word 'is', refer to the is reserved word article.

Example 1
plot uptick = close > close[1];
plot downtick = close < close[1];
plot neutral = close equals close[1];
uptick.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_UP);
downtick.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_DOWN);
neutral.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

Marks bars with different signs depending whether the Close value was less, equal or greater than the previous one.

Example 2
input price = close;
input length = 12;
input StudyType = {default SMA, EMA};
plot Avg;
if (StudyType == StudyType.SMA) {
    Avg = Average(price, length);
} else {
    Avg = ExpAverage(price, length);
}
AddLabel(StudyType != StudyType.SMA, "Exponential moving average is displayed.");

This example uses a condition operator to choose an averaging function and to set the hiding setting of a label.

Example 3
input percent = 5;
plot Doji = AbsValue(open - close) <= (high - low) * percent / 100;
Doji.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

This example tests if the difference between the Open and Close prices does not exceed a specific percentage of the price spread.

Example 4 (String Comparison)
def a =  getSymbolPart(1) == "SPX";

def b =  getSymbolPart(1) != "GOOG";

First condition tests if the first part of a composite symbol is "SPX" and the second checks if it is not "GOOG".

Arithmetic
Conditional

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Operators/Conditional
Arithmetic
Comparison
Conditional
Indexing
Logical
Operator Precedence
Conditional
Description

The conditional operator if-then-else also known as the if-expression is applied to three values. The first operand is interpreted as a logical statement. If the statement is true, then the result of the operator equals the second operand, otherwise - the third.

Example
input price = close;
input long_average = yes;

plot SimpleAvg = Average(price, if long_average then 26 else 12);

The value passed to the averaging function is defined depending on the long_average parameter.

Comparison
Indexing

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Operators/Indexing
Arithmetic
Comparison
Conditional
Indexing
Logical
Operator Precedence
Indexing
Description

The indexing operator [] is used to access the previous or future data in an array of data. The square brackets indicate the shift against the current moment. The positive values of the shift represent the values in the past, the negative shift values represent the values in the future. The indexing operator can be applied to fundamental data, function outputs, indicator outputs, variables, etc.

Example 1
input price = close;
input shift = 5;
plot PastPrice = price[shift];
plot FuturePrice = price[-shift];

Draws shifted price plots.

Example 2
plot PastMACD = MACD().Avg[10];

Shows the smoothed MACD value 10 bars ago.

Note that you can also use verbal syntax when referencing historical data. For more information, see the Referencing Historical Data article.

Conditional
Logical

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Operators/Logical
Arithmetic
Comparison
Conditional
Indexing
Logical
Operator Precedence
Logical
Description

Operator	Description
is true	logical value
!, is false	logical NOT
and, &&	logical AND
or	logical OR

Logical operators can be applied only to numeric data. Zero(0) is interpreted as a false value; all other values are interpreted as a true value. Therefore, expression x is true returns true when x is non-zero, and false when x is zero.

Consider the following rules when using the logical operators:

Logical NOT is true when the argument is false. For some expression x, it can be written as !x or x is false.

Logical AND is true when both arguments are true. Logical OR is true when at least one argument is true.

For examples of usage of is true and is false operators, refer to the is reserved word article.

Example 1
plot LocalMinimum = low < low[1] and low < low[-1];
LocalMinimum.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_UP);

Highlights local minumums of the lowest price.

Example 2
plot signal = open == high or close == high;
signal.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_DOWN);

Highlights moments, when the open or close price is the highest.

Example 3
input bubble = yes;
AddChartBubble(bubble and barNumber() == 1, high, "Displaying a bubble");
AddLabel(!bubble, "Displaying a label");

Draws a cloud or label near the first bar depending on the parameter. The label is displayed when the the bubble parameter is set to no.

Indexing
Operator Precedence

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Operators/Operator-Precedence
Arithmetic
Comparison
Conditional
Indexing
Logical
Operator Precedence
Operator Precedence
Precedence	Operator
1	[]; from
2	!
3	*; /; %
4	+ (string concatenation)
5	+ (addition); -
6	<; is less than; >; is greater than; <=; is less than or equal to; >=; is greater than or equal to; crosses above; crosses below; crosses
7	==; equals; is equal to; !=; <>; is not equal to
8	is true; is false
9	and; &&
10	or
11	if
12	within
Operator between has precedence lower than addition or subtraction but higher than the conditional operator.
Operator + can be used for both addition and string concatenation, in which case concatenation has higher precedence than addition (4 vs. 5).
Logical
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
Choose your command from the list:
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
above
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/above
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
above
Syntax

See the crosses reserved word article.

Description

The above reserved word is used with the crosses operator to test if a value gets higher than another value.

ago

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/ago
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
ago
Syntax

<value> from 1 bar ago
<value> from <length> bars ago

Description

This reserved word is used to specify a time offset in a human-friendly syntax. For more information, see the Referencing Historical Data article.

above
and

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/and
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
and
Syntax

<condition1> and <condition2>

Description

The and logical operator is used to define complex conditions. For a complex condition to be true it is required that each condition from it is true. In order to define the operator you can also use &&. This reserved word is also used to define an interval in the between expression.

Example
plot InsideBar = high <high[1] and low > low[1];
InsideBar.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

Draws a dot near each inside price bar.

ago
bar

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/bar
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
bar
Syntax

<value> from <length> bars ago

Description

This reserved word is used to specify a time offset in a human-friendly syntax. For more information, see the Referencing Historical Data article.

Note that bar and bars reserved words can be used interchangeably.

and
bars

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/bars
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
bars
Syntax

 <value> from <length> bars ago

Description

This reserved word is used to specify a time offset in a human-friendly syntax. For more information, see the Referencing Historical Data article.

Note that bar and bars reserved words can be used interchangeably.

bar
below

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/below
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
below
Syntax

See the crosses reserved word article.

Description

The below reserved word is used with the crosses operator to test if a value becomes less than another value.

bars
between

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/between
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
between
Syntax

<parameter> between <value1> and <value2>

Description

Example
declare lower;
def isIn = close between close[1] * 0.9 and close[1] * 1.1;
plot isOut = !isIn;

In this example between is used to check whether the current closing price hits the 10% channel of the previous closing price. The isOut plot reflects the opposite condition.

below
case

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/case
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
case
Syntax

See the switch statement.

Description

The reserved word is used in combination with the switch statement to define a condition.

between
crosses

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/crosses
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
crosses
Syntax

<value1> crosses above <value2>

<value1> crosses below <value2>

<value1> crosses <value2>

Description

This reserved word is used as a human-readable version of the Crosses function. It tests if value1 gets higher or lower than value2.

Example
plot Avg = Average(close, 10);
plot ArrowUp = close crosses above Avg;
plot ArrowDown = close crosses below Avg;
plot Cross = close crosses Avg;
ArrowUp.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_UP);
ArrowDown.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_DOWN);
Cross.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

This code plots up arrows indicating the bars at which the close price gets above its 10 period average, and down arrows where the close price gets below its 10 period average. The same result can be achieved by using the Crosses function:

plot Avg = Average(close, 10);
plot ArrowUp = Crosses(close, Avg, CrossingDirection.ABOVE);
plot ArrowDown = Crosses(close, Avg, CrossingDirection.BELOW);
plot Cross = Crosses(close, Avg, CrossingDirection.ANY);
ArrowUp.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_UP);
ArrowDown.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_DOWN);
Cross.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);
Example
plot Avg = Average(close, 10);
plot Cross = close crosses Avg;
Cross.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

This code plots arrows indicating the bars at which the Close price gets higher or lower than its 10 period average. The equivalent code is:

plot Avg = Average(close, 10);
plot Cross = close crosses above Avg or close crosses below Avg;
Cross.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);
case
declare

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/declare
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
declare
Syntax

declare <supported_declaration_name>

Description

Example
declare lower;

plot PriceOsc = Average(close, 9) - Average(close, 18);

crosses
def

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/def
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
def
Syntax

def <variable_name>=<expression>;

or

def <variable_name>;

<variable_name>=<expression>;

Description

Defines a variable you would like to work with.

Example 1. Non-recursive usage
def base = Average(close, 12);

plot UpperBand = base * 1.1;
plot LowerBand = base * 0.9;

This example shows a simplified SMAEnvelope study, where the def reserved word is used to define the base. The rationale of defining this variable is to avoid double calculations (increase performance) in UpperBand and LowerBand plots, because def variable values are cached (by means of increasing memory usage).

You can separate the variable definition from its value assignment. Consider the following example:

declare lower;

input index = {default SPX, "Nasdaq Composite", NDX};

def data;

switch (index) {

case SPX:

    data = close("SPX");

case "Nasdaq Composite":

    data = close("COMP");

case NDX:

    data = close("NDX");

}

plot IndexCorrelation = Correlation(close, data, 10);

This example script plots the correlation between the current instrument's data and the data of a specified index. Values of the data variable are controlled by the selected index input parameter via the switch command.

Example 2. Recursive usage
def C = C[1] + volume;
plot CumulativeVolume = C;

This example script illustrates how def variable "C" references its own historical values, i.e., "C" designates a recursive variable. Here, the plot will represent cumulative volume starting from the beginning of time period.

Example 3. Non-recursive and recursive enumerations

You can define a variable as having a limited number of possible values (in which case this variable is called enumeration):

def trend = {default bullish, bearish};
if close > Average(close, 10) {
    trend = trend.bullish;
} else {
    trend = trend.bearish;
}

AssignBackgroundColor(if trend == trend.bullish then Color.UPTICK else if trend == trend.bearish then Color.DOWNTICK else Color.CURRENT);

This example script defines variable trend as having two possible values: bullish or bearish. The first value is assigned to this variable when the Close price is greater than its 10 period simple moving average and the second value otherwise. This variable controls the color of the background: it is filled with Uptick color when the value is "bullish" and Downtick otherwise. Note that enumerations can only use string values.

The example above shows non-recursive usage of enumerations, however, these can be used recursively:

def a = {default neutral, up, down};	### line 1: declaration of a def enumeration
a = if (close == close[1]) then a.neutral		### line 2: assignment of the values
    else if (close > close[1]) then a.up
    else if (close < close[1]) then a.down
    else a[1];
plot q;							### line 6: plot declaration
switch (a) {						### line 7: switch statement
case up:
    q = low;
case down:
    q = high;
case neutral:
    q = close;
}

The first line of the script is a declaration of a def enumeration a having values neutral, up, and down. The default keyword indicates the default value of the enumeration. If a value is not assigned to the declared variable, it will always be equal to its default neutral value. The value is assigned to the variable in the second line, followed by plot declaration. Enumerations can only have one assignment statement. Command switch defines what should be plotted based on the value of variable a.

Note that enumerations are not interchangeable. This means that you cannot assign same values to two different enumerations. Note also that both sides of statements in the enumeration assignment should be of the same type:

def a = {q, w, e, default r, t, y};
def b = {q, w, e, default r, t, y};
a = a.q;
b = b.q;
plot z = a[1] == a.q;
plot x = a == z;                                                  ### error in this line
plot y = a != if (1==2) then a else a.q;
plot w = if (1==2) then a else a.q != if (1==2) then b else b.q;  ### error in this line

declare
default

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/default
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
default
Syntax

See the enum input and switch statements.

Description

The default reserved word is used in combination with the enum input or switch statements to specify a default value.

def
do

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/do
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
do
Syntax

def <result> = fold <index> = <start> to <end> [ with <variable> [ = <init> ] ] [ while <condition> ] do <expression>; 

Description

This reserved word defines an action to be performed when calculating the fold function. For more information, see the fold reserved word article.

default
else

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/else
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
else
Syntax

See the if reserved word article.

Description

do
equal

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/equal
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
equal
Syntax

<value1> is [not] equal to <value2>

<value1> is <greater/less> than or equal to <value2>

Description

The equal reserved word is used with the is operator to test if a value is equal to another value.

else
equals

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/equals
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
equals
Syntax

equals

Description

The reserved word is used as a logic operator to test equality of values. In order to define this operator you can also use the double equals sign ==.

Example
plot Doji = open equals close;
Doji.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

The code draws points on bars having the Doji pattern (equal close and open).

equal
false

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/false
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
false
Syntax

<value> is false

Description

The false reserved word is used with the is operator to test if a condition is false.

equals
fold

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/fold
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
fold
Syntax

def <result> = fold <index> = <start> to <end> [ with <variable> [ = <init> ] ] [ while <condition> ] do <expression>; 

Description

The fold operator allows you to perform iterated calculations. The list below explains the operator's logic (variable names are taken from the sample syntax above):

1. The purpose of the fold operator is to perform an iterated calculation and assign the final value to the result variable.

2. The index variable serves as a loop counter.

3. With each iteration, the index value increases by 1; the initial value of index is set by the start parameter.  

4. Iterated calculations will be performed while the index value is less than the end parameter. Once the index value becomes equal to the end parameter, the loop is terminated without calculation.

5. Within each iteration, the operator calculates the expression and assigns the result to the variable. In the expression, you are free to use the value of index and also reference the previous value of the variable. The initial value of the variable can be specified with the init parameter. If not specified, then the variable is assigned a value of 0 before the first iteration.

6. The variable value is thus re-written after each iteration; after the last iteration, its final value is assigned to the result variable.

7. You can also add a condition within the while block of the operator. If this condition is violated, the result is assigned the last known value of variable and the loop is terminated.

Example 1
input n = 10;
plot factorial = fold index = 1 to n + 1 with p = 1 do p * index;

This example script calculates the factorial of a number.

Here, the factorial variable stores the result value of the calculation; index is the counter and its values are increased by 1 from 1 through n+1. The p is the variable whose value is re-written over iterations; its initial value is set to 1. The expression is the product of p and index. After the first iteration, p is 1*1=1. After the second iteration, it is equal to its current value (1) multiplied by current index (2), i.e., 2. After the third iteration, its current value (2) is multiplied by current index (3), yielding 6. Since the input n is set to 10, there will be 10 iterations (the loop is terminated when the index becomes equal to n+1=11), so the last value of p will be equal to 3,628,800 (a product of all numbers from 1 through 10). This is the value that is assigned to the factorial variable after the loop is complete.

Example 2
input price = close;
input length = 9;
plot SMA = (fold n = 0 to length with s do s + getValue(price, n, length - 1)) / length;

This example script calculates a simple moving average using fold.

Example 3
plot NextHigh = fold i = 0 to 100 with price = Double.NaN while IsNaN(price) do if getValue(high, -i, -99) > 40 then getValue(high, -i, -99) else Double.NaN;

This example script plots the closest high price value greater than 40 out of the next 100 bars.

false
from

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/from
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
from
Syntax

<value> from 1 bar ago

<value> from <length> bars ago

Description

This reserved word is used to specify a time offset in a human-friendly syntax. For more information, see the Referencing Historical Data article.

fold
greater

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/greater
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
greater
Syntax

<value1> is greater than [or equal to] <value2>

Description

The greater reserved word is used with the is operator to compare two values.

from
if

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/if
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
if
Syntax (if-expression)
plot <plot_name> = if <condition> then <expression1>
    else <expression2>;

plot <plot_name> = if <condition1> then <expression1>
    else if <condition2> then <expression2>
    else <expression3>;
Syntax (if-statement)
plot <plot_name>;
if <condition1> [then] {
    <plot_name> = <expression1>;
} else if <condition2> [then] {
    <plot_name> = <expression2>;
} else {
    <plot_name> = <expression3>;
}

plot <plot_name>;
if <condition1> [then] {
    <plot_name> = <expression1>;
} else {
    if <condition2> [then] {
        <plot_name> = <expression2>;
    } else {
        <plot_name> = <expression3>;
    }
}
Description

Example 1. Non-recursive usage
input price = close;
input long_average = yes;

plot SimpleAvg = Average(price, if long_average then 26 else 12);

plot ExpAvg;
if long_average {
    ExpAvg = ExpAverage(price, 26);
} else {
    ExpAvg = ExpAverage(price, 12);
}

In this example, if-expression and if-statement are used to control the length parameter of moving averages.

Example 2. Recursive usage
def myHigh;

if high > myHigh[1] {
    myHigh = high;
} else {
    myHigh = myHigh[1];
}

plot H = myHigh;

This example script plots the highest high value by comparing the high price with the variable myHigh. If the high price is greater, the value of myHigh is rewritten, otherwise the variable keeps its previous value as defined by the else branch.

greater
input

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/input
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
boolean
constant
enum
float
integer
price
string
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
input
When defining inputs take the following notes into consideration:
Inputs are displayed on the GUI in the same order as they appear in the source code.
input test = "test in lowercase";
input TEST = "test in uppercase";
Inputs can't have empty spaces in their definitions. The following code will result in compilation error.
In order to have titles displayed on the GUI with spaces you can do one of the following:
input "input name with spaces" = "ERROR";
input input_name_with_spaces = "OK";
Find the full list of inputs in the following list:
boolean
constant
enum
float
integer
price
string
if
boolean
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/input/boolean
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
boolean
constant
enum
float
integer
price
string
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
boolean
Syntax

input <input name>=<boolean_value_used_by_default>;

Description

Defines a boolean input. The default value of the input can either be "yes" or "no".

Example
input useHighLow = yes;

plot HighPrice = if useHighLow then Highest(high, 10) else Highest(close, 10);
plot LowPrice = if useHighLow then Lowest(low, 10) else Lowest(close, 10);

Draws the channel based on the highest and lowest price for the length equal to 10. Whether to use or not the high and low prices instead of the closing price can be defined using the correspondent input, which is set to "yes" by default.

input
constant

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/input/constant
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
boolean
constant
enum
float
integer
price
string
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
constant
Syntax

input <input name>=<constant_used_by_default>;

Description

Note that color constants cannot be used for input definition.

Example
input secondaryPeriod = AggregationPeriod.DAY;
plot SecondaryPeriodOpen = open(period = secondaryPeriod);

This example script draws the Open price plot with specified aggregation period.

boolean
enum

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/input/enum
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
boolean
constant
enum
float
integer
price
string
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
enum
Syntax

input <input name>={default <enum_value_used_by_default>, <enum_value_1>, ... <enum_value_N>};

Description

Defines an enum input of string values. In order to define the input, make sure that:

all values are specified in braces;
equal values are avoided;
one value (not necessarily the first) is declared default using the default reserved word;
values containing space symbols are placed in double quotes.

 

Note: enum input names are case and underscore insensitive.

Example
declare lower;

input exchange = {default NYSE, NASDAQ, AMEX};

def breadth;

switch (exchange) {

case NYSE:

    breadth = close("$UVOL") - close("$DVOL");

case NASDAQ:

    breadth = close("$UVOL/Q") - close("$DVOL/Q");

case AMEX:

    breadth = close("$UVOA") - close("$DVOA");

}

plot CVI = if isNaN(close) then Double.NaN else TotalSum(if isNaN(breadth) then 0 else breadth);

CVI.SetDefaultColor(GetColor(8));

The script above is the implementation of the Cumulative Volume Index. The enum type input defines the exchange whose data will be used in calculations, with NYSE being the default one.

constant
float

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/input/float
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
boolean
constant
enum
float
integer
price
string
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
float
Syntax

input <input name>=<float_number_used_by_default>;

Description

Defines a float input. Note that in order to define this input you need to use a fullstop as a delimiter in its default value.

Example
input percentShift = 10.0;

plot UpperBand = close * (1 + percentShift / 100);
plot LowerBand = close * (1 - percentShift / 100);

Draws the envelope based on the closing price. The percent shift value can be adjusted using the correspondent input, which is set to 10.0 by default.

enum
integer

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/input/integer
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
boolean
constant
enum
float
integer
price
string
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
integer
Syntax

input <input name>=<integer_number_used_by_default>;

Description

Defines an integer input.

Example
input length = 10;

plot SMA = Average(close, length);

Draws the SMA using the close price data. The length value can be adjusted using the correspondent input, which is set to 10 by default

float
price

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/input/price
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
boolean
constant
enum
float
integer
price
string
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
price
Syntax

input <input name>=<price_value_used_by_default>;

Description

Defines a price input. Valid parameters for the price type are:

vwap

volume

open_interest

imp_volatility

tick_count

Example
input price = close;

plot EMA = ExpAverage(price, 10);

Draws the EMA with the length equal to 10. The type of price data can be adjusted using the correspondent input, which is set to "close" by default.

integer
string

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/input/string
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
boolean
constant
enum
float
integer
price
string
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
string
Syntax

input <input name>="<string_value_used_by_default>";

Description

Defines a string input. Note that in order to have this input defined you need to specify double quotes in its default value.

Example
input symbol = "SPX";

plot Comparison = close(symbol);

Draws the comparison plot based on the closing price. The symbol for the comparison plot can be adjusted using the correspondent input, which is set to "SPX" by default.

price
is

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/is
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
is
Syntax

<value1> is [not] equal to <value2>

<value1> is <greater/less> than or equal to <value2>

<value> is <false/true>

Description

This reserved word is used in phrases of human-readable syntax for boolean and comparison operators. In this article you will find the list of phrases this word can be used in.

1. "is equal to".

open is equal to close

This expression tests if Open price is equal to Close price. Used with reserved words equal and to, this phrase is an equivalent to logic operator ==.

2. "is greater than".

open is greater than close

This expression tests if Open price is greater than Close price. Used with reserved words greater and than, this phrase is an equivalent to logic operator >.

3. "is less than".

open is less than close

This expression tests if Open price is less than Close price. Used with reserved words less and than, this phrase is an equivalent to logic operator <.

4. "is not equal to".

open is not equal to close

This expression tests if Open price is not equal to Close price. Used with reserved words not, equal, and !=.

5. "is greater than or equal to".

 

open is greater than or equal to close

This expression tests if Open price is greater than or equal to Close price. Used with reserved words greater, than, >=.

6. "is less than or equal to".

 

open is less than or equal to close

This expression tests if Open price is less than or equal to Close price. Used with reserved words less, than, <=.

7. "is false".

 

reference ADXCrossover is false

This expression tests if ADX Crossover study returns false. This phrase is an equivalent to "!" (logical negation).

8. "is true".

reference ADXCrossover is true

This expression tests if ADX Crossover study returns true.

input
less

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/less
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
less
Syntax

<value1> is less than [or equal to] <value2> 

Description

The less reserved word is used with the is operator to compare two values.

is
no

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/no
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
no
Syntax

no

Description

The no reserved word is used as a value for the boolean input or as the false condition. In order to define the false condition, you can also use the 0 value.

Example
plot Price = if no then high else low;

Since the condition is always false, the low plot is always displayed.

less
not

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/not
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
not
Syntax

<value1> is not equal to <value2>

Description

The not reserved word is used with the is operator in comparison of two values.

no
or

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/or
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
or
Syntax

<condition1> or <condition2>
 
 <value1> is <greater/less> than 
 or equal to <value2>

Description

1. This reserved word is used to define complex conditions. For a complex condition to be true it is required that at least one condition from it is true.

2. This reserved word is also used in phrases of human-readable syntax for two comparison operators: "is greater than or equal to" and "is less than or equal to". See the is reserved word article for details.

Example
input NumberOfBars = 3;
def barsUp = if close > close[1] then barsUp[1] + 1 else 0;
def barsDown = if close < close[1] then barsDown[1] + 1 else 0;
plot ConsecutiveBars = barsUp >= NumberOfBars or barsDown >= NumberOfBars;
ConsecutiveBars.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

This example highlights bars having the closing price lower than the closing price of the specified number of previous bars with a dot.

not
plot

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/plot
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
plot
Syntax

plot <plot_name>=<expression>;

or

plot <plot_name>;

<plot_name>=<expression>;

Description

Renders the data you are working with on the chart.

Example
plot SMA = Average(close, 12);

This example draws a simple moving average study plot.

You can separate the plot definition from its value assignment. Consider the following example:

plot First;

plot Second;

Second = Average(close, 10);

First = Second[10];

Here, the plots are declared first, and their values are defined afterwards. This notation can be useful when you need to plot a value that depends on another while keeping the reverse order of plots.

or
profile

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/profile
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
profile
Syntax

profile <variable_name>=<expression>;

or

profile <variable_name>;

<variable_name>=<expression>;

Description

Defines a profile to be displayed on the chart.

plot
rec

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/rec
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
rec
Syntax

rec

Description

Enables you to reference a historical value of a variable that you are calculating in the study or strategy itself. Rec is short for "recursion".

Example
rec C = C[1] + volume;
plot CumulativeVolume = C;

This example plots the cumulative volume starting from the beginning of the time period.

profile
reference

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/reference
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
reference
Syntax

reference <StudyName>(parameter1=value1,.., parameterN=valueN ).<PlotName>

Description

References a plot from another script. Note that the reference reserved word can be dropped but in this case parenthesis are necessary.

Full form:

plot MyMACD = reference MACDHistogram;

Compressed form:

plot MyMACD = MACDHistogram();

The reference reserved word is required to distinguish the VWAP study from the vwap function, MoneyFlow study from the MoneyFlow function.

Calling the vwap function:

plot MyVWAP1 = vwap;

Referenicing the VWAP study:

plot MyVWAP1 = reference VWAP;

Full form:

plot MyBB2 = BollingerBandsSMA(price = open, displace = 0, length = 30);

Compact form:

plot MyBB =  BollingerBandsSMA(open, 0, 30);
Example

The following example references def variable instead of plot:

def st = ATRTrailingStop().state;
AssignPriceColor(if st == 1
    then GetColor(1)
    else if st == 2
        then GetColor(0)
        else Color.CURRENT);
def bs = !IsNaN(close) and ATRTrailingStop().BuySignal == yes;
def ss = !IsNaN(close) and ATRTrailingStop().SellSignal == yes;
AddVerticalLine(bs or ss, if bs then "Buy!" else "Sell!", if bs then GetColor(0) else GetColor(1));

First variable, st, is the reference to the state variable from the ATRTrailingStop study script; bs and ss are references to the BuySignal and SellSignal variables from the same study.

rec
script

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/script
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/switch
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
switch
Syntax

plot <plot_name>;
 switch (<enum input or enum_def>) {
 case <enum value1>:
 <plot_name> = <expression1>;
 ...
 default:
 <plot_name> = <expression>;
 }

Description

The switch statement is used to control the flow of program execution via a multiway branch depending on the input value. In the switch statement you either need to define the case with all values from the enum or use the default statement to define actions for all enums that are not defined using the case. Note that in the latter approach you cannot use case with equal enums.

Example
input price = close;
input plot_type = {default SMA, "Red EMA", "Green EMA", WMA};
plot Avg;
switch (plot_type) {
case SMA:
    Avg = Average(price);
case WMA:
    Avg = wma(price);
default:
    Avg = ExpAverage(price);
}
Avg.SetDefaultColor(
  if plot_type == plot_type."Red EMA" then color.RED else 
  if plot_type == plot_type."Green EMA" then color.GREEN else
  color.BLUE);

This example illustrates the usage of the switch reserved word to assign different values to plots. The default keyword must be used unless all possible values of variable are explicitly listed.

script
than

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/than
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
than
Syntax

<value1> is <greater/less> than [or equal to] <value2>

Description

The than reserved word is used with the is operator in comparison of two values.

switch
then

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/then
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
then
Syntax

See the if reserved word article.

Description

This reserved word is used to specify an action to be performed when the if condition is satisfied. It is used only in combination with if-expression or if-statement. Note that in if-statement, the "then" block can be omitted.

than
to

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/to
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
to
Syntax

def <result> = fold <index> = <start> to <end> [ with <variable> [ = <init> ] ] [ while <condition> ] do <expression>;

<value1> is <greater/less> than or equal to <value2>

<value1> is [not] equal to <value2>

Description

1. This reserved word is used to define an interval to be used when calculating the fold function. For more information, see the fold reserved word article.

2. This reserved word is also used with is operator in combination with word equal to test if a variable is equal to a certain value.

then
true

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/true
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
true
Syntax

<value> is true

Description

The true reserved word is used with the is operator to test if a condition is true.

to
while

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/while
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
while
Syntax

def <result> = fold <index> = <start> to <end> [ with <variable> [ = <init> ] ] [ while <condition> ] do <expression>; 

Description

This reserved word defines a condition upon violation of which the loop is terminated when calculating the fold function. For more information, see the fold reserved word article.

true
with

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/with
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
with
Syntax

def <result> = fold <index> = <start> to <end> [ with <variable> [ = <init> ] ] [ while <condition> ] do <expression>; 

Description

The reserved word is used to define an iteration step value in the fold function. For more information, see the fold reserved word article.

while
within

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/within
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
within
Syntax

<condition> within 1 bar

<condition> within <length> bars

Description

This reserved word is used to check if the specified condition is true at least one time for the given number of bars starting from the current one.

Example

plot IsDoji3 = Doji() within 3 bars;
IsDoji3.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);
		

This example script adds a point mark if there is at least one Doji among three candles including the current one.

with
yes

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/Reserved-Words/yes
above
ago
and
bar
bars
below
between
case
crosses
declare
def
default
do
else
equal
equals
false
fold
from
greater
if
input
is
less
no
not
or
plot
profile
rec
reference
script
switch
than
then
to
true
while
with
within
yes
yes
Syntax

yes

Description

The yes reserved word is used as a value for the boolean input or as the true condition. In order to define the true condition, you can also use 1 or any non-zero number.

Example
input DisplayPlot = yes;
plot Data = close;
Data.SetHiding(!DisplayPlot);

In this study, DisplayPlot input controls visibility of plot. Its default value is yes.

within

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials
Overview
Basic
Advanced
Appendices
Disclosures
The information presented in this guide is for educational and informational purposes only. Not investment advice, or a recommendation of any specific security, strategy, or account type.
Past performance of a security or strategy does not guarantee future results or success.
Market volatility, volume and system availability may delay account access and trade executions.
While this manual discusses technical analysis, other approaches, including fundamental analysis, may assert very different views. Technical analysis is not recommended as a sole means of investment research.
©2023Charles Schwab & Co., Inc. All rights reserved. Member SIPC (www.sipc.org).
Overview
Basic
Advanced
Appendices
Overview
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Advanced
Overview
Basic
Advanced
Chapter 10. Referencing Historical Data
Chapter 11. Referencing Secondary Aggregation
Chapter 12. Past/Future Offset and Prefetch
Chapter 13. Referencing Other Data
Chapter 14. Concatenating Strings
Chapter 15. Conclusion
Appendices
Advanced
Chapter 10. Referencing Historical Data
Chapter 11. Referencing Secondary Aggregation
Chapter 12. Past/Future Offset and Prefetch
Chapter 13. Referencing Other Data
Chapter 14. Concatenating Strings
Chapter 15. Conclusion
Basic
Chapter 10. Referencing Historical Data
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Advanced/Chapter-10---Referencing-Historical-Data
Overview
Basic
Advanced
Chapter 10. Referencing Historical Data
Chapter 11. Referencing Secondary Aggregation
Chapter 12. Past/Future Offset and Prefetch
Chapter 13. Referencing Other Data
Chapter 14. Concatenating Strings
Chapter 15. Conclusion
Appendices
Chapter 10. Referencing Historical Data
In chapter 6, we discussed how to use some past data in technical indicators, that is when you need a previous value of a variable or function when calculating those for the current bar. For example, close from 2 bars ago returns the Close price of the second last bar, close from 1 bar ago returns the Close price of the bar prior to the current, etc.
What we did not discuss is how to move back to the future, i.e., use values of following bars in calculations which is also possible. Negative numbers are here to help: these refer to the future data. For example, close from -1 bar ago returns the Close price one bar forward, low from -2 bars ago returns the Low price two bars forward, etc. This might look awkward but it will surely work.
Using human-readable syntax for referring to historical data only deems possible when some simple math is employed, e.g.,
plot scan = close from 4 bars ago + high from 1 bar ago;
This script will plot the sum of the Close price 4 bars ago and the High price 1 bar ago. But what should we do if we need lots of past and future data to perform numerous mathematical operations on? There was actually a hint for that in chapter 1 when we declared recursive variables. The following script was discussed there:
def vol = vol[1] + volume;
plot momentum = close - close[5];
The example will plot the difference between the current Close price and the Close price 5 bars ago.
Historical data is ubiquitously used in built-in studies and strategies. This is especially important when you need recursive variables as they need their previous values to be declared. A good example of recursively declared variables is Fibonacci sequence: each number in it is equal to the sum of previous to with first numbers being 1 and 1. Here is a script for that:
declare lower;
def x = CompoundValue(2, x[1] + x[2], 1);
plot FibonacciNumbers = x;
Here we used the CompoundValue function which has a very interesting calculation mechanism. First of all, let’s see what its arguments are:
CompoundValue(length, visible data, historical data);
So, being used to initialize studies with recursion, this function calculates a compound value according to following rule: if number of a bar is greater than length then the visible data value is returned, otherwise it returns the historical data value. In our Fibonacci sequence script, it assigned value of one to the first two bars (using 2 as the value of parameter length), and, starting from the third bar, each following number is calculated as the sum of the previous two. As a result, we get a plot with values of 1, 1, 2, 3, 5, 8, and so on.
Now that you’ve learned to move backward and forward all across the chart, let’s move on to discussing aggregation periods which actually form the bars on time charts.
Advanced
Chapter 11. Referencing Secondary Aggregation
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Advanced/Chapter-11---Referencing-Secondary-Aggregation
Overview
Basic
Advanced
Chapter 10. Referencing Historical Data
Chapter 11. Referencing Secondary Aggregation
Chapter 12. Past/Future Offset and Prefetch
Chapter 13. Referencing Other Data
Chapter 14. Concatenating Strings
Chapter 15. Conclusion
Appendices
Chapter 11. Referencing Secondary Aggregation
So far, we have learned many things about the bars on charts and values which can be calculated for them. But we never discussed the way they are formed (or, aggregated). In TOS Charts, three types of aggregation are available: time aggregation, tick aggregation, and range aggregation.
Time charts represent price action in terms of time: a new bar (or candlestick, line section, etc.) is plotted after completion of a certain time period (called aggregation period). For example, the 1y D bar chart plots the price action for one year, marking Open, High, Low, and Close prices on the daily basis.
Tick charts represent intraday price action in terms of quantity of trades: a new bar (or candlestick, line section, etc.) is plotted after completion of a certain number of trades (ticks). This aggregation type can be used on intraday charts with time interval not greater than five days. For example, the 2d 133t bar chart plots the price action for two days, defining Open, High, Low, and Close prices every time the number of trades becomes equal to 133.
All scripts we created before were the ones using aggregation period defined in chart settings. In order to access data of a different aggregation period in your code, specify the period parameter using the corresponding Aggregation Period constant. You can also use a pre-defined string value for this purpose: 1 min, 2 min, 3 min, 4 min, 5 min, 10 min, 15 min, 20 min, 30 min, 1 hour, 2 hours, 4 hours, Day, 2 Days, 3 Days, 4 Days, Week, Month, Opt Exp, or <current period>. Here is an example script:
plot dailyOpen = open(period = AggregationPeriod.DAY);
This script plots daily Open price for the current symbol.
plot weeklyClose = close("IBM", period = AggregationPeriod.WEEK);
This code plots weekly Close price for IBM. Interesting thing is that the IBM chart does not have to be opened to plot the Close price: it will be plotted on chart of any symbol you specified in chart settings. There is, however, a restriction in terms of time aggregation: secondary aggregation period cannot be less than the primary aggregation period defined by chart settings:
plot yesterdayHigh = High(period = AggregationPeriod.DAY)[1];
Designed to plot the High price reached on the previous day, this script will not work on weekly charts. Another restriction is that two different secondary aggregation periods cannot be used within a single variable:
plot Data = close(period = AggregationPeriod.MONTH) + close(period = AggregationPeriod.WEEK);
This script will not work on daily charts. In order to make it work, you need to break Data into two variables:
def a = close(period = AggregationPeriod.MONTH);
def b = close(period = AggregationPeriod.WEEK);
plot Data = a + b;
When referencing secondary aggregation with a variable, keep in mind that if this variable is used in an expression with any of the Fundamental or Date&Time functions with the primary aggregation period, the whole expression will use the latter, not the secondary one. E.g.,
def priClose = close; # primary context
def secClose = close(period = AggregationPeriod.DAY); # secondary context
def priContext = if GetYYYYMMDD() > 20130101 then secClose else secClose[1]; # primary context due to "GetYYYYMMDD()"
plot SecondaryAvg = Average(secClose , 12); # secondary context is kept
plot PrimaryAvg1 = Average((priClose + secClose) / 2 , 12); # primary context due to "priClose"
plot PrimaryAvg2 = Average(priContext , 12); # primary context
Here, SecondaryAvg is calculated with secondary aggregation period, but both PrimaryAvg1 and PrimaryAvg2 with primary aggregation period. Note also that some functions, e.g., BodyHeight use fundamental data implicitly, therefore, the same algorithm will be applied to expressions with them.
Expressions that use a variable referencing secondary aggregation and constant values will keep the secondary aggregation period:
def secClose10 = 10 + close(period = AggregationPeriod.DAY); # secondary context
plot SecondaryAvg = Average(secClose10 , 12); # secondary context is kept
The SecondaryAvg  plot will be calculated as a 12 day SMA of the Close price plus 10.
declare lower;
input over_bought = 80;
input over_sold = 20;
input KPeriod = 10;
input DPeriod = 10;
input priceH = FundamentalType.HIGH;
input priceL = FundamentalType.LOW;
input priceC = FundamentalType.CLOSE;
input aggregationPeriod = AggregationPeriod.DAY;
input slowing_period = 3;
input smoothingType = {Default SMA, EMA};
def lowest_k = Lowest(Fundamental(priceL, period = aggregationPeriod), KPeriod);
def c1 = Fundamental(priceC, period = aggregationPeriod) - lowest_k;
def c2 = Highest(Fundamental(priceH, period = aggregationPeriod), KPeriod) - lowest_k;
def FastK = if c2 != 0 then c1 / c2 * 100 else 0;
plot FullK;
plot FullD;
switch(smoothingType) {
case SMA:
    FullK = Average(FastK, slowing_period);
    FullD = Average(FullK, DPeriod);
case EMA:
    FullK = ExpAverage(FastK, slowing_period);
    FullD = ExpAverage(FullK, DPeriod);
}
plot OverBought = over_bought;
plot OverSold = over_sold;
This script is based on the Stochastic Full study but price inputs were substituted by FundamentalType constant input, new AggregationPeriod constant input was added, and old price input references were replaced with Fundamental function calls. This approach can be used to rewrite predefined studies to add support of secondary aggregation period.
Chapter 10. Referencing Historical Data
Chapter 12. Past/Future Offset and Prefetch
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Advanced/Chapter-12---Past-Offset-and-Prefetch
Overview
Basic
Advanced
Chapter 10. Referencing Historical Data
Chapter 11. Referencing Secondary Aggregation
Chapter 12. Past/Future Offset and Prefetch
Chapter 13. Referencing Other Data
Chapter 14. Concatenating Strings
Chapter 15. Conclusion
Appendices
Chapter 12. Past/Future Offset and Prefetch
Past Offset
When referencing historical data (described in chapter 10), you should keep in mind a feature called past offset. Let's study the following example.
plot CloseOffset = close[5];
This example script will plot the Close price five bars prior to the current bar. This calculation mechanism is obvious for bars from the sixth through the last one, but how exactly this plot is going to be calculated for the first five bars?
Past offset is a number of additional bars from the past, necessary for calculating a study. In this very example, the past offset is equal to five; it means that the calculation will start with the sixth bar using price data obtained from the first five bars. However, if additional historical data is available for the chart you are currently using, it will be used for calculating the plot for the first five bars.
When scripting a study, you might need to use several different past offsets for expressions in your script. Let's analyze the following example:
declare lower;  
def x = x[1] + 1;  
plot Average11 = Average(close, 11); 
plot myline = x;
Note that past offset might affect calculation mechanism of some studies due to setting a single intialization point for all expressions. However, if for some reason you need an independent initialization point for an expression, you can use the CompoundValue function that you are already familiar with:
declare lower; 
def x = compoundValue(1, x[1]+1, 1); 
plot ATR = average(TrueRange(high, close, low), 10); 
plot myline = x;
This would explicitly set the value for the myline plot for the first bar, and all other values of this plot will be calculated corresponding to it.
Prefetch
The number of bars needed for each of these to become range-independent can be calculated as follows:
ExpAverage: 4*length bars
Ema2: 8/α + 4 bars
WildersAverage: 7*length bars
Note that WildersAverage also uses a past offset which is equal to (length – 1) bars; two others have a zero past offset.
There is a notable difference between the past offset and prefetch: when historical data is not available, functions that only use prefetch will have the first bar on chart as an initialization point, while functions using past offset will be initialized at a bar whose number is equal to the past offset value.
Future Offset
Unlike the two previously described features, future offset affects re-calculation of values for the most recent bars. When the future offset is equal to zero, e.g., in
plot data = close;
the only value that has to be re-calculated is that of the last bar on chart. However, if we specify a future offset in this expression using a negative index:
plot data = close [-1];
 the study will wait for a new quote in order to calculate the value for the second latest bar. Basically, this script plots the close price of the next bar as soon as there is a quote for it.
Some functions use the future offset (and increase its value for the whole script) without waiting for the upcoming quotes. These functions produce values based on events, e.g., conference calls or earnings, scheduled for a future date. To see how it works, refer, for example, to the GetEventOffset function article.
Apart from its influence on recent values, future offset can be useful in a number of specific tasks. For example, it is widely employed to indicate the level of the last close price across several most recent bars:
input lineLength = 4;
def lastBar = !IsNaN(close) && IsNaN(close[-1]);
def lastClose = if lastBar then close else lastClose[1];
plot data = if IsNaN(close[-lineLength-1]) then lastClose[-lineLength] else Double.NaN;
data.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
data.SetDefaultColor(Color.BLUE);
This script records the last close price and plots it as a line across the last 4 bars, the number being customizable via the input parameter. In case you’re wondering what those IsNaN and !IsNaN are, refer to the Appendix D. Here, these constants are used for finding the last bar on chart. We strongly recommend that you use the “IsNaN + future offset” method for detection of the last bar, not the popular HighestAll method:
def isLastBar = BarNumber() == HighestAll(if !IsNaN(close) then BarNumber() else Double.NEGATIVE_INFINITY);
plot LastBarSignal = isLastBar;
LastBarSignal.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);
The script above makes the study dependent on all bars of chart, which may result in productivity problems. Besides, the re-calculation mode will be set to once per bar instead of once per quote, which may also affect the output in an unwanted way. Should you need to fix the last bar in your script, use the future offset version:
def isLastBar = !IsNaN(close) and IsNaN(close[-1]);
plot LastBarSignal = isLastBar;
LastBarSignal.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);
Three last chapters only covered time referencing: finding historical values, using secondary aggregation, or using additional bars from the past. However, there are several other things you might need to reference in your script; all of these will be explained in the next chapter.
Chapter 11. Referencing Secondary Aggregation
Chapter 13. Referencing Other Data
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Advanced/Chapter-13---Referencing-Other-Data
Overview
Basic
Advanced
Chapter 10. Referencing Historical Data
Chapter 11. Referencing Secondary Aggregation
Chapter 12. Past/Future Offset and Prefetch
Chapter 13. Referencing Other Data
Chapter 14. Concatenating Strings
Chapter 15. Conclusion
Appendices
Chapter 13. Referencing Other Data
In this chapter we are going to discuss how to reference data which is not defined by current chart settings. We actually started doing this in chapter 11 where we used secondary aggregation period which overrides timeframe specified in chart settings.
Let's start with referencing fundamental data with a different price type. We hope that you've carefully read our reference dealing with fundamental functions, e.g., high, low, close, etc. In those articles you might have seen that the last argument for each fundamental function is priceType. This argument specifies which value of the fundamental function is needed: LAST, ASK, BID, or MARK. By default, this price type coincides with the one specified by chart settings. Here is how we could change that:
plot ask = close(priceType = "ASK");
plot bid = close(priceType = "BID");
On the "MARK" price type chart for a Forex symbol, this code will plot ask and bid plots. Just like it was explained in chapter 9, we only change the default value of argument priceType while keeping the other two (symbol and period) so that we put the 'equals' sign and state that we need ASK and BID price types for the first and second Close price plots, respectively. Note also that for non-Forex symbols, the last three are only supported on intraday charts with time interval not greater than 15 days.
As it was implied before, you can also change the symbol for some fundamental function in your script:
plot spread = close - close("GOOG");
The last thing we are going to discuss here is referencing pre-defined studies. This is a convenient way to use values of more than 200 built-in studies in your script without reconstructing them.
In order to use default values of the study, type command reference:
plot MyMACD = reference MACDHistogram;
This script will add the plot of MACD Histogram which means that you are able incorporate this plot in your own study, e.g.,
plot MyMACD = reference MACDHistogram;
plot diff = Average(close, 5) – Average(close, 20);
Now your script displays MACD Histogram plot and difference between two averages.
You can also reference a study with parameters different from default ones:
plot SMA = SimpleMovingAvg(volume, 20);
This code will plot the 20 period SMA of volume. Note that in this case, you need to specify all the parameters that the study has; these should be separated with comma.
Currently users are only able to reference the built-in studies, however, there is a workaround for integrating their own scripts into new ones. This can be done using command script:
script avg {
input length = 10;
plot SMA = Average(close, length);
plot EMA = ExpAverage(close, length);
}
declare lower;
plot SMAOsc = avg(10) - avg(20);
plot EMAOsc = avg(10).EMA - avg(20).EMA;
The script will plot two moving average oscillators on the lower subgraph. Here is what we did: we had the script command introduce a study called avg which has two plots, SMA and EMA which happen to be simple and exponential moving averages of the Close price with variable length (we had the length input for this purpose). After that, we declared that we needed the lower subgraph and created two plots: SMAOsc and EMAOsc. For the latter, we called the newly created study avg, specified 10 and 20 in brackets in order to use these as lengths for EMA plot which was also specified after the dot in the notation:
plot EMAOsc = avg(10).EMA - avg(20).EMA;
For the SMAOsc plot, we did not state that we needed SMA from avg as it was the first plot in that study, thus it is referenced by default and there is no need to specifically call it like we did for EMA.
In the next chapter we will learn more about string concatenation as sometimes output demands compound string values.
Chapter 12. Past/Future Offset and Prefetch
Chapter 14. Concatenating Strings
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Advanced/Chapter-14---Concatenating-Strings
Overview
Basic
Advanced
Chapter 10. Referencing Historical Data
Chapter 11. Referencing Secondary Aggregation
Chapter 12. Past/Future Offset and Prefetch
Chapter 13. Referencing Other Data
Chapter 14. Concatenating Strings
Chapter 15. Conclusion
Appendices
Chapter 14. Concatenating Strings
In chapter 9, we've learned a lot about methods of outputting values beside plots. We considered the following example for AddLabel function:
AddLabel(yes, "Average: " + Average(close, 20));
This is where we first used string concatenation: we appended value of the average to the string using the “+” operator. In this last chapter we are going to find out other ways of concatenating strings and their peculiarities.
Beside the “+” operator, one can use the Concat function which was also briefly mentioned in chapter 9. Using both methods is beneficial when you need to pass resulting string to any of the following functions: AddLabel, AddVerticalLine, Alert, or AddChartBubble.
Note that the Concat function preliminarily converts values of different types to a string. For this reason you can use any numeric values as the function's parameters:
AddVerticalLine(getMonth() <> getMonth()[1], concat("Open: ", open));
This example draws a vertical line with the Open value for the beginning of each month. The same result will be obtained with concatenation operator “+”:
AddVerticalLine(getMonth() <> getMonth()[1], "Open: " + open);
The following example explains what should be done if you need to concatenate more than two values:
input price = close;
input threshold = 100;
alert(price > threshold, Concat("Current price ", Concat(price, Concat(" is greater than ", threshold))), Alert.TICK);
This example defines a local alert triggered once a new quotation arrives in case the current price is higher that the specified one. In order to concatenate more than two values, the example uses nested Concat function calls:
concat(value1, concat(value2, value3))
But we could, of course, make the script much simpler if we use the concatenation operator:
input price = close;
input threshold = 100;
alert(price > threshold, "Current price "+ price + " is greater than " + threshold, Alert.TICK);
But sometimes using the Concat function is unavoidable: it is the only way to convert a numerical value to string.
input isVerbose = yes;
AddLabel(yes, Concat(if isVerbose then "Close: " else "", close));
Let’s see what is going on here. This script adds a chart label which shows the Close price. If input isVerbose is set to yes, then the word “Close:” is prepended to the number. If it is set to no, only the number is displayed. As you can see from this example, in order to pass a numeric value as a string you need to preliminarily concatenate it with an empty string using the Concat function:
Concat(numerical_value, "")
Chapter 13. Referencing Other Data
Chapter 15. Conclusion
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Advanced/Chapter-15---Conclusion
Overview
Basic
Advanced
Chapter 10. Referencing Historical Data
Chapter 11. Referencing Secondary Aggregation
Chapter 12. Past/Future Offset and Prefetch
Chapter 13. Referencing Other Data
Chapter 14. Concatenating Strings
Chapter 15. Conclusion
Appendices
Chapter 15. Conclusion
Chapter 14. Concatenating Strings
Appendices
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Appendices
Overview
Basic
Advanced
Appendices
Appendix A. Creating Local Alerts
Appendix B. Using Profiles
Appendices
Appendix A. Creating Local Alerts
Appendix B. Using Profiles
Advanced
Appendix A. Creating Local Alerts
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Appendices/Appendix-A---Creating-Local-Alerts
Overview
Basic
Advanced
Appendices
Appendix A. Creating Local Alerts
Appendix B. Using Profiles
Appendix A. Creating Local Alerts
alert(condition, text, alert type, sound);
The condition parameter defines a condition upon which you want this alert to be triggered. The text parameter places a specified text next to the alert. The alert type parameter defines a type of the alert.
Available alert type values are:
Alert.ONCE – alert can be triggered only once after adding a study.
Alert.BAR – alert can be triggered only once per bar.
Alert.TICK – alert can be triggered after each tick
The sound parameter plays a sound when the alert is triggered.
Valid sound values are:
Sound.Bell
Sound.Chimes
Sound.Ding
Sound.NoSound
Sound.Ring
Consider the following script:
Alert(open > 400, "Open is greater than 400! Current value is" + open, alert.ONCE, Sound.Ring);
This example script triggers an alert when the Open price becomes higher than 400. The alert is triggered once and it plays the ring sound.
Appendices
Appendix B. Using Profiles
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Appendices/Appendix-B---Using-Profiles
Overview
Basic
Advanced
Appendices
Appendix A. Creating Local Alerts
Appendix B. Using Profiles
Appendix B. Using Profiles
In order to demonstrate the use of the functions, let's create a TPO profile study (colored blue) that aggregates all chart data on the right expansion.
Here is the code:
def allchart = 0;
profile tpo = timeProfile("startnewprofile" = allchart);
tpo.show("color" = Color.BLUE);
Appendix A. Creating Local Alerts
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Appendices/Appendix-C---Customizing-Study-Hints
Overview
Basic
Advanced
Appendices
Appendix A. Creating Local Alerts
Appendix B. Using Profiles
Creating Hints
Hints must be added before any declaration. To declare hints, use the pound sign (#) followed by the word hint. 
Here is an example:
#hint: <b>Hints</b> \n This study demonstrates hints. \n <li>And hints for inputs as well.</li>
#hint length: <b>Nothing</b> depends on this parameter.  
input price = close;
input length = 12;
plot Data = price;
This script defines two hints: one for the study itself and one for the length input. Study specific hints can be viewed by right clicking your study and selecting the Info option, while input specific hints are displayed under the Edit Studies and Strategies dialog window.
Formatting Hints
There are also options for hint formatting: 
Use the <b></b> tag to target text you wish to display in bold.
Use the escape sequence \n to add a new line. 
Use the <li></li> tags to break down a description into a list.
Thermo Mode Visualization
Adding hints is also a means of defining default values for Thermo Mode visualization. To do this you need to use thermo instead of hint.
Here’s an example:
#thermo plot : Data
#thermo input : length
#thermo minValue : 10
#thermo maxValue : 50
#thermo minColor : 0, 0, 255
#thermo maxColor : 255, 255, 255
input length = 35;
plot Data = Average(close, length);
Data is the plot for our Thermo visualization.
length sets the lookback period.
minValue and maxValue define the lower and upper limits, respectively.
minColor and maxColor determine the color of the lowest and highest values (blue and white, respectively). 
Consider including thermo hints in studies with multiple inputs and plots. This practice will help you identify values intended to be used in Thermo Mode.
Here's an example:
@Date
input beginDate = 20231106;
@Date
input endDate = 20231226;
AddLabel(yes, CountTradingDays(beginDate, endDate));
This script adds a chart label that displays the number of elapsed trading days between beginDate and endDate. We start by declaring a date annotation using @Date and define our inputs as integers in the YYYYMMDD format. Each annotation marks one input. 
Appendix B. Using Profiles
You may also like
MomentumPercentDiff
The Momentum Percent Diff is a momentum-based technical indicator. Unlike the regular Momentum ...
Tick Charts
Tick charts represent the count of intraday trades: a new bar (or candlestick, line section, ...
WilliamsAD
The Williams Accumulation/Distribution study is used to determine either the marketplace is ...
PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Appendices/Appendix-D---Using-NaN-and-Infinity-Constants
Overview
Basic
Advanced
Appendices
Appendix A. Creating Local Alerts
Appendix B. Using Profiles
Double.NaN
First of all, NaN here stands for "not a number". Basically speaking, this constant represents a value that cannot be plotted because it doesn't exist for some reason. Several examples of when it happens:
1. OHLC values of the current symbol are NaN when a script tries to retrieve them from the time point before IPO or before the first visible bar on tick and range charts. The same happens when the script tries to retrieve OHLC values from the right expansion of the chart (i.e., from the time point in the "future", which doesn't have any OHLC values yet).
2. OHLC values of the secondary symbol are NaN when there is a gap in the chart data. Consider the following script:
plot price = close ("SPX");
On an intraday /ES chart, values of price are NaN when there are no quotes for SPX.
3. Results of errors, where the expression has no mathematical sense, e.g.:
0/0; 0* Double.POSITIVE_INFINITY; Sqrt(-1).
Not being a number, Double.NaN is still a constant, so it's possible to use it in some expressions. However, its usage is somewhat specific:
1. When you use a Double.NaN in an if-expression, the result is also NaN, no matter what is stated in the then-else branches. For example, the following script (which could have been supposed to check for "not-a-number" situations on chart):
declare lower;
plot Data = if close == Double.NaN then 1 else 0;
will not plot anything because its output is always NaN and thus cannot be plotted. In order to check that close is NaN, the isNan() function can be used:
declare lower;
plot Data = if isNaN(close) then 1 else 0;
2. NaN plus any number is not a number. This is important for recursive variables: if at some point of recursion the variable becomes NaN, all its further values will be NaN as well. In order to avoid that, use the isNan() function.
3. The isNan() function can help you fill chart gaps with certain values. Consider the following script:
declare lower; 
input symbol = "IBM"; 
def closeSymbol = close(symbol); 
def closeSymbolWithOutNaN = CompoundValue(1, if IsNaN(closeSymbol) then closeSymbolWithOutNan[1] else closeSymbol, closeSymbol); 
plot Data = closeSymbolWithOutNaN;
This script plots the close price of IBM without gaps. Any possible gap in the plot is replaced with the last known value of close before it.
Checking for gaps or not existing values is not the only application of the NaN concept. It may also be applied in scripts where you need to plot something for certain bars and nothing for others. Consider the following script:
def isLastThreeBars = IsNaN(close[-3]) and !IsNaN(close[-2]);
def isRightExpansion = IsNaN(close);
def lastClose = CompoundValue(1, if isLastThreeBars then close[-2] else lastClose[1], Double.NaN);
plot Data = if !isRightExpansion then lastClose else Double.NaN;
This script detects three last bars by checking that there's nothing after them. It plots the last bar's close price across these three bars and nothing for other bars and the right expansion.
Double.POSITIVE_INFINITY and Double.NEGATIVE_INFINITY
While the whole concept of infinite values might seem esoteric, they can be successfully employed in your scripts. Consider the following examples.
Example 1

Here is a sophisticated way of plotting the smallest non-zero high-to-low range on chart:

declare lower; 

def range = high - low; 

plot SmallestRange = LowestAll(if range == 0 then Double.POSITIVE_INFINITY else range);

This plot replaces zero range values with infinitely large, which makes it possible to detect the smallest value.

Example 2

In chapter 9, we discussed a function called AddCloud(); this function visualizes the difference between two calculated values (variables or plots) by filling the area between them with a translucent color. Infinity bounds though may trick it into displaying something more impressive:

def hiLevel = if close >= Average(close) then Double.POSITIVE_INFINITY else Double.NEGATIVE_INFINITY; 

AddCloud(hiLevel, -hiLevel, Color.LIGHT_GREEN, Color.LIGHT_RED);

Assigning infinite values to a variable will have the addCloud() function display infinite stripes and paint them corresponding to a rule. In our case, the stripes where the close price is greater than or equal to its average will be painted green and the others will be painted red. The chart will not be re-scaled because infinity values are not plotted.

Example 3

Consider the script below:

input price = close; 

def length = if close > close[1] then 20 else 30; 

plot VariableMax = fold i = 0 to length with m = Double.NEGATIVE_INFINITY do Max(m, getValue(price, i, 30));

This script finds the greatest of several recent values of price, with a non-constant number of values being processed. This approach was used in the implementation of the Semi-Cup Formation study.


PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Basic
Overview
Basic
Chapter 1. Defining Variables
Chapter 3. Defining Inputs
Chapter 4. Using Averages
Chapter 5. Conditional Expressions
Chapter 6. Human-Readable Syntax
Chapter 7. Creating Strategies
Chapter 8. Formatting Output: Part I
Chapter 9. Formatting Output: Part II
Advanced
Appendices
Basic
Chapter 1. Defining Variables
Chapter 3. Defining Inputs
Chapter 4. Using Averages
Chapter 5. Conditional Expressions
Chapter 6. Human-Readable Syntax
Chapter 7. Creating Strategies
Chapter 8. Formatting Output: Part I
Chapter 9. Formatting Output: Part II
Overview
Chapter 1. Defining Variables

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Basic/Chapter-1---Defining-Variables
Overview
Basic
Chapter 1. Defining Variables
Chapter 3. Defining Inputs
Chapter 4. Using Averages
Chapter 5. Conditional Expressions
Chapter 6. Human-Readable Syntax
Chapter 7. Creating Strategies
Chapter 8. Formatting Output: Part I
Chapter 9. Formatting Output: Part II
Advanced
Appendices
Chapter 1. Defining Variables

Here is an example of the most basic script:

def price = close; 

This script will retrieve the Close price for each bar.

Was it too simple for you? Let’s make it a little bit more complex:

def price = (high + low)/2; 

Now this script will calculate the midpoint of each bar. Note, however, that we already have a built-in function for calculation of this value, it is called hl2. Thus, the following script will calculate the same value:

def price = hl2; 

A more interesting thing is that you can use logical expressions to declare a variable so that the latter has Boolean values. It is useful when you like to check if some condition is true for some bar:

def condition = close > 700; 

In this script, variable condition will have value of 1 for those bars having Close price greater than 700 and 0 for all others.

Note that Boolean values are translated into numerical. In other words, you can perform arithmetical operations on them. Consider the following script:

def condition1 = close > 700;
def condition2 = close > 900;
def condition3 = close > 1100;
def res = condition1 + condition2 + condition3; 

In this script, variable res will have value of 3 for those bars having Close price higher than 1100, 2 for bars with Close price in between 900 and 1100, 1 for those closing in between 700 and 900, and 0 for the rest. This script is also a good example of using multiple variables: once you have declared a variable, you are free to use it further on.

Variables can be declared recursively, so that they use their own values in further calculation. Let’s start with a basic example:

def vol = vol[1] + volume; 

def a = close + open;
def b = high + low;
 plot c = a/b;

This script will plot the ratio of Close+Open to High+Low. Note that reserved word plot replaces def, and we could actually plot the same value using a single line of script:

plot c = (close + open)/(high + low);

However, this is not the case when you need some serious calculations using complicated mathematics.

Note that the value will be plotted on upper (price) subgraph, however, you are free to choose another subgraph on which the plot will be displayed; use reserved word declare for this purpose. This should be the first line in the script, study the example:

declare lower;
def a = close + open;
def b = high + low;
plot c = a/b;

Basic

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Basic/Chapter-2---Mathematical-Functions
Overview
Basic
Chapter 1. Defining Variables
Chapter 3. Defining Inputs
Chapter 4. Using Averages
Chapter 5. Conditional Expressions
Chapter 6. Human-Readable Syntax
Chapter 7. Creating Strategies
Chapter 8. Formatting Output: Part I
Chapter 9. Formatting Output: Part II
Advanced
Appendices

While discussing variables, we already used the simplest mathematical operations: addition, subtraction, multiplication, and division. These operations do not require any special notation and can be performed using basic characters: plus (+), minus (-), asterisk (*), and slash(/), respectively. Also, declaration of Boolean variables often implies using comparison operators: greater than (>), less than (<), greater than or equals to (>=), less than or equals to (<=), etc. There are also equality operators falling into the same group. To test if two values are equal, use the double equals sign (==). For the inequality, use either '!=' or '<>' signs.

Here is an example script for using equality/inequality operators:

def a = close==open;
def b = close!=open;
def c = close<>open;

Variables b and c are identical: they will both have values of 0 for bars closing at the Open price (sometimes called Doji candles) and 1 for the rest; values of variable a will be vice versa.

def val = close/open;
def data1 = Sqr(val);
def data2 = Sqrt(val);
def data3 = Power(val, 3);
def data4 = Exp(val);
def data5 = Lg(val);
def data6 = Log(val);

This script calculates six data values based on the initial value of the Close to Open ratio for each bar. Data1 calculates the square of this value with Sqr function. Data2 returns the square root using Sqrt function. Data3 uses Power function to raise the value to the power of 3. Data4 calls the Exp to raise Euler's number to the power of the value. Data5 returns the common logarithm of the value and data6, the natural logarithm; functions Lg and Log are used for these purposes, respectively.

def val = close/open;
def data1 = Exp(val);
def data2 = Power(Double.E, val);

Variables data1 and data2 will always return identical values as they both raise Euler's number (Double.E) to the power of val.

def data1 = Ceil(Double.E);
def data2 = Floor(Double.E);
def data3 = RoundUp(Double.E, 3);
def data4 = RoundDown(Double.E, 3);
def data5 = Round(Double.E, 3);

 

Chapter 1. Defining Variables
Chapter 3. Defining Inputs

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Basic/Chapter-3---Defining-Inputs
Overview
Basic
Chapter 1. Defining Variables
Chapter 3. Defining Inputs
Chapter 4. Using Averages
Chapter 5. Conditional Expressions
Chapter 6. Human-Readable Syntax
Chapter 7. Creating Strategies
Chapter 8. Formatting Output: Part I
Chapter 9. Formatting Output: Part II
Advanced
Appendices
Chapter 3. Defining Inputs

In this chapter we will discuss how to make your study more flexible. Most of the built-in studies are adjustable in terms of timeframe, price data, or mode of calculation to employ. It is only a matter of seconds to switch from a larger timeframe to a shorter one using input parameters which will appear in your Edit Studies and Strategies dialog window if you properly use reserved word input in the beginning of the script. Let’s see how it works.

In chapter 2, the following script was discussed:

def val = close/open;
def data1 = Exp(val);
def data2 = Power(Double.E, val);

Now that you know that the variables data1 and data2 will yield identical values, let’s exclude the latter from the script:

def val = close/open;
def data1 = Exp(val);

Here is the question: what if you don’t need the Close to Open ratio anymore but need the inverse one? What if you don’t need this one either and want the High to Low ratio instead?

Here is the best way to do it:

input val1 = close;
input val2 = open;
def data = Exp (val1/val2);

Once added, this script will provide the same results as the above mentioned would. But this one is much better: whenever you need to change the ratio, you could go to the Edit Studies and Strategies dialog window and build this ratio directly in it. In order to do that, specify the fundamentals for val1 and val2 and click Apply; the script will be recalculated.

Integer inputs will allow you to enter another integer with which the calculation will be performed.

input length = 10;
plot SMA = Average(close, length);

This will calculate a 10 period SMA of close price (if you are not sure what it is, next chapter will explain everything) with an option to change its length via the corresponding input. And, of course, we could make it even more flexible:

input length = 10;
input price = close;
plot SMA = Average(price, length);

Now both price and length can be adjusted.

input percentShift = 10.0;
plot UpperBand = close * (1 + percentShift / 100);
plot LowerBand = close * (1 - percentShift / 100);

This script will draw an envelope based on the Close price. In this envelope, bands will be shifted up and down from the close price by 10 percent, although you are free to specify any percentage you need: 25.5, 47.8, 99.9, etc.

Using a string input can be especially useful when you need a quick change of symbol for which some value is calculated:

input symbol = "SPX";
plot Comparison = close(symbol);

This plot draws the Close price of the specified symbol which is set to “SPX” by default. Note that string inputs are defined using values in quotes.

Symbols are not the only application of string inputs as this type of input can be used for any function that accepts string values as input parameters.

Boolean inputs can quickly help you select a certain calculation mode out of two defined in the script: to define a Boolean input, use yes or no as the default value:

input useHighLow = yes;
plot HighPrice = if useHighLow then Highest(high, 10) else Highest(close, 10);
plot LowPrice = if useHighLow then Lowest(low, 10) else Lowest(close, 10);

This script will plot a channel based on the highest High and lowest Low price on the period of 10 bars if the input is set to yes. If this input is set to no, channel we be plotted based on the highest and lowest Close price. Note that we use an explicit condition in this script: it starts with word if and tests if we chose yes or no as the input value. Using conditional expressions will be discussed in chapter 6.

If you need more than two options to select from or if you prefer more meaningful naming for them, the enum type should be used. This will require just a little bit more scripting, but it’s not too difficult. First of all, list all the options for the input in braces and specify the default one:

input fastLength = 14;

input slowLength = 28;

input diffType = {default points, percent};

After that, you will need to specify what should happen if a certain option is selected. This is done by using commands switch and case:

input fastLength = 14;

input slowLength = 28;

input diffType = {default points, percent};

plot VolumeOsc;

switch (diffType) {

case points:

    VolumeOsc = Average(volume, fastLength) - Average(volume, slowLength);

case percent:

    VolumeOsc = (Average(volume, fastLength) - Average(volume, slowLength)) / Average(volume, slowLength);

}

Chapter 4. Using Averages

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Basic/Chapter-4---Using-Averages
Overview
Basic
Chapter 1. Defining Variables
Chapter 3. Defining Inputs
Chapter 4. Using Averages
Chapter 5. Conditional Expressions
Chapter 6. Human-Readable Syntax
Chapter 7. Creating Strategies
Chapter 8. Formatting Output: Part I
Chapter 9. Formatting Output: Part II
Advanced
Appendices
Chapter 4. Using Averages

def avg = Average(close, 9);

This will calculate the Simple Moving Average of Close price over last nine bars. Note that just like all the other averages, SMA has a default value for period on which it should be calculated: for this type of average it is equal to 12. In other words, if you omitted the 9 in the script above and just typed

def avg = Average (close);

The 12 period SMA of Close price would be calculated.

Compared to other averages, SMA assigns equal weight to each day’s price which, by some chartists, is believed not quite correct: according to them, heavier weight should be given to the more recent data.

def avg = WMA(open, 10);

This script will calculate the 10 period WMA of the Open price. If 10 is omitted, the default value of 9 will be used for the length parameter.

While WMA corrects SMA’s weighting problem, both averages share another disadvantage: their calculation suggests that the oldest value on the period be removed when passing to the following bar which means that only most recent data is taken into consideration. These issues are addressed by Exponential Moving Average (EMA).

Giving more weight to the more recent data, the Exponential Moving Average, however, does not completely eliminate price action prior to the calculation period. This is possible because EMA uses a different calculation mechanism than the SMA does. Here is the formula:

where p1 is the price of the last bar, p2 is the price of the previous bar, and so on, and α is a smoothing coefficient calculated as follows:

where N is equal to length.

EMA smoothing is applied to data by calling the ExpAverage function:

plot avg = ExpAverage(high,9);

This script will plot EMA of the High price with length equal to 9 which makes the smoothing coefficient equal to 20%. ExpAverage has 12 as the default value for the length parameter.

Another method of assigning weights while keeping older data is Wilder’s Average. Its calculation is similar to that of EMA except it uses SMA instead of the price itself as the last term in total sum of prices. Also, in Wilder’s Average, the smoothing coefficient α is equal to 1/N. To use the Wilder’s Average, the following script is suggested:

def avg = WildersAverage(low,20);

This script will plot Wilder’s Average of the Low price with length equal to 20 which makes the smoothing coefficient equal to 5%. Just like SMA and EMA, WildersAverage has 12 as the default value for the length parameter.

input length = 12;
input averageType = AverageType.SIMPLE;
plot MovAvg = MovingAverage(averageType, close, length);

AverageType.EXPONENTIAL;
AverageType.WEIGHTED;
AverageType.WILDERS;
AverageType.HULL.

The full list of constants and families they belong to can be found here. There is also information on which functions use a certain family of constants.

Chapter 3. Defining Inputs
Chapter 5. Conditional Expressions

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Basic/Chapter-5---Conditional-Expressions
Overview
Basic
Chapter 1. Defining Variables
Chapter 3. Defining Inputs
Chapter 4. Using Averages
Chapter 5. Conditional Expressions
Chapter 6. Human-Readable Syntax
Chapter 7. Creating Strategies
Chapter 8. Formatting Output: Part I
Chapter 9. Formatting Output: Part II
Advanced
Appendices
Chapter 5. Conditional Expressions

input price = close;
input long_average = yes;
plot SimpleAvg = Average(price, if long_average then 26 else 12);

This script uses an if-expression to calculate SMA of Close price: if long_average input is set to “yes”, its period will be equal to 26; if it is set to "no", 12 period SMA will be calculated. If-expression is a simple way to assign one of the two possible values to an input parameter, but what should we do if we need to change the function itself? For example, we might want to use an EMA instead of SMA if the input is set to “no”. Here comes the if-statement which has a different syntax but keeps quite the same meaning:

input price = close;
input long_average = yes;
plot Avg;
if long_average {
Avg = Average(price, 26);
} else {
Avg = ExpAverage(price, 12);
}

Depending on whether or not long_average input is set to “yes”, this script will plot either 26 period SMA or 12 period EMA of Close price. Note how this script declares the plot and the math behind it: command plot precedes the if-statement. Using the if-statement is helpful when you need some serious mathematic calculation and keeping it in a single line of code could be very confusing. When you however need a simple switch like in the example above, the if-expression will do:

input price = close;
input long_average = yes;
plot Avg = if long_average then Average(close, 26) else ExpAverage(close, 12);

In chapter 1, we discussed assigning Boolean values to a variable with this example:

def condition = close>open;

Once this variable outputs Boolean values 1 or 0 (“yes” or “no”), we could use this variable as a condition for the if-expression:

def condition = close>open;
plot Maximum = if condition then close else open;

This script will plot a line connecting the higher of Close and Open for each bar. This can be also achieved using the third type of conditional expressions: if-function. The if-function is, perhaps, the simplest way of defining a condition when you just need to specify numerical true and false values. The syntax of this function is trivial: you just specify the condition, true value and false value as input parameters; true value will be returned if the condition is fulfilled and false value will be returned otherwise. See how the Maximum plot from the example above can be constructed using the if-function:

plot Maximum = If (close>open, close, open);

As it was stated before, only numerical data can be specified as true and false values. If you, however, need a certain constant (e.g., Color constants) or a string value, the if-expression should be used.

Let’s see all the three ways to specify conditions in a single script:

plot Maximum1 = If(close > open, close, open);
plot Maximum2 = if close > open then close else open;
plot Maximum3;
if close > open {
Maximum3 = close;
} else {
Maximum3 = open;
}

Here, plot Maximum1 is defined by if-function, Maximum2 by if-expression, and Maximum3 by if-statement, all the three plotting the higher of Open and Close prices. Use the function for simple conditions with numerical true and false values, the expression for numerical or non-numerical ones, and if-statement for beautification of complex formulas you might need when creating indicators.

Chapter 4. Using Averages
Chapter 6. Human-Readable Syntax

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Basic/Chapter-6---Human-Readable-Syntax
Overview
Basic
Chapter 1. Defining Variables
Chapter 3. Defining Inputs
Chapter 4. Using Averages
Chapter 5. Conditional Expressions
Chapter 6. Human-Readable Syntax
Chapter 7. Creating Strategies
Chapter 8. Formatting Output: Part I
Chapter 9. Formatting Output: Part II
Advanced
Appendices
Chapter 6. Human-Readable Syntax

While watching price action and indicators reach certain values and conform to certain conditions can provide valuable results, it is often more interesting to know when exactly values reached a notable threshold or trend began its development. A popular technique called double crossover method uses two moving averages with different lengths based on a premise that a Buy signal is produced when the shorter moving average crosses above the longer, Sell signal in the opposite situation. Many chartists use length of 5 for the short SMA and 20 for the long one. You are already able to compose a script checking whether the short SMA is above or below the long one:

declare lower;
plot isAbove = Average(close, 5) > Average (close, 20);

Just like you expect, this will plot a line on the lower subgraph with value of 1 when the shorter is above and 0 otherwise. But this is not quite what the double crossover method implies: we need to know when exactly the shorter average crossed the longer one from below, i.e., it had been below for some time but started rising and finally went above. Human-readable syntax is here to help you:

declare lower;
plot isAbove = Average(close, 5) crosses above Average (close, 20);

  declare lower;
plot isBelow = Average(close, 5) crosses below Average (close, 20);

"Above" and "below" are additional statements to the main command "crosses" – they define the direction of crossovers we are interested in. If it doesn't matter to us if a line crosses another line from above or below and we only need to know the fact of the crossover itself, either of the two additional commands could be omitted:

declare lower;
plot Crossover = Average(close, 5) crosses Average (close, 20);

Now the lower subgraph will display a line with value of 1 for timestamps where crossovers happen and zero otherwise. Moving just a little bit forward: this kind of representation might seem not very convenient and, although output formatting will be discussed in chapters 9 and 10, consider using the following script to display the crossovers as dots at the bars where they take place:

plot Crossover = Average(close, 5) crosses Average (close, 20);
Crossover.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

Human-readable syntax is not restricted to crossover identification. Full vocabulary of commands can be found here. A number of sentences can be constructed using this vocabulary in order to define logical expressions, e.g.,

def condition1 = open is equal to close;
def condition2 = close is greater than Average(close,9);
def condition3 = condition1 is false and condition2 is false;

This looks more like a text than a script, doesn't it? However, it will work: condition1 will check if bars have equal Open and Close price, condition2 will define bars whose Close price is greater than its 9 period SMA, and condition3 will identify bars for which neither of the two is true.

Human-readable syntax can also be helpful to beginners when they need to use a past value of data (this is what we call 'referencing historical data' which is going to be fully described in chapter 11). For example, if you need to identify bars whose Close price is greater than its previous value, use this script:

declare lower;
plot Raise = close is greater than close from 1 bar ago;

Here, we used expression "from 1 bar ago" (which could be easily transformed to "from 2 bars ago", "from 20 bars ago", "from 77 bars ago" – whichever you prefer), and the result will be displayed as the line with values of 1 and 0. Again, for those who don't like the line representation, the Boolean points can be used: feel free to experiment with the SetPaintingStrategy function we revealed before.

Another interesting command is "within": it is used to check whether some condition was true at least once for any of the last several bars. So, we could expand a bit the previous script:

declare lower;
plot Raise = close is greater than close from 1 bar ago within 3 bars;

Now this script is going to work differently: the line will have value of 1 if the condition is true in at least one of the last three bars.

Now that we have learned many ways of specifying conditions which will possibly yield some valuable trading signals, we could test them by constructing a strategy to put these signals on chart and estimate the Profit/Loss value. Creating strategies will be thoroughly described in the next chapter.

Chapter 5. Conditional Expressions
Chapter 7. Creating Strategies

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Basic/Chapter-7---Creating-Strategies
Overview
Basic
Chapter 1. Defining Variables
Chapter 3. Defining Inputs
Chapter 4. Using Averages
Chapter 5. Conditional Expressions
Chapter 6. Human-Readable Syntax
Chapter 7. Creating Strategies
Chapter 8. Formatting Output: Part I
Chapter 9. Formatting Output: Part II
Advanced
Appendices
Chapter 7. Creating Strategies

At this very moment we presume that you are able to create a simple technical indicator as the most useful commands have been discussed in previous chapters. Let’s have a look at what this indicator could look like:

input price = close;
input length = 20;
plot avg = Average(price, length);

This script will plot a 20 period SMA of Close price with both length and price adjustable via the input parameters. You can also add a declaration stating that this study should be displayed on the lower subgraph, define several variables to be used in calculations, call some tricky mathematical functions, and specify conditions which will provide you with trading signals. However, the main part here is the plot whose values are going to be analyzed. In this chapter we are going to discuss strategies – a different type of indicators which have trading signals as the main target of analysis. These indicators are displayed on the “Strategies” tab of “Edit Studies and Strategies” window and this is where they should be added.

When you add a strategy to chart, Buy and Sell triggers appear in response to the specified conditions (and now you know a lot of ways to specify them; refer to chapter 5 and chapter 6 to refresh your knowledge). Strategies also provide you with ability to estimate the Profit/Loss value if you sent orders upon each Buy and Sell signal. This is what we call backtesting of a strategy: TOS Charts interface allows you to view the performance report upon clicking each signal on chart (the full procedure is described here).

As one can expect, strategies are similar to regular studies, but they just have something special to them. This something is AddOrder function which (if properly used) will turn any technical indicator into trading strategy. Now we are going to do it with the script above:

input price = close;
input length = 20;
def avg = Average(price, length);
AddOrder(OrderType.BUY_AUTO, price crosses above avg);
AddOrder(OrderType.SELL_AUTO, price crosses below avg);

Now it is a strategy which will add a Buy signal every time Close price crosses above its 20 period SMA and a Sell signal when it crosses below. Aside from the AddOrder function which will be discussed a bit later, we could notice a couple other differences peculiar to strategies. First of all, as you can see, this strategy does not have any plots (as the most studies do). This is characteristic of strategies: they do not normally show any plots, however, it won’t do any harm if you add a plot or several to this script. Secondly, defining the trading condition is crucial: in our case, it is price crossing above or below its SMA. But the main difference remains the same: the AddOrder function. Let us puzzle out its syntax:

AddOrder(OrderType.BUY_AUTO, price crosses above avg);
AddOrder(OrderType.SELL_AUTO, price crosses below avg);

We called this function twice: first for the Buy signal and second for the Sell. In order to specify which side of trading is considered, AddOrder function requires an OrderType constant as the first argument. BUY_AUTO is a constant which AddOrder function uses to add a buying order for entering a new long position or closing a short one. Vice versa, SELL_AUTO is used to add a selling order for entering a new short position or closing a long position. As you can see, both BUY_AUTO and SELL_AUTO constants open new positions and close previous ones. If you prefer a constant which only opens or closes a position, consider using some of the other four: BUY_TO_CLOSE, BUY_TO_OPEN, SELL_TO_CLOSE, and SELL_TO_OPEN. While names of the constants speak for themselves, feel free to read more about them in our reference.

The second argument of the function was the condition upon which the order of specified side and position effect will be added. This order will be added to the next bar after condition is fulfilled.

When the strategy is applied to chart, each time the condition is fulfilled, an order is displayed. Orders are shown as up and down arrows above and below the price plot. These arrows are also accompanied by position effect, caption, and a tick marking the trading price. Appearance of these elements can be customized via the full syntax of the AddOrder function which is just a little bit more complicated than what you’ve seen before:

AddOrder(type, condition, price, tradeSize, tickColor, arrowColor, name); 

Aside from previously described “type” and “condition”, arguments also include price, trade size, tick color, arrow color and name. Argument “price” defines price at which the order is added (by default, it is the Open of the following bar), “trade size” stands for the number of contracts traded; you can also specify colors for both tick and arrow. Colors need to be defined as Color constants, e.g., Color.RED, Color.GREEN, Color.ORANGE, etc. The full list of color constants can be found here; usage of these constants will be covered in the next chapter. The last argument is “name”; it defines the caption to be displayed (by default, it is the same as the name of the strategy itself).

Now we are ready to make the strategy we created before look outstanding:

input price = close;

input length = 20;

def avg = Average(price, length);

AddOrder(OrderType.BUY_AUTO, price crosses above avg, open[-1], 100, Color.YELLOW, Color.YELLOW, “Buy”);

AddOrder(OrderType.SELL_AUTO, price crosses below avg, open[-1], 100, Color.RED, Color.RED, “Sell”);

Now this strategy opens the long position or closes the short one at the Open price of the next bar upon respective crossovers of Close price above and below its 20 period SMA. The trade size will be equal to 100, Buy signals will be colored yellow, Sell signals will be colored red, and each signal will display the trade side. After you added a strategy to chart, you can view the performance report by right-clicking any of the signals and choosing “Show report” from the menu. More information on the report can be found here.

Before we pass to the next chapter which will explain how to make your plots even more beautiful, here is an important notice about the strategies: all the signals you get are hypothetical, i.e., you cannot send real orders using strategies.

 

Chapter 6. Human-Readable Syntax
Chapter 8. Formatting Output: Part I

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Basic/Chapter-8---Formatting-Output
Overview
Basic
Chapter 1. Defining Variables
Chapter 3. Defining Inputs
Chapter 4. Using Averages
Chapter 5. Conditional Expressions
Chapter 6. Human-Readable Syntax
Chapter 7. Creating Strategies
Chapter 8. Formatting Output: Part I
Chapter 9. Formatting Output: Part II
Advanced
Appendices
Chapter 8. Formatting Output: Part I

You might have noticed how good all the built-in studies look when applied to chart. But so far we only learned how to display plots as plain lines, except for chapter 6 where we gave you a hint on how to display a plot as Boolean points:

plot Crossover = Average(close, 5) crosses Average (close, 20);
Crossover.SetPaintingStrategy(PaintingStrategy.BOOLEAN_POINTS);

There are several other ways of representing Boolean values. Consider using BOOLEAN_ARROW_DOWN and BOOLEAN_ARROW_UP painting strategies. These can be especially useful in a script like this one:

plot isAbove = Average(close, 5) crosses above Average (close, 20);
plot isBelow = Average(close, 5) crosses below Average (close, 20);
isAbove.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_UP);
isBelow.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_DOWN);

Now you will see an up arrow below those bars at which the shorter moving average crosses above the longer one and down arrow above those bars when it crosses below.

There are also numerous ways to display the numerical plots. First of all, the line can be complemented with points, squares, or triangles which would definitely focus your attention on the values the line has at each bar (for this purpose, use LINE_VS_POINTS, LINE_VS_SQUARES, or LINE_VS_TRIANGLES). You can even discard the line and use only these basic shapes: POINTS, SQUARES, or TRIANGLES constants should be used then. Some values need to be represented as a histogram, use the HISTOGRAM constants for those. There are several other interesting painting strategies; the full list can be found here.

If you, however, prefer to keep the line, there are many options to make it look differently. For example, the SetStyle function. Consider the following script:

plot avg = ExpAverage(close, 15);
avg.SetStyle(Curve.SHORT_DASH);

Now the EMA line will be displayed as a short-dashed curve. The SetStyle function accepts Curve constants, the full list and descriptions can be found here.

SetLineWeight function is very simple to use: specify a number from 1 to 5 as an argument and it will define the width of the plot line in pixels:

plot avg = ExpAverage(close, 15);
avg.SetLineWeight(3);

Sometimes there are situations where you need to hide a plot; there are two functions to help you with that: Hide and SetHiding. First function will hide the plot by default while the second will only hide it dynamically, i.e., upon some condition:

plot SMA5 = Average(close, 5);
plot SMA10 = Average(close, 10);
plot SMA15 = Average(close, 15);
SMA10.hide();
SMA15.setHiding(getAggregationPeriod() < AggregationPeriod.DAY);

In this example, plot SMA10 plot is hidden by default and the SMA15 is hidden on intraday charts only.

In previous chapter we promised to tell you more about colors that can be used when drawing plots. You can color plots using any of the following functions: SetDefaultColor, AssignValueColor, or AssignNormGradientColor. SetDefaultColor is used to add a specific solid color to the whole plot. AssignValueColor is used to draw the plot with different colors depending on specified conditions. AssignNormGradientColor is used to color the plot in the gradient manner depending on values.

Before we move on to examples showing how to use these functions, let’s see how to specify which colors we will need. First way is to use a predefined Color constant, e.g, Color.RED (this is what we actually did in the previous chapter when assigning colors to strategy signals). Second way is to use functions Color and DefineColor: the former draws the plot with colors named by the latter function. Another way is to use the GetColor function which accepts a number as an argument and returns the respective color from the palette; this palette can be found here. For those who find our palettes insufficient, we have the CreateColor function which accepts three numerical arguments used as RGB values in order to create whichever color you might think of. And finally, function TakeValueColor will color the plot the same way as another plot; this is especially useful when colors of the plot change dynamically.

Now that you are provided you with a whole lot of functions, let’s see how they work together:

plot UpperBand = close * 1.1;
plot LowerBand = close *0.9;
plot Middle = close;
Middle.DefineColor("Highest", Color.RED);
Middle.DefineColor("Lowest", CreateColor(250, 150, 25));
LowerBand.SetDefaultColor(GetColor(5));
UpperBand.AssignValueColor(LowerBand.TakeValueColor());
Middle.AssignNormGradientColor(14, Middle.color("Highest"), Middle.color("Lowest"));

So, we started with drawing two bands of the Close price-based envelope: two bands shifted up and down by 10 percent from the Middle band which is the Close price plot. After that, we used the DefineColor function to define two named colors for the Middle plot: Highest and Lowest. The Highest color is defined by this function using the Color constant: Color.RED. In order to specify the value of Lowest color, we had the CreateColor function translate RGB value (250, 150, 25) into argument of the DefineColor function. After that we used the SetDefaultColor function to paint the LowerBand in a solid color taken from the dynamic palette by the GetColor function – and made sure that UpperBand would be colored the same (by using functions AssignValueColor and TakeValueColor). And still the result was not colorful enough to us – so, we decided to add gradient coloring to the Middle plot with Highest color for highest values and Lowest color for lowest ones.

Of course, we do not expect you to use all these functions in a single script, however, you may try. Also, if you feel tired of the plots, let’s move on to next chapter as there are several other ways to output values for you study.

Chapter 7. Creating Strategies
Chapter 9. Formatting Output: Part II

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Basic/Chapter-9---Formatting-Output
Overview
Basic
Chapter 1. Defining Variables
Chapter 3. Defining Inputs
Chapter 4. Using Averages
Chapter 5. Conditional Expressions
Chapter 6. Human-Readable Syntax
Chapter 7. Creating Strategies
Chapter 8. Formatting Output: Part I
Chapter 9. Formatting Output: Part II
Advanced
Appendices
Chapter 9. Formatting Output: Part II

Let's start with function AddLabel. This function adds a nice little label to the upper left corner of chart. This label indicates whichever data you prefer:

AddLabel(yes, if close > Average(close, 20) then "Uptrend" else "Downtrend");

This label will display word "Uptrend" if Close price is greater than its 20 period SMA and "Downtrend" otherwise. First argument of this function is a condition upon which the label is displayed; here, we used word yes for the label to be always visible. We also specified a condition (close > Average(close, 20)) which will select either word "Uptrend" or "Downtrend" to be shown, however, you might want to display some calculated value without any conditions:

AddLabel(yes, Average(close, 20));

Now the label will display value of the SMA itself. You can also add a short explanation of what is being displayed by using the following notation:

AddLabel(yes, "Average: " + Average(close, 20));

Here we specified the text to be displayed and concatenated it with the value of the average using the sign "+". There is also another way to concatenate some values in a string, which is the Concat function, but we advise that you use the plus sign as it is much more convenient.

And, of course, we could not leave you without an option to choose the color of the label. By default, it is displayed red, but let's make it dark orange:

AddLabel(yes, Average(close, 20), Color.DARK_ORANGE);

We used the simplest way, the Color constant, but you are free to color the label using techniques described in previous chapter. For example, let's make it chartreuse green (RGB value: 127,255,0 ):

AddLabel(yes, Average(close, 20),CreateColor(127,255,0));

Now you are displaying this label with a color which is the most visible to human eye. Feel free to experiment with other colors. Also, you can add some dynamic coloring:

AddLabel(yes, Average(close, 20), if close > Average(close, 20) then Color.GREEN else Color.RED);

This script will display 20 period SMA of Close price in a green label if Close price is greater than this average, or in a red label when the Close price is lower.

To sum it up, three arguments can be used for AddLabel function. These arguments are: condition upon which the label is visible (state yes to make it always visible), text and values to be displayed (specify text in quotes and use the "+" sign to concatenate it with a value), and color which is red by default.

Another way to output values is showing bubbles at price bars. This is done by using AddChartBubble function:

AddChartBubble(close crosses above Average(close, 20), close, "Close price " + close + " is greater");

This script will display chart bubbles at bars where Close price crosses above its 20 period SMA. Bubbles will be displayed at Close price of these bars (this is what the second argument, close, stands for) with default color (red). By default, bubbles are located above the price plot; if you would like to display them below, transform this script into:

 AddChartBubble(close crosses above Average(close, 20), close, "Close price " + close + " is greater", up = no);

When a bubble is not enough to draw attention to some price action, you can add a vertical line with some text. Function AddVerticalLine is used for this purpose:

AddVerticalLine(close crosses above Average(close, 20),  "Close price " + close + " is greater");

This script will mark the same bars as the previous did, but the vertical lines will be displayed instead of bubbles. Arguments for the AddVerticalLine function are: visible (identical to time condition argument of AddChartBubble), text (has the same application as the two previously described functions), color (all the same, again), and stroke (the style of the line to be displayed, set with Curve constants).

The last but not the least, AddCloud function is a nice way to avoid several plots when you only need difference in their values. This function visualizes the difference between two calculated values by filling area between them with a translucent color:

def avg1 = Average(close, 5);
def avg2 = Average(close, 20);
AddCloud(avg1, avg2, Color.PINK, Color.BLUE);

This script is another visualization of the previously mentioned double crossover method. We have two SMAs of the Close price: 5 period and 20 period. AddCloud function visualizes difference between them in the following way: those sections where the shorter average is greater are colored pink and those where the longer is greater, blue. Remember not to swap the arguments as this function compares the first argument to the second and colors the mentioned sections in respective colors.

Chapter 8. Formatting Output: Part I
Advanced

PAGE: https://toslc.thinkorswim.com/center/reference/thinkScript/tutorials/Overview
Overview
Basic
Advanced
Appendices
Overview
To start scripting, you will need to open the Editor window: this is where you type your script which is checked and parsed by the application and, if everything is correct (we are sure it will be if you read these tutorials), added to chart as a study or strategy. In order to open the Editor:
1. Go to the Charts tab.
2. Click Studies in the upper right corner of the page.
3. Select Edit Studies. The Edit Studies and Strategies window will open.
4. Click Create... below the list of studies. This will open the Editor window with pre-defined script:
plot Data = close; 
As one can figure out, this will plot the Close price for the specified symbol. Move on to chapter 2 where you will learn how to define variables and plot simple values like this one.
Basic