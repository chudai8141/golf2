import argparse
import copy

from tqdm import tqdm

from joint import Joint
from user_setting import impact_number, user_list ,choice_user
from user import User
from hht import get_data, MultEmpModeDeco, HilbertTrans, freq_amp_mean_norm, create_spectrum_time, memd_times
from MEMD_all import wafa
from plot import plot, output_bvh

def main(args):
    exist_memd = False
    for _joint in args.joint:
        output = args.output
        select_user = choice_user(args.user)

        user_name = select_user.user_name
        select_data = select_user.select_data[args.data]
        set_joint = Joint().joint[_joint]
        ballistic = select_data['select_data']
        impact_list = select_data['impact_list']

        user = User(
            user_name=user_name,
            set_joint=set_joint,
            ballistic=ballistic,
            impact_list=impact_list,
            output=output
        )


        # calculation memd
        # if this code run first time, not exec memd at seconde time
        
        if not exist_memd:
            print(f'calculation memd at {memd_times.pop(0)} times.\n this analysis infomation is user:{user.user}, ballistic:{user.ballistic} joint:{user.joint_name}')
            data_path = select_data['data_path']
            result_memd_list = []
            exist_memd = True

            for data in tqdm(data_path):
                #
                data, dt, text = get_data(data)
                result_memd = MultEmpModeDeco(user=user, data=data, dt=dt, text=text, set_joint=set_joint)
                result_memd_list.append(result_memd)
        else:
            print(f'calculated memd.\n this analysis infomation is user:{user.user} ballistic:{user.ballistic} joint:{user.joint_name}')
        
        Nod = 4
        result_hilbert_list = []

        print('hilbert transform')
        for i, result_memd in tqdm(enumerate(result_memd_list)):
            result_ht = HilbertTrans(result_memd=result_memd, select_data=select_data)
            result_ht.calc_means_norm()
            result_ht.set_freq_data(Nod=Nod, impact_number=impact_number[i])
            result_ht.set_amp_data(Nod=Nod, impact_number=impact_number[i])
            result_hilbert_list.append(result_ht)

        freq_all_data, amp_norm_data = freq_amp_mean_norm(result_hilbert_list=result_hilbert_list)
        # smoothing wafa
        freq_all_data_wafa = wafa(freq_all_data, amp_norm_data, m=3)

        # create spectrum time
        frame = freq_all_data.shape[1]
        spectrum_time = create_spectrum_time(Nod=Nod, frame=frame, dt=dt)

        # output plot
        print('output plot')
        user.output(output)
        for n in tqdm(range(1, Nod+1)):
            if n == 0:
                continue

            plot(
            spectrum_time=spectrum_time,
            freq_all_data=freq_all_data_wafa,
            amp_all_data=amp_norm_data,
            Nod=Nod,
            frame=frame,
            start=n-1,
            end=n,
            vmin=0.5,
            vmax=1,
            joint_name=set_joint['j_name'],
            select_data=select_data['select_data'],
            save_path=user.save_path
            )

            plot(
            spectrum_time=spectrum_time,
            freq_all_data=freq_all_data_wafa,
            amp_all_data=amp_norm_data,
            Nod=Nod,
            frame=frame,
            start=0,
            end=n,
            vmin=0,
            vmax=10,
            joint_name=set_joint['j_name'],
            select_data=select_data['select_data'],
            save_path=user.save_path,
            vflag=False,
            ymin=0,
            ymax=40,
            vline_flag=True,
            top_line=select_data['top_line']/120,
            impact_line=select_data["min_impact"]/120
            )
    
    # bvh output src
    print('output bvh file with imf.')
    output_bvh(result_memd_list=result_memd_list)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='output path', default='output_image')
    parser.add_argument('-u', '--user', help='choice the user want to analyze s', choices=user_list)
    parser.add_argument('-d', '--data', help='select data (straight_data, half_staraight, ...)')
    parser.add_argument('-j', '--joint', nargs='*', help='select joint', choices=list(Joint().joint.keys()))
    args = parser.parse_args()

    main(args)