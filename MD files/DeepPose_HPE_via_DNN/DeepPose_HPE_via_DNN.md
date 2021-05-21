**DeepPose: Human Pose Estimation via Deep Neural Networks**

**Link-[DeepPose**](https://openaccess.thecvf.com/content_cvpr_2014/papers/Toshev_DeepPose_Human_Pose_2014_CVPR_paper.pdf)**

**The 7 W's**

Q1. We propose a method for human pose estimation based on Deep Neural Networks (DNNs). The pose estimation is formulated as a DNN-based regression problem towards body joints. We present a cascade of such DNN regressors which results in high precision pose estimates. 

Q2. It is relevant because it seems to achieve state-of-art or better results on several challenging academic datasets.

Q3. More recently, a wide variety of models expressing complex joint relationships were proposed. Yang and Ramanan [26] use a mixture model of parts. Mixture models on the full model scale, by having mixture of PSs, have been studied by Johnson and Everingham [13]. Richer higher-order spatial relationships were captured in a hierarchical model by Tian et al. [24]. A different approach to capture higherorder relationship is through image-dependent PS models, which can be estimated via a global classifier [25, 19, 17].

Q4. Approaches which ascribe to our philosophy of reasoning about pose in a holistic manner have shown limited practicality. The closest work to ours uses convolution NNs together with Neighborhood Component Analysis to regress toward a point in an embedding representing pose [23]. However, this work does not employ a cascade of networks. Cascades of DNN regressors have been used for localization, however of facial points [21].

Q5 & Q6. We present, to our knowledge, the first application of Deep Neural Networks (DNNs) to human pose estimation. Our formulation of the problem as DNN-based regression to joint coordinates and the presented cascade of such regressors has the advantage of capturing context and reasoning about pose in a holistic manner. As a result, we are able to achieve state-of-art or better results on several challenging academic datasets. Further, we show that using a generic convolutional neural network, which was originally designed for classification tasks, can be applied to the different task of localization.

Q7. In future, we plan to investigate novel architectures which could be potentially better tailored towards localization problems in general, and in pose estimation in particular.

