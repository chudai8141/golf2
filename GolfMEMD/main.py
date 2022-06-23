import argparse

from tqdm import tqdm

from joint import Joint
from user_setting import impact_number, user_list ,choice_user
from user import User
from hht import get_data, MultEmpModeDeco, HilbertTrans, freq_amp_mean_norm, create_spectrum_time
from plot import plot

def main(args):
    output = args.output
    _joint = args.joint
    select_user = choice_user(args.user)

    set_joint = Joint().joint[_joint]
    select_data = select_user.half_straight_data
    ballistic = select_data['select_data']
    impact_list = select_data['impact_list']
    follor_throught = select_data['follor_throught']

    user_name = select_user.user_name
    user = User(
        user_name=user_name,
        set_joint=set_joint,
        ballistic=ballistic,
        impact_list=impact_list,
        last_frame=follor_throught
    )


    # calculation memd
    data_path = select_data['data_path']
    result_memd_list = []

    print('caluculation memd', user.user, user.ballistic, user.joint_name)
    for data in tqdm(data_path):
        #
        data, dt, text = get_data(data, set_joint)
        result_memd = MultEmpModeDeco(data=data, dt=dt, set_joint=set_joint)
        result_memd_list.append(result_memd)

    Nod = 6
    resutl_hilbert_list = []

    print('hilbert transform')
    for i, result_memd in tqdm(enumerate(result_memd_list)):
        result_ht = HilbertTrans(result_memd=result_memd, select_data=select_data)
        result_ht.calc_means_norm()
        result_ht.set_freq_data(Nod=Nod, impact_number=impact_number[i])
        result_ht.set_amp_data(Nod=Nod, impact_number=impact_number[i])
        resutl_hilbert_list.append(result_ht)

    freq_all_data, amp_norm_data = freq_amp_mean_norm(result_hilbert_list=resutl_hilbert_list)

    # create spectrum time
    frame = freq_all_data.shape[1]
    spectrum_time = create_spectrum_time(Nod=Nod, frame=frame, dt=dt)

    # output plot
    print('output plot')
    for n in tqdm(range(1, Nod+1)):
        if n == 0:
            continue

        plot(
        spectrum_time=spectrum_time,
        freq_all_data=freq_all_data,
        amp_all_data=amp_norm_data,
        Nod=Nod,
        frame=frame,
        start=n-1,
        end=n,
        joint_name=set_joint['j_name'],
        select_data=select_data['select_data'],
        save_path=user.save_path
        )

        plot(
        spectrum_time=spectrum_time,
        freq_all_data=freq_all_data,
        amp_all_data=amp_norm_data,
        Nod=Nod,
        frame=frame,
        start=0,
        end=n,
        joint_name=set_joint['j_name'],
        select_data=select_data['select_data'],
        save_path=user.save_path
        )




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input bvh file data', default=None)
    parser.add_argument('-o', '--output', help='output path', default='output_image')
    parser.add_argument('-j', '--joint', help='select joint', choices=list(Joint().joint.keys()))
    parser.add_argument('-u', '--user', help='choice the user want to analyze s', choices=user_list)
    args = parser.parse_args()
    main(args)