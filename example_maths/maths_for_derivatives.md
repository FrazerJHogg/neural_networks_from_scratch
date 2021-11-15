# Explination for the maths behind derivatives

* **Derivative** : The rate of change of a variable, or function, with respect to another variable, or function. 

    In `y = mx + b` the derivative will show the rate `y` is changing with respect to the value of `x` (N.b. Useful video on deriviatives https://youtu.be/wLTDW7t5Z2c )

    Another example is measuring the slope of the tangent line for a function that takes a single parameter as an input (Explained here: https://www.youtube.com/watch?v=29Px0qXE1BU, notes captured below).

    **Notes:** 

    *Eample 1:*

    * There are two points on a graph; `P` and `Q`

    * The coordinates for..

        * P are : `(x, f(x))`
        * Q are : `(x+Δx, f(x+Δx)`) 

    * Function `f(x)` to determine `y` at the first point (e.g `y=x^2`)

    * Function `f(x+Δx)` to determine `y` at the second point 

    * Slope the change between is `Δy / Δx` (i.e. the change in `y` divided by the change in `x`).

        *  To find the difference in `y` values between the two points;

            `f(x+Δx) - f(x)`

        * The difference in the `x` is simply `Δx`

        * Therefore,  `Δy / Δx` = `f(x+Δx) - f(x) / Δx`

        * The function at `x` (e.g. `y = x^2`) then needs to be plugged (i.e. replace every `x` with `x+Δx` into the equation to calculate the derivitive of the function;

            * So `f(x+Δx) - f(x) / Δx` becomes `(x+Δx)^2 - x^2 / Δx` 

            *  Multiplied out becomes `x^2 + 2xΔx + (Δx)^2 - x^2 / Δx`

                N.b. For explainations as to why `(x+Δx)^2` = `x^2 + 2xΔx + (Δx)^2` refer to the follow articles that discuss `(a+b)^2` as an example;

                * https://owlcation.com/stem/Why-ab-2-a2b22ab#gid=ci027409b7000027c6&pid=why-ab-2-a2b22ab-MTc0NjM5OTg1MDQxODc2OTgy 

                * https://www.quora.com/How-can-we-prove-by-induction-that-a-b-2-a-2-b-2-2ab

                * http://www.montereyinstitute.org/courses/DevelopmentalMath/COURSE_TEXT_RESOURCE/U01_L4_T2_text_final.html 

            * The `x^2` and `-x^2` cancel each other out, so the equation can be simplifed to;

                `2xΔx + (Δx)^2 / Δx`
            
            * Dividing by `Δx` then results in `2x + Δx`, which when `Δx` equates to `0` results in derivative being `2x`, which is also a function.

    *Example 2:*

     From: https://www.youtube.com/watch?v=kNwprrgfu_s

    * Function at `x`, `f(x)`, is `y = x^2 - 4x + 4` 

    * Function at `x+Δx`, `f(x+Δx)`, is `(x+Δx)^2 - 4(x+Δx) + 4`

    * Multiplied out equates to `x^2 + 2xΔx - 4x - 4Δx + 4 \ Δx`

    * Dividing `Δx` into the numerator equates to `x^2 + Δx - 4`

    * When `Δx` goes to 0 this mean the deriviatve (i.e. the slope of a function) equates to `2^x -4` 

