# polybar-stocks
Module for polybar for displaying stock prices
![](https://github.com/Holden1337/polybar-stocks/blob/main/screenshots/bar.gif)


## Dependencies
[yahoo_fin](https://pypi.org/project/yahoo-fin/) - yahoo finance

[zscroll](https://github.com/noctuid/zscroll#installation) - for polybar scroll

[scroll](https://github.com/Anachron/i3blocks#scroll) - for i3blocks scroll

## Modules

```

[module/stocks]
type = custom/script
tail = true
interval = 1
;format-prefix = "  "
;format-prefix = ""
format = <label>
label-padding = 1
exec = ~/.config/polybar/scripts/stocks/scroll_stocks.sh
;click-left = < ~/.config/polybar/scripts/news/current_url.txt xargs -I % xdg-open %

[module/stocks-grab]
type = custom/script
exec = ~/.config/polybar/scripts/stocks/stocks.py
interval = 900

```

