# Options Functions (Index)

## Option-chain/context helpers (platform-dependent availability)
- `GetStrike()`
- `GetUnderlyingSymbol()`
- `IsPut()`
- `IsCall()`
- `GetDaysToExpiration()`

## Greeks/volatility (availability may vary by study context)
- Delta/Gamma/Theta/Vega accessors where supported
- Implied volatility accessors where supported

## Typical use
- Filter by DTE
- Option-side logic (call/put)
- Strike-relative signals