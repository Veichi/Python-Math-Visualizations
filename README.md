Python Math Visualizations

A collection of small Python projects Im building while learning math, programming, and engineering.

Current Projects

Barnsley Fern

A fractal generated using an Iterated Function System, consisting of several affine transformations applied with different probabilities

Animated Sine & Cosine Waves

Simple animation of sine and cosine waves. You can change their amplitude and frequency on these lines 
-
sin_line.set_ydata(4*np.sin(x + frame/10))
cos_line.set_ydata(3*np.cos(x + frame/10))

#Tools Needed

* Python
* NumPy
* Matplotlib

Running the projects

Install the dependencies:

```bash
pip install numpy matplotlib
```

Then run whichever project you want:

```bash
python BarnsleyFern.py
```

or

```bash
python AnimatedSinCosWav.py
```

I'm sure this repository will grow and change over time as I experiment more.
