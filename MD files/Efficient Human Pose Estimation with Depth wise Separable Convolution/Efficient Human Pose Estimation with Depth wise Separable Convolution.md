**Efficient Human Pose Estimation with Depth wise Separable Convolution and Person Centroid Guided Joint Grouping**

1.what is the problem/topic?

à Efficient Human Pose Estimation with Depth wise Separable Convolution and Person Centroid Guided Joint Grouping.

\2. why is it relevant? 

àIt is relevant as it brings a new method called depth wise separable convulation to perform the task of 2D Human Pose Estimation.

\3. what have other people done to solve the problem?

àOne other method is Efficient Neural Networks - To adopt deep neural networks in real-time applications and/or on resource constrained devices, many research works have been devoted to build efficient neural networks with acceptable performance. Another Top-down multi-person pose estimation methods first detect people by a human detector (e.g. Faster-RCNN[25] ), then run a single person pose estimator on the cropped image of each person to get the final pose predictions. Bottom-up methods detect the human joints of all persons at once, and then allocate these joints to each person based on various joint grouping methods.

4.why is this not sufficient?

à The top-down approaches employ detectors to localize person instances and then apply joint detector to each person instance. Each step of top-down approaches requires a very large amount of calculations, and the run-time of the second step is proportional to the number of person.

\5. what is the proposed solution?

à The proposed method is to form a new ResBlock based on depth wise separable convolution and is utilized instead of the original one in Hourglass network. It can be further enhanced by replacing the vanilla depth wise convolution with a mixed depth wise convolution.  

\6. why is the solution better?

à . Experimental results on the MPII human dataset and the LSP dataset show that both our single person and multi-person pose estimation methods can achieve competitive accuracies with low computational costs.

\7. what is left/future work? 

à Hourglass network has been utilized in many human pose estimation methods it is hard to been adapted in practical applications due to its large model size. The task is to adapt it to real life application.

