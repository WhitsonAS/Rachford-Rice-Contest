# Rachford-Rice Contest

This is the 25 + 1 year anniversary version of the 1995 Rachford-Rice contest. Can you solve the Rachford-Rice problem for all these cases? With the initiative of Curtis Hays Whitson, and the extensive help by Aaron Zick, the original Rachford-Rice contest offered $1000 to any student who could solve the problem for all cases. Only three people were able to develop procedures that passed all the test, and none of these were students.

Today we are happy to re-release the Rachford-Rice contest, but now for Python. There are several differences between the original contest and this version, the main one being that this version will focus mainly on passing all the tests and not that much on speed. A timer will be set for your calculations, so if you want to optimize for speed as well you are free to do so.

To access the original version of the Rachford-Rice contest, go to [this](http://www.ipt.ntnu.no/~curtis/courses/Rachford-Rice-Contest/) link.

**Table of Contents**

- [How do you access the code?](#how-do-you-access-the-code?)
- [How do you enter your code?](#how-do-you-enter-your-code?)
- [Basic theory about Rachford-Rice problem ](#basic-theory-about-rachford-rice-problem)
- [List of participants who have successfully completed](#list-of-participants-who-have-successfully-completed)

# How do you access the code?

You can either use Git to clone the repository using

`git clone https://github.com/WhitsonAS/Rachford-Rice-Contest.git`

If you do not want to use Git or know how to use Git, you can manually download the repository by clicking the green code button and press the option called "Download ZIP".

![Code download button](img/code_download.png)

# How do you enter your code?

The main stucture of the code is not to be modified at all, so you are only supposed to write code in certain designated files or functions. The file that contains the function which you have to change is called `rachford_rice_solution.py` and the function is called `rachford_rice_solver()`. This is the only place where you can change anything.

The function takes in the number of components (`Nc`) as an integer, the composition (`zi`) as a numpy array, and the K-values (`Ki`) as a numpy array.

The output of the function must be given in the following order, as the following types. The number of iterations used (`N`) as an integer,

# Basic theory about Rachford-Rice problem

The Rachford-Rice equation is a combination of (1) the material balance equation, (2) the assumption that the vapor (y<sub>i</sub>) and liquid (x<sub>i</sub>) compositions are defined by a constant set of K-values (K<sub>i</sub>) and (3) that the sum of vapor and liquid molar fractions sum to one.

The equation is given by

![equation](https://latex.codecogs.com/gif.latex?h%28V%29%3D%5Csum_%7Bi%3D1%7D%5E%7BN_c%7D%20%5Cfrac%7Bz_i%20%5Ccdot%20%28K_i%20-%201%29%7D%7B1%20+%20V%20%5Ccdot%20%28K_i%20-1%29%7D)

where z<sub>i</sub> is the total molar composition of component _i_, and _V_ is the vapor molar fraction defined by

![equation](https://latex.codecogs.com/gif.latex?V%20%3D%20%5Cfrac%7Bn_V%7D%7Bn_V%20+%20n_L%7D)

where n<sub>V</sub> is the total molar amount of the vapor phase and n<sub>L</sub> is the total molar amount of the liquid phase.

The constraints for passing the contest are given by a set of test functions (_R_) and are given by

**Vapor composition test**

![equation](https://latex.codecogs.com/gif.latex?R_y%20%3D%20%7C1-%5Csum_%7Bi%3D1%7D%5E%7BN_c%7Dy_i%7C%20%5Cleq%20%5Cepsilon_y%20%3D%20%5Cepsilon_t%20+%20N_c%20%5Ccdot%20%5Cepsilon_m)

**Liquid composition test**

![equation](https://latex.codecogs.com/gif.latex?R_x%20%3D%20%7C1-%5Csum_%7Bi%3D1%7D%5E%7BN_c%7Dx_i%7C%20%5Cleq%20%5Cepsilon_x%20%3D%20%5Cepsilon_t%20+%20N_c%20%5Ccdot%20%5Cepsilon_m)

**Vapor and liquid fraction test**

![equation](https://latex.codecogs.com/gif.latex?R_F%20%3D%20%5Cfrac%7B%7CV%20+%20L%20-%201%7C%7D%7B%7CV%7C%20+%20%7CL%7C%20+%201%7D%20%5Cleq%20%5Cepsilon_F%20%3D%20%5Cepsilon_t)

**Material balance test**

![equation](https://latex.codecogs.com/gif.latex?R_z%20%3D%20%5Cfrac%7B%7CV%20%5Ccdot%20y_i%20+%20L%20%5Ccdot%20x_i%20-%20z_i%7C%7D%7B%7CV%20%5Ccdot%20y_i%7C%20+%20%7CL%20%5Ccdot%20x_i%7C%20+%20z_i%7D%20%5Cleq%20%5Cepsilon_z%20%3D%20%5Cepsilon_t)

**K-value test**

![equation](https://latex.codecogs.com/gif.latex?R_K%20%3D%20%5Cfrac%7B%7Cy_i%20-%20K_i%20%5Ccdot%20x_i%7C%7D%7B%7Cy_i%7C%20+%20%7CK_i%20%5Ccdot%20x_i%7C%7D%20%5Cleq%20%5Cepsilon_K%20%3D%20%5Cepsilon_t)

where the threshold value (ε<sub>t</sub>) is set to be 10<sup>-15</sup>.

The tests will be judged based on their _sensitivity_ which is given by

![equation](https://latex.codecogs.com/gif.latex?sensitivity%20%3D%20%5Clog%7B%28%5Cfrac%7BR%7D%7B%5Cepsilon%7D%29%7D)

For more information about the Rachford-Rice solution, watch the following videos:

- Video 1 found [here](https://youtu.be/6H6nSquWUqc)
- Video 2 found [here](https://youtu.be/yL6-QPKd-aY)
- Video 3 found [here](https://youtu.be/_4qwN6tqa_4)
- Video 4 found [here](https://youtu.be/6ASOMrjE_hQ)

# List of participants who have successfully completed

- Aaron Zick
- Michael Michelsen
- Kim Knudsen
