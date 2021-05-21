**Learning Feature Pyramids for Human Pose Estimation**

**The 7 W's**

Q1. Although pyramid methods are widely used to handle scale changes at inference time, learning feature pyramids in deep convolutional neural networks (DCNNs) is still not well explored. In this work, we design a Pyramid Residual Module (PRMs) to enhance the invariance in scales of DCNNs. 

Q2. It is relevant because it obtains state-of-the-art results on the investigated benchmarks and also achieving superior performance on the same.

Q3. In order to achieve higher ac- curacy, multi-scale testing on image pyramids was often utilized, which produced a multi-scale feature representation. On the other hand, to learn a model with strong scale in- variance, a multi-branch network trained on three scales of image pyramid was proposed in [51]. 

Q4. However, when image pyramids are used for training, computation and memory linearly increases with the number of scales. 

Q5. 

- We propose a Pyramid Residual Module, which enhances the invariance in scales of deep models by learning feature pyramids in DCNNs with only a small in- crease of complexity. 
- We identify the problem for initializing DCNNs including layers with multiple input or output branches. A weight initialization scheme is then provided, which can be used for many network structures including inception models [47, 30, 48, 46] and ResNets [25, 26]. 

Q6. Our pyramid residual module provides an efficient way of learning multi-scale features, with relatively small cost in computation and memory. We also adopt Hourglass as our basic structure, and replace its original residual units, which learn features from a single scale, with the proposed Pyramid Residual Module. 

