# Sensing Sound and Music

This is the source code for the e-book [Sensing Sound and Music](https://fourms.github.io/sensingsoundandmusic/), which contains lecture notes and materials for the [course MUS2640](https://www.uio.no/studier/emner/hf/imv/MUS2640/) at the University of Oslo (UiO). It has been written using [Jupyter Book](https://jupyterbook.org/) v2 and can be compiled to different formats. If you are mainly interested in the content, go to [the build](https://fourms.github.io/sensingsoundandmusic/).  

## How to run locally

To run the book using a local server: 

    cd book
    jupyter book start

To build the HTML version of the book: 

    cd book
    myst build --html

For a full local build with executed notebooks (as in CI), use:

    cd book
    myst build --html --execute

## Credits

Alexander Refsum Jensenius, Guilherme Schmidt Camara, Sara D'Amario, Laura Bishop.