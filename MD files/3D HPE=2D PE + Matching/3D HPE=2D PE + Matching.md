**3D Human Pose Estimation = 2D Pose Estimation + Matching**

**Link- [3D HPE=2D PE+ Matching**](https://openaccess.thecvf.com/content_cvpr_2017/papers/Chen_3D_Human_Pose_CVPR_2017_paper.pdf)**

**The 7 W's**

Q1. While many approaches try to directly predict 3D pose from image measurements, we explore a simple architecture that reasons through intermediate 2D pose predictions.

Q2. It is relevant because it provides simple and efficient method, combined with the its state-of-the-art performance on both benchmark datasets and unconstrained “in-the-wild” imagery.

Q3. 

- Most existing work that makes use of deep features tends to formulate the problem as a direct 2D image to 3D pose regression task. Li et al. [17] use deep learning to train a regression model to predict 3D pose directly from images.
- Other approaches have explored pipelines that use 2D poses as an intermediate result. Most focus on the second-stage that lifts 2D estimates to 3D. This is classically treated as a constrained optimization problem whose objective minimizes the 2D reprojection error of an unknown 3D pose and unknown camera


Q4. Such optimization-based approaches could be sensitive to initialization and local minima, and often require expensive constrained solvers.

Q5. Our approach is based on two key observations (1) Deep neural nets have revolutionized 2D pose estimation, producing accurate 2D predictions even for poses with self-occlusions (2) "Big-data" sets of 3D mocap data are now readily available, making it tempting to “lift” predicted 2D poses to 3D through simple memorization (e.g., nearest neighbors). 

Q6. 

- We use datadriven matching, that when combined with a simple closedform warping algorithm, yields a fast and accurate 3D solution.
- We demonstrate that such methods outperform almost all state-of-the art 3D pose estimation systems, most of which directly try to regress 3D pose from 2D measurements.
- The resulting architecture is straightforward to implement with off-the-shelf 2D pose estimation systems and 3D mocap libraries.

