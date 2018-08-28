def readnetcdf(filename):
	dataset = netCDF4.Dataset(filename,'r')
	alldata = {'metadata':{},'attributes':{},'data':{}}
	nc_attrs = dataset.ncattrs()
	for meta_attr in nc_attrs:
		alldata['metadata'][meta_attr] = dataset.getncattr(meta_attr)#new keyval pair in the subdict
	for var in dataset.variables:
		alldata['data'][var] = dataset.variables[var][:]
		alldata['attributes'][var] = {}
		for attr in dataset.variables[var].ncattrs():
			try:
				alldata['attributes'][var][attr] = dataset.variables[var].getncattr(attr)
			except ValueError:
				print('Unable to read attrs from: '+var)
	return alldata
