# gan_3d_point_cloud

## GAN for Point Cloud Object Detection

For my independent project, I’m interested in tackling a problem in robot
perception. While I am fascinated by many other areas of robotics such as control,
legged locomotion, and navigation, I feel that it would be best to focus on a project that
compliments the classes I am taking this quarter, namely Deep Learning and Advanced
Computer Vision. Additionally, I’d like to continue to develop my skills with ROS, dive
further into some of the packages we were introduced to in ME 495, and sharpen my
software development skills in preparation for a summer internship.
As such, I’d like to create a Generative Adversarial Network for object
detection in 3-D point clouds. My ultimate goal is to design robots that operate in harsh
environments, and I feel that training such systems using point cloud data can overcome
some of the difficulties that camera-based systems face.
My project is inspired by both Suhail’s and Will’s independent projects from last
year. I plan on using a RGB-D camera (Kinect or Asus) to collect point cloud data from
an arbitrary object. Pictures from multiple angles could be taken and then stitched
together. If stitching does not work well, I could use a stereo vision camera to collect
point cloud data from a single viewing point, or perhaps pull data from a pre-existing
dataset that contains 3-d points clouds for various objects.
In any case, surface reconstruction will be ignored since I am interested in the
physical geometry of the object versus appearance. Rather than superimposing different
backgrounds and lighting conditions over the 3-D point cloud data to create a dataset, I
would like to create a dataset by modifying my object’s point cloud directly. I will do this
by removing certain chunks of points from the model (to mimic occlusion) or by adding
points to various sections. Through this method, I can identify:
1) what features are key to identifying certain objects in a point cloud
environments
2) in what ways can a classifier be tricked based the presence of absence of
certain features
I plan on modifying my point clouds in rviz or gazebo using pre-existing ROS packages,
or through a script that uses other techniques [1]. Further research will be needed to
determine feasible, repeatable methods.
Modifying the point clouds through my GAN’s generator will probably be the
most challenging aspect of my project. If modification does not go as planned, a backup
plan could be to include some type of covering over the object during initial data
collection. This could mimic the type of modifications a GAN would make.
Ideally, I’d like to place the individual point clouds of my modified objects in
larger point cloud environments taken from self-driving car companies like NuTonomy.
While point cloud datasets from other industries (i.e agriculture) could be used, I feel

that the current popularity of self-driving cars makes acquiring these types of point
cloud environments low-hanging fruit.
If using pre-existing point cloud environments does not work or proves difficult
to integrate, a backup plan could be to capture a 3-D point cloud of the MSR lab instead,
and then place my object’s point cloud in this space at different orientations. Another
option could be to simply use a GAN generator on the point cloud environments
themselves to produce a larger dataset of environments.
In summary, my goals are as follows:
1) Collect 3-D point cloud data for an object
2) Add points to or remove points from this data automatically through a GAN
generator
3) Consolidate these modified point clouds into a dataset
4) Train a GAN discriminator on the generated dataset
5) Paste data from the generated set into pre-existing point cloud environments
from NuTonomy or some other source
6) Test GAN discriminator to detect object point clouds in these environments
7) Analyze misclassifications to determine critical features of point cloud data

Sources:
[1] https://arxiv.org/abs/1707.02392 - paper on point cloud shape modification

## Timeline
1/17 - 1/24: initial meeting, share ideas, preliminary research

1/24 - 1/31: collect working/well documented GAN point clouds
narrow down point cloud library(s), narrow down equipment, create skeleton for
GAN in python, work through PCL tutorials, work through Rviz refresher

1/31 - 2/7: show manipulation of one point cloud, collect more object data,
begin building database, display in Rviz

2/7 - 2/14:
2/14 - 2/21:
2/21 - 2/28:
2/28 - 3/7:
3/7 - 3/14:
3/14 - 3/21:
