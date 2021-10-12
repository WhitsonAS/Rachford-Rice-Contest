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

<img src="https://latex.codecogs.com/gif.latex? h(V)=\sum_{i=1}^{N_c} \frac{z_i \cdot (K_i - 1)}{1 + V \cdot (K_i -1)}" /> 

where z<sub>i</sub> is the total molar composition of component *i*, and *V* is the vapor molar fraction defined by

<img src="https://latex.codecogs.com/gif.latex? V = \frac{n_V}{n_V + n_L}" />

where n<sub>V</sub> is the total molar amount of the vapor phase and n<sub>L</sub> is the total molar amount of the liquid phase.

The constraints for passing the contest are given by a set of test functions (*R*) and are given by

**Vapor composition test**

<img src="https://latex.codecogs.com/gif.latex? R_y = |1-\sum_{i=1}^{N_c}y_i| \leq \epsilon_y = \epsilon_t + N_c \cdot \epsilon_m" />

**Liquid composition test**

<img src="https://latex.codecogs.com/gif.latex? R_x = |1-\sum_{i=1}^{N_c}x_i| \leq \epsilon_x = \epsilon_t + N_c \cdot \epsilon_m" />

**Vapor and liquid fraction test**

<img src="https://latex.codecogs.com/gif.latex? R_F = \frac{|V + L - 1|}{|V| + |L| + 1} \leq \epsilon_F = \epsilon_t" />

**Material balance test**

<img src="https://latex.codecogs.com/gif.latex? R_z = \frac{|V \cdot y_i + L \cdot x_i - z_i|}{|V \cdot y_i| + |L \cdot x_i| + z_i} \leq \epsilon_z = \epsilon_t" />

**K-value test**

<img src="https://latex.codecogs.com/gif.latex? R_F = \frac{|y_i - K_i \cdot x_i|}{|y_i| + |K_i \cdot x_i|} \leq \epsilon_K = \epsilon_t" />

where the threshold value (ε<sub>t</sub>) is set to be 10<sup>-15</sup>.

The tests will be judged based on their *sensitivity* which is given by

<img src="https://latex.codecogs.com/gif.latex? sensitivity = \log{(\frac{R}{\epsilon})}" />

For more information about the Rachford-Rice solution, watch the following videos:

- Video 1 found [here](https://youtu.be/6H6nSquWUqc)
- Video 2 found [here](https://youtu.be/yL6-QPKd-aY)
- Video 3 found [here](https://youtu.be/_4qwN6tqa_4)
- Video 4 found [here](https://youtu.be/6ASOMrjE_hQ)

# List of participants who have successfully completed

- Aaron Zick
- Michael Michelsen
- Kim Knudsen
