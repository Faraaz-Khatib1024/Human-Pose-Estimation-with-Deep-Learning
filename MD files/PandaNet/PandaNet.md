**PandaNet: Anchor-Based Single-Shot Multi-Person 3D Pose Estimation**

1.what is the problem/topic?

-->Anchor-Based Single-Shot Multi-Person 3D Pose Estimation.

\2. why is it relevant? 

-->It is relevant because it exceeds the approaches that only focus on the single-person case or estimate 3D pose of a few people at high resolution. PandaNet (Pose estimAtioN and Dectection Anchor-based Network) is a new single-shot, anchor-based and multi-person 3D pose estimation approach.

\3. what have other people done to solve the problem?

-->Previously, the approach was based on the number of people in the picture, which was a single shot method to run 3d pose estimation of a limited number of people in picture.

4.why is this not sufficient?

-->Real world applications of 3d pose estimation do not benefit from limited single shot approach in high resolution, we need low resolution multi-person estimation for self driving cars and crowd analysis.


\5. what is the proposed solution? 

-->The proposed solution is PandaNet (Pose estimAtioN and Dectection Anchor-based Network). It is a new approach that performs bounding box detection in a dense way and regresses 2D and 3D human poses for each detected person. Contrary to previous top-down multi-person approaches, PandaNet has a forward inference complexity that does not depend on the number of people in the image. It can efficiently process images with a large number of people.


\6. why is the solution better?

-->The previous top-down multi-person approaches were limited to few people in frame but PandaNet has a forward inference complexity that does not depend on the number of people in the image. It can efficiently process images with a large number of people.


\7. what is left/future work? 

-->Older 2d and 3d methods studied in this paper relied heavily on heatmaps which seems to not work well for bigger crowds as the human joints seem to overlap giving an off estimate. We should use a better approach like the one used here called an anchor based approach.


\8. keywords or points you didn't understand?

-->Bounding box detection and regression of 2D and 3D images.

