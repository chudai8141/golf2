import os

from matplotlib import pyplot as plt


imf_name = ['IMF1', 'IMF2', 'IMF3', 'IMF4', 'IMF5', 'IMF6', 'IMF7', 'IMF8']


def plot(
    spectrum_time,
    freq_all_data,
    amp_all_data,
    Nod,
    frame,
    start,
    end,
    joint_name,
    select_data,
    save_path
):
    plt.clf()
    plt.figure(dpi=200, figsize=(16, 9))
    plt.rcParams['font.family'] = 'Times new Roman'
    plt.rcParams['font.size'] = 30
    for n in range(start, end):
        plt.scatter(spectrum_time[n, :], freq_all_data[n, :], s = 100, c=amp_all_data[n, :frame], cmap='jet')
    ax = plt.gca()
    ax.set_facecolor([0.0, 0.0, 0.5])
    plt.ylim(0, 10)
    plt.xlabel('time [s]')
    plt.ylabel('frequency [Hz]')
    plt.colorbar()
    file_name = '_'.join(imf_name[start:end])
    # print('save figure', os.path.join(save_path, file_name) )
    plt.savefig(os.path.join(save_path, file_name))