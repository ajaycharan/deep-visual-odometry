#!/usr/local/lib/python3.5/dist-packages
import sys
import formatData
sys.path.append('/home/sexy/source/deep-visual-odometry/models')
from alexNet_4 import run_model, create_model

Xtr, Ytr, Xte, Yte = formatData.knownEnv(formatData.load_data(),formatData.load_poses(), training_ratio=(8/10.0))

run_model(create_model(), Xtr, Ytr, Xte, Yte, "/home/sexy/source/deep-visual-odometry/models/alexNet_4/alexNet_4_trined_8.h5")

#run_model(create_model(), Xtr, Ytr, Xte, Yte, "/home/sexy/source/deep-visual-odometry/models/alexNet_3/alexNet_3_trined_7.h5")

#run_model(create_model(), Xtr, Ytr, Xte, Yte, "/home/sexy/source/deep-visual-odometry/models/alexNet_3/alexNet_3_trined_6.h5")

#run_model(create_model(), Xtr, Ytr, Xte, Yte, "/home/sexy/source/deep-visual-odometry/models/alexNet_3/alexNet_3_trined_5.h5")
