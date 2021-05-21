**DRPose3D: Depth Ranking in 3D Human Pose Estimation**

1. **What is the problem/topic?**
   3D pose is hard to get without sophisticated tracking devices. Images that are captured in laboratory (such as Human 3.6M) and data augmentation can be performed in 3D space.
1. **Why is it relevant?**
   Their method is robust to new camera positions and our data augmentation is very effective.
1. **What have other people done to solve the problem?**
   Point-wise, pairwise and list-wise. Pairwise ranking is the most popular because of more efficient data labelling.
1. **Why is this not sufficient?**
   Their methods provide an effective way of ranking learning but have to extract hand designed features from each item.
1. **What is the proposed solution?**
   They propose a depth ranking based method to tackle the problem of 3D Human Pose Estimation. They design a Pairwise Ranking Convolutional Neural Network (PRCNN) to extract depth rankings of human joints from images. Secondly, a coarse-to-fine 3D Pose Network (DPNet) is proposed to estimate 3D poses from both depth rankings and 2D human joint locations. Additionally, to improve the generality of their model, they introduce a statistical method to augment depth rankings.
1. **Why is this solution better?**
   Their approach outperforms the state-of-the art methods in the Human3.6M benchmark for all three testing protocols, indicating that depth ranking is an essential geometric feature which can be learned to improve the 3D pose estimation.**

1. **What is the left/future work?**
   <NIL>
1. **Points I didn't understand.**
   Pairwise ranking**

