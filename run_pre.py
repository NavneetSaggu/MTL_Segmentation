

""" Generate commands for pre-train phase. """
import os

def run_exp(lr=0.1, gamma=0.2, step_size=30):
    max_epoch = 2
    num_classes=184
    query = 15
    gpu = 1
    way=5
    shot =1
    base_lr = 0.01
    
    the_command = 'python3 main.py' \
        + ' --pre_max_epoch=' + str(max_epoch) \
        + ' --num_classes=' + str(num_classes) \
        + ' --shot=' + str(shot) \
        + ' --train_query=' + str(query) \
        + ' --pre_step_size=' + str(step_size) \
        + ' --pre_gamma=' + str(gamma) \
        + ' --gpu=' + str(gpu) \
        + ' --base_lr=' + str(base_lr) \
        + ' --pre_lr=' + str(lr) \
        + ' --phase=pre_train' \
        + ' --way=' + str(way)    

    os.system(the_command)

run_exp(lr=0.1, gamma=0.2, step_size=30)
