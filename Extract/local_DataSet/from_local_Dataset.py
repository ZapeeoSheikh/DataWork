import json

items = '''
{
	"USD": {
		"symbol": "$",
		"name": "US Dollar",
		"symbol_native": "$",
		"decimal_digits": 2,
		"rounding": 0,
		"code": "USD",
		"name_plural": "US dollars"
	},
	"CAD": {
		"symbol": "CA$",
		"name": "Canadian Dollar",
		"symbol_native": "$",
		"decimal_digits": 2,
		"rounding": 0,
		"code": "CAD",
		"name_plural": "Canadian dollars"
	},
	"EUR": {
		"symbol": "€",
		"name": "Euro",
		"symbol_native": "€",
		"decimal_digits": 2,
		"rounding": 0,
		"code": "EUR",
		"name_plural": "euros"
	},
	"AED": {
		"symbol": "AED",
		"name": "United Arab Emirates Dirham",
		"symbol_native": "د.إ.‏",
		"decimal_digits": 2,
		"rounding": 0,
		"code": "AED",
		"name_plural": "UAE dirhams"
	}
'''

data = json.loads(items)
print(data)
del items['AED']

newdata = json.dumps(data, indent=2, sort_keys=True)
print(newdata)
