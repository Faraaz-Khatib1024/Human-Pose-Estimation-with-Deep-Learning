**Simple Baselines for Human Pose Estimation and Tracking**

**Link- [Simple Baseline for HPE**](https://openaccess.thecvf.com/content_ECCV_2018/papers/Bin_Xiao_Simple_Baselines_for_ECCV_2018_paper.pdf)**

**The 7 W's**

Q1. Due to the significant progress on pose estimation and increasing interests on pose tracking in recent years, the overall algorithm and system complexity increases as well, making the algorithm analysis and comparison more difficult. This work provides simple and effective baseline methods. They are helpful for inspiring and evaluating new ideas for the field. State-of-the-art results are achieved on challenging benchmarks.

Q2. It is relevant because this work aims to ease this problem by asking a question from the opposite direction, how good could a simple method be? To answer the question, this work provides baseline methods for both pose estimation and tracking. They are quite simple but surprisingly effective.

Q3 & Q4. The leading methods on MPII benchmark have considerable difference in many details but minor difference in accuracy. It is hard to tell which details are crucial. Also, the representative works on COCO benchmark are also complex but differ significantly. Comparison between such works is mostly on system level and less informative. About pose tracking, although there has not been much work, the system complexity can be expected to further increase due to the increased problem dimension and solution space.

Q5. Our pose estimation is based on a few deconvolutional layers added on a backbone network, ResNet [13] in this work. It is probably the simplest way to estimate heat maps from deep and low-resolution feature maps. Our single model’s best result achieves the state-of-the-art at mAP of 73.7 on COCO test-dev split, which has an improvement of 1.6% and 0.7% over the winner of COCO 2017 keypoint Challenge’s single model and their ensembled model [6, 9].

Q6. This solution is better than its predecessors because it provides better results and beats the best model by achieving a mAP score of 73.7 and a best score of 74.6.


