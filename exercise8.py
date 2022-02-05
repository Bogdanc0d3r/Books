def convert_temperatures(t, source, target):
 """ (number, str, str) -> number
 Convert t from source temperature scale to target temperature scale
 and return the result.
 >>> convert_temperatures(0, 'Celsius', 'Kelvin')
 273.15
 >>> convert_temperatures(100, 'Celsius', 'Fahrenheit')
 212.0
 """
 if source == 'Kelvin':
 celsius = t - 273.15
  elif source == 'Celsius':
    celsius = t
  elif source == 'Fahrenheit':
    celsius = (t - 32) * 5 / 9
  elif source == 'Rankine':
    celsius = (t - 491.67) * 5 / 9
  elif source == 'Delisle':
    celsius = 100 - t * 2 / 3
  elif source == 'Newton':
    celsius = t * 100 / 33
  elif source == 'Reamur':
    celsius = t * 5 / 4
  elif source == 'Romer':
    celsius = (t - 7.5) * 40 / 21
 
 
 if target == 'Kelvin':
  return celsius + 273.15
    elif target == 'Celsius':
      return celsius
    elif target == 'Fahrenheit':
      return celsius * 9 / 5 + 32
    elif target == 'Rankine':
      return (celsius + 273.15) * 9 / 5
    elif target == 'Delisle':
      return (100 - celsius) * 3 / 2
    elif target == 'Newton':
      return celsius * 33 / 100
    elif target == 'Reamur':
      return celsius * 4 / 5
    elif target == 'Romer':
      return celsius * 21 / 40 + 7.5
