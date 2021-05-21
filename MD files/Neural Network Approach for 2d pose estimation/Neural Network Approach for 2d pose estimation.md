**Neural Network Approach for 2-Dimension Person Pose Estimation With Encoded Mask and Keypoint Detection**

1.what is the problem/topic?

àHow to use Neural network approach for 2D pose estimation using encoded mask and keypoiny detection.

\2. why is it relevant? 

à It is relevant because it gives a new approach to do 2d pose estimation using neural deep networks.

\3. what have other people done to solve the problem?

àSeveral methods are developed for human pose estimation - traditional methods adopt pictorial structure technique, whereas recent research introduces deep learning based methods. Early works identify that mask information is one of the essential factors for human pose estimation. They are either top-down or bottom-up approach methods.

4.why is this not sufficient?

àTraditional methods are prone to be slow and are down with more overhead when using just pictorial structure technique to rely on heatmaps for estimation.

\5. what is the proposed solution? 

à The proposed solution is to use a convolution neural network model by combining the image segmentation technique with the bottom-up approach for human pose estimation. It is observed that the construction of a two stage-network for training an end-to-end manner is beneficial to one another: for person mask prediction and 2D person pose estimation.

\6. why is the solution better?

àCompared with former top-down approaches, the proposed plan is not prone to bounding-box move or stiffness. As a result, it is more robust. In addition, it does not confuse to analyze which joint belongs to which person, due to adding the mask prediction technique that handles the overlapped people problem more efficiently in packed images.

\7. what is left/future work? 

à It is not been tested under the real-time scenario and the speed of our network is slow, especially when there is a large number of persons in a single image. These should be improved in future work

