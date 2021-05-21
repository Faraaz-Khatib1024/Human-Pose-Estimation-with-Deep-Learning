**Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields**

1.what is the problem/topic?

àRealtime Multi-Person 2D Pose Estimation using Part Affinity Fields

\2. why is it relevant? 

àThe paper provides with an efficient way to do human 2d pose estimation with a better result and accuracy parameters.

\3. what have other people done to solve the problem?

à The previous approach used to employ a top-down approach unlike the part affinity fields which use a better bottom-up approach which is better in terms on efficiency and accuracy.

4.why is this not sufficient?

à Top-down approaches directly leverage existing techniques for single-person pose estimation, but suffer from early commitment. Furthermore, the runtime of these top-down approaches is proportional to the number of people: for each detection, a single-person pose estimator is run, and the more people there are, the greater the computational cost.

\5. what is the proposed solution? 

à The solution is to use bottom-up representation of association scores via Part Affinity Fields (PAFs), a set of 2D vector fields that encode the location and orientation of limbs over the image domain. We demonstrate that simultaneously inferring these bottom-up representations of detection and association encode global context sufficiently well to allow a greedy parse to achieve high-quality results, at a fraction of the computational cost.

\6. why is the solution better?

à Bottom-up approaches are attractive as they offer robustness to early commitment and have the potential to decouple runtime complexity from the number of people in the image. Yet, bottom-up approaches do not directly use global contextual cues from other body parts and other people.

\7. what is left/future work? 

à To find ways to improve estimation and translate the results to 3D pose estimation for real time application use cases.

