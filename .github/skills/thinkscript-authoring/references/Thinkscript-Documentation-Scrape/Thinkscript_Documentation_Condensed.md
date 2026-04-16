# thinkScript Language Reference - Condensed

## ANNOTATIONS
@Date - Annotates integer input as date (YYYYMMDD format)
  - Only integer inputs can be annotated as date
  - To annotate multiple inputs, specify annotations for each
  - Change by: using built-in date picker or right-clicking chart area on specific date
  Example 1: @Date input date = 20240101;
           AddVerticalLine(GetYYYYMMDD() >= date and GetYYYYMMDD()[1] < date);
  Example 2: @Date input beginDate = 20231106;
             @Date input endDate = 20231226;
             plot Line = if GetYYYYMMDD() >= beginDate and GetYYYYMMDD()[1] < beginDate or 
                           GetYYYYMMDD() >= endDate and GetYYYYMMDD()[1] < endDate 
                           then close else Double.NaN;
             Line.EnableApproximation();

## CONSTANTS

### MIN, TWO_MIN, THREE_MIN, FOUR_MIN, FIVE_MIN, TEN_MIN, FIFTEEN_MIN, TWENTY_MIN, THIRTY_MIN
HOUR, TWO_HOURS, FOUR_HOURS
DAY, TWO_DAYS, THREE_DAYS, FOUR_DAYS, WEEK, MONTH, QUARTER, YEAR, OPT_EXP
Note: Aggregation period cannot be less than chart aggregation period

### Alert
ONCE - Once per study (after adding a study)
BAR - Once per bar
TICK - After each tick

### AverageType
SIMPLE, EXPONENTIAL, WEIGHTED, WILDERS, HULL
Used with MovingAverage function

### ChartType
BAR, CANDLE, CANDLE_TREND, HEIKIN_ASHI, EQUIVOLUME, LINE, AREA
Used with SetChartType function

### Color (RGB values in parentheses)
BLACK(0,0,0), BLUE(0,0,255), CYAN(0,255,255), GRAY(128,128,128), GREEN(0,255,0)
DARK_GRAY(64,64,64), DARK_GREEN(0,100,0), DARK_ORANGE(255,127,0), DARK_RED(128,0,0)
LIGHT_GRAY(192,192,192), LIGHT_GREEN(144,238,114), LIGHT_ORANGE(255,165,0), LIGHT_RED(255,63,0)
LIME(191,255,0), MAGENTA(255,0,255), ORANGE(255,200,0), PINK(255,175,175), PLUM(128,0,128)
RED(255,0,0), VIOLET(153,153,255), WHITE(255,255,255), YELLOW(255,255,0)
DOWNTICK(204,0,0), UPTICK(3,128,0)
CURRENT - Refers to default plot color (or redefined color). For AssignPriceColor: price bar color. For AssignBackgroundColor: background color

### CrossingDirection
ABOVE (yes) - First value becomes greater than second
BELOW (no) - First value becomes less than second
ANY - Change of relation irrespective of direction

### Curve
FIRM, LONG_DASH, MEDIUM_DASH, SHORT_DASH, POINTS
Used with SetStyle function

### Double
E - Exponent constant (value of e)
NaN - Not a number (result of operation is not a number)
NEGATIVE_INFINITY - Negative value of infinitely large magnitude
POSITIVE_INFINITY - Positive value of infinitely large magnitude
Pi - Pi constant (value of π)

### EarningTime
ANY - Announcement before market open, after market close, during market hours, or unspecified time
BEFORE_MARKET - Announcement before market open
AFTER_MARKET - Announcement after market close
Used with HasEarnings function

### Events
CONFERENCE_CALL - Used with GetEventOffset to return offset for conference calls
DIVIDEND - Used with GetEventOffset to return offset for dividend events
EARNINGS - Used with GetEventOffset to return offset for earnings announcements
SPLIT - Used with GetEventOffset to return offset for split events

### FiscalPeriod
QUARTER - Quarterly fiscal data
YEAR - Yearly fiscal data (default for all Stock Fundamentals functions)

### FontSize
SMALL (default), MEDIUM (+150%), LARGE (+200%), LARGER (+250%), VERY_LARGE (+300%), X_LARGE (+350%)
Used with AddLabel() function

### FundamentalType
HIGH, LOW, CLOSE, OPEN, HL2, HLC3, OHLC4, VWAP, VOLUME, OPEN_INTEREST, IMP_VOLATILITY, TICK_COUNT
Used with Fundamental function

### Location
TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT
Used with AddLabel() function

### MonkeyVolumeShowStyle
ALL - Supplement each section with Volume Profile histogram
LAST - Supplement last section with Volume Profile histogram
NONE - Volume Profile histograms not displayed
Used with MonkeyBars function

### NumberFormat
DOLLAR - "$" prepended, two digits after decimal, thousand separators
TWO_DECIMAL_PLACES - Rounded to two digits after decimal
THREE_DECIMAL_PLACES - Rounded to three digits after decimal
Used with AsText function

### OptionClass
CALL - Call option (used with GetATMOption)
PUT - Put option (used with GetATMOption)

### OrderType
BUY_AUTO - Buy order for entering long or closing short (can switch in Strategy Properties)
BUY_TO_CLOSE - Buy order for closing short (can switch in Strategy Properties)
BUY_TO_OPEN - Buy order for entering long (can switch in Strategy Properties)
SELL_AUTO - Sell order for entering short or closing long (can switch in Strategy Properties)
SELL_TO_CLOSE - Sell order for closing long (can switch in Strategy Properties)
SELL_TO_OPEN - Sell order for entering short (can switch in Strategy Properties)
Used with AddOrder function

### PaintingStrategy
ARROW_DOWN, ARROW_UP
BOOLEAN_ARROW_DOWN - Marks true values with down arrows above high prices
BOOLEAN_ARROW_UP - Marks true values with up arrows below low prices
BOOLEAN_POINTS - Displays true values as points at current closing price
BOOLEAN_WEDGE_DOWN - Marks true values with down wedges below low prices
BOOLEAN_WEDGE_UP - Marks true values with up wedges above high prices
DASHES, HISTOGRAM, HORIZONTAL - Long segments forming continuous line when same value for adjacent bars
LINE, LINE_VS_POINTS, LINE_VS_SQUARES, LINE_VS_TRIANGLES
POINTS, SQUARED_HISTOGRAM - Wide columns, adjacent columns not divided (unlike basic HISTOGRAM)
SQUARES, TRIANGLES
VALUES_ABOVE - Draws numeric plot values above current high price
VALUES_BELOW - Draws numeric plot values below current low price

### PricePerRow
AUTOMATIC - Height calculated to have 50 rows for Monkey Bars, 85 rows for other profiles
TICKSIZE - Height equal to minimal price change for current symbol
Used with Profile functions

### PriceType
ASK, BID, LAST, MARK
For non-Forex symbols: ASK, BID, MARK only supported on intraday charts with time interval ≤15 days

### ProfitLossMode
COST_BASIS - P/L as difference between net liquidation value and cost basis × position size (cost basis from Schwab, includes commissions and tax elections)
EXECUTION_PRICE - P/L as difference between net liquidation value and execution price × position size
Used with GetOpenPL function

### Sound
NoSound, Bell, Ding, Ring, Chimes
Used with Alert function

## DATA TYPES
boolean - Logical value: true (yes) or false (no)
int - Integer number, e.g. 5
double - Floating point number, e.g. 1.5 (can drop zero integer part: 0.02 = .02)
String - Text in double quotes, e.g. "TEXT"
Symbol - Symbol names in double quotes
CustomColor - Color value, e.g. Color.RED
IDataHolder - Array of data, floating point values, e.g. close or volume
Any - Value of any data type except CustomColor

Data Conversion:
Argument Type | Data Accepted | Conversion Rule
-------------|---------------|----------------
Any | boolean, double, IDataHolder, int, String | -
boolean | double, IDataHolder, int | 0 (0.0) and Double.NaN → no (false), other numbers → yes (true)
CustomColor | - | -
double | boolean, IDataHolder, int | yes → 1.0, no → 0.0
IDataHolder | boolean, double, int | Number → array with elements equal to that number (logical values converted to numerical first)
int | boolean, double, IDataHolder | yes → 1, no → 0; non-integer numbers rounded towards zero
String | Symbol | -
Symbol | String | -

## DECLARATIONS
declare hide_on_daily; - Hides study on charts with aggregation ≥1 day
declare hide_on_intraday; - Hides study on intraday charts (time charts <1 day and tick charts)
declare lower; - Places study on lower subgraph (for values considerably lower/higher than price/volume)
declare upper; - Places study on base/volume subgraph (default for studies not containing lower/on_volume)
declare on_volume; - Forces placement on volume subgraph
declare once_per_bar; - Recalculates last values only once per bar (reduces CPU; for studies not needing tick recalculation)
declare real_size; - Uses absolute units for superimposed lower studies (single scale marked in absolute units; percentage view not used)
declare weak_volume_dependency; - Places on volume subgraph when at least one volume value used
declare zerobase; - Sets minimum axis value to zero if no negative values

## FUNDAMENTAL FUNCTIONS
ask - Ask price (cannot reference historical: ask[1] is invalid)
bid - Bid price (cannot reference historical: bid[1] is invalid)
close(symbol, period, priceType) - Close price
  Default parameters: symbol=getSymbol(), period="<current period>", priceType="<current type>"
  Valid priceType: LAST, ASK, BID, MARK (or PriceType constants)
  Valid period: AggregationPeriod constants or pre-defined strings (Day, 2 Days, Week, Month, etc.)
  For non-Forex: ASK, BID, MARK only on intraday charts ≤15 days
high(symbol, period, priceType) - High price (same defaults and restrictions as close)
hl2(symbol, period, priceType) - (High + Low)/2 (same defaults and restrictions as close)
hlc3(symbol, period, priceType) - Typical price: (High + Low + Close)/3 (same defaults and restrictions as close)
imp_volatility(symbol, period, priceType) - Implied volatility (same defaults and restrictions as close)
low(symbol, period, priceType) - Low price (same defaults and restrictions as close)
ohlc4(symbol, period, priceType) - (Open + High + Low + Close)/4 (same defaults and restrictions as close)
open(symbol, period, priceType) - Open price (same defaults and restrictions as close)
open_interest(symbol, period, priceType) - Open interest (same defaults and restrictions as close)
tick_count(symbol, period, priceType) - Number of trades for intraday bar (intraday only; only intraday aggregations allowed)
  For priceType: LAST returns number of trades; MARK/BID/ASK count changes in quotes of corresponding price type
volume(symbol, period, priceType) - Volume (same defaults and restrictions as close)
vwap(symbol, period, priceType) - Volume weighted average price (same defaults and restrictions as close)

## LOOK AND FEEL FUNCTIONS
AddChartBubble(condition, price, text, color, up) - Adds bubble with text when condition true. Use \n for line breaks
  Default: color=Color.RED, up=Yes
AddCloud(data1, data2, color1, color2, showBorder) - Plots translucent cloud. data1>data2 use color1, else color2
  Default: color1=Color.YELLOW, color2=Color.RED, showBorder=no
  Accepts both defined variables and plots as input. Invisible border by default (set showBorder=yes to make visible)
  Can use Double.POSITIVE_INFINITY/NEGATIVE_INFINITY for infinite bounds
AddLabel(visible, text, color, location, size, rowOwnership) - Adds text label
  Default: color=Color.RED, location=Location.TOP_LEFT, size=FontSize.SMALL, rowOwnership=no
  rowOwnership=yes: label claims entire row, no other labels in same row
  When calls another function (e.g., GetDividend()), only uses value at last real bar
  Tip: Enable "Fit study markers" in Chart Settings > Price axis to avoid overlap with bubbles/bars
AddVerticalLine(visible, text, color, stroke) - Adds vertical line
  Default: text="", color=Color.RED, stroke=Curve.SHORT_DASH
AssignBackgroundColor(color) - Sets background color (in custom quote: sets quote cell background color)
AssignNormGradientColor(length, lowestColor, highestColor) - Fills plot with gradient
  Current value positive and highest: highestColor
  Current value negative and lowest: lowestColor
  Zero level: center color (positive part uses higher colors, negative uses lower colors)
  Note: Past Offset not affected by length (function sets length=1 for first bar, increases to specified value)
AssignPriceColor(color) - Sets price bar color. Cannot paint same bar from multiple studies
AssignValueColor(color) - Paints plot intervals with colors. Overrides default color
  In custom quote: sets quote value color
CreateColor(red, green, blue) - Generates color from RGB (0-255)
DefineColor(name, color) - Defines named color for plot (user-editable in Edit Studies dialog)
DefineGlobalColor(name, color) - Defines named global color (editable in Globals sub-tab of Study Properties)
plot.Color(name) - Gets plot color by name (color must be defined using DefineColor)
GlobalColor(name) - Gets global color by name (color must be defined using DefineGlobalColor)
GetColor(index) - Returns color from palette (0-9, repeats cyclically). Colors vary by Look and Feel
EnableApproximation() - Connects adjacent non-NaN values
Hide() - Makes plot hidden by default
HideBubble() - Makes last value bubble invisible
HidePricePlot(condition) - Hides price plot if condition is yes (default: yes)
HideTitle() - Removes plot value from graph title
SetChartType(chartType) - Sets chart type (Area, Bar, Candle, Candle Trend, Heikin Ashi, Line)
  Accepts ChartType constants. Can also set in Chart Settings window
SetDefaultColor(color) - Sets default plot color (affects color when study first initialized/added)
SetHiding(condition) - Controls visibility: if condition true, plot hidden
  Note: For Boolean function as condition, only value at last real bar is used
SetLineWeight(pixels) - Sets line weight (1-5 pixels)
SetPaintingStrategy(strategy) - Sets painting style (accepts PaintingStrategy constants)
SetStyle(curve) - Controls curve style (default: Curve.SHORT_DASH). Accepts Curve constants
TakeValueColor() - Returns color of current bar

## OPTION RELATED FUNCTIONS
Delta(underlyingPrice, volatility) - Calculates delta option greek
  Default: underlyingPrice=close(getUnderlyingSymbol()), volatility=imp_volatility(getUnderlyingSymbol())
Gamma(underlyingPrice, volatility) - Calculates gamma option greek
  Default: underlyingPrice=close(getUnderlyingSymbol()), volatility=imp_volatility(getUnderlyingSymbol())
GetATMOption(underlyingSymbol, yyyyMmDd, optionType) - Returns code of option with strike closest to current market price
  Default: underlyingSymbol=Underlying symbol, optionType=OptionClass.CALL
GetDaysToExpiration() - Returns days till expiration of current option
GetNextExpirationOption(optionCode) - Returns code of option in next series (same strike, underlying, side)
  Default: optionCode=Option code
GetNextITMOption(optionCode) - Returns code of next option in ITM direction (not necessarily ITM)
  Default: optionCode=Option code
  For Put: next option with higher strike. For Call: next option with lower strike
GetNextOTMOption(optionCode) - Returns code of next option in OTM direction (not necessarily OTM)
  Default: optionCode=Option code
  For Put: next option with lower strike. For Call: next option with higher strike
GetStrike() - Returns strike price for current option
GetUnderlyingSymbol() - Returns underlying symbol for current option
IsEuropean() - Returns true if current option is European, false if American
IsOptionable() - Returns true if current symbol is optionable
IsPut() - Returns true if current option is PUT, false if CALL
OptionPrice(strike, isPut, daysToExp, underlyingPrice, volatility, isEuropean, yield, interestRate) - Calculates theoretical option price
  Default: strike=getStrike(), isPut=isPut(), daysToExp=getDaysToExpiration(),
           underlyingPrice=close(getUnderlyingSymbol()), volatility=imp_volatility(getUnderlyingSymbol()),
           isEuropean=isEuropean(), yield=getYield(), interestRate=getInterestRate()
  Note: Uses implied volatility averaged over different options, so result is approximate
Rho(underlyingPrice, volatility) - Calculates rho option greek
  Default: underlyingPrice=close(getUnderlyingSymbol()), volatility=imp_volatility(getUnderlyingSymbol())
Theta(underlyingPrice, volatility) - Calculates theta option greek
  Default: underlyingPrice=close(getUnderlyingSymbol()), volatility=imp_volatility(getUnderlyingSymbol())
Vega(underlyingPrice, volatility) - Calculates vega option greek
  Default: underlyingPrice=close(getUnderlyingSymbol()), volatility=imp_volatility(getUnderlyingSymbol())

## MATHEMATICAL FUNCTIONS
AbsValue(value) - Returns absolute value (if positive: value; if negative: -value)
ACos(value) - Returns arc cosine (range: 0 through pi; input: [-1,1])
ASin(value) - Returns arc sine (range: -pi/2 through pi/2; input: [-1,1])
ATan(value) - Returns arc tangent (range: -pi/2 through pi/2)
Ceil(value) - Rounds up to nearest integer (not less than value)
Cos(angle) - Returns trigonometric cosine (angle in radians)
Crosses(data1, data2, direction) - Tests if data1 gets higher or lower than data2
  Default: direction=CrossingDirection.ANY
  Returns true when: direction=ABOVE and data1 becomes > data2
                     direction=BELOW and data1 becomes < data2
                     direction=ANY and crossover occurs (irrespective of direction)
Exp(number) - Returns exponential value (e^number)
Floor(value) - Rounds down to nearest integer (not greater than value)
IsInfinite(value) - Returns true if number is infinitely large in magnitude
IsNaN(value) - Returns true if parameter is not a number, false otherwise
Lg(number) - Returns base-10 logarithm
Log(number) - Returns natural logarithm
Max(value1, value2) - Returns greater of two values
Min(value1, value2) - Returns smaller of two values
Power(number, power) - Returns first argument raised to power of second
Random() - Returns value with positive sign, ≥0.0 and <1.0
Round(number, digits) - Rounds to specified digits (default: 2)
RoundDown(number, digits) - Rounds towards zero to specified digits (default: 2)
RoundUp(number, digits) - Rounds up to specified digits (default: 2)
Sign(number) - Returns 1 if positive, 0 if zero, -1 if negative
Sin(angle) - Returns trigonometric sine (angle in radians)
Sqr(value) - Calculates square (value^2)
Sqrt(value) - Calculates square root
Sum(data, length) - Returns sum of values for last length bars (default: 12)
Tan(angle) - Returns trigonometric tangent (angle in radians)
TotalSum(data) - Returns sum of all values from first bar to current

## STATISTICAL FUNCTIONS
Correlation(data1, data2, length) - Returns correlation coefficient between data1 and data2 for last length bars (default: 10)
  Correlation defines relation between two variables
Covariance(data1, data2, length) - Returns covariance coefficient between data1 and data2 for last length bars (default: 10)
  Covariance defines whether two variables have same trend (positive: same direction; negative: inverse)
Inertia(data, length) - Draws linear regression curve using least-squares method (y = a*current_bar + b)
  Applies approximation method for each set of bars defined by length
InertiaAll(data, length, startDate, startTime, extendLeft, extendRight) - Linear regression for entire plot or interval
  Default: length=all chart, startDate=0, startTime=0, extendLeft=No, extendRight=No
  startDate (YYYYMMDD) and startTime (HHMM) override length if startDate non-zero
  Returns Double.NaN outside interval unless extendLeft/extendRight are non-zero
LinDev(data, length) - Returns linear deviation (average absolute difference between mean and current value) (default: 12)
StDev(data, length) - Returns standard deviation (square root of variance) (default: 12)
  Variance: average of squared deviations from mean
StDevAll(data, length, startDate, startTime, extendLeft, extendRight) - Standard deviation for entire plot or interval
  Default: length=all chart, startDate=0, startTime=0, extendLeft=No, extendRight=No
  Output result for last bar used for whole interval. If length not specified, calculated for entire plot
  startDate (YYYYMMDD) and startTime (HHMM) override length if startDate non-zero
  Returns Double.NaN outside interval unless extendLeft/extendRight are non-zero
StErr(data, length) - Returns standard error (standard deviation between data and linear regression of data) (default: 12)
StErrAll(data, length, startDate, startTime, extendLeft, extendRight) - Standard error for entire plot or interval
  Default: length=all chart, startDate=0, startTime=0, extendLeft=No, extendRight=No
  Output result for last bar used for whole interval. If length not specified, calculated for entire plot
  startDate (YYYYMMDD) and startTime (HHMM) override length if startDate non-zero
  Returns Double.NaN outside interval unless extendLeft/extendRight are non-zero

## DATE AND TIME FUNCTIONS
CountTradingDays(fromDate, toDate) - Returns number of trading days in period (YYYYMMDD format; includes both start and end dates)
DaysFromDate(fromDate) - Returns days from specified date (YYYYMMDD, EST timezone)
DaysTillDate(tillDate) - Returns days till specified date (YYYYMMDD, EST timezone)
GetDay() - Returns current bar day number in CST (1-365/366 for leap years)
GetDayOfMonth(yyyyMmDd) - Returns day number in month (based on given YYYYMMDD)
GetDayOfWeek(yyyyMmDd) - Returns day of week (1=Monday through 7=Sunday; based on given YYYYMMDD)
GetLastDay() - Returns last bar day number in CST (1-365/366 for leap years)
GetLastMonth() - Returns last bar month number in CST (1-12)
GetLastWeek() - Returns last bar week number in CST (1-53)
GetLastYear() - Returns last bar year number in CST
GetMonth() - Returns current bar month number in CST (1-12)
GetTime() - Returns milliseconds since epoch (January 1, 1970, 00:00:00 GMT)
GetWeek() - Returns current bar week number in CST (1-53)
GetYear() - Returns current bar year number in CST
GetYYYYMMDD() - Returns date in YYYYMMDD format (corresponds to trading session day containing current bar)
  Note: On intraday charts, this date and actual date might differ for Forex and Futures
RegularTradingStart(yyyyMmDd) - Returns milliseconds since epoch till regular trading hours start for given day (YYYYMMDD)
RegularTradingEnd(yyyyMmDd) - Returns milliseconds since epoch till regular trading hours end for given day (YYYYMMDD)
SecondsFromTime(fromTime) - Returns seconds from specified time (HHMM, 24hr, EST; always zero for ≥1 day aggregation)
SecondsTillTime(tillTime) - Returns seconds till specified time (HHMM, 24hr, EST; always zero for ≥1 day aggregation)

## CORPORATE ACTIONS FUNCTIONS
GetActualEarnings() - Returns actual earnings (diluted) for current symbol
GetDividend() - Returns dividend amount for current symbol
GetEstimatedEarnings() - Returns estimate earnings for current symbol
GetEventOffset(eventType, numberOfEventsToSkip) - Returns bars before upcoming/after past event
  Default: eventType=Events.DIVIDEND, numberOfEventsToSkip=0
  eventType: Uses Events constant (CONFERENCE_CALL, DIVIDEND, SPLIT, EARNINGS)
  numberOfEventsToSkip: Negative values=past events; zero/positive=upcoming (0=closest)
  Return value sign opposite of numberOfEventsToSkip: positive for negative input, negative for zero/positive input
GetSplitDenominator() - Returns split denominator for current symbol
GetSplitNumerator() - Returns split numerator for current symbol
HasConferenceCall() - Returns true if earnings conference call, false otherwise
HasEarnings(type) - Returns true if announced earnings, false otherwise (default: EarningTime.ANY)
  Use EarningTime constant to specify announcement time

## PORTFOLIO FUNCTIONS
Portfolio functions limitations:
- GetAveragePrice, GetOpenPL, GetQuantity: Cannot use on charts with price type other than LAST; if futures, subscribe to active contract data
- Can only use with aggregation periods: 1min, 2min, 3min, 4min, 5min, 10min, 15min, 20min, 30min, 1h, 1day
- Time period for 1day aggregation limited to 1yr
- If applied to futures chart, functions subscribe to active contract data

GetAggregatedPL(symbol) - Returns aggregated P/L from chart start (difference between current MARK value and trade price at chart start, adjusted for all trades during period)
  Default: symbol=current symbol
  Unlike GetOpenPL (real-time P/L on open position), provides historical P/L from defined start point
GetAveragePrice(symbol) - Returns average trade price for specified instrument (currently selected account)
  Default: symbol=current symbol
GetNetLiq() - Returns net liquidation value (currently selected account; current account value if all positions closed at current market price)
  Requires Show Extended-Hours Trading session enabled (Style > Settings > Equities/Options/Futures > Show Extended-Hours Trading session checkbox)
GetOpenPL(symbol, profitLossMode) - Returns Open P/L (currently selected account)
  Default: symbol=current symbol, profitLossMode=ProfitLossMode.EXECUTION_PRICE
  Difference between position's net liquidation value and either execution price or cost basis × position size
  ProfitLossMode.COST_BASIS: cost basis values from Schwab (include commissions and tax elections)
  ProfitLossMode.EXECUTION_PRICE: based on execution price (default)
GetPortfolioAggregatedPL() - Returns aggregated P/L for all positions over chart timeframe
  Cumulative difference between current market value and initial trade price of all positions opened during chart interval
  Considers all instruments in portfolio; reflects realized and unrealized P/L
GetPortfolioSharePrice() - Returns Portfolio Share Price (PSP) performance metric
  Tracks profitability of currently selected account over time, isolating market gains/losses from cash movements (deposits, withdrawals, dividends)
GetQuantity(symbol) - Returns number of shares/contracts held (currently selected account)
  Default: symbol=current symbol
GetTotalCash() - Returns total cash available (currently selected account)
  Requires Show Extended-Hours Trading session enabled (Style > Settings > Equities/Options/Futures > Show Extended-Hours Trading session checkbox)

## PROFILE FUNCTIONS
DataProfile(data, pricePerRow, startNewProfile, onExpansion, numberOfProfiles, valueAreaPercent) - Plots activity profile for any input variable
  Default: pricePerRow=PricePerRow.AUTOMATIC, onExpansion=Yes, numberOfProfiles="all", valueAreaPercent=70.0
  Horizontal diagram showing which values most often reached by input variable
  Algorithm: (1) Find value range (2) Break into intervals: automatic (85 equal parts), ticksize-based (each interval=minimum value movement), or manual (user-specified)
             (3) Calculate number of times variable reached each interval (4) Row length proportional to count from step 3
  Point of Control: longest row (value most often reached)
  Value Area: range surrounding POC where 70% (default, modifiable) of value movements occurred (represents frequent values)
TimeProfile(symbol, pricePerRow, startNewProfile, onExpansion, numberOfProfiles, valueAreaPercent) - Displays TPO profile
  Default: symbol=getSymbol(), pricePerRow=PricePerRow.AUTOMATIC, onExpansion=Yes, numberOfProfiles="all", valueAreaPercent=70.0
VolumeProfile(symbol, pricePerRow, startNewProfile, onExpansion, numberOfProfiles, valueAreaPercent) - Displays volume profile
  Default: symbol=getSymbol(), pricePerRow=PricePerRow.AUTOMATIC, onExpansion=Yes, numberOfProfiles="all", valueAreaPercent=70.0
  pricePerRow: "height" (price range) of each profile row (actual price range or PricePerRow constant)
  startNewProfile: condition; when true, function calculates new profile
  onExpansion: show profile on expansion area (Yes/No)
  numberOfProfiles: number of profiles displayed if onExpansion=no (ignored if onExpansion=yes, only one profile shown)
  valueAreaPercent: percentage of trading activity for which Value Area determined
MonkeyBars(timeInterval, symbol, pricePerRow, startNewProfile, onExpansion, numberOfProfiles, playgroundPercent, emphasizeFirstDigit, volumeShowStyle, volumePercentVA, showInitialBalance, ibRange) - Calculates Monkey Bars profile
  Default: symbol=getSymbol(), pricePerRow=PricePerRow.AUTOMATIC, onExpansion=Yes, numberOfProfiles="all",
           playgroundPercent=70.0, emphasizeFirstDigit=No, volumeShowStyle=MonkeyVolumeShowStyle.NONE,
           volumePercentVA=70.0, showInitialBalance=Yes, initialBalanceRange=3
  timeInterval: ordinal number of aggregation period (first decade: digits 1-9-0 in first palette color; second decade: 1-9-0 in second color, etc.)
  playgroundPercent: percentage of trading activity for which The Playground determined
  emphasizeFirstDigit: highlight opening digit of each period in bold (Yes/No)
  volumeShowStyle: Monkey Bars sections complemented with Volume Profile (MonkeyVolumeShowStyle constant: ALL/LAST/NONE)
  volumePercentVA: percentage of trading activity for Value Area of Volume profile (ignored if volumeShowStyle=NONE)
  showInitialBalance: mark Initial Balance with bracket (Yes/No). Initial Balance: High-Low range of first several bars
  initialBalanceRange: number of bars for Initial Balance if showInitialBalance=yes (ignored if showInitialBalance=no)

profile.Show(color, pocColor, vaColor, opacity, openColor, closeColor, ibColor, volumeColor, volumeVaColor, volumePocColor) - Controls visibility and color scheme
  Default: color=Color.PLUM, pocColor=Color.CURRENT, vaColor=Color.CURRENT, opacity=50.0,
           openColor=Color.CURRENT, closeColor=Color.CURRENT, ibColor=Color.CURRENT,
           volumeColor=Color.PLUM, volumeVaColor=Color.CURRENT, volumePocColor=Color.CURRENT
  Profiles only visible if Show() applied. Color.CURRENT for any element: element not displayed
  color: main color of Time and Volume profile bars
  pocColor: color of Point of Control
  vaColor: color of Value Area
  opacity: degree of histogram opacity (percent)
  openColor: color of square marking Monkey Bars Open price
  closeColor: color of arrow marking Monkey Bars Close price
  ibColor: color of Initial Balance bracket (MonkeyBars only)
  volumeColor: color of Volume Profile (MonkeyBars only, if complemented with Volume Profile)
  volumeVaColor: color of Value Area of Volume Profile (MonkeyBars only)
  volumePocColor: color of Point of Control of Volume Profile (MonkeyBars only)

profile.GetHighest() - Returns highest price within profile period
profile.GetLowest() - Returns lowest price within profile period
profile.GetHighestValueArea() - Returns highest price of Value Area
profile.GetLowestValueArea() - Returns lowest price of Value Area
profile.GetPointOfControl() - Returns price value of POC closest to middle of profile's price range

## STOCK FUNDAMENTALS
All functions: (symbol, fiscalPeriod)
Default: symbol=current symbol, fiscalPeriod=FiscalPeriod.YEAR
All values based on annual fiscal data by default
Functions supporting FiscalPeriod.QUARTER: CurrentRatio, DividendsPerShareTTM, EarningsPerShareTTM, FinancialLeverage,
                                           FixedChargeCoverageRatio, GrossProfitMargin, NetProfitMargin,
                                           OperatingProfitMargin, ReturnOnAssets, ReturnOnEquity, TaxRate, TotalAssetTurnover

BookValuePerShare - Book value ÷ outstanding shares (amount allocated per share if company liquidated)
  FiscalPeriod.QUARTER not compatible
CurrentRatio - Total assets ÷ total current liabilities
DividendPayout - Common dividends ÷ (net income - bottom line - preferred dividend requirement) × 100
  FiscalPeriod.QUARTER not compatible
DividendsPerShareTTM - Total dividends ÷ outstanding shares (trailing 12 months)
EarningsPerShareTTM - Profit ÷ outstanding shares (trailing 12 months)
FinancialLeverage - Total assets ÷ common equity
FixedChargeCoverageRatio - EBIT ÷ fixed charges (interest expense on debt + preferred dividends including tax)
FreeCashFlowPerShare - (Operating cash flow - capital expenditures - total dividends) ÷ outstanding shares
  FiscalPeriod.QUARTER not compatible
GrossProfitMargin - Gross income ÷ net sales or revenues
InterestRate - Interest expense on debt ÷ debt amount × 100
  Debt amount: short-term debt + current portion of long-term debt + long-term debt
  FiscalPeriod.QUARTER not compatible
InventoryTurnover - Cost of goods sold ÷ average inventory (average of last year and current year)
  Only uses yearly fiscal data; FiscalPeriod.QUARTER not compatible
LongTermDebtToCapital - Long-term debt ÷ total capital × 100
  Only uses yearly fiscal data; FiscalPeriod.QUARTER not compatible
NetProfitMargin - (Income - bottom line) ÷ total sales or revenues × 100
OperatingProfitMargin - Operating income ÷ net sales or revenues × 100
  Operating income: total sales or revenues - total operating expenses
QuickRatio - (Cash + short-term investments + net receivables) ÷ total current liabilities
  FiscalPeriod.QUARTER not compatible
ReturnOnAssets - Net income ÷ total assets
ReturnOnEquity - Net income ÷ average shareholders' equity × 100 (average of last year and current year common equity)
  Net income: total profit - bottom line - preferred dividend requirement
SalesPerShare - Sales or revenues ÷ outstanding shares
TaxRate - Income tax ÷ income before tax × 100
TotalAssetTurnover - Net sales or revenues ÷ total assets

## OTHER FUNCTIONS
AddOrder(type, condition, price, tradeSize, tickColor, arrowColor, name) - Adds order for next bar when condition true
  Default: type=OrderType.BUY_AUTO, price=open[-1], tradeSize=specified by strategy settings,
           tickColor=Color.MAGENTA, arrowColor=Color.MAGENTA, name="<strategy name>"
  tradeSize: overrides trade size in Strategy Global Settings
  name: displayed on "Orders" tabs in strategy settings, in strategy report, and as captions to Buy/Sell signal arrows
        (default: all orders use same name as strategy)

Alert(condition, text, alertType, sound) - Shows alert when condition true
  Default: alertType=Alert.ONCE, sound=Sound.NoSound
  Can create studies containing only alert function call without defining plots
  When calls another function (e.g., HasEarnings()), only uses value at last real bar

AsDollars(value) - Converts number to dollar string ("$" prepended, two digits after decimal, thousand separators)
AsPercent(value) - Converts number to percent string ("%" appended, up to two digits after decimal, thousand separators, precision 0.01%)
AsPrice(value) - Converts number to string using instrument price notation (only applies notation, does not round to tick size)
Assert(condition, message) - Throws runtime error if condition false (default message: "assert failed")
  Error message viewed by clicking Exclamation indicator in top left corner of chart
AsText(value, format) - Converts number to string with format (default: NumberFormat.TWO_DECIMAL_PLACES)
  format: NumberFormat constant

BarNumber() - Returns current bar number
  Output increments by one on each new bar; represents linear dependency

Between(parameter, value1, value2) - Tests if parameter within range (inclusive)
  Returns 1 (true) if data between values, 0 (false) if outside

CompoundValue(length, visibleData, historicalData) - Used to initialize recursion (default: 1)
  If bar number > length: returns visibleData; otherwise returns historicalData

Concat(value1, value2) - Concatenates two string values (can use + operator instead)
  Non-string types first converted to string (doubles: saves four decimal places)

EntryPrice() - Returns entry order price (for multiple entries in same direction: average price)

First(data) - Returns value of expression in first bar

FPL() - Returns floating Profit/Loss based on strategy signals
  For each bar: possible P/L if position exited at Close price

Fundamental(fundamentalType, symbol, period, priceType) - Returns specified fundamental value
  Default: symbol=getSymbol(), period="<current period>", priceType="<current type>"
  fundamentalType: FundamentalType constant
  period: AggregationPeriod constants or pre-defined strings (Day, 2 Days, Week, Month, etc.)
  priceType: LAST, ASK, BID, MARK (or PriceType constants)
  For non-Forex: ASK, BID, MARK only on intraday charts ≤15 days

GetAggregationPeriod() - Returns current aggregation period (milliseconds for time, ticks for tick, dollars for range)
  Note: For time charts: milliseconds to complete one candle
        For tick charts: ticks to complete one candle
        For range charts: price range to complete range bar
        1 Day and 24 hours are same (even if different results on charts)

GetInterestRate() - Returns global interest rate (cannot use in Study Filters)

GetPriceType() - Returns price type selected: "Last", "Bid", "Ask", or "Mark"
  For non-Forex on charts other than intraday ≤15 days: always returns "Last"

GetSymbol() - Returns currently selected symbol
  For futures: returns symbol with namespace appended (market identifier code)
  Example: /ES returns /ES:XCME (XCME=Chicago Mercantile Exchange namespace)
  Use namespaces in string comparisons to avoid unexpected results

GetSymbolPart(position) - Returns part of composite symbol (default position: 1)
  For futures: returns with namespace appended
  All parts read in alphabetical order (e.g., "KO+GE" read as "GE+KO")

GetValue(data, dynamicOffset, maxOffset) - Returns value of data with dynamic offset (default maxOffset: 0)
  For positive offset: dynamicOffset ≤ maxOffset
  For negative offset: dynamicOffset ≤ maxOffset

GetYield() - Returns yield of current stock or underlying symbol for current option

HasContractChangeEvent(rootSymbol) - Returns true if active futures contract changed, false otherwise
  Default: rootSymbol=getSymbol()

If(condition, trueValue, falseValue) - Returns trueValue if condition true, else falseValue
  Only accepts double type for input arguments
  For other values (e.g., Color constants), use if-expression instead:
    AssignPriceColor(if close > open then Color.UPTICK else Color.DOWNTICK); // Valid
    AssignPriceColor(if(close > open, Color.UPTICK, Color.DOWNTICK)); // Compilation error

TickSize(symbol) - Returns minimum tick size (default: current symbol)
TickValue(symbol) - Returns dollar value of tick (default: current symbol)

## OPERATORS
Arithmetic: + - * / %
Comparison: == != > >= < <=
Logical: && (and) || (or) ! (not)
Historical: [n] - Reference n bars ago

## RESERVED WORDS
def, plot, input, script
if, then, else
while, do
fold, to, with
yes, no (true, false)
declare

## COMMON PATTERNS
# Moving average crossover
def fastMA = Average(close, 10);
def slowMA = Average(close, 30);
plot signal = Crosses(fastMA, slowMA, CrossingDirection.ABOVE);

# Bollinger Bands
def basis = Average(close, 20);
def dev = 2 * StDev(close, 20);
plot upper = basis + dev;
plot lower = basis - dev;

# Color by condition
plot price = close;
price.AssignValueColor(if close > close[1] then Color.GREEN else Color.RED);

# Custom indicator with input
input length = 14;
def rsi = reference RSI(length = length);
plot overbought = 70;
plot oversold = 30;

# Strategy order
AddOrder(OrderType.BUY_AUTO, 
  close crosses above Average(close, 20), 
  open[-1], 
  100, 
  Color.GREEN, 
  Color.GREEN);

# Recursive calculation (Fibonacci)
def x = CompoundValue(2, x[1] + x[2], 1);

#### RoundDown(number, numberOfDigits)
Rounds towards zero to specified digits (default: 2)

#### RoundUp(number, numberOfDigits)
Rounds up to specified digits (default: 2)

#### Sign(number)
Returns 1 if positive, 0 if zero, -1 if negative

#### Sin(angle)
Returns trigonometric sine (angle in radians)

#### Sqr(value)
Calculates square (value^2)

#### Sqrt(value)
Calculates square root

#### Tan(angle)
Returns trigonometric tangent (angle in radians)

## SYNTAX RULES
- Statements end with semicolon
- Comments: # single line
- Case-insensitive for keywords
- plot name = expression; - Create visible plot
- def name = expression; - Create variable
- input name = defaultValue; - Create input parameter
- Historical reference: variable[barsAgo]
- Function calls: functionName(param1, param2)
- Named parameters: functionName(paramName = value)
- Conditional: if condition then value1 else value2
- Script definition: script scriptName { declarations; plot output = expression; }
- Fold loop: fold index = start to end with accumulator do expression
- String concatenation: "text" + variable or Concat()

### SYNTAX CLARIFICATION

**Important Note on Color Constants:**
Colors can only be changed in Edit Studies dialog if using the Color() function to define them. In other cases, colors can only be changed by editing source code.

**Important Note on AssignPriceColor:**
Cannot paint the same price bar using multiple studies simultaneously.

**Important Note on SetHiding:**
If Boolean function used as condition, only its value at last real bar is taken into account.

### PROFILE FUNCTIONS (Additional Detail)
**PaintingStrategy.HORIZONTAL** is specifically used to draw Point of Control, Value Area High, Value Area Low, Profile High, and Profile Low plots by profile studies (TPOProfile, VolumeProfile, MonkeyBars).

### LOOK AND FEEL FUNCTIONS (Additional Detail)
**AddCloud** - Add note that even though script contains no plots, values used in AddCloud are displayed as cloud border if showBorder=yes.

### DATA TYPE CONVERSION TABLE
String and Symbol data types only convert between each other (not to/from other types).