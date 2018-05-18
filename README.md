# Bird or not? | Solver for [XKCD 1425](https://xkcd.com/1425/)

In a few lines of Python code (with Keras), leveraging a [ResNet-50](https://arxiv.org/abs/1512.03385) trained on [ImageNet](http://www.image-net.org/). No further finetuning was used.

## Installation

Clone the repository. Make sure you have [Pipenv](https://github.com/pypa/pipenv) installed, and run:

```bash
pipenv sync
```

## Usage

Invoke with the command line argument with a directory containing (only) images:

```bash
python birds.py <DIR_WITH_IMAGES>
```

To run with the example images:

```bash
python birds.py ./images
```

## Images

The images in the `images` folder are free and obtained from [pixabay](https://pixabay.com).

* https://pixabay.com/en/raindrop-dewdrop-strawberry-flower-3402550/
* https://pixabay.com/en/panorama-sky-city-architecture-3094696/
* https://pixabay.com/en/owl-snow-snow-owl-bird-forest-3184032/
* https://pixabay.com/en/bird-wild-world-animal-nature-3113835/
* https://pixabay.com/en/trees-forest-forest-path-sunlight-3410836/
* https://pixabay.com/en/raindrop-dewdrop-strawberry-flower-3402550/


## License
Released under the [BSD 3-Clause](https://github.com/dekked/bird-or-not/blob/master/LICENSE).
