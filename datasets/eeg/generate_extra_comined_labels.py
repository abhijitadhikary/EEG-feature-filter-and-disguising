import scipy.io as sio
import numpy as np

def add_combined_label(filename):
    data = sio.loadmat(filename)
    label_combined = []
    for i in range(data['label_stimulus'].shape[0]): #0,1  0,1,2,3,4
        label = 5 * data['label_alcoholism'][i,0] + data['label_stimulus'][i,0]
        label_combined.append(label)
    label_combined = np.reshape(label_combined,(-1,1))
    if 'label_id' in data.keys():
        sio.savemat(filename+'_extra.mat',{'data':data['data'],
                                                     'label_alcoholism':data['label_alcoholism'],
                                                     'label_stimulus':data['label_stimulus'],
                                                     'label_id':data['label_id'],
                                                     'label_combined':label_combined})
    else:
        sio.savemat(filename+'_extra.mat',{'data':data['data'],
                                         'label_alcoholism':data['label_alcoholism'],
                                         'label_stimulus':data['label_stimulus'],
                                         'label_combined':label_combined})
       
add_combined_label('eeg_dummy_images_w_label_step3_within')
add_combined_label('uci_eeg_images_train_within')