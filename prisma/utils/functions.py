from scipy.interpolate import griddata

def get_values(x,y,img):    
    x_known = [4, 0, 0, 4]
    y_known = [4, 0, 4, 0]

    z_known = [img.shape[1]*0.50, img.shape[1]*0.50, img.shape[1]*0.73, img.shape[1]*0.27]
    w_known = [0, img.shape[0]*0.91, img.shape[0]*0.46, img.shape[0]*0.46]

    z_interp = griddata((x_known, y_known), z_known, (x, y), method='linear')
    w_interp = griddata((x_known, y_known), w_known, (x, y), method='linear')
    return z_interp, w_interp