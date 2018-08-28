import numpy as np
import scipy.interpolate as irp


def grid2grid(lats,lons,Z_arr,lats_q,lons_q):
	'''
	lats,lons are the x and y vectors from the array
	lats_q,lons_q are also the x and y vectors from the target array. However these ones are arrayed and flattened
	'''
	my_interpolating_function = irp.RegularGridInterpolator((lats,lons), Z_arr,bounds_error =False,fill_value=None)
	#bounds_error : bool, optional, If True, when interpolated values are requested outside of the domain of the input data, a ValueError is raised. If False, then fill_value is used.
	#fill_value : number, optional, If provided, the value to use for points outside of the interpolation domain. If None, values outside the domain are extrapolated.
	LONS_OBS,LATS_OBS = np.meshgrid(lons_q,lats_q)
	pts = np.swapaxes( np.asarray([LATS_OBS.flatten(),LONS_OBS.flatten()]) ,1,0)
	z_target = my_interpolating_function(pts)
	return z_target.reshape(LATS_OBS.shape)
