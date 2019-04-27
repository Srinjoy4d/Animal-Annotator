Animal Annotator

Animal Annotator is a software to annotate images animals, mainly for the use of pose-estimation.It does not perform Region-of-Interest annotation.
Built using Python3.5 and OpenCV4 
Tested on Ubuntu 16.04

Usage

Point the path to the directory where the images to be annotated are located.
Each image in the directory will show up one after another.
Press and key to move to the next image.
Press left mousebutton to create a red dot for visible joint.
Press middle mousebutton to create a yellow dot for hidden joint.
The joints have to be annotated in the following order:
0-Nose, 1-Head,2-Neck,3-BaseOfTail,4-TailEnd,5,6,7-FrontLeftABC,8,9,10-FrontRightABC,11,12,13-RearLeftABC,14,15,16-RearRightABC,17,18-LeftEarAB,19,20-RightEarAB
The annotations are stored as numpy format in an npy file

Not viable for animals that have greater degrees of motion that those defined by the annotated joints. For example, an elephant's trunk would require more annotation and its ears would require more points. 

Use the visualize file to view the skeletal overlay on the image with lines joining the appropriate joints. Utilizes the saved annotations file to apply the skeleton on the corresponding images.

Currently no error handling options are provided, a wrong joint requires re-annotation the beginning or ignoring that particular joint.

To-Do
-Redo current image in case of error
-Undo last annotated point
-Support larger number of animals by allowing user to choose which points they require for their use
-Create a substantial annotated dataset of various animals
