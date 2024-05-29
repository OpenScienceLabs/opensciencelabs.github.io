---
title: "Plotting ternary phase diagrams for solving thermodynamics problems using fqlearn"
slug: fqlearn-ternary-plot
date: 2024-05-29
authors: ["Faith Njamiu Hunja"]
tags: [open science, thermodynamics, visualization, ternary phase diagram]
categories: [science, python, visualization]
description: |
  An article on how to use the open source fqlearn library to plot three 
  phase diagrams used in thermodynamics, also known as ternary plots.

thumbnail: "/header.png"
template: "blog-post.html"
---

<!-- # Plotting ternary phase diagrams for solving thermodynamics problems using fqlearn -->

  An article on how to use the open source fqlearn library to plot three phase diagrams 
  used in thermodynamics, also known as ternary plots.

<!-- TEASER_END -->

## Introduction

During the Open Science Labs Q1 2024 internship, I worked on the Fqlearn project. [Fqlearn](https://github.com/osl-pocs/fqlearn) is an open source python library, currently in development, which aims to facilitate the teaching of mass transfer and thermodynamics.

My main task involved developing methods to use a three phase diagram to solve thermodynamics problems graphically. For this purpose, I wrote code for the [`ThreeComponent.py`](https://github.com/osl-pocs/fqlearn/blob/main/src/fqlearn/ThreeComponent.py) class, as well as corresponding [tests](https://github.com/osl-pocs/fqlearn/blob/main/tests/test_three_component.py) for the class.

### Ternary phase diagram

A ternary plot, ternary graph, triangle plot, simplex plot, or Gibbs triangle is a barycentric plot on three variables which sum to a constant. It graphically depicts the ratios of the three variables as positions in an equilateral triangle. It is used in physical chemistry, petrology, mineralogy, metallurgy, and other physical sciences to show the compositions of systems composed of three species. Ternary plots are tools for analyzing compositional data in the three-dimensional case.

![A ternary plot example](plot.png)

In a ternary plot, the values of the three variables a, b, and c must sum to some constant, K. Usually, this constant is represented as 1.0 or 100%. Because a + b + c = K for all substances being graphed, any one variable is not independent of the others, so only two variables must be known to find a sample's point on the graph: for instance, c must be equal to K − a − b. Because the three numerical values cannot vary independently—there are only two degrees of freedom—it is possible to graph the combinations of all three variables in only two dimensions.

The advantage of using a ternary plot for depicting chemical compositions is that three variables can be conveniently plotted in a two-dimensional graph. Ternary plots can also be used to create phase diagrams by outlining the composition regions on the plot where different phases exist [[1](https://en.wikipedia.org/wiki/Ternary_plot)]. 

## Methods

To begin with, we import the libraries required for plotting the ternary phase diagrams. We used [`python-ternary`](https://github.com/marcharper/python-ternary), a plotting library that uses matplotlib to make ternary plots. Using this library, many features could be added to the fqlearn library for various purposes, as described in this article.

```python
import matplotlib as plt
import numpy as np
import ternary
from scipy.interpolate import CubicSpline
```

Then we define our class, `ThreeComponent`, in which we create some functions, a few of which will be explained in this article. To see how these functions work, we create some variables, which are lists containing an unordered list of tuples, each containing 3 values, representing the x, y and z values.

```python
 right_eq_line = [(0.02, 0.02, 0.96), (0.025, 0.06, 0.915), (0.03, 0.1, 0.87), 
                (0.035, 0.16, 0.805), (0.04, 0.2, 0.76), (0.045, 0.25, 0.705), 
                (0.05, 0.3, 0.65), (0.07, 0.36, 0.57), (0.09, 0.4, 0.51), 
                (0.14, 0.48, 0.38), (0.33, 0.49, 0.18)]
left_eq_line = [(0.97, 0.01, 0.02), (0.95, 0.03, 0.02), (0.91, 0.06, 0.03), 
                (0.88, 0.09, 0.03), (0.83, 0.13, 0.04), (0.79, 0.17, 0.04), 
                (0.745, 0.2, 0.055), (0.68, 0.26, 0.06), (0.62, 0.3, 0.08), 
                (0.49, 0.4, 0.11), (0.33, 0.49, 0.18)]

points = left_eq_line + right_eq_line
```

We also set the scale of our plot to 100 in the `__init__ function`.

```python
self.scale = 100
```

To start using the Three Component class, we can use the following code:

```python
from fqlearn import ThreeComponent
model = ThreeComponent()
```

We can then call the functions as needed. We define a function `sort_points` that sorts the values it receives as an argument. The points are added using the `add_point` function, which ensures that the argument is not an empty list, removes duplicate points, and multiplies each point by 100, since the scale in the plot is set to 100. `sort_points` sorts the points using the x value in each tuple. This allows us to have the values sorted in ascending order along the x-axis.

```python
def sort_points(self, points):
    points_to_plot = self.add_point(points)
    # Sort the points in ascending order
    xyz = [(x, y, z) for x, y, z in points_to_plot]
    sorted_points = sorted(xyz, key=lambda m: m[0])

    # New list to store sorted points
    new_sorted_points = []

    # Check if the points are in a list of lists or a single list
    if isinstance(
        sorted_points[0], (int, float)
    ):  # Check if the first element of points is a number
        assert sorted_points[0] + sorted_points[1] + sorted_points[2] == self.scale
        new_sorted_points.append(sorted_points)
    else:
        # If the points are in a list of lists
        for sorted_point in sorted_points:
            assert sorted_point[0] + sorted_point[1] + sorted_point[2] == self.scale
            new_sorted_points.append(sorted_point)

    # Add the points to the plot
    self.tax.scatter(new_sorted_points, linewidth=1.0, marker="o", color="red")
    return new_sorted_points
```

If we print the returned values, we get the following output:

```console
[(2.0, 2.0, 96.0), (2.5, 6.0, 91.5), (3.0, 10.0, 87.0), (3.5000000000000004, 16.0, 80.5), (4.0, 20.0, 76.0), (4.5, 25.0, 70.5), (5.0, 30.0, 65.0), (7.000000000000001, 36.0, 56.99999999999999), (9.0, 40.0, 51.0), (14.000000000000002, 48.0, 38.0), (33.0, 49.0, 18.0), (49.0, 40.0, 11.0), (62.0, 30.0, 8.0), (68.0, 26.0, 6.0), (74.5, 20.0, 5.5), (79.0, 17.0, 4.0), (83.0, 13.0, 4.0), (88.0, 9.0, 3.0), (91.0, 6.0, 3.0), (95.0, 3.0, 2.0), (97.0, 1.0, 2.0)]
```

We can then call the `plot` function, to plot the ternary phase diagram in order to visualize the plotted points.

```python
def plot(self):
    self.tax.clear_matplotlib_ticks()
    self.tax.get_axes().axis("off")
    ternary.plt.show()
```
We obtain the ternary plot shown below:

![Adding points to the diagram](add_point.png)

We define the `composition_line` function to plot equilibrium lines joining the corresponding points between two compositions in the phase diagram.

```python
def composition_line(self, left_eq_line, right_eq_line):
    # Multiply each point by the scale
    new_left_eq_line = [
        (x * self.scale, y * self.scale, z * self.scale) for x, y, z in left_eq_line
    ]
    new_right_eq_line = [
        (x * self.scale, y * self.scale, z * self.scale)
        for x, y, z in right_eq_line
    ]

    # Sort the left points in ascending order
    xyz = [(x, y, z) for x, y, z in new_left_eq_line]
    sorted_left_eq_line = sorted(xyz, key=lambda m: m[0])
    # Sort the right points in descending order
    xyz = [(x, y, z) for x, y, z in new_right_eq_line]
    sorted_right_eq_line = sorted(xyz, key=lambda m: m[0], reverse=True)

    for i in range(len(left_eq_line)):
        # Ensure all points add up to the scale
        pointA = sorted_left_eq_line[i]
        assert sum(pointA) == self.scale
        pointB = sorted_right_eq_line[i]
        assert sum(pointB) == self.scale

        # Extract x and y coordinates of each point
        xA, yA, zA = pointA
        xB, yB, zB = pointB

        # Add the two points to the plot
        self.tax.scatter([(xA, yA, zA), (xB, yB, zB)], marker="s", color="red")
        # Plot a line connecting the two points
        self.tax.plot(
            [(xA, yA, zA), (xB, yB, zB)],
            linewidth=1.0,
            color="blue",
        )
```

We obtain the following ternary plot:
![Equilibrium line plot](solute_points.png)

We can plot a ternary phase diagram with an equilibrium line to join all the plotted points by calling the `add_eq_line` function.

```python
def add_eq_line(self, right_eq_line, left_eq_line):
    # Add the points
    self.right_eq_line = self.sort_points(right_eq_line)
    self.left_eq_line = self.sort_points(left_eq_line)
    eq_line = self.right_eq_line + self.left_eq_line

    # Remove duplicate points
    eq_line_plot = list(set(eq_line))

    # Sort the points in ascending order
    xyz = [(x, y, z) for x, y, z in eq_line_plot]
    sorted_eq = sorted(xyz, key=lambda m: m[0])

    self.tax.plot(sorted_eq, linewidth=1.0, color="blue", label="Equilibrium line")
```

We get the ternary plot below:
![Joining points with equilibrium line](eq_line.png)

However, the equilibrium line plotted above is not smooth. To generate a smooth line, we use the CubicSpline function, imported from SciPy's library [[2](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html)], to interpolate points along which the equilibrium line is plotted.

```python
def interpolate_points(self, points):
    sorted_points = self.sort_points(points)

    # Cubic spline interpolation
    x = [x for x, y, z in sorted_points]
    y = [y for x, y, z in sorted_points]

    f = CubicSpline(x, y, bc_type="natural")
    x_cubic = np.linspace(0, self.scale, self.scale)
    y_cubic = f(x_cubic)

    # Remove negative points
    interpolated_points = [
        [i, j]
        for i, j in np.column_stack((x_cubic, y_cubic))
        if 0 <= i <= self.scale and 0 <= j <= self.scale
    ]

    return interpolated_points
```        

Printing the output of the function, we obtain the output below, showing the interpolated points:
```console
[[2.0202020202020203, 2.1691472640742586], [3.0303030303030303, 10.329514857514697], [4.040404040404041, 20.340775738329878], [5.050505050505051, 30.41604117022922], [6.0606060606060606, 34.9725244736696], [7.070707070707071, 36.0788150823154], [8.080808080808081, 37.866519430111914], [9.090909090909092, 40.207639450509895], [10.101010101010102, 42.33305618527275], [11.111111111111112, 44.15164951408806], [12.121212121212121, 45.70152886497335], [13.131313131313131, 47.02080366594621], [14.141414141414142, 48.147569717383064], [15.151515151515152, 49.11261947676193], [16.161616161616163, 49.927423194367556], [17.171717171717173, 50.600292249170636], [18.181818181818183, 51.13953802014185], [19.191919191919194, 51.55347188625187], [20.202020202020204, 51.850405226471395], [21.212121212121215, 52.038649419771076], [22.222222222222225, 52.12651584512162], [23.232323232323235, 52.122315881493684], [24.242424242424242, 52.03436090785797], [25.252525252525253, 51.87096230318516], [26.262626262626263, 51.640431446445916], [27.272727272727273, 51.35107971661092], [28.282828282828284, 51.011218492650855], [29.292929292929294, 50.62915915353641], [30.303030303030305, 50.213213078238255], [31.313131313131315, 49.771691645727074], [32.323232323232325, 49.31290623497355], [33.333333333333336, 48.84510804535748], [34.343434343434346, 48.37284930204433], [35.35353535353536, 47.89489752249601], [36.36363636363637, 47.409516570717145], [37.37373737373738, 46.91497031071236], [38.38383838383839, 46.40952260648627], [39.3939393939394, 45.891437322043494], [40.40404040404041, 45.358978321388655], [41.41414141414142, 44.81040946852637], [42.42424242424243, 44.24399462746127], [43.43434343434344, 43.65799766219796], [44.44444444444445, 43.050682436741056], [45.45454545454546, 42.4203128150952], [46.46464646464647, 41.765152661265006], [47.47474747474748, 41.083465839255076], [48.484848484848484, 40.373516213070054], [49.494949494949495, 39.63371670174959], [50.505050505050505, 38.86607499990182], [51.515151515151516, 38.076288591118626], [52.525252525252526, 37.270223020764256], [53.535353535353536, 36.45374383420295], [54.54545454545455, 35.63271657679892], [55.55555555555556, 34.81300679391643], [56.56565656565657, 34.000480030919704], [57.57575757575758, 33.201001833172974], [58.58585858585859, 32.42043774604049], [59.5959595959596, 31.664653314886465], [60.60606060606061, 30.93951408507516], [61.61616161616162, 30.250885601970786], [62.62626262626263, 29.60336029919871], [63.63636363636364, 28.983912044764498], [64.64646464646465, 28.366648419185424], [65.65656565656566, 27.72538388514391], [66.66666666666667, 27.0339329053224], [67.67676767676768, 26.26610994240331], [68.68686868686869, 25.39917799115036], [69.6969696969697, 24.44860975371087], [70.70707070707071, 23.453665293050822], [71.71717171717172, 22.45396405508463], [72.72727272727273, 21.489125485726685], [73.73737373737374, 20.59876903089141], [74.74747474747475, 19.822230508859366], [75.75757575757576, 19.162761793258028], [76.76767676767678, 18.552564414178864], [77.77777777777779, 17.915539652280298], [78.7878787878788, 17.175588788220747], [79.7979797979798, 16.27016258697005], [80.80808080808082, 15.240129979240486], [81.81818181818183, 14.174027140890017], [82.82828282828284, 13.160644754568583], [83.83838383838385, 12.27416074496895], [84.84848484848486, 11.4905826393484], [85.85858585858587, 10.745488901010873], [86.86868686868688, 9.974332435176901], [87.87878787878789, 9.112566147067007], [88.8888888888889, 8.11684009659671], [89.89898989898991, 7.065697936762742], [90.90909090909092, 6.081168542871885], [91.91919191919193, 5.257512388433542], [92.92929292929294, 4.543021889369125], [93.93939393939395, 3.8382841183777483], [94.94949494949496, 3.043859233178794], [95.95959595959597, 2.0885249765853326], [96.96969696969697, 1.0322241687602192]]
```

Next, we define a function to divide an equilibrium line in half, dividing the interpolated points in the left side from those in the right side. 

Before that, we define some helper functions, `derivative` and `min_diff`. The `derivative` function calculates the derivative between each of the interpolated points.

```python
def derivative(self, points):
    points_to_derive = self.interpolate_points(points)

    # Extract x and y values
    x = [x for x, _ in points_to_derive]
    y = [y for _, y in points_to_derive]

    # Calculate derivative
    dydx = np.diff([y]) / np.diff([x])

    return dydx
```

Then the `min_diff` function finds the index of the point that is at the centre of the equilibrium line, dividing it into 2 sides.

```python
def min_diff(self, right_eq_line, left_eq_line):
    self.points = right_eq_line + left_eq_line
    dydx = self.derivative(self.points)
    avg_slope = self.eq_slope(right_eq_line, left_eq_line)

    min_index = 0
    # Initialize min_diff_value with the first element difference
    min_diff_value = abs(dydx[0][0] - avg_slope)

    # Iterate over indices of dydx to find the index with the derivative value closest to the average slope
    for index in range(0, dydx.size):
        diff = abs(dydx[0][index] - avg_slope)
        if diff < min_diff_value:
            min_diff_value = diff
            min_index = index

    return min_index
```

We then define the `div_half` function that divides the equilibrium line precisely in half. We use the interpolated points from the `interpolate_points` function, which ensures that the point of division is very precise. Then we use the `min_diff` function to obtain the index of the point dividing the equilibrium line. Using this index, we can separate the interpolated points, and plot two equilibrium lines on the right and left side of the ternary plot.

```python
def div_half(self, right_eq_line, left_eq_line):
    # Add the points
    self.points = right_eq_line + left_eq_line
    interpolated_points = self.interpolate_points(self.points)

    # Use index to separate right and left side
    index = self.min_diff(right_eq_line, left_eq_line)
    self.interpolated_right_side = interpolated_points[index:]
    self.interpolated_left_side = interpolated_points[: index + 1]

    # Plot the curve
    self.tax.plot(
        self.interpolated_right_side,
        linewidth=1.0,
        color="blue",
        label="Right interpolated curve",
    )
    self.tax.plot(
        self.interpolated_left_side,
        linewidth=1.0,
        color="orange",
        label="Left interpolated curve",
    )
```

We obtain the following ternary plot:
![Dividing the interpolated points in half](div_half.png)

## Acknowledgements
I would like to thank the [Open Science Labs](https://opensciencelabs.org/) and The Graph Network for the opportunity to learn and gain experience working in open source through this internship. I also thank [Ever Vino](https://github.com/EverVino) for his guidance and mentorship throughout this internship program. If you would like to connect with me, you can find me on [LinkedIn](https://www.linkedin.com/in/faithhunja).

## References

[1] Ternary plots - Wikipedia: <https://en.wikipedia.org/wiki/Ternary_plot>

[2] scipy.interpolate.CubicSpline - SciPy v1.13.1 Manual:<https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html>
